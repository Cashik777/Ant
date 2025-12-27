#!/usr/bin/env python3
"""
Add cart.more_items translation and remove emojis from all HTML files
"""
import json
import os
import re

base_dir = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect'
locales_dir = os.path.join(base_dir, 'locales')

# Add cart.more_items to all common.json files
cart_additions = {
    'uk': {"more_items": "+ ще {count} товарів"},
    'en': {"more_items": "+ {count} more items"},
    'ru': {"more_items": "+ ещё {count} товаров"}
}

for lang, additions in cart_additions.items():
    filepath = os.path.join(locales_dir, lang, 'common.json')
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if 'cart' in data:
            data['cart'].update(additions)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"[OK] Added cart translations to {lang}/common.json")
    except Exception as e:
        print(f"[ERROR] {lang}/common.json: {e}")

# Replace emojis with FontAwesome icons in all HTML files
emoji_replacements = [
    ('🔥', '<i class="fas fa-fire" style="color:#e74c3c;"></i>'),
    ('☕', '<i class="fas fa-coffee" style="color:#8B4545;"></i>'),
    ('⚡', '<i class="fas fa-bolt" style="color:#f39c12;"></i>'),
    ('🎁', '<i class="fas fa-gift" style="color:#9b59b6;"></i>'),
    ('⭐', '<i class="fas fa-star" style="color:#f39c12;"></i>'),
    ('💳', '<i class="fas fa-credit-card"></i>'),
    ('🚚', '<i class="fas fa-truck"></i>'),
    ('💰', '<i class="fas fa-tag"></i>'),
    ('🌍', '<i class="fas fa-globe"></i>'),
    ('🎉', '<i class="fas fa-gift"></i>'),
    ('👋', ''),
    ('✓', '<i class="fas fa-check"></i>'),
    ('<span>🍓</span>', ''),
    ('<span>🍫</span>', ''),
    ('<span>🌸</span>', ''),
]

def fix_html_file(filepath):
    """Remove/replace emojis in HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        for emoji, replacement in emoji_replacements:
            content = content.replace(emoji, replacement)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[FIXED] {os.path.basename(filepath)}")
            return True
        return False
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return False

# Process all HTML files
html_files = []
for root, dirs, files in os.walk(base_dir):
    if '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

fixed_count = 0
for filepath in sorted(html_files):
    if fix_html_file(filepath):
        fixed_count += 1

print(f"\nFixed {fixed_count} HTML files")
