#!/usr/bin/env python3
"""
Add common translations for topbar and other shared elements
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

COMMON_TRANSLATIONS = {
    "uk": {
        "common": {
            "topbar_free_delivery": "🔥 Безкоштовна доставка від 500₴",
            "back": "Назад",
            "back_to_articles": "Назад до статей",
            "read_more": "Читати далі",
            "categories": "Категорії",
            "search": "Пошук",
            "filter": "Фільтр",
            "sort": "Сортування",
            "loading": "Завантаження...",
            "error": "Помилка",
            "success": "Успіх",
            "add_to_cart": "До кошика",
            "buy_now": "Купити зараз",
            "out_of_stock": "Немає в наявності",
            "in_stock": "В наявності"
        }
    },
    "ru": {
        "common": {
            "topbar_free_delivery": "🔥 Бесплатная доставка от 500₴",
            "back": "Назад",
            "back_to_articles": "Назад к статьям",
            "read_more": "Читать далее",
            "categories": "Категории",
            "search": "Поиск",
            "filter": "Фильтр",
            "sort": "Сортировка",
            "loading": "Загрузка...",
            "error": "Ошибка",
            "success": "Успех",
            "add_to_cart": "В корзину",
            "buy_now": "Купить сейчас",
            "out_of_stock": "Нет в наличии",
            "in_stock": "В наличии"
        }
    },
    "en": {
        "common": {
            "topbar_free_delivery": "🔥 Free delivery from 500₴",
            "back": "Back",
            "back_to_articles": "Back to articles",
            "read_more": "Read more",
            "categories": "Categories",
            "search": "Search",
            "filter": "Filter",
            "sort": "Sort",
            "loading": "Loading...",
            "error": "Error",
            "success": "Success",
            "add_to_cart": "Add to cart",
            "buy_now": "Buy now",
            "out_of_stock": "Out of stock",
            "in_stock": "In stock"
        }
    }
}

def update_all_locales():
    """Add common translations to locale files"""
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Add common translations
        if "common" not in data:
            data["common"] = {}
        
        data["common"].update(COMMON_TRANSLATIONS[lang]["common"])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path} with common translations")

if __name__ == "__main__":
    print("Adding common translations...")
    update_all_locales()
    print("Done!")
