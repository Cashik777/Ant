#!/usr/bin/env python3
"""
Add blog page and category translations
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

TRANSLATIONS = {
    "uk": {
        "pages": {
            "blog_title": "Історії про каву",
            "blog_subtitle": "Занурюйтесь у світ specialty кави: від плантацій Ефіопії до вашої чашки"
        },
        "blog": {
            "cat_all": "Усі",
            "cat_about": "Про каву",
            "cat_recipes": "Рецепти",
            "cat_equipment": "Обладнання",
            "cat_tips": "Поради",
            "read_more": "Читати далі →",
            "views": "переглядів"
        }
    },
    "ru": {
        "pages": {
            "blog_title": "Истории о кофе",
            "blog_subtitle": "Погружайтесь в мир specialty кофе: от плантаций Эфиопии до вашей чашки"
        },
        "blog": {
            "cat_all": "Все",
            "cat_about": "О кофе",
            "cat_recipes": "Рецепты",
            "cat_equipment": "Оборудование",
            "cat_tips": "Советы",
            "read_more": "Читать далее →",
            "views": "просмотров"
        }
    },
    "en": {
        "pages": {
            "blog_title": "Coffee Stories",
            "blog_subtitle": "Dive into the world of specialty coffee: from Ethiopian plantations to your cup"
        },
        "blog": {
            "cat_all": "All",
            "cat_about": "About Coffee",
            "cat_recipes": "Recipes",
            "cat_equipment": "Equipment",
            "cat_tips": "Tips",
            "read_more": "Read more →",
            "views": "views"
        }
    }
}

def update_all_locales():
    """Add blog page translations"""
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Update pages section
        if "pages" not in data:
            data["pages"] = {}
        data["pages"].update(TRANSLATIONS[lang]["pages"])
        
        # Update blog section
        if "blog" not in data:
            data["blog"] = {}
        data["blog"].update(TRANSLATIONS[lang]["blog"])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path}")

if __name__ == "__main__":
    print("Adding blog page translations...")
    update_all_locales()
    print("Done!")
