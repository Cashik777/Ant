import re
import os
from pathlib import Path

# New compact footer - ONLY the bottom part (trust + payment + copyright)
NEW_FOOTER_BOTTOM = '''<!-- Compact Footer Bottom: Trust + Payment + Copyright -->
            <div class="footer-compact-bottom">
                <div class="footer-compact-row">
                    <div class="compact-trust">
                        <span class="trust-item"><i class="fas fa-shield-alt"></i> <span data-i18n="footer.badge_return_days">14 днів</span> <span data-i18n="footer.badge_return">повернення</span></span>
                        <span class="trust-item"><i class="fas fa-coffee"></i> <span data-i18n="footer.badge_specialty">100% Specialty</span></span>
                        <span class="trust-item"><i class="fas fa-shipping-fast"></i> <span data-i18n="footer.badge_free">Безкоштовна</span> <span data-i18n="footer.badge_shipping">від 500₴</span></span>
                        <span class="trust-item"><i class="fas fa-fire"></i> <span data-i18n="footer.badge_fresh">Свіжа обсмажка</span></span>
                    </div>
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
            </div>
        </div>
    </footer>'''

SKIP_FILES = ['footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html', '_header_template.html', 'concept_demo.html']

def read_file_any_encoding(filepath):
    encodings = ['utf-8', 'utf-8-sig', 'cp1251', 'windows-1251', 'latin-1']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read(), enc
        except (UnicodeDecodeError, UnicodeError):
            continue
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        return f.read(), 'utf-8-replace'

def update_footer_safe(filepath):
    """Safely replace only footer-trust through </footer> section"""
    try:
        content, original_enc = read_file_any_encoding(filepath)
        
        # Skip if already has compact footer
        if 'footer-compact-bottom' in content:
            return 'ALREADY_DONE'
        
        # Look for footer-trust section and replace everything from there to </footer>
        # Pattern: from <div class="footer-trust"> OR <!-- Trust Badges --> to </footer>
        pattern = re.compile(
            r'(<!--\s*Trust Badges\s*-->|<div class="footer-trust">).*?</footer>',
            re.DOTALL
        )
        
        if not pattern.search(content):
            return 'NO_FOOTER_PATTERN'
        
        new_content = pattern.sub(NEW_FOOTER_BOTTOM, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return f'UPDATED (was {original_enc})'
        return 'NO_CHANGE'
        
    except Exception as e:
        return f'ERROR: {e}'

# Process only articles folder
articles_dir = Path('articles')
html_files = list(articles_dir.glob('*.html'))

updated = 0
skipped = 0
errors = []

print("Updating articles safely...")
for filepath in html_files:
    if filepath.name in SKIP_FILES:
        print(f"SKIP: {filepath}")
        skipped += 1
        continue
    
    result = update_footer_safe(filepath)
    
    if 'UPDATED' in result:
        print(f"OK: {filepath}")
        updated += 1
    elif result == 'ALREADY_DONE':
        print(f"DONE: {filepath}")
        skipped += 1
    elif result == 'NO_FOOTER_PATTERN':
        print(f"SKIP: {filepath} (no footer)")
        skipped += 1
    else:
        print(f"ERR: {filepath} - {result}")
        errors.append((filepath, result))

print(f"\n=== ARTICLES RESULT ===")
print(f"Updated: {updated}")
print(f"Skipped: {skipped}")
print(f"Errors: {len(errors)}")
