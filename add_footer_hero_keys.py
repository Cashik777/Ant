#!/usr/bin/env python3
"""Add footer badge and hero button translation keys"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
LOCALES_DIR = PROJECT_ROOT / 'locales'

# Footer badge keys
FOOTER_KEYS = {
    'uk': {
        'badge_return_days': '14 днів',
        'badge_return': 'повернення',
        'badge_specialty': '100% Specialty',
        'badge_quality': 'якість зерна',
        'badge_free': 'Безкоштовна',
        'badge_shipping': 'доставка від 500₴',
        'badge_fresh': 'Свіжа обсмажка',
        'badge_days': 'до 3 днів'
    },
    'ru': {
        'badge_return_days': '14 дней',
        'badge_return': 'возврат',
        'badge_specialty': '100% Specialty',
        'badge_quality': 'качество зерна',
        'badge_free': 'Бесплатная',
        'badge_shipping': 'доставка от 500₴',
        'badge_fresh': 'Свежая обжарка',
        'badge_days': 'до 3 дней'
    },
    'en': {
        'badge_return_days': '14 Days',
        'badge_return': 'Returns',
        'badge_specialty': '100% Specialty',
        'badge_quality': 'Bean Quality',
        'badge_free': 'Free',
        'badge_shipping': 'Shipping over 500₴',
        'badge_fresh': 'Fresh Roast',
        'badge_days': 'Within 3 Days'
    }
}

# Hero A/B test keys
HERO_KEYS = {
    'uk': {
        'hero_cta_control': 'Обрати свіжу каву',
        'hero_cta_variant_a': 'Спробувати specialty каву',
        'hero_cta_variant_b': 'Замовити зараз — від 240₴'
    },
    'ru': {
        'hero_cta_control': 'Выбрать свежий кофе',
        'hero_cta_variant_a': 'Попробовать specialty кофе',
        'hero_cta_variant_b': 'Заказать сейчас — от 240₴'
    },
    'en': {
        'hero_cta_control': 'Choose Fresh Coffee',
        'hero_cta_variant_a': 'Try Specialty Coffee',
        'hero_cta_variant_b': 'Order Now — from 240₴'
    }
}

def update_locale(lang):
    json_path = LOCALES_DIR / f'{lang}.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Add footer keys
    if 'footer' not in data:
        data['footer'] = {}
    
    added = 0
    for key, value in FOOTER_KEYS[lang].items():
        if key not in data['footer']:
            data['footer'][key] = value
            added += 1
            print(f"  Added footer.{key} to {lang}.json")
    
    # Add hero keys
    if 'hero' not in data:
        data['hero'] = {}
    
    for key, value in HERO_KEYS[lang].items():
        if key not in data['hero']:
            data['hero'][key] = value
            added += 1
            print(f"  Added hero.{key} to {lang}.json")
    
    if added > 0:
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    return added

def main():
    print("Adding footer badge and hero button translation keys...")
    total = 0
    for lang in ['uk', 'ru', 'en']:
        added = update_locale(lang)
        total += added
    print(f"\nDone! Added {total} new keys.")

if __name__ == '__main__':
    main()
