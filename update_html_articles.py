#!/usr/bin/env python3
"""
Update HTML articles with data-i18n attributes
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Map of file names to article keys
FILE_TO_KEY = {
    "what-is-specialty.html": "what_is_specialty",
    "light-vs-dark-roast.html": "light_vs_dark",
    "natural-vs-washed.html": "natural_vs_washed",
    "water-for-coffee.html": "water_for_coffee",
    "grinder-guide.html": "grinder_guide",
    "aeropress-recipes.html": "aeropress_recipes",
    "cold-brew-recipe.html": "cold_brew_recipe",
    "espresso-mistakes.html": "espresso_mistakes",
    "turka-recipe.html": "turka_recipe",
    "how-to-brew-v60.html": "how_to_brew_v60",
    "coffee-storage.html": "coffee_storage",
    "caffeine-myths.html": "caffeine_myths",
}

def update_html_file(filename, article_key):
    """Update a single HTML file with data-i18n attributes"""
    filepath = BASE_DIR / "articles" / filename
    
    if not filepath.exists():
        print(f"File not found: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add data-i18n-title to html tag
    content = re.sub(
        r'<html lang="uk">',
        f'<html lang="uk" data-i18n-title="articles.{article_key}.title">',
        content
    )
    
    # Update top-bar-center with translation
    content = re.sub(
        r'<div class="top-bar-center"><span>.*?</span></div>',
        '<div class="top-bar-center"><span data-i18n="common.topbar_free_delivery">🔥 Безкоштовна доставка від 500₴</span></div>',
        content
    )
    
    # Update "Назад" link
    content = re.sub(
        r'(<i\s+class="fas fa-arrow-left"></i>)\s*Назад',
        r'\1 <span data-i18n="common.back">Назад</span>',
        content
    )
    
    # Add back link with translation (alternative pattern)
    content = re.sub(
        r'Назад до статей',
        '<span data-i18n="articles.' + article_key + '.back_to_articles">Назад до статей</span>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}")

def main():
    print("Updating HTML files with data-i18n attributes...")
    
    for filename, article_key in FILE_TO_KEY.items():
        update_html_file(filename, article_key)
    
    print("Done!")

if __name__ == "__main__":
    main()
