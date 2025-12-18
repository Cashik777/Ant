# Script to batch update remaining blog files with professional header and footer
import re, glob, os

# List of remaining files to update
remaining_files = [
    "espresso-guide.html", "ethiopia-origins.html", "french-press-guide.html",
    "sca-grading.html", "specialty-coffee.html", "turka-guide.html",
    "v60-guide.html", "yirgacheffe-region.html"
]

blog_dir = r"c:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect\blog"

# Professional footer HTML
footer = '''
    <!-- PROFESSIONAL FOOTER COMPONENT -->
    <footer class="footer-pro">
        <div class="container">
            <!-- Main Footer Content -->
            <div class="footer-grid">
                <!-- Column 1: Brand -->
                <div class="footer-col">
                    <h4 style="font-family:var(--font-heading); font-size:1.5rem; color:white; margin-bottom:20px;">
                        <a href="../index.html" style="text-decoration:none; color:white;">EthioDirect</a>
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
                        <li><a href="../shop.html">Весь каталог</a></li>
                        <li><a href="../subscription.html">Підписка на каву</a></li>
                        <li><a href="../gift-certificates.html">Сертифікати</a></li>
                        <li><a href="../b2b.html">B2B рішення</a></li>
                        <li><a href="../account.html">Особистий кабінет</a></li>
                    </ul>
                </div>

                <!-- Column 3: Support -->
                <div class="footer-col">
                    <h4>Підтримка</h4>
                    <ul class="footer-links">
                        <li><a href="../delivery.html">Доставка та оплата</a></li>
                        <li><a href="../return.html">Повернення та обмін</a></li>
                        <li><a href="../faq.html">Часті питання</a></li>
                        <li><a href="../contacts.html">Контакти</a></li>
                        <li><a href="../about.html">Про нас</a></li>
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
                    <a href="../privacy.html">Політика конфіденційності</a>
                    <span>·</span>
                    <a href="../return.html">Умови повернення</a>
                    <span>·</span>
                    <a href="#">Публічна оферта</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- CART & MODALS -->
    <div class="overlay"></div>
    <div class="drawer">
        <div class="drawer-header">
            <h3>Ваш кошик</h3>
            <button onclick="closeDrawer()"
                style="background:none;border:none;font-size:1.5rem;color:var(--text-dark);cursor:pointer;">&times;</button>
        </div>
        <div class="drawer-body" id="cart-list"></div>
        <div class="drawer-footer">
            <div style="display:flex; justify-content:space-between; margin-bottom:20px; font-weight:700;">
                <span>Разом:</span>
                <span id="cart-total">0 ₴</span>
            </div>
            <button class="btn btn-primary" style="width:100%;">Оформити замовлення</button>
        </div>
    </div>
    <div class="toast" id="toast">
        <i class="fas fa-check-circle" style="color:var(--success); font-size:1.2rem;\"></i>
        <span id="toast-msg">Товар додано</span>
    </div>
'''

for filename in remaining_files:
    filepath = os.path.join(blog_dir, filename)
    if not os.path.exists(filepath):
        print(f"Skipping (not found): {filename}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add footer before closing script tag if not already present
    if 'footer-pro' not in content:
        content = content.replace('    <script src="../js/main.js"></script>', footer + '\n    <script src="../js/main.js"></script>')
        print(f"Added footer to: {filename}")
    
    # Fix header navigation - add missing items
    if '🎁 Сертифікати' not in content:
        # This is a simplified fix - replace entire nav
        old_nav_pattern = r'<nav class="nav-desktop">.*?</nav>'
        new_nav = '''<nav class="nav-desktop">
                <a href="../shop.html" class="nav-link">Каталог</a>
                <a href="../subscription.html" class="nav-link">Підписка</a>
                <a href="../gift-certificates.html" class="nav-link">🎁 Сертифікати</a>
                <a href="../blog.html" class="nav-link active">Історії</a>
                <a href="../about.html" class="nav-link">Про нас</a>
                <a href="#" class="nav-link" onclick="openQuiz(); return false;">Тест</a>
            </nav>'''
        content = re.sub(old_nav_pattern, new_nav, content, flags=re.DOTALL)
        print(f"Updated header for: {filename}")
    
    # Fix cart icon
    if 'fa-shopping-cart' in content:
        content = content.replace('fa-shopping-cart', 'fa-shopping-bag')
        content = content.replace('<div class="cart-trigger">', '<div class="cart-trigger" onclick="openDrawer()">')
        content = content.replace('<i class="fas fa-shopping-bag"></i>', '<i class="fas fa-shopping-bag" style="font-size:1.2rem;"></i>')
        print(f"Updated cart for: {filename}")
    
    # Add menu toggle if missing
    if 'menu-toggle' not in content:
        content = content.replace('</div>\n        </div>\n    </header>', '</div>\n            <button class="menu-toggle" aria-label="Menu"><i class="fas fa-bars"></i></button>\n        </div>\n    </header>')
        print(f"Added menu toggle to: {filename}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Processed: {filename}")

print("\nAll remaining blog files updated successfully!")
