#!/usr/bin/env python3
"""
Update blog HTML files with data-i18n attributes
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Map of file names to blog keys
FILE_TO_KEY = {
    "arabica-vs-robusta.html": "arabica_vs_robusta",
    "bean-to-cup.html": "bean_to_cup",
    "brewing-methods.html": "brewing_methods",
    "coffee-processing.html": "coffee_processing",
    "coffee-seasonality.html": "coffee_seasonality",
    "coffee-storage.html": "blog_coffee_storage",
    "cold-brew-guide.html": "cold_brew_guide",
    "espresso-guide.html": "espresso_guide",
    "ethiopia-origins.html": "ethiopia_origins",
    "french-press-guide.html": "french_press_guide",
    "sca-grading.html": "sca_grading",
    "specialty-coffee.html": "specialty_coffee",
    "turka-guide.html": "turka_guide",
    "v60-guide.html": "v60_guide",
    "yirgacheffe-region.html": "blog_yirgacheffe",
}

def update_blog_file(filename, blog_key):
    """Update a single blog HTML file with data-i18n attributes"""
    filepath = BASE_DIR / "blog" / filename
    
    if not filepath.exists():
        print(f"File not found: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add data-i18n-title to html tag if not present
    if 'data-i18n-title' not in content:
        content = re.sub(
            r'<html lang="uk">',
            f'<html lang="uk" data-i18n-title="blog.{blog_key}.title">',
            content
        )
    
    # Update top-bar-center with translation if not present
    if 'data-i18n="common.topbar_free_delivery"' not in content:
        content = re.sub(
            r'<div class="top-bar-center"><span>🔥 Безкоштовна доставка від 500₴</span></div>',
            '<div class="top-bar-center"><span data-i18n="common.topbar_free_delivery">🔥 Безкоштовна доставка від 500₴</span></div>',
            content
        )
    
    # Update "Всі статті блогу" link with translation
    content = re.sub(
        r'(<a href="\.\./blog\.html" class="btn btn-outline">)← Всі статті блогу(</a>)',
        r'\1<span data-i18n="blog.' + blog_key + r'.back_to_blog">← Всі статті блогу</span>\2',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}")

def main():
    print("Updating blog HTML files with data-i18n attributes...")
    
    for filename, blog_key in FILE_TO_KEY.items():
        update_blog_file(filename, blog_key)
    
    print("Done!")

if __name__ == "__main__":
    main()
