import re
import os
import shutil

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TWEE_DIR = os.path.join(BASE_DIR, 'twee')
TARGET_FILE = os.path.join(TWEE_DIR, 'draft_components', 'story_passages.twee')
BACKUP_FILE = os.path.join(TWEE_DIR, 'draft_components', 'story_passages.twee.bak')

def fix_paragraph_tags():
    if not os.path.exists(BACKUP_FILE):
        print(f"Error: {BACKUP_FILE} not found. Cannot restore.")
        # Fallback to target file if no backup, but warn
        if os.path.exists(TARGET_FILE):
            print("Using current file as source.")
            SOURCE = TARGET_FILE
        else:
            return
    else:
        print(f"Restoring from {BACKUP_FILE}...")
        SOURCE = BACKUP_FILE

    with open(SOURCE, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # 1. Empty lines or Headers: preserve
        if not stripped or line.startswith("::"):
            new_lines.append(line)
            continue
            
        # 2. Macros (<<) or HTML Tags (<) or Comments (/): preserve
        # This covers <p>, </p>, <div>, <!--, <<if>>, <<set>>, //, /*
        if stripped.startswith("<") or stripped.startswith("/") or stripped.startswith("*"):
            new_lines.append(line)
            continue
            
        # 3. Existing HTML end tags (e.g. `Text</p>`)
        # If a line ends with strict HTML closing tag, assume it's handled.
        if stripped.endswith(">") and ("</" in stripped or "/>" in stripped):
             new_lines.append(line)
             continue

        # 4. Links and Prose -> Wrap
        # [[Link]] or "Text"
        new_lines.append(f"<p>{stripped}</p>")

    # Write back to TARGET
    with open(TARGET_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(new_lines))
        
    print(f"Updated {TARGET_FILE} (Clean run)")

if __name__ == "__main__":
    fix_paragraph_tags()
