# Markdown Formatting Showcase

This sample demonstrates **Standard Markdown**, **Notion-Friendly Markdown**, and **CriticMarkup** — all supported by Pandoc for conversion to DOCX.

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

# Part 3: CriticMarkup

CriticMarkup is a syntax for editorial markup. Pandoc can process these with the right settings.

## Additions

{++This text was added.++}

Example in context:
The quick brown fox {++quickly++} jumps over the lazy dog.

## Deletions

{--This text was deleted.--}

Example in context:
The quick {--slow--} brown fox jumps over the lazy dog.

## Substitutions

{~~old text~>new text~~}

Example in context:
She walked {~~slowly~>quickly~~} through the garden.

## Comments

{>>This is a comment from the editor.<<}

Example in context:
The protagonist entered the room.{>>Consider adding more sensory details here.<<}

## Highlights

{==This text is highlighted for attention.==}

Example in context:
The key clue was hidden in {==the third paragraph of the letter==}.

---

# Part 4: Combined Example — Editing a Manuscript

Here's how an editor might use CriticMarkup on a manuscript:

---

## Chapter 1: The Arrival

{--It was a dark and stormy night.--}{++Lightning split the sky as rain hammered the windows.++}{>>Replaced cliché opening with more vivid imagery.<<}

Sarah {~~walked~>strode~~} into the manor, her coat dripping onto the marble floor. {==The butler was nowhere to be seen.==}{>>This becomes important in Chapter 5.<<}

"Hello?" she called out. {++Her voice echoed through the empty halls.++}

{--She felt scared.--}{++A chill ran down her spine as shadows danced in the flickering candlelight.++}{>>Show, don't tell.<<}

---

# Pandoc Conversion Notes

## Basic Conversion
```bash
pandoc sample.md -o sample.docx
```

## With CriticMarkup Support
```bash
pandoc sample.md --track-changes=all -o sample.docx
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
