"""
Script to apply global layout improvements to all HTML pages.
Adds: top-bar, floating contacts, improved drawer cart, toast notifications
"""

import os
import re
from pathlib import Path

# Directory with HTML files
BASE_DIR = Path(r"C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect")

# HTML files to update (excluding index.html which already has changes)
HTML_FILES = [
    "shop.html",
    "subscription.html", 
    "about.html",
    "b2b.html",
    "blog.html",
    "contacts.html",
    "delivery.html",
    "faq.html",
    "gift-certificates.html",
    "account.html",
    "return.html",
    "privacy.html",
    "product.html",
    "quiz.html"
]

# Top bar HTML to insert after <body>
TOP_BAR_HTML = '''
    <!-- TOP BAR - Competitor Feature -->
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
                <a href="#" class="lang-switch active">UA</a>
                <a href="#" class="lang-switch">RU</a>
            </div>
        </div>
    </div>

'''

# Floating contacts HTML to insert before </body>
FLOATING_CONTACTS_HTML = '''
    <!-- FLOATING CONTACT BUTTONS -->
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
    </div>

    <!-- TOAST -->
    <div class="toast" id="toast">
        <i class="fas fa-check-circle"></i>
        <span id="toast-msg">Товар додано</span>
    </div>

'''

# Improved drawer cart HTML
IMPROVED_DRAWER_HTML = '''    <div class="overlay"></div>
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
    </div>
'''

def process_file(filepath):
    """Process a single HTML file to add improvements"""
    print(f"Processing: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # 1. Add top bar after <body> if not present
    if 'class="top-bar"' not in content:
        content = re.sub(
            r'(<body[^>]*>)\s*\n',
            r'\1\n' + TOP_BAR_HTML,
            content
        )
        modified = True
        print("  + Added top bar")
    
    # 2. Replace old drawer cart with improved version
    old_drawer_pattern = r'<div class="overlay">.*?</div>\s*<div class="drawer">.*?</div>\s*</div>\s*</div>'
    if 'drawer-shipping-progress' not in content and '<div class="drawer">' in content:
        # Find and replace the old drawer
        content = re.sub(
            r'<div class="overlay"></div>\s*<div class="drawer">.*?</div>\s*</div>\s*</div>',
            IMPROVED_DRAWER_HTML,
            content,
            flags=re.DOTALL
        )
        modified = True
        print("  + Updated drawer cart")
    
    # 3. Add floating contacts before </body> if not present
    if 'class="floating-contacts"' not in content:
        content = re.sub(
            r'(\s*<script src="js/main.js">)',
            FLOATING_CONTACTS_HTML + r'\1',
            content
        )
        modified = True
        print("  + Added floating contacts")
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] Saved changes")
    else:
        print("  - No changes needed")
    
    return modified


def main():
    print("=" * 50)
    print("Applying global layout improvements")
    print("=" * 50)
    
    updated_count = 0
    
    for filename in HTML_FILES:
        filepath = BASE_DIR / filename
        if filepath.exists():
            if process_file(filepath):
                updated_count += 1
        else:
            print(f"File not found: {filename}")
    
    print("=" * 50)
    print(f"Updated {updated_count} / {len(HTML_FILES)} files")
    print("=" * 50)


if __name__ == "__main__":
    main()
