# ============================================
# Universal Batch Markdown to HTML Converter
# ============================================
# 
# HOW TO USE:
# 1. Put your .md files in the input/ folder
# 2. Run: python convert_batch_to_html.py
# 3. Find your .html files in the output/ folder
#
# FEATURES:
# - Auto-detects CriticMarkup and applies formatting
# - Plain markdown files convert normally
# - Batch processes all .md files in input folder
#
# REQUIREMENTS:
# - pip install markdown
#
# ============================================

# ----- Settings (edit these) -----

INPUT_FOLDER = "input"             # Folder with your .md files
OUTPUT_FOLDER = "output"           # Where to save .html files
FILE_PATTERN = "*.md"              # Which files to convert

# CSS styles for output
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
del { color: #ff0000; text-decoration: line-through; }
/* CriticMarkup styles */
.critic-add { color: #008000; text-decoration: underline; }
.critic-del { color: #ff0000; text-decoration: line-through; }
.critic-comment { color: #0066cc; }
.critic-highlight { background-color: #ffff00; }
.critic-braces { color: #666; }
</style>
"""

# ----- The code -----

import os
import re
import glob
import markdown as md_lib

# CriticMarkup detection
CRITIC_PATTERNS = ['{++', '{--', '{~~', '{>>', '{==']

# CriticMarkup regex patterns
PATTERNS = {
    'substitution': re.compile(r'(\{~~)(.+?)(~>)(.+?)(~~\})', re.DOTALL),
    'addition': re.compile(r'(\{\+\+)(.+?)(\+\+\})', re.DOTALL),
    'deletion': re.compile(r'(\{--)(.+?)(--\})', re.DOTALL),
    'comment': re.compile(r'(\{>>)(.+?)(<<\})', re.DOTALL),
    'highlight': re.compile(r'(\{==)(.+?)(==\})', re.DOTALL),
}


def has_criticmarkup(text):
    """Check if text contains CriticMarkup syntax."""
    return any(p in text for p in CRITIC_PATTERNS)


def process_criticmarkup(text):
    """Convert CriticMarkup to HTML spans with CSS classes."""
    
    def sub_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-del">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>'
                f'<span class="critic-add">{m.group(4)}</span>'
                f'<span class="critic-braces">{m.group(5)}</span>')
    text = PATTERNS['substitution'].sub(sub_repl, text)
    
    def add_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-add">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>')
    text = PATTERNS['addition'].sub(add_repl, text)
    
    def del_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-del">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>')
    text = PATTERNS['deletion'].sub(del_repl, text)
    
    def com_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-comment">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>')
    text = PATTERNS['comment'].sub(com_repl, text)
    
    def hlt_repl(m):
        return (f'<span class="critic-braces">{m.group(1)}</span>'
                f'<span class="critic-highlight">{m.group(2)}</span>'
                f'<span class="critic-braces">{m.group(3)}</span>')
    text = PATTERNS['highlight'].sub(hlt_repl, text)
    
    return text


def convert_file(input_file, output_file):
    """Convert a single markdown file to HTML, with optional CriticMarkup."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_critic = has_criticmarkup(content)
    
    if has_critic:
        content = process_criticmarkup(content)
    
    # Convert markdown to HTML
    html_body = md_lib.markdown(content, extensions=['tables', 'fenced_code', 'toc', 'md_in_html'])
    
    # Handle strikethrough
    html_body = re.sub(r'~~(.+?)~~', r'<del>\1</del>', html_body)
    
    # Fix image paths for output folder
    html_body = re.sub(r'src="input/', r'src="../input/', html_body)
    
    # Wrap in full HTML document
    basename = os.path.basename(input_file).replace('.md', '')
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{basename}</title>
    {CSS_STYLES}
</head>
<body>
{html_body}
</body>
</html>
"""
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return has_critic


# ----- Main -----

if __name__ == '__main__':
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    md_files = glob.glob(os.path.join(INPUT_FOLDER, FILE_PATTERN))
    
    if not md_files:
        print(f"⚠️  No {FILE_PATTERN} files found in {INPUT_FOLDER}/")
        print(f"   Put your markdown files there and try again.")
        exit(1)
    
    print(f"📚 Found {len(md_files)} file(s) to convert\n")
    
    converted = 0
    with_critic = 0
    errors = 0
    
    for md_file in md_files:
        basename = os.path.basename(md_file)
        html_name = basename.replace(".md", ".html")
        output_path = os.path.join(OUTPUT_FOLDER, html_name)
        
        try:
            has_critic = convert_file(md_file, output_path)
            if has_critic:
                print(f"📄 {basename} → {html_name} (with CriticMarkup)")
                with_critic += 1
            else:
                print(f"📄 {basename} → {html_name}")
            converted += 1
        except Exception as e:
            print(f"❌ {basename}: {e}")
            errors += 1
    
    print(f"\n{'='*40}")
    print(f"✅ Converted: {converted}")
    if with_critic:
        print(f"🎨 With CriticMarkup: {with_critic}")
    if errors:
        print(f"❌ Errors: {errors}")
    print(f"📁 Output folder: {OUTPUT_FOLDER}/")
