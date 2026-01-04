# ============================================
# Markdown to HTML with CriticMarkup Support
# ============================================
# 
# HOW TO USE:
# 1. Edit the settings below if needed
# 2. Run: python convert_to_html.py
#
# REQUIREMENTS:
# - pip install markdown
#
# CRITICMARKUP FORMATTING (braces stay visible, content gets styled):
# {++addition++}     → green underline
# {--deletion--}     → red strikethrough
# {~~old~>new~~}     → old red strikethrough, new green underline
# {>>comment<<}      → blue text
# {==highlight==}    → yellow background
#
# ============================================

# ----- Settings (edit these) -----

INPUT_FILE = "input/sample-criticmarkup.md"    # Your markdown file
OUTPUT_FILE = "output/sample-criticmarkup.html" # Where to save the HTML

# CSS styles for CriticMarkup
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
.critic-add {
    color: #008000;
    text-decoration: underline;
}
.critic-del {
    color: #ff0000;
    text-decoration: line-through;
}
.critic-comment {
    color: #0066cc;
}
.critic-highlight {
    background-color: #ffff00;
}
.critic-braces {
    color: #666;
}
</style>
"""

# ----- The code -----

import os
import re
import markdown

# CriticMarkup patterns
PATTERNS = {
    'substitution': re.compile(r'(\{~~)(.+?)(~>)(.+?)(~~\})', re.DOTALL),
    'addition': re.compile(r'(\{\+\+)(.+?)(\+\+\})', re.DOTALL),
    'deletion': re.compile(r'(\{--)(.+?)(--\})', re.DOTALL),
    'comment': re.compile(r'(\{>>)(.+?)(<<\})', re.DOTALL),
    'highlight': re.compile(r'(\{==)(.+?)(==\})', re.DOTALL),
}


def process_criticmarkup(text):
    """Convert CriticMarkup to HTML spans with CSS classes."""
    
    # Handle substitution: {~~old~>new~~}
    def sub_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-del">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>'
                f'<span class="critic-add">{m.group(4)}</span>'
                f'<span class="critic-braces">{m.group(5)}</span>')
    text = PATTERNS['substitution'].sub(sub_repl, text)
    
    # Handle addition: {++content++}
    def add_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-add">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>')
    text = PATTERNS['addition'].sub(add_repl, text)
    
    # Handle deletion: {--content--}
    def del_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-del">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>')
    text = PATTERNS['deletion'].sub(del_repl, text)
    
    # Handle comment: {>>content<<}
    def com_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-comment">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>')
    text = PATTERNS['comment'].sub(com_repl, text)
    
    # Handle highlight: {==content==}
    def hlt_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-highlight">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>')
    text = PATTERNS['highlight'].sub(hlt_repl, text)
    
    return text


def convert_to_html(input_file, output_file):
    """Convert markdown with CriticMarkup to styled HTML."""
    
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"📄 Converting: {input_file}")
    
    # First, process CriticMarkup to HTML spans
    content = process_criticmarkup(content)
    
    # Then convert markdown to HTML
    html_body = markdown.markdown(content, extensions=['tables', 'fenced_code'])
    
    # Wrap in full HTML document with styles
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CriticMarkup Document</title>
    {CSS_STYLES}
</head>
<body>
{html_body}
</body>
</html>
"""
    
    # Create output directory
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Write HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"📁 Output: {output_file}")
    print("✅ Done!")


if __name__ == '__main__':
    try:
        convert_to_html(INPUT_FILE, OUTPUT_FILE)
    except FileNotFoundError:
        print(f"❌ File not found: {INPUT_FILE}")
    except ImportError:
        print("❌ Missing dependency. Install with:")
        print("   pip install markdown")
    except Exception as e:
        print(f"❌ Error: {e}")
