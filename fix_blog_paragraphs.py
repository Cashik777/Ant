#!/usr/bin/env python3
"""
Add data-i18n to all main content paragraphs in blog posts
Uses line-by-line replacement for better accuracy
"""
from pathlib import Path
import re

BASE_DIR = Path(__file__).parent / "blog"

BLOG_MAPPINGS = {
    "arabica-vs-robusta": "arabica_vs_robusta",
    "bean-to-cup": "bean_to_cup",
    "brewing-methods": "brewing_methods",
    "coffee-processing": "coffee_processing",
    "coffee-seasonality": "coffee_seasonality",
    "coffee-storage": "coffee_storage_blog",
    "cold-brew-guide": "cold_brew_guide",
    "espresso-guide": "espresso_guide",
    "ethiopia-origins": "ethiopia_origins",
    "french-press-guide": "french_press_guide",
    "sca-grading": "sca_grading",
    "specialty-coffee": "specialty_coffee",
    "turka-guide": "turka_guide",
    "v60-guide": "v60_guide",
    "yirgacheffe-region": "yirgacheffe_region"
}

def process_blog(filename, key):
    """Add data-i18n to paragraphs in a blog file"""
    filepath = BASE_DIR / f"{filename}.html"
    
    if not filepath.exists():
        print(f"Skipping {filename} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    prefix = f"blog.{key}"
    p_counter = 0
    modified = False
    in_main_content = False
    
    new_lines = []
    for i, line in enumerate(lines):
        # Detect start of main content (after main image)
        if '<div style="line-height:1.8' in line:
            in_main_content = True
        
        # Detect end of main content
        if 'footer' in line.lower() or '</main>' in line:
            in_main_content = False
        
        # Process paragraph starts in main content
        if in_main_content and '<p>' in line and 'data-i18n=' not in line:
            # Check if this is a real content paragraph
            next_text = line + (lines[i+1] if i+1 < len(lines) else '')
            text_content = re.sub(r'<[^>]+>', '', next_text)
            
            # Skip short paragraphs (like just "<p><strong>...")
            if len(text_content.strip()) > 40 or '<strong>' in line:
                p_counter += 1
                if p_counter <= 5:
                    line = line.replace('<p>', f'<p data-i18n="{prefix}.p{p_counter}">')
                    modified = True
        
        new_lines.append(line)
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Updated {filename}: added {p_counter} paragraphs")
    else:
        print(f"No changes for {filename}")

def main():
    print("Adding data-i18n to blog paragraphs (line-by-line)...")
    for filename, key in BLOG_MAPPINGS.items():
        process_blog(filename, key)
    print("Done!")

if __name__ == "__main__":
    main()
