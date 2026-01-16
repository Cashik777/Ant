#!/usr/bin/env python3
"""
Replace article body content in HTML files with new expanded data-i18n keys
FIXED: Uses correct class name "article-body" and proper pattern matching
"""

import json
import os
import re

# Load blog.json
with open("locales/uk/blog.json", "r", encoding="utf-8-sig") as f:
    blog_data = json.load(f)

ARTICLES_DIR = "articles"

ARTICLES = {
    "ethiopia-coffee-origin.html": "ethiopia_origin",
    "sidamo-guide.html": "sidamo_guide",
    "what-is-specialty.html": "what_is_specialty",
    "yirgacheffe-region.html": "yirgacheffe_region",
    "aeropress-recipes.html": "aeropress_recipes",
    "cold-brew-recipe.html": "cold_brew_recipe",
    "turka-recipe.html": "turka_recipe",
    "grinder-guide.html": "grinder_guide",
    "espresso-mistakes.html": "espresso_mistakes",
    "caffeine-myths.html": "caffeine_myths",
    "coffee-storage.html": "coffee_storage",
    "how-to-brew-v60.html": "how_to_brew_v60",
    "light-vs-dark-roast.html": "light_vs_dark",
    "natural-vs-washed.html": "natural_vs_washed",
    "water-for-coffee.html": "water_for_coffee",
}

def read_file(filepath):
    """Read file with latin1 encoding"""
    with open(filepath, 'rb') as f:
        return f.read().decode('latin1')

def generate_article_body(article_key):
    """Generate HTML body content for an article"""
    if article_key not in blog_data.get("articles", {}):
        return None
    
    article = blog_data["articles"][article_key]
    prefix = f"articles.{article_key}"
    lines = []
    
    skip_keys = {"title", "subtitle", "cta_title", "cta_text"}
    
    for key in article.keys():
        if key in skip_keys:
            continue
        
        data_i18n = f"{prefix}.{key}"
        
        if key.startswith("h2_"):
            lines.append(f'            <h2 data-i18n="{data_i18n}"></h2>')
        elif key.startswith("h3_"):
            lines.append(f'            <h3 data-i18n="{data_i18n}"></h3>')
        elif key.startswith("intro_"):
            lines.append(f'            <p class="intro" data-i18n="{data_i18n}"></p>')
        else:
            lines.append(f'            <p data-i18n="{data_i18n}"></p>')
    
    return "\n".join(lines)

def update_file(filename, article_key):
    """Update single file"""
    filepath = os.path.join(ARTICLES_DIR, filename)
    
    if not os.path.exists(filepath):
        print(f"  [SKIP] File not found")
        return False
    
    content = read_file(filepath)
    
    # Generate new body
    new_body = generate_article_body(article_key)
    if new_body is None:
        print(f"  [ERR] No article data")
        return False
    
    # Find article-body section
    # Pattern: <article class="article-body"> ... image ... paragraphs... cta-box
    
    # Find where article-body starts (after opening tag and image)
    article_start = re.search(r'<article[^>]*class="article-body"[^>]*>', content, re.IGNORECASE)
    if not article_start:
        print(f"  [ERR] No article-body tag found")
        return False
    
    # Find first <p with data-i18n (after the image)
    search_start = article_start.end()
    first_p = re.search(r'<p[^>]*data-i18n="articles\.' + re.escape(article_key), content[search_start:], re.IGNORECASE)
    if not first_p:
        print(f"  [ERR] No first paragraph found")
        return False
    
    content_start = search_start + first_p.start()
    
    # Find cta-box (end of content)
    cta_match = re.search(r'<div[^>]*class="article-cta"', content[content_start:], re.IGNORECASE)
    if not cta_match:
        print(f"  [ERR] No cta-box found")
        return False
    
    content_end = content_start + cta_match.start()
    
    # Build new content: keep before, add new body, keep after
    new_content = content[:content_start] + new_body + "\n            " + content[content_end:]
    
    # Write with UTF-8
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"  [OK] Updated")
    return True

def main():
    print("=" * 60)
    print("UPDATING ARTICLE HTML FILES")
    print("=" * 60)
    
    success = 0
    failed = 0
    
    for filename, article_key in ARTICLES.items():
        print(f"\n[{article_key}]")
        if update_file(filename, article_key):
            success += 1
        else:
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"RESULT: {success} success, {failed} failed")
    print("=" * 60)

if __name__ == "__main__":
    main()
