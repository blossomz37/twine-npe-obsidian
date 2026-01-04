# Markdown Converter Example

Convert Markdown files to DOCX or HTML, with optional CriticMarkup support.

## Features

- ✅ Convert markdown to DOCX (Word) or HTML
- ✅ Auto-detect and format CriticMarkup annotations
- ✅ Single file or batch conversion
- ✅ Strikethrough, tables, code blocks supported

---

## Requirements

- Python 3.10+
- Pandoc (for DOCX output)

### Install Dependencies

```bash
# For DOCX conversion
brew install pandoc           # Mac
# OR: sudo apt install pandoc  # Linux
# OR: Download from https://pandoc.org/installing.html  # Windows

pip install pypandoc python-docx markdown
```

---

## Quick Start

### Batch Conversion (Recommended)

Put your `.md` files in `input/`, then run:

```bash
# Convert to DOCX
python convert_batch_to_docx.py

# Convert to HTML
python convert_batch_to_html.py
```

Output files appear in `output/`.

### Single File Conversion

Edit the script to set your input/output files:

```bash
# Markdown → DOCX
python convert_markdown_to_docx.py

# Markdown → HTML
python convert_markdown_to_html.py

# CriticMarkup → DOCX
python convert_criticmarkup_to_docx.py

# CriticMarkup → HTML
python convert_criticmarkup_to_html.py
```

---

## Scripts

| Script | Output | CriticMarkup |
|--------|--------|--------------|
| `convert_batch_to_docx.py` | `.docx` | Auto-detect ✅ |
| `convert_batch_to_html.py` | `.html` | Auto-detect ✅ |
| `convert_markdown_to_docx.py` | `.docx` | No |
| `convert_markdown_to_html.py` | `.html` | No |
| `convert_criticmarkup_to_docx.py` | `.docx` | Yes |
| `convert_criticmarkup_to_html.py` | `.html` | Yes |

---

## CriticMarkup Syntax

| Syntax | Meaning | Formatting |
|--------|---------|------------|
| `{++text++}` | Addition | Green, underlined |
| `{--text--}` | Deletion | Red, strikethrough |
| `{~~old~>new~~}` | Substitution | Red → Green |
| `{>>comment<<}` | Comment | Blue text |
| `{==text==}` | Highlight | Yellow background |

The braces remain visible; only the content gets formatted.

---

## Sample Files

| File | Contents |
|------|----------|
| `input/sample-markdown.md` | Standard markdown with formatting examples |
| `input/sample-criticmarkup.md` | CriticMarkup annotation examples |
| `input/image.png` | Sample image for testing |

---

## Folder Structure

```
md-to-docx/
├── input/                          # Put .md files here
│   ├── sample-markdown.md
│   ├── sample-criticmarkup.md
│   └── image.png
│
├── output/                         # Converted files appear here
│
├── convert_batch_to_docx.py        # Batch → DOCX (auto-detects CriticMarkup)
├── convert_batch_to_html.py        # Batch → HTML (auto-detects CriticMarkup)
├── convert_markdown_to_docx.py     # Single file → DOCX
├── convert_markdown_to_html.py     # Single file → HTML
├── convert_criticmarkup_to_docx.py # CriticMarkup → DOCX
├── convert_criticmarkup_to_html.py # CriticMarkup → HTML
└── README.md
```
