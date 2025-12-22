#!/usr/bin/env python3
"""
Fix blog HTML files - add data-i18n to H1, category, reading time
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Blogs to fix with their translation keys and H1 titles
BLOGS = {
    "arabica-vs-robusta.html": {
        "key": "arabica_vs_robusta",
        "h1": "Arabica vs Robusta: Повний гід"
    },
    "bean-to-cup.html": {
        "key": "bean_to_cup",
        "h1": "Шлях кавового зерна: від ферми до чашки"
    },
    "brewing-methods.html": {
        "key": "brewing_methods",
        "h1": "Методи заварювання кави: повний гід"
    },
    "coffee-processing.html": {
        "key": "coffee_processing",
        "h1": "Обробка кави: як вона впливає на смак"
    },
    "coffee-seasonality.html": {
        "key": "coffee_seasonality",
        "h1": "Сезонність кави: коли найсвіжіша?"
    },
    "coffee-storage.html": {
        "key": "blog_coffee_storage",
        "h1": "Як правильно зберігати каву"
    },
    "cold-brew-guide.html": {
        "key": "cold_brew_guide",
        "h1": "Cold Brew: повний гід"
    },
    "espresso-guide.html": {
        "key": "espresso_guide",
        "h1": "Еспресо вдома: повний гід"
    },
    "ethiopia-origins.html": {
        "key": "ethiopia_origins",
        "h1": "Ефіопія — батьківщина кави"
    },
    "french-press-guide.html": {
        "key": "french_press_guide",
        "h1": "Френч-прес: простий та смачний"
    },
    "sca-grading.html": {
        "key": "sca_grading",
        "h1": "Оцінка SCA: що означають бали"
    },
    "specialty-coffee.html": {
        "key": "specialty_coffee",
        "h1": "Що таке Specialty кава?"
    },
    "turka-guide.html": {
        "key": "turka_guide",
        "h1": "Кава в турці: традиційний метод"
    },
    "v60-guide.html": {
        "key": "v60_guide",
        "h1": "V60: мистецтво пуроверу"
    },
    "yirgacheffe-region.html": {
        "key": "blog_yirgacheffe",
        "h1": "Yirgacheffe: найвідоміший регіон Ефіопії"
    }
}

def fix_blog(filename, info):
    """Add data-i18n to blog content elements"""
    filepath = BASE_DIR / "blog" / filename
    
    if not filepath.exists():
        print(f"File not found: {filepath}")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    key = info["key"]
    h1_text = info["h1"]
    
    # Fix H1 title - various patterns
    h1_escaped = re.escape(h1_text)
    
    # Pattern 1: simple h1
    content = re.sub(
        f'<h1[^>]*>\\s*{h1_escaped}\\s*</h1>',
        f'<h1 data-i18n="blog.{key}.title">{h1_text}</h1>',
        content
    )
    
    # Pattern 2: h1 with style
    content = re.sub(
        f'(<h1[^>]*style="[^"]*"[^>]*)>\\s*{h1_escaped}\\s*</h1>',
        f'\\1 data-i18n="blog.{key}.title">{h1_text}</h1>',
        content
    )
    
    # Fix "До каталогу" / "В каталог" buttons
    content = re.sub(
        r'>До каталогу</a>',
        f' data-i18n="blog.{key}.cta_button">До каталогу</a>',
        content
    )
    
    # Fix back to blog link
    content = re.sub(
        r'← Всі статті блогу',
        f'<span data-i18n="blog.{key}.back_to_blog">← Всі статті блогу</span>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {filename}")

def main():
    print("Fixing blog HTML files...")
    for filename, info in BLOGS.items():
        fix_blog(filename, info)
    print("Done!")

if __name__ == "__main__":
    main()
