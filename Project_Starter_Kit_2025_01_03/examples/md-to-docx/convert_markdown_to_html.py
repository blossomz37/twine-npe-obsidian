# ============================================
# Markdown to HTML Converter
# ============================================
# 
# HOW TO USE:
# 1. Edit the settings below if needed
# 2. Run: python convert_markdown_to_html.py
#
# REQUIREMENTS:
# - pip install markdown
#
# ============================================

# ----- Settings (edit these) -----

INPUT_FILE = "input/sample-markdown.md"         # Your markdown file
OUTPUT_FILE = "output/sample-markdown.html"     # Where to save the HTML

# ----- The conversion -----

import os
import markdown

# CSS styles for nice output
CSS_STYLES = """
<style>
body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    line-height: 1.6;
    max-width: 800px;
    margin: 40px auto;
    padding: 0 20px;
    color: #333;
}
h1, h2, h3 { color: #222; }
code { background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }
pre { background: #f4f4f4; padding: 16px; border-radius: 6px; overflow-x: auto; }
blockquote { border-left: 4px solid #ddd; margin: 0; padding-left: 16px; color: #666; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background: #f4f4f4; }
</style>
"""

# Create output folder if it doesn't exist
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

print(f"📄 Converting: {INPUT_FILE}")
print(f"📁 Output: {OUTPUT_FILE}")

try:
    # Read markdown
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert to HTML (with extensions for tables, code blocks, and strikethrough)
    html_body = markdown.markdown(
        md_content, 
        extensions=['tables', 'fenced_code', 'toc', 'md_in_html'],
        extension_configs={}
    )
    
    # Handle strikethrough manually since markdown lib doesn't support it
    import re
    html_body = re.sub(r'~~(.+?)~~', r'<del>\1</del>', html_body)
    
    # Wrap in full HTML document
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    {CSS_STYLES}
</head>
<body>
{html_body}
</body>
</html>
"""
    
    # Write HTML file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✅ Done!")
    
except FileNotFoundError:
    print(f"❌ File not found: {INPUT_FILE}")
except ImportError:
    print("❌ Missing dependency. Install with:")
    print("   pip install markdown")
except Exception as e:
    print(f"❌ Error: {e}")
