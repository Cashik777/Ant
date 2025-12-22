#!/usr/bin/env python3
"""Add data-i18n to footer trust badges across all HTML files"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

# Old pattern (without i18n)
OLD_TRUST_BLOCK = '''<div class="trust-badge">
                        <i class="fas fa-shield-alt"></i>
                        <div>
                            <strong>14 днів</strong>
                            <span>повернення</span>
                        </div>
                    </div>
                    <div class="trust-badge">
                        <i class="fas fa-coffee"></i>
                        <div>
                            <strong>100% Specialty</strong>
                            <span>якість зерна</span>
                        </div>
                    </div>
                    <div class="trust-badge">
                        <i class="fas fa-shipping-fast"></i>
                        <div>
                            <strong>Безкоштовна</strong>
                            <span>доставка від 500₴</span>
                        </div>
                    </div>
                    <div class="trust-badge">
                        <i class="fas fa-fire"></i>
                        <div>
                            <strong>Свіжа обсмажка</strong>
                            <span>до 3 днів</span>
                        </div>
                    </div>'''

# New pattern (with i18n)
NEW_TRUST_BLOCK = '''<div class="trust-badge">
                        <i class="fas fa-shield-alt"></i>
                        <div>
                            <strong data-i18n="footer.badge_return_days">14 днів</strong>
                            <span data-i18n="footer.badge_return">повернення</span>
                        </div>
                    </div>
                    <div class="trust-badge">
                        <i class="fas fa-coffee"></i>
                        <div>
                            <strong data-i18n="footer.badge_specialty">100% Specialty</strong>
                            <span data-i18n="footer.badge_quality">якість зерна</span>
                        </div>
                    </div>
                    <div class="trust-badge">
                        <i class="fas fa-shipping-fast"></i>
                        <div>
                            <strong data-i18n="footer.badge_free">Безкоштовна</strong>
                            <span data-i18n="footer.badge_shipping">доставка від 500₴</span>
                        </div>
                    </div>
                    <div class="trust-badge">
                        <i class="fas fa-fire"></i>
                        <div>
                            <strong data-i18n="footer.badge_fresh">Свіжа обсмажка</strong>
                            <span data-i18n="footer.badge_days">до 3 днів</span>
                        </div>
                    </div>'''


def fix_file(filepath):
    """Fix trust badges in a single file"""
    try:
        content = filepath.read_text(encoding='utf-8')
    except:
        return False
    
    if 'trust-badge' not in content:
        return False
    
    # Check if already fixed
    if 'footer.badge_return_days' in content:
        return False
    
    # Try to find and replace the trust block using regex
    # Pattern: find trust-badges div with its content
    pattern = r'(<div class="trust-badge">\s*<i class="fas fa-shield-alt"></i>\s*<div>\s*<strong>14 днів</strong>)'
    
    if re.search(pattern, content):
        # Replace the entire block
        content = content.replace(OLD_TRUST_BLOCK, NEW_TRUST_BLOCK)
        filepath.write_text(content, encoding='utf-8')
        return True
    
    return False


def main():
    print("Fixing footer trust badges with i18n...")
    print("=" * 60)
    
    fixed = 0
    for filepath in PROJECT_ROOT.rglob('*.html'):
        if fix_file(filepath):
            print(f"  [+] Fixed {filepath.relative_to(PROJECT_ROOT)}")
            fixed += 1
    
    print("=" * 60)
    print(f"Fixed {fixed} files")


if __name__ == '__main__':
    main()
