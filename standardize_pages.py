#!/usr/bin/env python3
"""
Script to standardize header and footer across all HTML pages.
Uses index.html as the template.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect")

# Standard Top Bar
TOP_BAR = '''    <!-- TOP BAR -->
    <div class="top-bar">
        <div class="container top-bar-inner">
            <div class="top-bar-left">
                <span><i class="fas fa-phone-alt"></i> +380 (50) 123-45-67</span>
                <span class="divider-dot">•</span>
                <span><i class="fas fa-clock"></i> Пн-Пт: 9:00-18:00</span>
            </div>
            <div class="top-bar-center">
                <div class="promo-ticker">
                    <span class="ticker-item">🔥 <strong>АКЦІЯ:</strong> безкоштовна доставка від 500₴</span>
                    <span class="ticker-divider">|</span>
                    <span class="ticker-item">☕ Підписка: <strong>-10%</strong> на кожну доставку</span>
                    <span class="ticker-divider">|</span>
                    <span class="ticker-item">⚡ Свіжа обсмажка <strong>до 3 днів</strong></span>
                </div>
            </div>
            <div class="top-bar-right">
                <a href="#" class="lang-switch active" onclick="switchLang('uk'); return false;">UA</a>
                <a href="#" class="lang-switch" onclick="switchLang('ru'); return false;">RU</a>
                <a href="#" class="lang-switch" onclick="switchLang('en'); return false;">EN</a>
            </div>
        </div>
    </div>'''

# Standard Header (with active link placeholder)
def get_header(active_page=''):
    active = {
        'shop.html': ' class="nav-link active"' if active_page == 'shop.html' else ' class="nav-link"',
        'subscription.html': ' class="nav-link active"' if active_page == 'subscription.html' else ' class="nav-link"',
        'gift-certificates.html': ' class="nav-link active"' if active_page == 'gift-certificates.html' else ' class="nav-link"',
        'blog.html': ' class="nav-link active"' if active_page == 'blog.html' else ' class="nav-link"',
        'about.html': ' class="nav-link active"' if active_page == 'about.html' else ' class="nav-link"',
        'quiz.html': ' class="nav-link active"' if active_page == 'quiz.html' else ' class="nav-link"',
    }
    return f'''    <!-- HEADER -->
    <header class="header">
        <div class="container header-inner">
            <a href="index.html" class="logo">
                <i class="fas fa-certificate"></i> ETHIODIRECT
            </a>

            <nav class="nav-desktop">
                <a href="shop.html"{active.get('shop.html', ' class="nav-link"')}>Каталог</a>
                <a href="subscription.html"{active.get('subscription.html', ' class="nav-link"')}>Підписка</a>
                <a href="gift-certificates.html"{active.get('gift-certificates.html', ' class="nav-link"')}>Сертифікати</a>
                <a href="blog.html"{active.get('blog.html', ' class="nav-link"')}>Історії</a>
                <a href="about.html"{active.get('about.html', ' class="nav-link"')}>Про нас</a>
                <a href="quiz.html"{active.get('quiz.html', ' class="nav-link"')}>Тест</a>
            </nav>

            <!-- Search Bar -->
            <div class="header-search">
                <div class="search-wrapper">
                    <input type="text" class="search-input" id="search-input" placeholder="Пошук кави..."
                        oninput="handleSearch(this.value)">
                    <button class="search-btn"><i class="fas fa-search"></i></button>
                    <div class="search-results" id="search-results"></div>
                </div>
            </div>

            <div class="header-actions">
                <a href="account.html"><i class="far fa-user"></i></a>

                <!-- Cart with Mini-Cart Dropdown -->
                <div class="cart-wrapper">
                    <div class="cart-trigger" onclick="openDrawer()">
                        <i class="fas fa-shopping-bag" style="font-size:1.2rem;"></i>
                        <span class="cart-count">0</span>
                    </div>
                    <div class="mini-cart" id="mini-cart">
                        <div class="mini-cart-header">
                            <h4>Ваш кошик</h4>
                            <span class="mini-cart-count" id="mini-cart-count">0 товарів</span>
                        </div>
                        <div class="mini-cart-items" id="mini-cart-items"></div>
                        <div class="mini-cart-footer" id="mini-cart-footer">
                            <div class="mini-cart-subtotal">
                                <strong>Разом:</strong>
                                <span id="mini-cart-total">0 ₴</span>
                            </div>
                            <div class="mini-cart-shipping" id="mini-cart-shipping">
                                <i class="fas fa-truck"></i> До безкоштовної доставки: <strong>500 ₴</strong>
                            </div>
                            <button class="mini-cart-btn" onclick="openDrawer()">
                                <i class="fas fa-shopping-cart"></i> Оформити замовлення
                            </button>
                        </div>
                    </div>
                </div>

                <button class="menu-toggle" aria-label="Відкрити меню" onclick="toggleMobileMenu()">
                    <i class="fas fa-bars"></i>
                </button>
            </div>
        </div>
    </header>'''

# Standard Footer
FOOTER = '''    <!-- FOOTER -->
    <footer class="footer-pro">
        <div class="container">
            <!-- Main Footer Content -->
            <div class="footer-grid">
                <!-- Column 1: Brand -->
                <div class="footer-col">
                    <h4 style="font-family:var(--font-heading); font-size:1.5rem; color:white; margin-bottom:20px;">
                        <a href="index.html" style="text-decoration:none; color:white;">EthioDirect</a>
                    </h4>
                    <p style="color:#aaa; line-height:1.8; margin-bottom:20px;">Ми доставляємо справжню specialty каву
                        прямо
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
                        <li><i class="fas fa-envelope"></i> <a
                                href="mailto:hello@ethiodirect.ua">hello@ethiodirect.ua</a>
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
    </footer>'''

# Drawer Cart
DRAWER_CART = '''    <!-- CART & MODALS -->
    <div class="overlay"></div>
    <div class="drawer">
        <div class="drawer-header">
            <h3><i class="fas fa-shopping-bag" style="margin-right:10px; color:var(--primary);"></i> Ваш кошик</h3>
            <button onclick="closeDrawer()"
                style="background:none;border:none;font-size:1.5rem;color:var(--text-dark);cursor:pointer;">&times;</button>
        </div>
        <div class="drawer-body" id="cart-list"></div>
        <div class="drawer-footer">
            <!-- Free Shipping Progress Bar -->
            <div class="free-shipping-progress" id="drawer-shipping-progress">
                <div class="progress-bar">
                    <div class="progress-fill" id="drawer-progress-fill" style="width: 0%;"></div>
                </div>
                <p class="progress-text" id="drawer-progress-text">
                    <i class="fas fa-truck"></i> До безкоштовної доставки: <strong>500 ₴</strong>
                </p>
            </div>

            <div style="display:flex; justify-content:space-between; margin-bottom:15px; font-size:1.1rem;">
                <span>Разом:</span>
                <span id="cart-total" style="font-weight:700; color:var(--primary); font-size:1.3rem;">0 ₴</span>
            </div>
            <button class="btn btn-primary" style="width:100%;">
                <i class="fas fa-lock" style="margin-right:8px;"></i>
                Оформити замовлення
            </button>
            <p style="text-align:center; margin-top:12px; font-size:0.8rem; color:var(--text-muted);">
                <i class="fas fa-shield-alt"></i> Безпечна оплата • <i class="fas fa-undo"></i> 14 днів на повернення
            </p>
        </div>
    </div>'''

# Floating Contacts
FLOATING_CONTACTS = '''    <!-- FLOATING CONTACT BUTTONS -->
    <div class="floating-contacts">
        <a href="https://t.me/ethiodirect" class="float-btn telegram" title="Написати в Telegram">
            <i class="fab fa-telegram-plane"></i>
        </a>
        <a href="viber://chat?number=+380501234567" class="float-btn viber" title="Написати в Viber">
            <i class="fab fa-viber"></i>
        </a>
        <a href="tel:+380501234567" class="float-btn phone" title="Зателефонувати">
            <i class="fas fa-phone-alt"></i>
        </a>
    </div>'''

# Toast
TOAST = '''    <!-- TOAST -->
    <div class="toast" id="toast">
        <i class="fas fa-check-circle"></i>
        <span id="toast-msg">Товар додано</span>
    </div>'''

# Pages to update (excluding index.html which is the template)
PAGES = [
    'shop.html',
    'subscription.html',
    'gift-certificates.html',
    'blog.html',
    'about.html',
    'quiz.html',
    'delivery.html',
    'contacts.html',
    'account.html',
    'return.html',
    'faq.html',
    'b2b.html',
]

def get_active_page_from_content(content):
    """Try to determine which page this is from the title or active nav link"""
    if 'class="nav-link active"' in content:
        match = re.search(r'<a href="([^"]+)"[^>]*class="nav-link active"', content)
        if match:
            return match.group(1)
    return ''

def update_page(filepath):
    """Update a single HTML page with standardized header and footer"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[SKIP] Could not read {filepath}: {e}")
        return False

    filename = os.path.basename(filepath)
    
    # Get the active page for nav highlighting
    active_page = filename if filename in PAGES else get_active_page_from_content(content)
    
    # Replace top bar
    content = re.sub(
        r'<!-- TOP BAR[^>]*-->.*?</div>\s*</div>\s*</div>',
        TOP_BAR,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Replace header
    content = re.sub(
        r'<!-- HEADER[^>]*-->.*?</header>',
        get_header(active_page),
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Replace footer
    content = re.sub(
        r'<footer class="footer[^"]*"[^>]*>.*?</footer>',
        FOOTER,
        content,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # Update/add drawer cart before </main> or before floating contacts
    if 'class="overlay"' not in content:
        # Add drawer cart before floating contacts or footer
        if 'class="floating-contacts"' in content:
            content = content.replace('<div class="floating-contacts">', DRAWER_CART + '\n\n    <div class="floating-contacts">')
        elif '</main>' in content:
            content = content.replace('</main>', '</main>\n\n' + DRAWER_CART)
    
    # Ensure floating contacts exist
    if 'class="floating-contacts"' not in content:
        if FOOTER in content:
            content = content.replace(FOOTER, FLOATING_CONTACTS + '\n\n' + FOOTER)
    
    # Ensure toast exists
    if 'class="toast"' not in content and 'id="toast"' not in content:
        if '<script src="js/main.js"' in content:
            content = content.replace('<script src="js/main.js"', TOAST + '\n\n    <script src="js/main.js"')
    
    # Write back
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Updated {filename}")
        return True
    except Exception as e:
        print(f"[ERROR] Could not write {filepath}: {e}")
        return False

def main():
    print("=== Standardizing Header and Footer ===")
    print(f"Base directory: {BASE_DIR}")
    print()
    
    success_count = 0
    for page in PAGES:
        filepath = BASE_DIR / page
        if filepath.exists():
            if update_page(filepath):
                success_count += 1
        else:
            print(f"[SKIP] {page} does not exist")
    
    print()
    print(f"=== Done: {success_count}/{len(PAGES)} pages updated ===")

if __name__ == "__main__":
    main()
