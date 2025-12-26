#!/usr/bin/env python3
"""
Fix footer structure in all article and blog pages.
Move Newsletter column inside footer-grid div.
"""
import os
import re

# Define the correct footer template (relative paths for articles/blog subfolders)
CORRECT_FOOTER = '''    <!-- FOOTER -->
    <footer class="footer-pro">
        <div class="container">
            <div class="footer-grid">
                <!-- Column 1: Brand -->
                <div class="footer-col">
                    <h4 style="font-family:var(--font-heading); font-size:1.5rem; color:white; margin-bottom:20px;">
                        <a href="../index.html" style="text-decoration:none; color:white;">EthioDirect</a>
                    </h4>
                    <p style="color:#aaa; line-height:1.8; margin-bottom:20px;" data-i18n="footer.description">Ми доставляємо справжню specialty каву прямо з ефіопських ферм до вашого дому.</p>
                    <div class="social-links">
                        <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                        <a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
                        <a href="#" aria-label="Telegram"><i class="fab fa-telegram"></i></a>
                        <a href="#" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                    </div>
                </div>
                <!-- Column 2: Shop -->
                <div class="footer-col">
                    <h4 data-i18n="footer.shop_title">Магазин</h4>
                    <ul class="footer-links">
                        <li><a href="../shop.html" data-i18n="footer.catalog">Весь каталог</a></li>
                        <li><a href="../subscription.html" data-i18n="footer.subscription">Підписка на каву</a></li>
                        <li><a href="../gift-certificates.html" data-i18n="nav.certificates">Сертифікати</a></li>
                        <li><a href="../b2b.html" data-i18n="footer.b2b">B2B рішення</a></li>
                    </ul>
                </div>
                <!-- Column 3: Support -->
                <div class="footer-col">
                    <h4 data-i18n="footer.support_title">Підтримка</h4>
                    <ul class="footer-links">
                        <li><a href="../delivery.html" data-i18n="footer.delivery">Доставка та оплата</a></li>
                        <li><a href="../faq.html" data-i18n="footer.faq">Часті питання</a></li>
                        <li><a href="../contacts.html" data-i18n="footer.contacts">Контакти</a></li>
                        <li><a href="../about.html" data-i18n="nav.about">Про нас</a></li>
                    </ul>
                </div>
                <!-- Column 4: Contacts -->
                <div class="footer-col">
                    <h4 data-i18n="footer.contacts_title">Контакти</h4>
                    <ul class="footer-contacts">
                        <li><i class="fas fa-phone"></i> <a href="tel:+380501234567">+380 (50) 123-45-67</a></li>
                        <li><i class="fas fa-envelope"></i> <a href="mailto:hello@ethiodirect.ua">hello@ethiodirect.ua</a></li>
                        <li><i class="fas fa-map-marker-alt"></i> <span data-i18n="footer.location">Одеса, Україна</span></li>
                        <li><i class="fas fa-clock"></i> <span data-i18n="topbar.hours">Пн-Пт: 9:00-18:00</span></li>
                    </ul>
                </div>
                <!-- Column 5: Newsletter -->
                <div class="footer-col">
                    <h4 data-i18n="footer.newsletter_title">Підписка на новини</h4>
                    <p style="color:#aaa; margin-bottom:15px; font-size:0.9rem;" data-i18n="footer.newsletter_text">Отримуйте акції, новинки та поради щодо заварювання</p>
                    <form class="newsletter-form" onsubmit="subscribeNewsletter(event)">
                        <input type="email" placeholder="Ваш email" data-i18n-placeholder="footer.newsletter_placeholder" required>
                        <button type="submit" class="btn-newsletter" data-i18n="footer.newsletter_cta">Підписатись</button>
                    </form>
                </div>
            </div>

            <!-- Trust Badges -->
            <div class="footer-trust">
                <div class="trust-badges">
                    <div class="trust-badge">
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
                    </div>
                </div>
            </div>

            <!-- Payment Methods -->
            <div class="footer-payment">
                <p style="color:#666; font-size:0.85rem; margin-bottom:15px;" data-i18n="footer.payment_methods">Способи оплати:</p>
                <div class="payment-icons">
                    <i class="fab fa-cc-visa" title="Visa"></i>
                    <i class="fab fa-cc-mastercard" title="Mastercard"></i>
                    <i class="fab fa-apple-pay" title="Apple Pay"></i>
                    <i class="fab fa-google-pay" title="Google Pay"></i>
                    <span class="payment-text">LiqPay</span>
                </div>
            </div>

            <!-- Bottom Bar -->
            <div class="footer-bottom">
                <div class="footer-bottom-left">
                    <p>&copy; 2025 EthioDirect. Всі права захищені.</p>
                </div>
                <div class="footer-bottom-right">
                    <a href="../privacy.html" data-i18n="footer.privacy">Політика конфіденційності</a>
                    <span>·</span>
                    <a href="../return.html" data-i18n="footer.terms">Умови повернення</a>
                </div>
            </div>
        </div>
    </footer>'''


def fix_footer_in_file(filepath):
    """Replace the footer in a file with the correct structure."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try different footer patterns
    patterns = [
        r'<!-- FOOTER -->.*?</footer>',
        r'<!-- PROFESSIONAL FOOTER COMPONENT -->.*?</footer>'
    ]
    
    for pattern in patterns:
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, CORRECT_FOOTER, content, flags=re.DOTALL)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[OK] Fixed: {filepath}")
            return True
    
    print(f"[SKIP] No footer found: {filepath}")
    return False


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Process articles folder
    articles_dir = os.path.join(base_dir, 'articles')
    if os.path.exists(articles_dir):
        for filename in os.listdir(articles_dir):
            if filename.endswith('.html'):
                fix_footer_in_file(os.path.join(articles_dir, filename))
    
    # Process blog folder
    blog_dir = os.path.join(base_dir, 'blog')
    if os.path.exists(blog_dir):
        for filename in os.listdir(blog_dir):
            if filename.endswith('.html') and not filename.startswith('_'):
                fix_footer_in_file(os.path.join(blog_dir, filename))


if __name__ == '__main__':
    main()
    print("\nDone! Footer fixed in all article and blog pages.")
