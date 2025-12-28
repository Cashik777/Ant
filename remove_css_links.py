import os

root_dir = r"c:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect"

css_to_remove = [
    "premium-upgrades.css",
    "ux-enhancements.css"
]

def clean_html_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        modified = False
        for line in lines:
            if any(css in line for css in css_to_remove) and '<link' in line:
                modified = True
                continue # Skip this line
            new_lines.append(line)
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"Cleaned: {filepath}")
        else:
            pass
            # print(f"No changes: {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            clean_html_file(os.path.join(subdir, file))
