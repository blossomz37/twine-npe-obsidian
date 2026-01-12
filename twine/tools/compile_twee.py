import os
import re

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TWEE_DIR = os.path.join(BASE_DIR, 'twee')
INPUT_DIR = os.path.join(TWEE_DIR, 'draft_components')

# Definitions
ORDER_START = [
    'StoryTitle.twee',
    'StoryData.twee',
    'StoryInit.twee',
    'StoryStylesheet.twee',
    'StoryBanner.twee',
    'StoryCaption.twee',
    'StoryScript.twee',
    'StoryJavaScript.twee',
    'Widgets.twee'
]

ORDER_END = [
    'story_passages.twee'
]

def get_next_version_filename(base_name="midnight_working_copy"):
    """
    Scans TWEE_DIR for files matching base_name_vN.twee and returns
    the next filename in sequence.
    """
    pattern = re.compile(rf"{re.escape(base_name)}_v(\d+)\.twee")
    max_version = 0
    
    if os.path.exists(TWEE_DIR):
        for filename in os.listdir(TWEE_DIR):
            match = pattern.match(filename)
            if match:
                version = int(match.group(1))
                if version > max_version:
                    max_version = version
    
    next_version = max_version + 1
    return os.path.join(TWEE_DIR, f"{base_name}_v{next_version}.twee")

def compile_story():
    output_file = get_next_version_filename()
    base_name_no_ext = os.path.splitext(os.path.basename(output_file))[0]
    
    # 1. Compile content
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Start Components
        for filename in ORDER_START:
            path = os.path.join(INPUT_DIR, filename)
            
            # Special handling for StoryTitle to inject versioned name
            if filename == 'StoryTitle.twee':
                print(f"Adding {filename} (with updated title: {base_name_no_ext})...")
                outfile.write(":: StoryTitle\n")
                outfile.write(f"{base_name_no_ext}\n")
                outfile.write("\n\n")
                continue

            if os.path.exists(path):
                print(f"Adding {filename}...")
                with open(path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    if not content.endswith('\n'):
                        outfile.write('\n')
                    outfile.write('\n') # Extra newline
            else:
                pass

        # Main Passages
        for filename in ORDER_END:
            path = os.path.join(INPUT_DIR, filename)
            if os.path.exists(path):
                print(f"Adding {filename}...")
                with open(path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    outfile.write(content)
                    if not content.endswith('\n'):
                        outfile.write('\n')
                    outfile.write('\n')
            else:
                print(f"WARNING: Main content {filename} not found!")

    print(f"Compiled to {output_file}")

if __name__ == "__main__":
    compile_story()
