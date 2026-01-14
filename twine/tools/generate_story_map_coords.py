#!/usr/bin/env python3
"""
Generate centered Story Map coordinates for Twee 3 passages.
Non-story passages are placed on a single disconnected row.
Story passages are placed in depth rows, centered to form a pyramid.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict, deque
from pathlib import Path


HEADER_RE = re.compile(r"^::\s")
LINK_RE = re.compile(r"\[\[(.+?)\]\]")


def parse_header(line: str) -> tuple[str, list[str] | None, dict | None]:
    rest = line[3:].strip()
    meta = None
    if rest.endswith("}"):
        idx = rest.rfind("{")
        if idx != -1:
            candidate = rest[idx:]
            try:
                meta = json.loads(candidate)
                rest = rest[:idx].rstrip()
            except json.JSONDecodeError:
                meta = None
    tags = None
    if rest.endswith("]"):
        lb = rest.rfind("[")
        if lb != -1:
            tag_str = rest[lb + 1 : -1]
            tags = tag_str.split() if tag_str.strip() else []
            rest = rest[:lb].rstrip()
    name = rest
    return name, tags, meta


def parse_passages(text: str) -> list[dict]:
    passages = []
    current = None
    for line in text.splitlines():
        if HEADER_RE.match(line):
            if current is not None:
                passages.append(current)
            name, tags, meta = parse_header(line)
            current = {"name": name, "tags": tags, "meta": meta, "body": []}
        else:
            if current is None:
                continue
            current["body"].append(line)
    if current is not None:
        passages.append(current)
    return passages


def resolve_pipe(content: str, existing_names: set[str]) -> str:
    left, right = content.split("|", 1)
    left = left.strip()
    right = right.strip()
    left_is = left in existing_names
    right_is = right in existing_names
    if left_is and not right_is:
        return left
    if right_is and not left_is:
        return right
    if left_is and right_is:
        return left
    return left


def parse_links(body_text: str, existing_names: set[str]) -> list[str]:
    result = []
    for match in LINK_RE.finditer(body_text):
        content = match.group(1)
        target = None
        if "->" in content:
            target = content.split("->")[-1]
            if "|" in target:
                target = target.split("|")[0]
        elif "|" in content:
            target = resolve_pipe(content, existing_names)
        else:
            target = content
        target = target.strip()
        if target:
            result.append(target)
    return result


def determine_root(passages: list[dict], name_to_passage: dict[str, dict]) -> str | None:
    if "Start" in name_to_passage:
        return "Start"
    story_data = name_to_passage.get("StoryData")
    if story_data:
        try:
            story_json = json.loads("\n".join(story_data["body"]))
            start_name = story_json.get("start")
            if start_name in name_to_passage:
                return start_name
        except json.JSONDecodeError:
            return None
    return passages[0]["name"] if passages else None


def compute_layout(
    passages: list[dict],
    *,
    x_gap: int,
    y_gap: int,
    story_y0: int,
    non_story_y: int,
    margin: int,
    loop_y_offset: int,
    loop_back_x_offset: int,
    min_y_gap: int,
) -> dict[str, tuple[int, int]]:
    name_to_passage = {p["name"]: p for p in passages}
    existing_names = set(name_to_passage.keys())

    edges: dict[str, list[str]] = defaultdict(list)
    parents: dict[str, set[str]] = defaultdict(set)
    for p in passages:
        body_text = "\n".join(p["body"])
        seen = set()
        for target in parse_links(body_text, existing_names):
            if target in existing_names and target not in seen:
                edges[p["name"]].append(target)
                parents[target].add(p["name"])
                seen.add(target)

    root = determine_root(passages, name_to_passage)

    special_names = {
        "StoryTitle",
        "StoryData",
        "StoryInit",
        "StoryStylesheet",
        "StoryScript",
        "StoryJavascript",
        "StoryJavaScript",
        "StoryBanner",
        "StoryCaption",
        "StoryMenu",
        "StoryFooter",
        "StoryHeader",
    }

    non_story = []
    for p in passages:
        name = p["name"]
        tags = p["tags"] or []
        if name in special_names or name.startswith("Story"):
            non_story.append(name)
            continue
        if set(tags).intersection({"widget", "script", "stylesheet"}):
            non_story.append(name)
            continue

    non_story = [n for n in non_story if n in existing_names]
    non_story_set = set(non_story)

    story_nodes = [p["name"] for p in passages if p["name"] not in non_story_set]
    story_set = set(story_nodes)

    depth: dict[str, int] = {}
    if root and root in story_set:
        depth[root] = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for nxt in edges.get(node, []):
                if nxt not in story_set:
                    continue
                if nxt not in depth:
                    depth[nxt] = depth[node] + 1
                    queue.append(nxt)

    max_depth = max(depth.values()) if depth else 0
    for name in story_nodes:
        if name not in depth:
            depth[name] = max_depth + 1

    by_depth: dict[int, list[str]] = defaultdict(list)
    for name in story_nodes:
        by_depth[depth[name]].append(name)

    original_index = {p["name"]: idx for idx, p in enumerate(passages)}
    order_index: dict[str, int] = {}

    ordered_by_depth: dict[int, list[str]] = {}
    for d in sorted(by_depth.keys()):
        nodes = by_depth[d]
        if d == 0:
            ordered = sorted(nodes, key=lambda n: original_index.get(n, 0))
        else:
            def bary_key(n: str) -> tuple[float, int]:
                ps = [p for p in parents.get(n, []) if depth.get(p, -1) < d]
                if ps:
                    avg = sum(order_index.get(p, 0) for p in ps) / len(ps)
                    return (avg, original_index.get(n, 0))
                return (float("inf"), original_index.get(n, 0))

            ordered = sorted(nodes, key=bary_key)
        for idx, name in enumerate(ordered):
            order_index[name] = idx
        ordered_by_depth[d] = ordered

    row_counts = [len(ordered_by_depth[d]) for d in ordered_by_depth]
    if non_story:
        row_counts.append(len(non_story))
    max_count = max(row_counts) if row_counts else 1
    max_width = (max_count - 1) * x_gap
    center_x = margin + max_width / 2

    positions: dict[str, tuple[int, int]] = {}

    if non_story:
        row_width = (len(non_story) - 1) * x_gap
        left_x = center_x - row_width / 2
        for idx, name in enumerate(non_story):
            x = int(round(left_x + idx * x_gap))
            positions[name] = (x, non_story_y)

    for d in sorted(ordered_by_depth.keys()):
        nodes = ordered_by_depth[d]
        row_width = (len(nodes) - 1) * x_gap
        left_x = center_x - row_width / 2
        y = story_y0 + d * y_gap
        for idx, name in enumerate(nodes):
            x = int(round(left_x + idx * x_gap))
            positions[name] = (x, y)

    # Loop handling: offset Y relative to nearest non-loop parent or sibling, and X for back-edges.
    def is_loop(n: str) -> bool:
        return "loop" in n.lower()

    for name, (x, y) in list(positions.items()):
        if name not in story_set or not is_loop(name):
            continue

        base_y = y
        parent_candidates = [p for p in parents.get(name, []) if p in positions and not is_loop(p)]
        if parent_candidates:
            # Choose the closest parent vertically (same row) if available.
            parent_candidates.sort(key=lambda p: abs(positions[p][1] - y))
            base_y = positions[parent_candidates[0]][1]
        else:
            depth_nodes = ordered_by_depth.get(depth.get(name, 0), [])
            sibling = next((n for n in depth_nodes if n in positions and not is_loop(n)), None)
            if sibling:
                base_y = positions[sibling][1]

        y = base_y + loop_y_offset

        # Back-edge: loop points to same or shallower depth.
        loop_targets = edges.get(name, [])
        for target in loop_targets:
            if target in depth and depth.get(target, 0) <= depth.get(name, 0):
                x += loop_back_x_offset
                break

        positions[name] = (x, y)

    # Collision avoidance with minimum Y gap.
    used = set()
    for name, (x, y) in sorted(positions.items(), key=lambda item: (item[1][1], item[1][0])):
        while (x, y) in used:
            y += min_y_gap
        positions[name] = (x, y)
        used.add((x, y))

    return positions


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate centered Story Map coordinates for Twee 3.")
    parser.add_argument("--in-file", dest="in_file", required=True, help="Input .twee file")
    parser.add_argument("--out-file", dest="out_file", help="Output .twee file (default: in-place)")
    parser.add_argument("--x-gap", type=int, default=360, help="Horizontal gap between passages in a row")
    parser.add_argument("--y-gap", type=int, default=300, help="Vertical gap between depth rows")
    parser.add_argument("--story-y0", type=int, default=520, help="Y coordinate for depth 0 row")
    parser.add_argument("--non-story-y", type=int, default=120, help="Y coordinate for non-story row")
    parser.add_argument("--margin", type=int, default=120, help="Left margin for centering rows")
    parser.add_argument("--loop-y-offset", type=int, default=160, help="Additional Y offset for passages containing 'Loop'")
    parser.add_argument("--loop-back-x-offset", type=int, default=120, help="Extra X offset for loops with back-edges")
    parser.add_argument("--min-y-gap", type=int, default=140, help="Minimum Y gap when resolving collisions")
    args = parser.parse_args()

    in_path = Path(args.in_file)
    out_path = Path(args.out_file) if args.out_file else in_path

    text = in_path.read_text()
    passages = parse_passages(text)

    positions = compute_layout(
        passages,
        x_gap=args.x_gap,
        y_gap=args.y_gap,
        story_y0=args.story_y0,
        non_story_y=args.non_story_y,
        margin=args.margin,
        loop_y_offset=args.loop_y_offset,
        loop_back_x_offset=args.loop_back_x_offset,
        min_y_gap=args.min_y_gap,
    )

    out_lines = []
    for p in passages:
        name = p["name"]
        tags = p["tags"]
        meta = p["meta"] if isinstance(p["meta"], dict) else {}

        if name == "StoryData":
            header = f":: {name}"
            if tags:
                header += f" [{' '.join(tags)}]"
        else:
            x, y = positions.get(name, (args.margin, args.story_y0))
            pos_str = f"{int(x)},{int(y)}"
            if tags:
                header = f":: {name} [{' '.join(tags)}]"
            else:
                header = f":: {name}"

            meta_out = {"position": pos_str}
            if "size" in meta:
                meta_out["size"] = meta["size"]
            for key, value in meta.items():
                if key in {"position", "size"}:
                    continue
                meta_out[key] = value

            parts = [f"\"position\":\"{meta_out['position']}\""]
            if "size" in meta_out:
                parts.append(f"\"size\":\"{meta_out['size']}\"")
            for key, value in meta_out.items():
                if key in {"position", "size"}:
                    continue
                parts.append(json.dumps(key) + ":" + json.dumps(value))

            header += " {" + ",".join(parts) + "}"

        out_lines.append(header)
        out_lines.extend(p["body"])
        out_lines.append("")

    out_path.write_text("\n".join(out_lines).rstrip() + "\n")


if __name__ == "__main__":
    main()
