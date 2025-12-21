#!/usr/bin/env python3
"""
Comprehensive i18n fix script.
Adds data-i18n to all remaining hardcoded elements.
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
SKIP_FILES = {'footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html'}


def fix_social_links(content):
    """Add i18n to social link aria-labels."""
    replacements = [
        ('aria-label="Instagram"', 'aria-label="Instagram" data-i18n="social.instagram" data-i18n-aria'),
        ('aria-label="Facebook"', 'aria-label="Facebook" data-i18n="social.facebook" data-i18n-aria'),
        ('aria-label="Telegram"', 'aria-label="Telegram" data-i18n="social.telegram" data-i18n-aria'),
        ('aria-label="TikTok"', 'aria-label="TikTok" data-i18n="social.tiktok" data-i18n-aria'),
    ]
    for old, new in replacements:
        content = content.replace(old, new)
    return content


def fix_payment_icons(content):
    """Add i18n to payment method icon titles."""
    replacements = [
        ('title="Visa"', 'title="Visa" data-i18n="payment.visa" data-i18n-title'),
        ('title="Mastercard"', 'title="Mastercard" data-i18n="payment.mastercard" data-i18n-title'),
        ('title="Apple Pay"', 'title="Apple Pay" data-i18n="payment.apple_pay" data-i18n-title'),
        ('title="Google Pay"', 'title="Google Pay" data-i18n="payment.google_pay" data-i18n-title'),
        ('title="PrivatBank"', 'title="PrivatBank" data-i18n="payment.privatbank" data-i18n-title'),
    ]
    for old, new in replacements:
        content = content.replace(old, new)
    return content


def fix_menu_toggle(content):
    """Add i18n to menu toggle aria-label."""
    patterns = [
        (r'aria-label="[^"]*[Вв]ідкрити меню[^"]*"', 'aria-label="Open menu" data-i18n="common.open_menu" data-i18n-aria'),
        (r'aria-label="[Oo]pen menu"', 'aria-label="Open menu" data-i18n="common.open_menu" data-i18n-aria'),
    ]
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    return content


def fix_floating_buttons(content):
    """Ensure floating contact buttons have proper i18n."""
    # Already handled in previous script, but ensure title attributes are correct
    if 'title="Telegram"' in content and 'data-i18n="float_buttons.telegram"' not in content:
        content = content.replace(
            'title="Telegram"',
            'title="Telegram" data-i18n="float_buttons.telegram" data-i18n-title'
        )
    if 'title="Viber"' in content and 'data-i18n="float_buttons.viber"' not in content:
        content = content.replace(
            'title="Viber"',
            'title="Viber" data-i18n="float_buttons.viber" data-i18n-title'
        )
    return content


def fix_trust_badges(content):
    """Add i18n to trust badge text."""
    replacements = [
        ('>14 днів повернення<', ' data-i18n="footer.trust_return">14 днів повернення<'),
        ('>100% Specialty якість зерна<', ' data-i18n="footer.trust_specialty">100% Specialty якість зерна<'),
        ('>Безкоштовна доставка від 500₴<', ' data-i18n="footer.trust_shipping">Безкоштовна доставка від 500₴<'),
        ('>Свіжа обсмажка до 3 днів<', ' data-i18n="footer.trust_roast">Свіжа обсмажка до 3 днів<'),
    ]
    for old, new in replacements:
        if old in content and 'data-i18n="footer.trust' not in content.split(old)[0][-100:]:
            content = content.replace(old, new)
    return content


def add_dynamic_title_update(content):
    """Add script for dynamic page title update based on language."""
    if '</body>' in content and 'updatePageTitle' not in content:
        title_script = '''
    <!-- Dynamic page title update -->
    <script>
        document.addEventListener('languageChanged', function() {
            if (typeof t === 'function') {
                const pageKey = document.body.getAttribute('data-page-title');
                if (pageKey) {
                    document.title = t(pageKey);
                }
            }
        });
    </script>
'''
        # Only add to pages that don't have it
        if 'languageChanged' not in content.split('</body>')[0][-200:]:
            content = content.replace('</body>', title_script + '</body>')
    return content


def update_file(filepath):
    """Update a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        content = fix_social_links(content)
        content = fix_payment_icons(content)
        content = fix_menu_toggle(content)
        content = fix_floating_buttons(content)
        content = fix_trust_badges(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [UPDATED] {filepath.name}")
            return True
        else:
            print(f"  [OK] {filepath.name}")
            return False
            
    except Exception as e:
        print(f"  [ERROR] {filepath.name}: {e}")
        return False


def main():
    print("=" * 60)
    print("   COMPREHENSIVE I18N FIX")
    print("=" * 60)
    
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    html_files = [f for f in html_files if f.name not in SKIP_FILES]
    
    print(f"\nProcessing {len(html_files)} files...\n")
    
    updated = 0
    for filepath in sorted(html_files):
        if update_file(filepath):
            updated += 1
    
    print("\n" + "=" * 60)
    print(f"   DONE: Updated {updated} files")
    print("=" * 60)


if __name__ == '__main__':
    main()
