import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Old footer sections pattern (Trust Badges + Payment + Bottom Bar)
old_pattern = r'<!-- Trust Badges -->.*?</div>\s*</div>\s*\n\s*<!-- Payment Methods -->.*?</div>\s*</div>\s*\n\s*<!-- Bottom Bar -->.*?</div>\s*</div>'

new_footer = '''<!-- Compact Footer Bottom: Trust + Payment + Copyright -->
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

# Replace using regex with DOTALL flag
new_content = re.sub(old_pattern, new_footer, content, flags=re.DOTALL)

if new_content != content:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Footer replaced successfully!")
else:
    print("Pattern not found, trying alternative approach...")
    # Find the specific lines and replace
    lines = content.split('\n')
    start_idx = None
    end_idx = None
    
    for i, line in enumerate(lines):
        if '<!-- Trust Badges -->' in line:
            start_idx = i
        if start_idx and 'footer-bottom-right' in line:
            # Find closing divs after this
            for j in range(i, min(i+10, len(lines))):
                if '</div>' in lines[j] and '</div>' in lines[j+1] if j+1 < len(lines) else False:
                    end_idx = j + 2
                    break
            if end_idx:
                break
    
    if start_idx and end_idx:
        new_lines = lines[:start_idx] + [new_footer] + lines[end_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        print(f"Footer replaced! Lines {start_idx} to {end_idx}")
    else:
        print(f"Could not find boundaries: start={start_idx}, end={end_idx}")
