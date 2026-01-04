---
description: Create a new file conversion script using existing examples as patterns
---

# Create Conversion Script

Help the user create a custom file conversion script.

## Step 1: Understand Requirements

Ask the user:
1. **Input format?** (markdown, HTML, text, etc.)
2. **Output format?** (DOCX, HTML, PDF, EPUB, etc.)
3. **Single file or batch?**
4. **Any special formatting needs?** (CriticMarkup, custom styles, etc.)

## Step 2: Find the Right Pattern

Review existing examples in `tool_examples/convert_markdown/`:

| Pattern | Use When |
|---------|----------|
| `convert_markdown_to_html.py` | Simple single-file conversion |
| `convert_criticmarkup_to_*.py` | Need pre/post-processing |
| `convert_batch_to_*.py` | Multiple files at once |

Read the appropriate file(s) to understand the pattern.

## Step 3: Create the New Script

1. Copy the pattern's structure
2. Modify for the new input/output formats
3. Add any requested features
4. Keep the same style:
   - Settings at the top
   - Clear comments
   - Helpful error messages
   - Emoji status output

## Step 4: Test

1. Create a sample input file if needed
2. Run the script
3. Verify the output is correct
4. Fix any issues

## Step 5: Document

Add a brief comment at the top explaining:
- What the script does
- Requirements (pip packages, external tools)
- How to use it
