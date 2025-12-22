#!/usr/bin/env python3
"""
Update all article HTML files with data-i18n attributes for body content
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent / "articles"

# Article key mappings for each file
ARTICLE_KEYS = {
    "what-is-specialty.html": "what_is_specialty",
    "ethiopia-coffee-origin.html": "ethiopia_origin", 
    "light-vs-dark-roast.html": "light_vs_dark",
    "yirgacheffe-region.html": "yirgacheffe",
    "sidamo-guide.html": "sidamo_guide",
    "how-to-brew-v60.html": "how_to_brew_v60",
    "coffee-storage.html": "coffee_storage",
    "natural-vs-washed.html": "natural_vs_washed",
    "water-for-coffee.html": "water_for_coffee",
    "grinder-guide.html": "grinder_guide",
    "aeropress-recipes.html": "aeropress_recipes",
    "cold-brew-recipe.html": "cold_brew_recipe",
    "espresso-mistakes.html": "espresso_mistakes",
    "turka-recipe.html": "turka_recipe",
    "caffeine-myths.html": "caffeine_myths"
}

def update_article_html(filename, key):
    """Add data-i18n to article body elements"""
    filepath = BASE_DIR / filename
    
    if not filepath.exists():
        print(f"Skipping {filename} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = f"articles.{key}"
    
    # Skip if already has lots of data-i18n (already processed)
    i18n_count = content.count('data-i18n="articles.')
    if i18n_count > 10:
        print(f"Skipping {filename} - already has {i18n_count} data-i18n attributes")
        return
    
    # Add data-i18n to H2 tags in article-body
    # Pattern: <h2>Text</h2> -> <h2 data-i18n="prefix.h2_xxx">Text</h2>
    h2_counter = [0]
    def replace_h2(match):
        h2_counter[0] += 1
        text = match.group(1)
        return f'<h2 data-i18n="{prefix}.h2_{h2_counter[0]}">{text}</h2>'
    
    content = re.sub(r'<h2>([^<]+)</h2>', replace_h2, content)
    
    # Add data-i18n to H3 tags
    h3_counter = [0]
    def replace_h3(match):
        h3_counter[0] += 1
        text = match.group(1)
        return f'<h3 data-i18n="{prefix}.h3_{h3_counter[0]}">{text}</h3>'
    
    content = re.sub(r'<h3>([^<]+)</h3>', replace_h3, content)
    
    # Add data-i18n to paragraphs in article-body (carefully)
    # Only target paragraphs that start with text
    p_counter = [0]
    def replace_p(match):
        full_match = match.group(0)
        # Skip if already has data-i18n
        if 'data-i18n=' in full_match:
            return full_match
        # Skip if it's a short paragraph (likely not content)
        text = match.group(1)
        if len(text) < 30:
            return full_match
        p_counter[0] += 1
        return f'<p data-i18n="{prefix}.p_{p_counter[0]}">{text}'
    
    # Match opening <p> with text content (at least 30 chars)
    content = re.sub(r'<p>([А-Яа-яЄєІіЇїҐґ\w][^<]{30,})', replace_p, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}: {h2_counter[0]} H2, {h3_counter[0]} H3, {p_counter[0]} P tags")

def main():
    print("Updating article HTML files with data-i18n attributes...")
    for filename, key in ARTICLE_KEYS.items():
        update_article_html(filename, key)
    print("Done!")

if __name__ == "__main__":
    main()
