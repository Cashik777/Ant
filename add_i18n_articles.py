#!/usr/bin/env python3
"""Add data-i18n attributes to all article HTML files"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

ARTICLES_MAP = {
    "ethiopia-coffee-origin.html": "ethiopia_origin",
    "light-vs-dark-roast.html": "light_vs_dark",
    "water-for-coffee.html": "water_for_coffee",
    "aeropress-recipes.html": "aeropress",
    "how-to-brew-v60.html": "v60_guide",
    "espresso-mistakes.html": "espresso_mistakes",
    "cold-brew-recipe.html": "cold_brew",
    "coffee-storage.html": "coffee_storage",
    "grinder-guide.html": "grinder_guide",
    "caffeine-myths.html": "caffeine_myths",
    "turka-recipe.html": "turka_recipe",
    "natural-vs-washed.html": "natural_washed",
    "sidamo-guide.html": "sidamo_guide",
    "yirgacheffe-region.html": "yirgacheffe_region"
}

def add_i18n_to_article(filepath, article_key):
    """Add data-i18n attributes to article HTML"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Add article key to title
        if f'data-i18n="articles.{article_key}.title"' not in content:
            # Find h1 tag and add data-i18n if not present
            content = re.sub(
                r'<h1([^>]*)>([^<]+)</h1>',
                lambda m: f'<h1{m.group(1)} data-i18n="articles.{article_key}.title">{m.group(2)}</h1>' if 'data-i18n' not in m.group(0) else m.group(0),
                content
            )
        
        # Add to category
        if f'data-i18n="articles.{article_key}.category"' not in content:
            content = re.sub(
                r'<span class="article-category">([^<]+)</span>',
                lambda m: f'<span class="article-category" data-i18n="articles.{article_key}.category">{m.group(1)}</span>' if 'data-i18n' not in m.group(0) else m.group(0),
                content
            )
        
        # Add to reading time
        if f'data-i18n="articles.{article_key}.reading_time"' not in content:
            content = re.sub(
                r'<i class="far fa-clock"></i>\s*(\d+ хвилин[а-я]* читання)',
                lambda m: f'<i class="far fa-clock"></i> <span data-i18n="articles.{article_key}.reading_time">{m.group(1)}</span>',
                content
            )
        
        # Add to subtitle/lead
        if f'data-i18n="articles.{article_key}.subtitle"' not in content:
            content = re.sub(
                r'<p class="article-lead">([^<]+)</p>',
                lambda m: f'<p class="article-lead" data-i18n="articles.{article_key}.subtitle">{m.group(1)}</p>' if 'data-i18n' not in m.group(0) else m.group(0),
                content
            )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath.name}")
            return True
        else:
            print(f"No changes: {filepath.name}")
            return False
    except Exception as e:
        print(f"Error with {filepath}: {e}")
        return False

def main():
    articles_dir = BASE_DIR / "articles"
    updated = 0
    
    for filename, article_key in ARTICLES_MAP.items():
        filepath = articles_dir / filename
        if filepath.exists():
            if add_i18n_to_article(filepath, article_key):
                updated += 1
        else:
            print(f"Not found: {filename}")
    
    print(f"Updated {updated}/{len(ARTICLES_MAP)} articles")

if __name__ == "__main__":
    main()
