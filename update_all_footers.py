import re
import os
from pathlib import Path

# New compact footer HTML
NEW_FOOTER = '''<!-- Compact Footer Bottom: Trust + Payment + Copyright -->
            <div class="footer-compact-bottom">
                <div class="footer-compact-row">
                    <!-- Trust badges inline -->
                    <div class="compact-trust">
                        <span class="trust-item"><i class="fas fa-shield-alt"></i> <span data-i18n="footer.badge_return_days">14 днів</span> <span data-i18n="footer.badge_return">повернення</span></span>
                        <span class="trust-item"><i class="fas fa-coffee"></i> <span data-i18n="footer.badge_specialty">100% Specialty</span></span>
                        <span class="trust-item"><i class="fas fa-shipping-fast"></i> <span data-i18n="footer.badge_free">Безкоштовна</span> <span data-i18n="footer.badge_shipping">від 500₴</span></span>
                        <span class="trust-item"><i class="fas fa-fire"></i> <span data-i18n="footer.badge_fresh">Свіжа обсмажка</span></span>
                    </div>
                    
                    <!-- Payment icons -->
                    <div class="compact-payment">
                        <i class="fab fa-cc-visa" title="Visa"></i>
                        <i class="fab fa-cc-mastercard" title="Mastercard"></i>
                        <i class="fab fa-apple-pay" title="Apple Pay"></i>
                        <i class="fab fa-google-pay" title="Google Pay"></i>
                        <span class="payment-liqpay">LiqPay</span>
                    </div>
                </div>
                
                <div class="footer-compact-legal">
                    <span data-i18n="footer.copyright">&copy; 2025 EthioDirect. Всі права захищено.</span>
                    <span class="legal-divider">|</span>
                    <a href="privacy.html" data-i18n="footer.privacy">Політика конфіденційності</a>
                    <a href="return.html" data-i18n="footer.terms">Умови повернення</a>
                    <a href="#" data-i18n="footer.offer">Договір оферти</a>
                </div>
            </div>'''

# Patterns for old footer sections
OLD_FOOTER_PATTERN = re.compile(
    r'<!-- Trust Badges -->.*?</div>\s*</div>\s*\n\s*'
    r'<!-- Payment Methods -->.*?</div>\s*</div>\s*\n\s*'
    r'<!-- Bottom Bar -->.*?</div>\s*</div>',
    re.DOTALL
)

ALT_PATTERN = re.compile(
    r'<div class="footer-trust">.*?</div>\s*</div>\s*\n\s*'
    r'<div class="footer-payment">.*?</div>\s*</div>\s*\n\s*'
    r'<div class="footer-bottom">.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

SKIP_FILES = ['footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html', '_header_template.html', 'concept_demo.html']

def read_file_any_encoding(filepath):
    """Try multiple encodings to read file"""
    encodings = ['utf-8', 'utf-8-sig', 'cp1251', 'windows-1251', 'latin-1']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read(), enc
        except (UnicodeDecodeError, UnicodeError):
            continue
    # Last resort - binary with errors ignored
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        return f.read(), 'utf-8-replace'

def update_footer(filepath):
    try:
        content, original_enc = read_file_any_encoding(filepath)
        
        # Skip if already has compact footer
        if 'footer-compact-bottom' in content:
            return 'ALREADY_UPDATED'
        
        # Skip if no footer at all
        if 'footer-trust' not in content and 'Trust Badges' not in content:
            return 'NO_FOOTER'
        
        # Try main pattern
        new_content = OLD_FOOTER_PATTERN.sub(NEW_FOOTER, content)
        
        # If no change, try alternative
        if new_content == content:
            new_content = ALT_PATTERN.sub(NEW_FOOTER, content)
        
        if new_content != content:
            # Save as UTF-8 (normalize encoding)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return f'UPDATED (was {original_enc})'
        else:
            return 'PATTERN_NOT_MATCHED'
    except Exception as e:
        return f'ERROR: {e}'

# Find all HTML files
base_dir = Path('.')
html_files = list(base_dir.glob('*.html')) + list(base_dir.glob('**/*.html'))

updated = 0
skipped = 0
errors = []

for filepath in html_files:
    filename = filepath.name
    if filename in SKIP_FILES:
        print(f"SKIP: {filepath}")
        skipped += 1
        continue
    
    result = update_footer(filepath)
    
    if 'UPDATED' in result:
        print(f"OK: {filepath} - {result}")
        updated += 1
    elif result == 'ALREADY_UPDATED':
        print(f"DONE: {filepath}")
        skipped += 1
    elif result == 'NO_FOOTER':
        print(f"SKIP: {filepath}")
        skipped += 1
    else:
        print(f"ERR: {filepath} - {result}")
        errors.append((filepath, result))

print(f"\n=== RESULT ===")
print(f"Updated: {updated}")
print(f"Skipped: {skipped}")
print(f"Errors: {len(errors)}")
