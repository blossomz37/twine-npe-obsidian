---
description: Create a new file conversion script based on existing examples
---

# Create Conversion Script

When the user asks for a new conversion script:

1. **Check existing examples** in `tool_examples/convert_markdown/`:
   - [convert_markdown_to_html.py](cci:7://file:///Users/carlo/Midnight_At_Starlight_Cove_2025_10_26/Project_Starter_Kit_2025_01_03/examples/md-to-docx/convert_markdown_to_html.py:0:0-0:0) — Basic conversion pattern
   - `convert_criticmarkup_to_*.py` — Pre/post-processing pattern
   - `convert_batch_to_*.py` — Batch processing pattern

2. **Use the appropriate pattern** based on user's needs:
   - Single file → Use `convert_markdown_to_*.py` as template
   - Batch files → Use `convert_batch_to_*.py` as template
   - Custom formatting → Use `convert_criticmarkup_to_*.py` as template

3. **Modify the pattern** to meet the user's specific requirements

4. **Test the script** after creation