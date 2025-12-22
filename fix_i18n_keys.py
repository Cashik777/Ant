#!/usr/bin/env python3
"""
Fix i18n keys in HTML files to match JSON structure.
Converts underscore keys to dot notation (shop_title -> shop.title)
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

# Mapping of old keys to new keys (underscore to dot notation)
KEY_MAPPINGS = {
    # Cart
    'cart_title': 'cart.title',
    'cart_total': 'cart.subtotal',
    'cart_checkout': 'cart.checkout',
    'cart_secure': 'cart.secure_payment',
    'cart_free_shipping': 'cart.free_shipping_progress',
    'cart_empty': 'cart.empty',
    
    # Shop
    'shop_title': 'shop.title',
    'shop_subtitle': 'shop.subtitle',
    'filter_roast': 'shop.filter_roast',
    'filter_taste': 'shop.filter_taste',
    'filter_price': 'shop.filter_price',
    'filter_light': 'shop.roast_light',
    'filter_medium': 'shop.roast_medium',
    'filter_dark': 'shop.roast_dark',
    'sort_label': 'shop.sort',
    
    # Product
    'product_bestseller': 'product.bestseller',
    'product_new': 'product.new',
    'product_stock_left': 'product.stock_left',
    'product_add_to_cart': 'product.add_to_cart',
    'product_quick_view': 'product.quick_view',
    
    # Common
    'common_close': 'common.close',
    'common_loading': 'common.loading',
    
    # Account
    'account_title': 'account.page_title',
    'account_login': 'account.login',
    'account_register': 'account.register',
    
    # Delivery
    'delivery_title': 'delivery.page_title',
    
    # FAQ
    'faq_title': 'faq.page_title',
    
    # Contacts
    'contacts_title': 'contacts.page_title',
    
    # About
    'about_title': 'about.page_title',
}

# Additional patterns to fix (regex-based)
PATTERN_REPLACEMENTS = [
    # subscription_page. -> subscription_page.
    # These are already correct in JSON
]


def fix_file(filepath):
    """Fix i18n keys in a single file"""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return False
    
    original = content
    changes = 0
    
    # Apply direct key mappings
    for old_key, new_key in KEY_MAPPINGS.items():
        # Match data-i18n="old_key" or data-i18n='old_key'
        pattern = f'data-i18n=["\']({re.escape(old_key)})["\']'
        replacement = f'data-i18n="{new_key}"'
        
        new_content = re.sub(pattern, replacement, content)
        if new_content != content:
            changes += content.count(f'data-i18n="{old_key}"')
            changes += content.count(f"data-i18n='{old_key}'")
            content = new_content
    
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return changes
    return 0


def add_missing_shop_subtitle():
    """Add shop.subtitle to JSON if missing"""
    for lang in ['uk', 'ru', 'en']:
        json_path = PROJECT_ROOT / 'locales' / f'{lang}.json'
        try:
            import json
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'shop' in data and 'subtitle' not in data['shop']:
                if lang == 'uk':
                    data['shop']['subtitle'] = 'Оберіть свій ідеальний смак'
                elif lang == 'ru':
                    data['shop']['subtitle'] = 'Выберите свой идеальный вкус'
                else:
                    data['shop']['subtitle'] = 'Choose your perfect taste'
                
                with open(json_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                print(f"  Added shop.subtitle to {lang}.json")
        except Exception as e:
            print(f"  Error updating {lang}.json: {e}")


def main():
    print("Fixing i18n keys in HTML files...")
    print("=" * 60)
    
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    total_changes = 0
    files_changed = 0
    
    for filepath in html_files:
        # Skip template files
        if 'template' in filepath.name.lower():
            continue
            
        changes = fix_file(filepath)
        if changes:
            rel_path = filepath.relative_to(PROJECT_ROOT)
            print(f"  [+] {rel_path}: {changes} key(s) fixed")
            total_changes += changes
            files_changed += 1
    
    print("=" * 60)
    print(f"Fixed {total_changes} keys in {files_changed} files")
    
    # Add missing JSON keys
    print("\nUpdating JSON files...")
    add_missing_shop_subtitle()
    
    print("\nDone!")


if __name__ == '__main__':
    main()
