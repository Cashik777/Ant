#!/usr/bin/env python3
"""
Standardize blog article headers and footers to match main site
"""
import os
import re

base_dir = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect'
blog_dir = os.path.join(base_dir, 'blog')
articles_dir = os.path.join(base_dir, 'articles')

# Standard header template for blog articles (with ../ relative paths)
STANDARD_HEADER = '''    <!-- TOP BAR -->
    <div class="top-bar">
        <div class="container top-bar-inner">
            <div class="top-bar-left">
                <span><i class="fas fa-phone-alt"></i> <span data-i18n="topbar.phone">+380 (50) 123-45-67</span></span>
                <span class="divider-dot">•</span>
                <span><i class="fas fa-clock"></i> <span data-i18n="topbar.hours">Пн-Пт: 9:00-18:00</span></span>
            </div>
            <div class="top-bar-center">
                <div class="promo-ticker">
                    <span class="ticker-item"><i class="fas fa-fire" style="color:#e74c3c;"></i> <strong
                            data-i18n="topbar.promo_action">АКЦІЯ:</strong> <span
                            data-i18n="topbar.promo_delivery">безкоштовна доставка від 500₴</span></span>
                    <span class="ticker-divider">|</span>
                    <span class="ticker-item"><i class="fas fa-coffee" style="color:#8B4545;"></i> <span
                            data-i18n="topbar.promo_subscription">Підписка:</span> <strong
                            data-i18n="topbar.promo_subscription_text">-10% на кожну доставку</strong></span>
                    <span class="ticker-divider">|</span>
                    <span class="ticker-item"><i class="fas fa-bolt" style="color:#f39c12;"></i> <span
                            data-i18n="topbar.promo_roast">Свіжа обсмажка</span> <strong 
                            data-i18n="topbar.promo_roast_days">до 3 днів</strong></span>
                </div>
            </div>
            <div class="top-bar-right language-switcher">
                <button data-lang="uk" onclick="setLanguage('uk')" class="lang-btn active" translate="no">UK</button>
                <button data-lang="ru" onclick="setLanguage('ru')" class="lang-btn" translate="no">RU</button>
                <button data-lang="en" onclick="setLanguage('en')" class="lang-btn" translate="no">EN</button>
            </div>
        </div>
    </div>

    <!-- HEADER -->
    <header class="header">
        <div class="container header-inner">
            <a href="../index.html" class="logo">
                <i class="fas fa-certificate"></i> ETHIODIRECT
            </a>

            <nav class="nav-desktop">
                <a href="../shop.html" class="nav-link" data-i18n="nav.catalog">Каталог</a>
                <a href="../subscription.html" class="nav-link" data-i18n="nav.subscription">Підписка</a>
                <a href="../gift-certificates.html" class="nav-link" data-i18n="nav.certificates">Сертифікати</a>
                <a href="../blog.html" class="nav-link active" data-i18n="nav.stories">Історії</a>
                <a href="../about.html" class="nav-link" data-i18n="nav.about">Про нас</a>
                <a href="../quiz.html" class="nav-link" data-i18n="nav.test">Тест</a>
            </nav>

            <!-- Search Bar -->
            <div class="header-search">
                <div class="search-wrapper">
                    <input type="text" class="search-input" id="search-input" placeholder="Пошук кави..."
                        data-i18n-placeholder="search.placeholder" oninput="handleSearch(this.value)">
                    <button class="search-btn"><i class="fas fa-search"></i></button>
                    <div class="search-results" id="search-results"></div>
                </div>
            </div>

            <div class="header-actions">
                <a href="../account.html"><i class="far fa-user"></i></a>

                <!-- Cart with Mini-Cart Dropdown -->
                <div class="cart-wrapper">
                    <div class="cart-trigger" onclick="openDrawer()">
                        <i class="fas fa-shopping-bag" style="font-size:1.2rem;"></i>
                        <span class="cart-count">0</span>
                    </div>
                    <div class="mini-cart" id="mini-cart">
                        <div class="mini-cart-header">
                            <h4 data-i18n="cart.title">Ваш кошик</h4>
                            <span class="mini-cart-count" id="mini-cart-count"><span>0</span> <span
                                    data-i18n="cart.items">товарів</span></span>
                        </div>
                        <div class="mini-cart-items" id="mini-cart-items"></div>
                        <div class="mini-cart-footer" id="mini-cart-footer">
                            <div class="mini-cart-subtotal">
                                <strong data-i18n="cart.subtotal">Разом:</strong>
                                <span id="mini-cart-total">0 ₴</span>
                            </div>
                            <div class="mini-cart-shipping" id="mini-cart-shipping">
                                <i class="fas fa-truck"></i> <span data-i18n="cart.free_shipping_progress">До
                                    безкоштовної доставки:</span> <strong>500 ₴</strong>
                            </div>
                            <button class="mini-cart-btn" onclick="openDrawer()">
                                <i class="fas fa-shopping-cart"></i> <span data-i18n="cart.checkout">Оформити
                                    замовлення</span>
                            </button>
                        </div>
                    </div>
                </div>

                <button class="menu-toggle" aria-label="Open menu" onclick="toggleMobileMenu()">
                    <i class="fas fa-bars"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- MOBILE NAVIGATION -->
    <nav class="nav-mobile" id="nav-mobile">
        <button class="nav-mobile-close" onclick="toggleMobileMenu()" aria-label="Close menu">
            <i class="fas fa-times"></i>
        </button>
        <a href="../shop.html" data-i18n="nav.catalog">Каталог</a>
        <a href="../subscription.html" data-i18n="nav.subscription">Підписка</a>
        <a href="../quiz.html" data-i18n="nav.test">Тест смаку</a>
        <a href="../gift-certificates.html" data-i18n="nav.certificates">Сертифікати</a>
        <a href="../about.html" data-i18n="nav.about">Про нас</a>
        <a href="../contacts.html" data-i18n="footer.contacts">Контакти</a>
        <div class="nav-mobile-footer">
            <a href="https://t.me/ethiodirect"><i class="fab fa-telegram"></i></a>
            <a href="tel:+380501234567"><i class="fas fa-phone"></i></a>
            <a href="mailto:hello@ethiodirect.ua"><i class="fas fa-envelope"></i></a>
        </div>
    </nav>

    <!-- DRAWER CART -->
    <div class="overlay"></div>
    <div class="drawer">
        <div class="drawer-header">
            <h3><i class="fas fa-shopping-bag" style="margin-right:10px; color:var(--primary);"></i> <span
                    data-i18n="cart.your_cart">Ваш кошик</span></h3>
            <button onclick="closeDrawer()"
                style="background:none;border:none;font-size:1.5rem;cursor:pointer;">&times;</button>
        </div>
        <div class="drawer-body" id="cart-list"></div>
        <div class="drawer-footer">
            <div class="free-shipping-progress" id="drawer-shipping-progress">
                <div class="progress-bar">
                    <div class="progress-fill" id="drawer-progress-fill"></div>
                </div>
                <p class="progress-text" id="drawer-progress-text"><i class="fas fa-truck"></i> До безкоштовної
                    доставки: <strong>500 ₴</strong></p>
            </div>
            <div style="display:flex; justify-content:space-between; margin-bottom:15px;">
                <span data-i18n="cart.subtotal">Разом:</span><span id="cart-total"
                    style="font-weight:700; color:var(--primary);">0 ₴</span>
            </div>
            <button class="btn btn-primary" style="width:100%;"><i class="fas fa-lock"></i> <span
                    data-i18n="cart.checkout">Оформити замовлення</span></button>
        </div>
    </div>'''

def fix_article(filepath):
    """Replace article header with standard header"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Find and replace the header section
        # Pattern: from <body> tag until <main> tag
        body_match = re.search(r'<body[^>]*>', content)
        main_match = re.search(r'<main[^>]*>', content)
        
        if body_match and main_match:
            body_end = body_match.end()
            main_start = main_match.start()
            
            # Replace everything between <body> and <main>
            new_content = content[:body_end] + '\n\n' + STANDARD_HEADER + '\n\n    ' + content[main_start:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"[FIXED] {os.path.basename(filepath)}")
            return True
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
    return False

fixed_count = 0

# Process blog directory
if os.path.exists(blog_dir):
    for filename in os.listdir(blog_dir):
        if filename.endswith('.html') and filename != '_header_template.html':
            filepath = os.path.join(blog_dir, filename)
            if fix_article(filepath):
                fixed_count += 1

# Process articles directory  
if os.path.exists(articles_dir):
    for filename in os.listdir(articles_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(articles_dir, filename)
            if fix_article(filepath):
                fixed_count += 1

print(f"\nFixed {fixed_count} article files")
