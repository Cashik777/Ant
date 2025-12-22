#!/usr/bin/env python3
"""
Add more data-i18n to remaining paragraphs in blogs
Skip intro paragraphs that already have it
"""
import re
from pathlib import Path

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

def add_remaining_p_i18n(filename, key):
    """Add data-i18n to paragraphs that don't have it yet"""
    filepath = BASE_DIR / f"{filename}.html"
    
    if not filepath.exists():
        print(f"Skipping {filename} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = f"blog.{key}"
    
    # Count existing data-i18n on paragraphs
    existing_count = len(re.findall(rf'<p[^>]*data-i18n="{prefix}\.p\d+"', content))
    
    modified = False
    p_counter = existing_count
    
    # Find all <p> tags in the main content area (line-height:1.8 section)
    # We'll add data-i18n to paragraphs after H2 tags
    
    # Pattern to find paragraphs immediately after H2 tags or other content paragraphs
    def replace_p(match):
        nonlocal p_counter, modified
        full = match.group(0)
        
        # Skip if already has data-i18n
        if 'data-i18n=' in full:
            return full
        
        # Skip short paragraphs (meta info)
        text_content = re.sub(r'<[^>]+>', '', full)
        if len(text_content.strip()) < 30:
            return full
            
        # Skip paragraphs in footer, header, or special sections
        if 'color:#aaa' in full or 'margin-bottom:20px;' in full and '<p style="margin-bottom:20px;">' in full:
            return full
            
        p_counter += 1
        if p_counter <= 5:  # Max 5 paragraphs per blog
            modified = True
            # Insert data-i18n after <p
            if 'style=' in full:
                return full.replace('<p style=', f'<p data-i18n="{prefix}.p{p_counter}" style=')
            else:
                return full.replace('<p>', f'<p data-i18n="{prefix}.p{p_counter}">')
        return full
    
    # Match paragraphs
    pattern = r'<p[^>]*>[^<]{30,}(?:<[^>]+>[^<]*)*</p>'
    new_content = re.sub(pattern, replace_p, content)
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}: added up to p{p_counter}")
    else:
        print(f"No changes for {filename}")

def main():
    print("Adding remaining paragraph data-i18n...")
    for filename, key in BLOG_MAPPINGS.items():
        add_remaining_p_i18n(filename, key)
    print("Done!")

if __name__ == "__main__":
    main()
