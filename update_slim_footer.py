"""
Update footer-compact-bottom to footer-slim-bottom across all HTML files
"""
import os
import re

NEW_FOOTER = '''            <!-- Compact Footer Bottom: Single-line elegant design -->
            <div class="footer-slim-bottom">
                <!-- Row 1: Trust badges + Payment icons -->
                <div class="footer-slim-row">
                    <div class="slim-trust">
                        <span><i class="fas fa-shield-alt"></i> <span data-i18n="footer.badge_return_days">14 днів</span> <span data-i18n="footer.badge_return">повернення</span></span>
                        <span><i class="fas fa-coffee"></i> <span data-i18n="footer.badge_specialty">100% Specialty</span></span>
                        <span><i class="fas fa-shipping-fast"></i> <span data-i18n="footer.badge_free">Безкоштовна</span> <span data-i18n="footer.badge_shipping">від 500₴</span></span>
                        <span><i class="fas fa-fire"></i> <span data-i18n="footer.badge_fresh">Свіжа обсмажка</span></span>
                    </div>
                    <div class="slim-payment">
                        <i class="fab fa-cc-visa"></i>
                        <i class="fab fa-cc-mastercard"></i>
                        <i class="fab fa-apple-pay"></i>
                        <i class="fab fa-google-pay"></i>
                        <span class="liqpay-badge">LiqPay</span>
                    </div>
                </div>
                <!-- Row 2: Copyright + Legal links in one line -->
                <div class="footer-slim-legal">
                    <span data-i18n="footer.copyright">&copy; 2025 EthioDirect. Всі права захищено.</span>
                    <span class="dot">·</span>
                    <a href="privacy.html" data-i18n="footer.privacy">Політика конфіденційності</a>
                    <span class="dot">·</span>
                    <a href="return.html" data-i18n="footer.terms">Умови повернення</a>
                    <span class="dot">·</span>
                    <a href="#" data-i18n="footer.offer">Договір оферти</a>
                </div>
            </div>'''

# Pattern to match the old footer-compact-bottom section
OLD_PATTERN = re.compile(
    r'<!-- Compact Footer Bottom:.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

# Alternative pattern for slightly different structures
OLD_PATTERN2 = re.compile(
    r'<div class="footer-compact-bottom">.*?</div>\s*</div>\s*</div>\s*</div>',
    re.DOTALL
)

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if already has the new footer
        if 'footer-slim-bottom' in content:
            print(f"SKIP (already updated): {filepath}")
            return False
        
        # Check if file has the old footer
        if 'footer-compact-bottom' not in content:
            print(f"SKIP (no footer-compact-bottom): {filepath}")
            return False
        
        # Try to replace with pattern matching
        # Find the start of footer-compact-bottom and end of its closing divs
        start_marker = '<!-- Compact Footer Bottom:'
        if start_marker not in content:
            start_marker = '<div class="footer-compact-bottom">'
        
        if start_marker in content:
            start_idx = content.find(start_marker)
            
            # Find the closing </footer> tag after this
            footer_end = content.find('</footer>', start_idx)
            if footer_end != -1:
                # Find the proper closing of the footer-compact-bottom div
                # We need to find multiple closing divs before </footer>
                section_end = footer_end
                
                # Replace the section
                # Find where the footer-compact-bottom content ends
                # by finding <!-- and </footer> after start
                temp_content = content[start_idx:footer_end]
                
                # Count opening divs to find matching closes
                new_content = content[:start_idx] + NEW_FOOTER + '\n    ' + content[footer_end:]
                
                # Verify the replacement looks reasonable
                if '</footer>' in new_content and 'footer-slim-bottom' in new_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"UPDATED: {filepath}")
                    return True
        
        print(f"FAILED to update: {filepath}")
        return False
        
    except Exception as e:
        print(f"ERROR {filepath}: {e}")
        return False

# Find all HTML files
base_dir = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect'
html_files = []

for root, dirs, files in os.walk(base_dir):
    # Skip blog directory (has different structure)
    if 'blog' in root:
        continue
    for filename in files:
        if filename.endswith('.html'):
            html_files.append(os.path.join(root, filename))

# Also add articles
articles_dir = os.path.join(base_dir, 'articles')
if os.path.exists(articles_dir):
    for filename in os.listdir(articles_dir):
        if filename.endswith('.html'):
            html_files.append(os.path.join(articles_dir, filename))

print(f"Found {len(html_files)} HTML files to check")
updated = 0
for filepath in html_files:
    if update_file(filepath):
        updated += 1

print(f"\nDone! Updated {updated} files.")
