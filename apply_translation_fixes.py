#!/usr/bin/env python3
"""
Apply translation fixes to all HTML pages:
1. Update top-bar elements with data-i18n attributes
2. Update search input with data-i18n-placeholder 
3. Update floating contact buttons with data-i18n-title
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

# Skip template files
SKIP_FILES = {'footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html', '_header_template.html'}

def fix_top_bar(content):
    """Fix top-bar elements to have proper data-i18n attributes."""
    
    # Pattern for top-bar-left phone and hours
    old_phone = r'<span><i class="fas fa-phone-alt"></i> \+380 \(50\) 123-45-67</span>'
    new_phone = '<span><i class="fas fa-phone-alt"></i> <span data-i18n="topbar.phone">+380 (50) 123-45-67</span></span>'
    content = re.sub(old_phone, new_phone, content)
    
    old_hours = r'<span><i class="fas fa-clock"></i> Пн-Пт: 9:00-18:00</span>'
    new_hours = '<span><i class="fas fa-clock"></i> <span data-i18n="topbar.hours">Пн-Пт: 9:00-18:00</span></span>'
    content = re.sub(old_hours, new_hours, content)
    
    # Pattern for promo ticker - АКЦІЯ line
    old_action = r'<span class="ticker-item">🔥 <strong>АКЦІЯ:</strong> безкоштовна доставка від 500₴</span>'
    new_action = '<span class="ticker-item">🔥 <strong data-i18n="topbar.promo_action">АКЦІЯ:</strong> <span data-i18n="topbar.promo_delivery">безкоштовна доставка від 500₴</span></span>'
    content = re.sub(old_action, new_action, content)
    
    # Pattern for subscription promo
    old_sub = r'<span class="ticker-item">☕ Підписка: <strong>-10%</strong> на кожну доставку</span>'
    new_sub = '<span class="ticker-item">☕ <span data-i18n="topbar.promo_subscription">Підписка:</span> <strong data-i18n="topbar.promo_subscription_text">-10% на кожну доставку</strong></span>'
    content = re.sub(old_sub, new_sub, content)
    
    # Pattern for fresh roast promo
    old_roast = r'<span class="ticker-item">⚡ Свіжа обсмажка <strong>до 3 днів</strong></span>'
    new_roast = '<span class="ticker-item">⚡ <span data-i18n="topbar.promo_roast">Свіжа обсмажка</span> <strong data-i18n="topbar.promo_roast_days">до 3 днів</strong></span>'
    content = re.sub(old_roast, new_roast, content)
    
    return content

def fix_search_input(content):
    """Fix search input to have data-i18n-placeholder attribute."""
    
    # Pattern for search input without data-i18n
    pattern = r'<input type="text" class="search-input" id="search-input" placeholder="Пошук кави\.\.\."\s*oninput="handleSearch\(this\.value\)">'
    replacement = '<input type="text" class="search-input" id="search-input" placeholder="Пошук кави..."\n                        data-i18n="search.placeholder" data-i18n-placeholder\n                        oninput="handleSearch(this.value)">'
    content = re.sub(pattern, replacement, content)
    
    return content

def fix_floating_buttons(content):
    """Fix floating contact buttons to have data-i18n-title attribute."""
    
    # Telegram button
    old_telegram = r'<a href="https://t\.me/ethiodirect" class="float-btn telegram" title="Написати в Telegram">'
    new_telegram = '<a href="https://t.me/ethiodirect" class="float-btn telegram" title="Написати в Telegram" data-i18n="float_buttons.telegram" data-i18n-title>'
    content = re.sub(old_telegram, new_telegram, content)
    
    # Viber button
    old_viber = r'<a href="viber://chat\?number=\+380501234567" class="float-btn viber" title="Написати в Viber">'
    new_viber = '<a href="viber://chat?number=+380501234567" class="float-btn viber" title="Написати в Viber" data-i18n="float_buttons.viber" data-i18n-title>'
    content = re.sub(old_viber, new_viber, content)
    
    # Phone button
    old_phone = r'<a href="tel:\+380501234567" class="float-btn phone" title="Зателефонувати">'
    new_phone = '<a href="tel:+380501234567" class="float-btn phone" title="Зателефонувати" data-i18n="float_buttons.phone" data-i18n-title>'
    content = re.sub(old_phone, new_phone, content)
    
    return content

def fix_html_file(filepath):
    """Fix a single HTML file for translation system."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Skip if already has the new data-i18n attributes in top-bar
        if 'data-i18n="topbar.promo_action"' in content:
            print(f"  [SKIP] {filepath.name} (already fixed)")
            return False
        
        # Apply fixes
        content = fix_top_bar(content)
        content = fix_search_input(content)
        content = fix_floating_buttons(content)
        
        # Check if changes were made
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [FIXED] {filepath.name}")
            return True
        else:
            print(f"  [OK] {filepath.name}")
            return False
            
    except Exception as e:
        print(f"  [ERROR] {filepath.name}: {e}")
        return False

def main():
    print("=" * 60)
    print("Applying Translation Fixes to All HTML Pages")
    print("=" * 60)
    
    # Find all HTML files
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    html_files = [f for f in html_files if f.name not in SKIP_FILES]
    
    print(f"\nProcessing {len(html_files)} HTML files...\n")
    
    fixed = 0
    for filepath in sorted(html_files):
        if fix_html_file(filepath):
            fixed += 1
    
    print("\n" + "=" * 60)
    print(f"DONE! Fixed {fixed} files")
    print("=" * 60)

if __name__ == '__main__':
    main()
