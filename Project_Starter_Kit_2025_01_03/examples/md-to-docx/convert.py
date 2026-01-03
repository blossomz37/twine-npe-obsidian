# ============================================
# Markdown to DOCX Converter
# ============================================
# 
# HOW TO USE:
# 1. Edit the settings below if needed
# 2. Run: python convert.py
#
# REQUIREMENTS:
# - Pandoc installed (brew install pandoc)
# - pip install pypandoc
#
# ============================================

# ----- Settings (edit these) -----

INPUT_FILE = "sample.md"           # Your markdown file
OUTPUT_FILE = "output/sample.docx" # Where to save the Word doc

# ----- The conversion -----

import os
import pypandoc

# Create output folder if it doesn't exist
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

print(f"📄 Converting: {INPUT_FILE}")
print(f"📁 Output: {OUTPUT_FILE}")

try:
    pypandoc.convert_file(INPUT_FILE, "docx", outputfile=OUTPUT_FILE)
    print("✅ Done!")
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure Pandoc is installed:")
    print("  Mac: brew install pandoc")
    print("  Windows: https://pandoc.org/installing.html")
