#!/usr/bin/env python3
"""Add page title translation keys to locales and data-i18n-title to HTML files"""

import json
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
LOCALES_DIR = PROJECT_ROOT / 'locales'

# Page title translations
PAGE_TITLES = {
    'shop.html': {
        'key': 'pages.shop',
        'uk': 'Магазин — EthioDirect',
        'ru': 'Магазин — EthioDirect',
        'en': 'Shop — EthioDirect'
    },
    'index.html': {
        'key': 'pages.home',
        'uk': 'EthioDirect — Кава, що просилася до вас',
        'ru': 'EthioDirect — Кофе, который ждал вас',
        'en': 'EthioDirect — Coffee That Was Waiting for You'
    },
    'subscription.html': {
        'key': 'pages.subscription',
        'uk': 'Підписка — EthioDirect',
        'ru': 'Подписка — EthioDirect',
        'en': 'Subscription — EthioDirect'
    },
    'about.html': {
        'key': 'pages.about',
        'uk': 'Про нас — EthioDirect',
        'ru': 'О нас — EthioDirect',
        'en': 'About Us — EthioDirect'
    },
    'contacts.html': {
        'key': 'pages.contacts',
        'uk': 'Контакти — EthioDirect',
        'ru': 'Контакты — EthioDirect',
        'en': 'Contact Us — EthioDirect'
    },
    'blog.html': {
        'key': 'pages.blog',
        'uk': 'Блог — EthioDirect',
        'ru': 'Блог — EthioDirect',
        'en': 'Blog — EthioDirect'
    },
    'delivery.html': {
        'key': 'pages.delivery',
        'uk': 'Доставка та оплата — EthioDirect',
        'ru': 'Доставка и оплата — EthioDirect',
        'en': 'Shipping & Payment — EthioDirect'
    },
    'faq.html': {
        'key': 'pages.faq',
        'uk': 'Часті питання — EthioDirect',
        'ru': 'Частые вопросы — EthioDirect',
        'en': 'FAQ — EthioDirect'
    },
    'quiz.html': {
        'key': 'pages.quiz',
        'uk': 'Тест смаку — EthioDirect',
        'ru': 'Тест вкуса — EthioDirect',
        'en': 'Taste Quiz — EthioDirect'
    },
    'account.html': {
        'key': 'pages.account',
        'uk': 'Особистий кабінет — EthioDirect',
        'ru': 'Личный кабинет — EthioDirect',
        'en': 'My Account — EthioDirect'
    },
    'b2b.html': {
        'key': 'pages.b2b',
        'uk': 'B2B — EthioDirect',
        'ru': 'B2B — EthioDirect',
        'en': 'B2B — EthioDirect'
    },
    'gift-certificates.html': {
        'key': 'pages.gift',
        'uk': 'Подарункові сертифікати — EthioDirect',
        'ru': 'Подарочные сертификаты — EthioDirect',
        'en': 'Gift Cards — EthioDirect'
    }
}


def update_locales():
    """Add page title keys to locale files"""
    for lang in ['uk', 'ru', 'en']:
        json_path = LOCALES_DIR / f'{lang}.json'
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'pages' not in data:
            data['pages'] = {}
        
        added = 0
        for page, config in PAGE_TITLES.items():
            key_parts = config['key'].split('.')
            if len(key_parts) == 2 and key_parts[0] == 'pages':
                page_key = key_parts[1]
                if page_key not in data['pages']:
                    data['pages'][page_key] = config[lang]
                    added += 1
        
        if added > 0:
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"  Added {added} page titles to {lang}.json")


def update_html_files():
    """Add data-i18n-title attribute to html elements"""
    for page, config in PAGE_TITLES.items():
        filepath = PROJECT_ROOT / page
        if not filepath.exists():
            continue
        
        try:
            content = filepath.read_text(encoding='utf-8')
        except:
            continue
        
        # Check if already has data-i18n-title on html tag
        if 'data-i18n-title' in content[:500]:
            continue
        
        # Add data-i18n-title to <html> tag
        pattern = r'<html([^>]*)>'
        match = re.search(pattern, content)
        if match:
            existing_attrs = match.group(1)
            if 'data-i18n-title' not in existing_attrs:
                new_html = f'<html{existing_attrs} data-i18n-title="{config["key"]}">'
                content = re.sub(pattern, new_html, content, count=1)
                filepath.write_text(content, encoding='utf-8')
                print(f"  Added data-i18n-title to {page}")


def main():
    print("Adding page title translations...")
    print("=" * 60)
    update_locales()
    print("\nUpdating HTML files...")
    update_html_files()
    print("\nDone!")


if __name__ == '__main__':
    main()
