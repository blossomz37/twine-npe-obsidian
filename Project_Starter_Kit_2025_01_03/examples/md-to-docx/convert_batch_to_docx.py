# ============================================
# Batch Markdown to DOCX Converter
# ============================================
# 
# HOW TO USE:
# 1. Put your .md files in the input/ folder
# 2. Run: python convert_batch.py
# 3. Find your .docx files in the output/ folder
#
# REQUIREMENTS:
# - Pandoc installed (brew install pandoc)
# - pip install pypandoc
#
# ============================================

# ----- Settings (edit these) -----

INPUT_FOLDER = "input"             # Folder with your .md files
OUTPUT_FOLDER = "output"           # Where to save .docx files
FILE_PATTERN = "*.md"              # Which files to convert

# ----- The conversion -----

import os
import glob
import pypandoc

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Find all markdown files
md_files = glob.glob(os.path.join(INPUT_FOLDER, FILE_PATTERN))

if not md_files:
    print(f"⚠️  No {FILE_PATTERN} files found in {INPUT_FOLDER}/")
    print(f"   Put your markdown files there and try again.")
    exit(1)

print(f"📚 Found {len(md_files)} file(s) to convert\n")

converted = 0
errors = 0

for md_file in md_files:
    # Generate output filename
    basename = os.path.basename(md_file)
    docx_name = basename.replace(".md", ".docx")
    output_path = os.path.join(OUTPUT_FOLDER, docx_name)
    
    print(f"📄 {basename} → {docx_name}")
    
    try:
        pypandoc.convert_file(md_file, "docx", outputfile=output_path)
        converted += 1
    except Exception as e:
        print(f"   ❌ Error: {e}")
        errors += 1

print(f"\n{'='*40}")
print(f"✅ Converted: {converted}")
if errors:
    print(f"❌ Errors: {errors}")
print(f"📁 Output folder: {OUTPUT_FOLDER}/")
