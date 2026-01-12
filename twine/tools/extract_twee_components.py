import re
import os
import glob

# Configuration
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TWEE_DIR = os.path.join(BASE_DIR, 'twee')
INPUT_FILE = os.path.join(TWEE_DIR, 'midnight_working_copy_v1.twee')
OUTPUT_DIR = os.path.join(TWEE_DIR, 'draft_components')

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def parse_twee(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    passage_pattern = re.compile(r'(^::.*?)(?=\n::|\Z)', re.MULTILINE | re.DOTALL)
    
    passages = []
    matches = passage_pattern.findall(content)
    
    for match in matches:
        header_match = re.match(r'^::\s*(.*?)(?:\s*\[(.*?)\])?(?:\s*\{(.*?)\})?\s*$', match.splitlines()[0])
        if header_match:
            title = header_match.group(1).strip()
            tags = header_match.group(2) if header_match.group(2) else ""
            metadata = header_match.group(3) if header_match.group(3) else ""
            body = "\n".join(match.splitlines()[1:])
            passages.append({
                'title': title,
                'tags': tags,
                'metadata': metadata,
                'full_content': match,
                'body': body
            })
    return passages

def extract_sort_key(passage):
    image_match = re.search(r'<<passageimage\s+"(\d+)_', passage['body'])
    if image_match:
        return int(image_match.group(1))
    return 999999

def main():
    ensure_dir(OUTPUT_DIR)
    
    passages = parse_twee(INPUT_FILE)
    print(f"Found {len(passages)} passages.")
    
    story_passages = []
    widgets = []
    
    # Specific component mapping
    special_components = {
        'StoryTitle': 'StoryTitle.twee',
        'StoryData': 'StoryData.twee',
        'StoryInit': 'StoryInit.twee',
        'StoryCaption': 'StoryCaption.twee',
        'StoryStylesheet': 'StoryStylesheet.twee',
        'StoryScript': 'StoryScript.twee', # Keep as is found in file
        'StoryJavaScript': 'StoryJavaScript.twee' # Just in case
    }
    
    widget_names = ['PassageImage', 'SceneVideo']

    for p in passages:
        title = p['title']
        content = p['full_content']
        
        if title in special_components:
            filename = special_components[title]
            with open(os.path.join(OUTPUT_DIR, filename), 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Extracted {title} to {filename}")
        elif title in widget_names:
            widgets.append(p)
        else:
            story_passages.append(p)

    # Write Widgets
    if widgets:
        with open(os.path.join(OUTPUT_DIR, 'Widgets.twee'), 'w', encoding='utf-8') as f:
            for w in widgets:
                f.write(w['full_content'])
                f.write('\n\n')
        print(f"Extracted {len(widgets)} widgets to Widgets.twee")

    # Sort and Write Story Passages
    story_passages.sort(key=extract_sort_key)
    with open(os.path.join(OUTPUT_DIR, 'story_passages.twee'), 'w', encoding='utf-8') as f:
        for p in story_passages:
            f.write(p['full_content'])
            f.write('\n\n')
            
    print(f"Wrote {len(story_passages)} passages to story_passages.twee")

    # Reference
    with open(os.path.join(OUTPUT_DIR, 'component_reference.md'), 'w', encoding='utf-8') as f:
        f.write("# Component Reference\n\n")
        f.write("## Special Components\n\n")
        for sc in special_components:
             if any(p['title'] == sc for p in passages):
                 f.write(f"- {sc} -> {special_components[sc]}\n")
        
        f.write("\n## Widgets\n\n")
        for w in widgets:
            f.write(f"- {w['title']} -> Widgets.twee\n")

        f.write("\n## Story Passages Order\n\n")
        for p in story_passages:
            sort_key = extract_sort_key(p)
            key_display = sort_key if sort_key != 999999 else "No ID"
            f.write(f"- [{key_display}] {p['title']}\n")
            
    print("Generated component_reference.md")

if __name__ == "__main__":
    main()
