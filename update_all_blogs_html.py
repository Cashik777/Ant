#!/usr/bin/env python3
"""
Add data-i18n attributes to all blog post HTML files
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent / "blog"

# Blog file to key mapping (file name without .html -> translation key)
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

def update_blog_html(filename, key):
    """Add data-i18n to blog body elements"""
    filepath = BASE_DIR / f"{filename}.html"
    
    if not filepath.exists():
        print(f"Skipping {filename} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = f"blog.{key}"
    
    # Check if already has many data-i18n (skip if processed)
    i18n_count = content.count(f'data-i18n="{prefix}')
    if i18n_count > 5:
        print(f"Skipping {filename} - already has {i18n_count} data-i18n attributes")
        return
    
    modified = False
    
    # Add data-i18n to H1 title if not present
    if f'data-i18n="{prefix}.title"' not in content:
        # Find H1 tag and add data-i18n
        h1_pattern = r'<h1[^>]*>([^<]+)</h1>'
        h1_match = re.search(h1_pattern, content)
        if h1_match:
            old_h1 = h1_match.group(0)
            if 'data-i18n' not in old_h1:
                new_h1 = old_h1.replace('<h1', f'<h1 data-i18n="{prefix}.title"')
                content = content.replace(old_h1, new_h1)
                modified = True
    
    # Add data-i18n to H2 tags
    h2_counter = [0]
    def replace_h2(match):
        full_match = match.group(0)
        if 'data-i18n=' in full_match:
            return full_match
        h2_counter[0] += 1
        return full_match.replace('<h2', f'<h2 data-i18n="{prefix}.h2_{h2_counter[0]}"')
    
    new_content = re.sub(r'<h2[^>]*>', replace_h2, content)
    if new_content != content:
        content = new_content
        modified = True
    
    # Add data-i18n to H3 tags
    h3_counter = [0]
    def replace_h3(match):
        full_match = match.group(0)
        if 'data-i18n=' in full_match:
            return full_match
        h3_counter[0] += 1
        return full_match.replace('<h3', f'<h3 data-i18n="{prefix}.h3_{h3_counter[0]}"')
    
    new_content = re.sub(r'<h3[^>]*>', replace_h3, content)
    if new_content != content:
        content = new_content
        modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}: {h2_counter[0]} H2, {h3_counter[0]} H3 tags")
    else:
        print(f"No changes for {filename}")

def main():
    print("Updating blog HTML files with data-i18n attributes...")
    for filename, key in BLOG_MAPPINGS.items():
        update_blog_html(filename, key)
    print("Done!")

if __name__ == "__main__":
    main()
