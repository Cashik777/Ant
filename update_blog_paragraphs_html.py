#!/usr/bin/env python3
"""
Add data-i18n to paragraph elements in all blog HTML files
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

def add_p_i18n(filename, key):
    """Add data-i18n to paragraph elements"""
    filepath = BASE_DIR / f"{filename}.html"
    
    if not filepath.exists():
        print(f"Skipping {filename} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = f"blog.{key}"
    
    # Check if already has paragraph data-i18n
    if f'data-i18n="{prefix}.intro"' in content:
        print(f"Skipping {filename} - already has paragraph i18n")
        return
    
    modified = False
    
    # Find intro paragraph (first p with style that has font-size:1.2rem or first p in content)
    intro_pattern = r'<p style="font-size:1\.2rem;[^>]*>([^<]+(?:<[^>]+>[^<]*)*)</p>'
    intro_match = re.search(intro_pattern, content)
    if intro_match:
        old_p = intro_match.group(0)
        if 'data-i18n=' not in old_p:
            new_p = old_p.replace('<p ', f'<p data-i18n="{prefix}.intro" ')
            content = content.replace(old_p, new_p, 1)
            modified = True
            print(f"  Added intro paragraph")
    
    # Find main content paragraphs (after H2s, before next H2 or end)
    # We'll add data-i18n to paragraphs that don't have it yet and are direct content
    p_counter = [0]
    
    def replace_content_p(match):
        full_match = match.group(0)
        # Skip if already has data-i18n or if it's a short paragraph (likely meta)
        if 'data-i18n=' in full_match or len(match.group(1)) < 50:
            return full_match
        p_counter[0] += 1
        if p_counter[0] <= 5:  # Only first 5 main paragraphs
            return full_match.replace('<p', f'<p data-i18n="{prefix}.p{p_counter[0]}"', 1)
        return full_match
    
    # Match paragraphs with style containing margin or line-height
    pattern = r'<p style="margin[^>]*>([^<]+(?:<[^>]+>[^<]*)*)</p>'
    new_content = re.sub(pattern, replace_content_p, content)
    if new_content != content:
        content = new_content
        modified = True
        print(f"  Added {p_counter[0]} content paragraphs")
    
    # Also try paragraphs inside the main content div
    if p_counter[0] == 0:
        p_counter[0] = 0
        pattern2 = r'(<p[^>]*>)([^<]{50,}(?:<[^>]+>[^<]*)*)(</p>)'
        def replace_p2(match):
            open_tag = match.group(1)
            content_text = match.group(2)
            close_tag = match.group(3)
            if 'data-i18n=' in open_tag:
                return match.group(0)
            p_counter[0] += 1
            if p_counter[0] <= 5:
                return open_tag.replace('<p', f'<p data-i18n="{prefix}.p{p_counter[0]}"', 1) + content_text + close_tag
            return match.group(0)
        
        new_content = re.sub(pattern2, replace_p2, content)
        if new_content != content:
            content = new_content
            modified = True
            print(f"  Added {p_counter[0]} paragraphs (pattern 2)")
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}")

def main():
    print("Adding data-i18n to blog paragraphs...")
    for filename, key in BLOG_MAPPINGS.items():
        add_p_i18n(filename, key)
    print("Done!")

if __name__ == "__main__":
    main()
