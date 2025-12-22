#!/usr/bin/env python3
"""Add missing shop sidebar translation keys to all locales"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
LOCALES_DIR = PROJECT_ROOT / 'locales'

# New keys to add to shop section
NEW_KEYS = {
    'uk': {
        'filters': 'Фільтри',
        'taste_fruity': 'Фруктовий',
        'taste_chocolate': 'Шоколадний',
        'taste_floral': 'Квітковий',
        'price_from': 'від',
        'price_to': 'до',
        'found': 'Знайдено:',
        'products_count': 'товарів'
    },
    'ru': {
        'filters': 'Фильтры',
        'taste_fruity': 'Фруктовый',
        'taste_chocolate': 'Шоколадный', 
        'taste_floral': 'Цветочный',
        'price_from': 'от',
        'price_to': 'до',
        'found': 'Найдено:',
        'products_count': 'товаров'
    },
    'en': {
        'filters': 'Filters',
        'taste_fruity': 'Fruity',
        'taste_chocolate': 'Chocolate',
        'taste_floral': 'Floral',
        'price_from': 'from',
        'price_to': 'to',
        'found': 'Found:',
        'products_count': 'products'
    }
}

def update_locale(lang):
    json_path = LOCALES_DIR / f'{lang}.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'shop' not in data:
        data['shop'] = {}
    
    added = 0
    for key, value in NEW_KEYS[lang].items():
        if key not in data['shop']:
            data['shop'][key] = value
            added += 1
            print(f"  Added shop.{key} to {lang}.json")
    
    if added > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    return added

def main():
    print("Adding missing shop keys to locale files...")
    total = 0
    for lang in ['uk', 'ru', 'en']:
        added = update_locale(lang)
        total += added
    print(f"\nDone! Added {total} new keys.")

if __name__ == '__main__':
    main()
