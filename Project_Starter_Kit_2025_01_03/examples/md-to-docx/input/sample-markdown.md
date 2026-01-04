# Markdown Formatting Showcase

This sample demonstrates **Standard Markdown**, and **Notion-Friendly Markdown** — all supported by Pandoc for conversion to DOCX.

---

# Part 1: Standard Markdown

## Text Formatting

**Bold text** for emphasis.
*Italic text* for subtle emphasis.
***Bold and italic*** for strong emphasis.
~~Strikethrough~~ for deleted content.
`Inline code` for technical terms.

## Headings

# Heading 1
## Heading 2
### Heading 3
#### Heading 4

## Lists

### Unordered List
- First item
- Second item
  - Nested item
  - Another nested item
- Third item

### Ordered List
1. Step one
2. Step two
   1. Sub-step A
   2. Sub-step B
3. Step three

### Task List
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task to do

## Links and Images

[Link to Google](https://google.com)

![Alt text for image](image.png)

## Blockquotes

> "The only thing we have to fear is fear itself."
> — Franklin D. Roosevelt

Nested blockquotes:
> First level
>> Second level
>>> Third level

## Code Blocks

```python
def hello_world():
    print("Hello, World!")
```

## Tables

| Character | Role | Status |
|-----------|------|--------|
| Sarah | Protagonist | Active |
| Marcus | Antagonist | Mysterious |
| Elena | Mentor | Deceased |

## Horizontal Rules

---

## Footnotes

Here is a sentence with a footnote[^1].

[^1]: This is the footnote content.

---

# Part 2: Notion-Friendly Markdown

Notion uses standard Markdown plus some special features.

## Callout Blocks

> 💡 **Tip:** Use callouts to highlight important information.

> ⚠️ **Warning:** This syntax may not convert perfectly to DOCX.

> ℹ️ **Note:** Pandoc handles most Notion exports well.

## Toggle Lists (Notion-specific)

In Notion, these are collapsible. In Markdown/DOCX, they appear as nested content:

<details>
<summary>Click to expand</summary>

This content is hidden by default in HTML but visible in DOCX.

- Hidden item 1
- Hidden item 2

</details>

## Database-style Tables

Notion databases export as standard tables:

| Title | Tags | Priority | Status |
|-------|------|----------|--------|
| Draft Chapter 1 | #fiction, #wip | High | In Progress |
| Research Notes | #research | Medium | Complete |
| Character Profiles | #planning | Low | Not Started |

## Inline Mentions

In Notion: @person, [[Page Link]], @date
In Markdown export: These become plain text or links.

---

# Pandoc Conversion Notes

## Basic Conversion
```bash
pandoc sample.md -o sample.docx
```

## From Notion Export
```bash
pandoc notion-export.md -o notion-document.docx
```

## With Custom Styling
```bash
pandoc sample.md --reference-doc=template.docx -o styled-output.docx
```

---

*This sample was created to demonstrate the power of Markdown and Pandoc for authors.*
