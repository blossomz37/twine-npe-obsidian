# ============================================
# Markdown to DOCX with CriticMarkup Support
# ============================================
# 
# HOW TO USE:
# 1. Edit the settings below if needed
# 2. Run: python convert_with_critic.py
#
# REQUIREMENTS:
# - Pandoc installed (brew install pandoc)
# - pip install pypandoc python-docx
#
# CRITICMARKUP SYNTAX:
# {++addition++}     → Green text, underlined
# {--deletion--}     → Red text, strikethrough
# {~~old~>new~~}     → Red strikethrough → Green underline
# {>>comment<<}      → Yellow highlight, italic
# {==highlight==}    → Yellow background
#
# ============================================

# ----- Settings (edit these) -----

INPUT_FILE = "sample-criticmarkup.md"              # Your markdown file
OUTPUT_FILE = "output/sample-criticmarkup.docx"    # Where to save the Word doc

# ----- The code -----

import os
import re
import tempfile
import pypandoc
from docx import Document
from docx.shared import RGBColor, Pt
from docx.enum.text import WD_COLOR_INDEX

# CriticMarkup patterns
PATTERNS = {
    'addition': (r'\{\+\+(.+?)\+\+\}', '⟦ADD:{}⟧'),
    'deletion': (r'\{--(.+?)--\}', '⟦DEL:{}⟧'),
    'substitution': (r'\{~~(.+?)~>(.+?)~~\}', '⟦DEL:{}⟧⟦ADD:{}⟧'),
    'comment': (r'\{>>(.+?)<<\}', '⟦COM:{}⟧'),
    'highlight': (r'\{==(.+?)==\}', '⟦HLT:{}⟧'),
}

# Marker pattern for post-processing
MARKER_PATTERN = re.compile(r'⟦(ADD|DEL|COM|HLT):(.+?)⟧')


def preprocess_criticmarkup(text):
    """Replace CriticMarkup with markers that survive Pandoc."""
    
    # Handle substitution first (has two capture groups)
    sub_pattern, sub_replace = PATTERNS['substitution']
    text = re.sub(sub_pattern, lambda m: f'⟦DEL:{m.group(1)}⟧⟦ADD:{m.group(2)}⟧', text, flags=re.DOTALL)
    
    # Handle other patterns
    for name, (pattern, replacement) in PATTERNS.items():
        if name != 'substitution':
            text = re.sub(pattern, lambda m: replacement.format(m.group(1)), text, flags=re.DOTALL)
    
    return text


def apply_run_formatting(run, marker_type):
    """Apply Word formatting based on marker type."""
    
    if marker_type == 'ADD':
        # Green text, underlined
        run.font.color.rgb = RGBColor(0, 128, 0)  # Green
        run.font.underline = True
        
    elif marker_type == 'DEL':
        # Red text, strikethrough
        run.font.color.rgb = RGBColor(255, 0, 0)  # Red
        run.font.strike = True
        
    elif marker_type == 'COM':
        # Yellow highlight, italic
        run.font.highlight_color = WD_COLOR_INDEX.YELLOW
        run.font.italic = True
        run.font.color.rgb = RGBColor(128, 128, 128)  # Gray
        
    elif marker_type == 'HLT':
        # Yellow background highlight
        run.font.highlight_color = WD_COLOR_INDEX.YELLOW


def process_paragraph(paragraph):
    """Process a paragraph, applying formatting to marked sections."""
    
    full_text = paragraph.text
    if '⟦' not in full_text:
        return  # No markers, skip
    
    # Clear the paragraph
    for run in paragraph.runs:
        run.text = ''
    
    # Parse and rebuild with formatting
    last_end = 0
    
    for match in MARKER_PATTERN.finditer(full_text):
        # Add text before the marker (plain)
        before_text = full_text[last_end:match.start()]
        if before_text:
            run = paragraph.add_run(before_text)
        
        # Add the marked text with formatting
        marker_type = match.group(1)
        marked_text = match.group(2)
        run = paragraph.add_run(marked_text)
        apply_run_formatting(run, marker_type)
        
        last_end = match.end()
    
    # Add any remaining text after the last marker
    remaining = full_text[last_end:]
    if remaining:
        paragraph.add_run(remaining)


def postprocess_docx(docx_path):
    """Apply CriticMarkup formatting to the DOCX file."""
    
    doc = Document(docx_path)
    
    # Process paragraphs
    for paragraph in doc.paragraphs:
        process_paragraph(paragraph)
    
    # Process tables too
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    process_paragraph(paragraph)
    
    doc.save(docx_path)


def convert_with_critic(input_file, output_file):
    """Convert markdown with CriticMarkup to formatted DOCX."""
    
    # Read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"📄 Converting: {input_file}")
    
    # Pre-process CriticMarkup
    processed = preprocess_criticmarkup(content)
    
    # Write to temp file for Pandoc
    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as tmp:
        tmp.write(processed)
        tmp_path = tmp.name
    
    try:
        # Create output directory
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Convert with Pandoc
        pypandoc.convert_file(tmp_path, 'docx', outputfile=output_file)
        
        # Post-process to apply formatting
        print("🎨 Applying CriticMarkup formatting...")
        postprocess_docx(output_file)
        
        print(f"📁 Output: {output_file}")
        print("✅ Done!")
        
    finally:
        # Clean up temp file
        os.unlink(tmp_path)


if __name__ == '__main__':
    try:
        convert_with_critic(INPUT_FILE, OUTPUT_FILE)
    except FileNotFoundError:
        print(f"❌ File not found: {INPUT_FILE}")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nMake sure you have installed:")
        print("  pip install pypandoc python-docx")
        print("  brew install pandoc  (or apt install pandoc)")
