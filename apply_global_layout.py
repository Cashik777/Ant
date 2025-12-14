import os
import re

# The "Gold Standard" Header (Fixed: Removed inline style from Certificates)
HEADER_TEMPLATE = """    <header class="header">
        <div class="container header-inner">
            <a href="index.html" class="logo">
                <i class="fas fa-leaf text-accent"></i>
                <span style="font-family:var(--font-heading); letter-spacing:1px; font-size:1.5rem;">EthioDirect</span>
            </a>
            <nav class="nav-desktop">
                <a href="shop.html" class="nav-link">Каталог</a>
                <a href="subscription.html" class="nav-link">Підписка</a>
                <a href="gift-certificates.html" class="nav-link">🎁 Сертифікати</a>
                <a href="blog.html" class="nav-link">Історії</a>
                <a href="about.html" class="nav-link">Про нас</a>
                <a href="quiz.html" class="nav-link">Тест</a>
            </nav>
            <div class="header-actions">
                <a href="account.html"><i class="far fa-user"></i></a>
                <div class="cart-trigger"><i class="fas fa-shopping-cart"></i><span class="cart-count">0</span></div>
            </div>
            <button class="menu-toggle" aria-label="Menu"><i class="fas fa-bars"></i></button>
        </div>
    </header>"""

# The "Gold Standard" Footer (Professional v2)
FOOTER_TEMPLATE = """<footer class="footer-pro">
    <div class="container">
        <!-- Main Footer Content -->
        <div class="footer-grid">
            <!-- Column 1: Brand -->
            <div class="footer-col">
                <h4 style="font-family:var(--font-heading); font-size:1.5rem; color:white; margin-bottom:20px;">
                    <a href="index.html" style="text-decoration:none; color:white;">EthioDirect</a>
                </h4>
                <p style="color:#aaa; line-height:1.8; margin-bottom:20px;">Ми доставляємо справжню specialty каву прямо
                    з ефіопських ферм до вашого дому. Свіжа обсмажка, чесна ціна, любов до кави.</p>
                <div class="social-links">
                    <a href="#" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                    <a href="#" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
                    <a href="#" aria-label="Telegram"><i class="fab fa-telegram"></i></a>
                    <a href="#" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                </div>
            </div>

            <!-- Column 2: Shop -->
            <div class="footer-col">
                <h4>Магазин</h4>
                <ul class="footer-links">
                    <li><a href="shop.html">Весь каталог</a></li>
                    <li><a href="subscription.html">Підписка на каву</a></li>
                    <li><a href="gift-certificates.html">Сертифікати</a></li>
                    <li><a href="b2b.html">B2B рішення</a></li>
                    <li><a href="account.html">Особистий кабінет</a></li>
                </ul>
            </div>

            <!-- Column 3: Support -->
            <div class="footer-col">
                <h4>Підтримка</h4>
                <ul class="footer-links">
                    <li><a href="delivery.html">Доставка та оплата</a></li>
                    <li><a href="return.html">Повернення та обмін</a></li>
                    <li><a href="faq.html">Часті питання</a></li>
                    <li><a href="contacts.html">Контакти</a></li>
                    <li><a href="about.html">Про нас</a></li>
                </ul>
            </div>

            <!-- Column 4: Contacts -->
            <div class="footer-col">
                <h4>Контакти</h4>
                <ul class="footer-contacts">
                    <li><i class="fas fa-phone"></i> <a href="tel:+380501234567">+380 (50) 123-45-67</a></li>
                    <li><i class="fas fa-envelope"></i> <a href="mailto:hello@ethiodirect.ua">hello@ethiodirect.ua</a>
                    </li>
                    <li><i class="fas fa-map-marker-alt"></i> Одеса, Україна</li>
                    <li><i class="fas fa-clock"></i> Пн-Пт: 9:00-18:00</li>
                </ul>
            </div>

            <!-- Column 5: Newsletter -->
            <div class="footer-col">
                <h4>Підписка на новини</h4>
                <p style="color:#aaa; margin-bottom:15px; font-size:0.9rem;">Отримуйте акції, новинки та поради щодо
                    заварювання</p>
                <form class="newsletter-form" onsubmit="subscribeNewsletter(event)">
                    <input type="email" placeholder="Ваш email" required>
                    <button type="submit" class="btn-newsletter">Підписатись</button>
                </form>
            </div>
        </div>

        <!-- Trust Badges -->
        <div class="footer-trust">
            <div class="trust-badges">
                <div class="trust-badge">
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
                </div>
            </div>
        </div>

        <!-- Payment Methods -->
        <div class="footer-payment">
            <p style="color:#666; font-size:0.85rem; margin-bottom:15px;">Способи оплати:</p>
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
                <a href="privacy.html">Політика конфіденційності</a>
                <span>·</span>
                <a href="return.html">Умови повернення</a>
                <span>·</span>
                <a href="#">Публічна оферта</a>
            </div>
        </div>
    </div>
</footer>"""

def apply_layout():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace Header
        # Regex to find <header class="header">...</header> (non-greedy)
        # Note: We need to be careful if header has dynamic active states.
        # Ideally, we should inject the "active" class based on filename.
        
        # 1. Remove existing header
        content = re.sub(r'<header class="header">.*?</header>', '[[HEADER_PLACEHOLDER]]', content, flags=re.DOTALL)
        
        # 2. Remove existing footer (generic or pro)
        content = re.sub(r'<footer.*?>.*?</footer>', '[[FOOTER_PLACEHOLDER]]', content, flags=re.DOTALL)
        
        # 3. Insert new Header
        # Add 'active' class logic
        header_to_insert = HEADER_TEMPLATE
        if filename == 'index.html':
            pass # No link is active on home usually, or logo?
        elif filename == 'shop.html':
            header_to_insert = header_to_insert.replace('href="shop.html" class="nav-link"', 'href="shop.html" class="nav-link active"')
        elif filename == 'subscription.html':
            header_to_insert = header_to_insert.replace('href="subscription.html" class="nav-link"', 'href="subscription.html" class="nav-link active"')
        elif filename == 'gift-certificates.html':
            header_to_insert = header_to_insert.replace('href="gift-certificates.html" class="nav-link"', 'href="gift-certificates.html" class="nav-link active"')
        elif filename == 'blog.html':
            header_to_insert = header_to_insert.replace('href="blog.html" class="nav-link"', 'href="blog.html" class="nav-link active"')
        elif filename == 'about.html':
            header_to_insert = header_to_insert.replace('href="about.html" class="nav-link"', 'href="about.html" class="nav-link active"')
        elif filename == 'quiz.html':
             header_to_insert = header_to_insert.replace('href="quiz.html" class="nav-link"', 'href="quiz.html" class="nav-link active"')
        
        content = content.replace('[[HEADER_PLACEHOLDER]]', header_to_insert)
        
        # 4. Insert new Footer
        content = content.replace('[[FOOTER_PLACEHOLDER]]', FOOTER_TEMPLATE)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

if __name__ == "__main__":
    apply_layout()
