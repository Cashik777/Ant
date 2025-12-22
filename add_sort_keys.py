#!/usr/bin/env python3
"""Add remaining shop translation keys to locales"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
LOCALES_DIR = PROJECT_ROOT / 'locales'

# New keys to add to shop section
NEW_KEYS = {
    'uk': {
        'sort': 'Сортування',
        'sort_popular': 'За популярністю',
        'sort_price_asc': 'Ціна: від низької',
        'sort_price_desc': 'Ціна: від високої',
        'sort_rating': 'За рейтингом',
        'clear_filters': 'Скинути фільтри',
        'nothing_found': 'Нічого не знайдено',
        'try_change_filters': 'Спробуйте змінити фільтри'
    },
    'ru': {
        'sort': 'Сортировка',
        'sort_popular': 'По популярности',
        'sort_price_asc': 'Цена: по возрастанию',
        'sort_price_desc': 'Цена: по убыванию',
        'sort_rating': 'По рейтингу',
        'clear_filters': 'Сбросить фильтры',
        'nothing_found': 'Ничего не найдено',
        'try_change_filters': 'Попробуйте изменить фильтры'
    },
    'en': {
        'sort': 'Sort By',
        'sort_popular': 'Popularity',
        'sort_price_asc': 'Price: Low to High',
        'sort_price_desc': 'Price: High to Low',
        'sort_rating': 'Rating',
        'clear_filters': 'Clear Filters',
        'nothing_found': 'Nothing Found',
        'try_change_filters': 'Try changing filters'
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
    print("Adding remaining shop keys to locale files...")
    total = 0
    for lang in ['uk', 'ru', 'en']:
        added = update_locale(lang)
        total += added
    print(f"\nDone! Added {total} new keys.")

if __name__ == '__main__':
    main()
