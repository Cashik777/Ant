#!/usr/bin/env python3
"""
Fix article HTML files - add data-i18n to ALL content elements
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Articles to fix with their translation keys
ARTICLES = {
    "what-is-specialty.html": {
        "key": "what_is_specialty",
        "h1": "Що таке Specialty кава і чому вона коштує дорожче",
        "lead": "Розбираємось, чим відрізняється specialty кава від звичайної",
        "category": "Про каву",
        "reading": "5 хвилин читання"
    },
    "light-vs-dark-roast.html": {
        "key": "light_vs_dark",
        "h1": "Світла чи темна обсмажка: що обрати?",
        "category": "Обсмажка",
        "reading": "6 хвилин читання"
    },
    "natural-vs-washed.html": {
        "key": "natural_vs_washed",
        "h1": "Натуральна vs мита обробка кави",
        "category": "Обробка",
        "reading": "5 хвилин читання"
    },
    "water-for-coffee.html": {
        "key": "water_for_coffee",
        "h1": "Вода для кави: повний гід",
        "category": "Заварювання",
        "reading": "5 хвилин читання"
    },
    "grinder-guide.html": {
        "key": "grinder_guide",
        "h1": "Як обрати кавомолку: повний гід",
        "category": "Обладнання",
        "reading": "7 хвилин читання"
    },
    "aeropress-recipes.html": {
        "key": "aeropress_recipes",
        "h1": "5 рецептів для аеропресу",
        "category": "Рецепти",
        "reading": "5 хвилин читання"
    },
    "cold-brew-recipe.html": {
        "key": "cold_brew_recipe",
        "h1": "Cold Brew в домашніх умовах",
        "category": "Рецепти",
        "reading": "4 хвилини читання"
    },
    "espresso-mistakes.html": {
        "key": "espresso_mistakes",
        "h1": "10 помилок при приготуванні еспресо",
        "category": "Еспресо",
        "reading": "6 хвилин читання"
    },
    "turka-recipe.html": {
        "key": "turka_recipe",
        "h1": "Кава в турці: секрети ідеального приготування",
        "category": "Рецепти",
        "reading": "5 хвилин читання"
    },
    "how-to-brew-v60.html": {
        "key": "how_to_brew_v60",
        "h1": "Як заварювати каву в V60",
        "category": "Заварювання",
        "reading": "6 хвилин читання"
    },
    "coffee-storage.html": {
        "key": "coffee_storage",
        "h1": "Як правильно зберігати каву",
        "category": "Поради",
        "reading": "4 хвилини читання"
    },
    "caffeine-myths.html": {
        "key": "caffeine_myths",
        "h1": "10 міфів про кофеїн",
        "category": "Про каву",
        "reading": "5 хвилин читання"
    }
}

def fix_article(filename, info):
    """Add data-i18n to article content elements"""
    filepath = BASE_DIR / "articles" / filename
    
    if not filepath.exists():
        print(f"File not found: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    key = info["key"]
    
    # Fix H1 title
    if info.get("h1"):
        h1_text = re.escape(info["h1"])
        content = re.sub(
            f'<h1>{h1_text}</h1>',
            f'<h1 data-i18n="articles.{key}.title">{info["h1"]}</h1>',
            content
        )
    
    # Fix category span
    if info.get("category"):
        cat_text = re.escape(info["category"])
        content = re.sub(
            f'<span class="article-category">{cat_text}</span>',
            f'<span class="article-category" data-i18n="articles.{key}.category">{info["category"]}</span>',
            content
        )
    
    # Fix reading time 
    if info.get("reading"):
        reading_text = re.escape(info["reading"])
        content = re.sub(
            f'<i class="far fa-clock"></i> {reading_text}',
            f'<i class="far fa-clock"></i> <span data-i18n="articles.{key}.reading_time">{info["reading"]}</span>',
            content
        )
    
    # Fix "до статей" in back link
    content = re.sub(
        r'(<span data-i18n="common\.back">Назад</span>)\s*до статей',
        r'\1 <span data-i18n="common.back_to_articles">до статей</span>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {filename}")

def main():
    print("Fixing article HTML files...")
    for filename, info in ARTICLES.items():
        fix_article(filename, info)
    print("Done!")

if __name__ == "__main__":
    main()
