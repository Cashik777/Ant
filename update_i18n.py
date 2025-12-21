"""
Update HTML pages to use i18n instead of google-translate.
- Replace google-translate.js with i18n.js
- Add data-i18n attributes to translatable elements
"""

import os
import re
from pathlib import Path

def update_script_reference(content, is_subdirectory=False):
    """Replace google-translate.js with i18n.js"""
    # Handle both relative and absolute paths
    script_path = '../js/i18n.js' if is_subdirectory else 'js/i18n.js'
    
    # Replace google-translate.js reference
    patterns = [
        r'<script src="[./]*js/google-translate\.js"></script>',
        r'<script src="\.\./js/google-translate\.js"></script>',
    ]
    
    new_script = f'<script src="{script_path}"></script>'
    
    for pattern in patterns:
        content = re.sub(pattern, new_script, content)
    
    return content

def add_data_i18n_to_nav(content):
    """Add data-i18n to navigation links"""
    # Navigation link mappings
    nav_mappings = [
        (r'>Каталог</a>', ' data-i18n="nav.catalog">Каталог</a>'),
        (r'>Підписка</a>', ' data-i18n="nav.subscription">Підписка</a>'),
        (r'>Сертифікати</a>', ' data-i18n="nav.certificates">Сертифікати</a>'),
        (r'>Історії</a>', ' data-i18n="nav.stories">Історії</a>'),
        (r'>Про нас</a>', ' data-i18n="nav.about">Про нас</a>'),
        (r'>Тест</a>', ' data-i18n="nav.test">Тест</a>'),
    ]
    
    for old, new in nav_mappings:
        content = content.replace(old, new)
    
    return content

def add_data_i18n_to_footer(content):
    """Add data-i18n to footer links"""
    footer_mappings = [
        ('>Магазин</h4>', ' data-i18n="footer.shop_title">Магазин</h4>'),
        ('>Весь каталог</a>', ' data-i18n="footer.catalog">Весь каталог</a>'),
        ('>Підписка на каву</a>', ' data-i18n="footer.subscription">Підписка на каву</a>'),
        ('>Сертифікати</a>', ' data-i18n="footer.certificates">Сертифікати</a>'),
        ('>B2B рішення</a>', ' data-i18n="footer.b2b">B2B рішення</a>'),
        ('>Особистий кабінет</a>', ' data-i18n="footer.account">Особистий кабінет</a>'),
        ('>Підтримка</h4>', ' data-i18n="footer.support_title">Підтримка</h4>'),
        ('>Доставка та оплата</a>', ' data-i18n="footer.delivery">Доставка та оплата</a>'),
        ('>Повернення та обмін</a>', ' data-i18n="footer.return">Повернення та обмін</a>'),
        ('>Часті питання</a>', ' data-i18n="footer.faq">Часті питання</a>'),
        ('>Контакти</a>', ' data-i18n="footer.contacts">Контакти</a>'),
        ('>Про нас</a>', ' data-i18n="footer.about">Про нас</a>'),
        ('>Контакти</h4>', ' data-i18n="footer.contacts_title">Контакти</h4>'),
        ('>Підписка на новини</h4>', ' data-i18n="footer.newsletter_title">Підписка на новини</h4>'),
        ('>Підписатись</button>', ' data-i18n="footer.newsletter_cta">Підписатись</button>'),
        ('>Політика конфіденційності</a>', ' data-i18n="footer.privacy">Політика конфіденційності</a>'),
        ('>Умови повернення</a>', ' data-i18n="footer.terms">Умови повернення</a>'),
        ('>Публічна оферта</a>', ' data-i18n="footer.offer">Публічна оферта</a>'),
    ]
    
    for old, new in footer_mappings:
        content = content.replace(old, new)
    
    return content

def add_data_i18n_to_cart(content):
    """Add data-i18n to cart drawer"""
    cart_mappings = [
        ('>Ваш кошик</h3>', ' data-i18n="cart.title">Ваш кошик</h3>'),
        ('>Разом:</span>', ' data-i18n="cart.subtotal">Разом:</span>'),
        ('>Оформити замовлення</button>', ' data-i18n="cart.checkout">Оформити замовлення</button>'),
    ]
    
    for old, new in cart_mappings:
        content = content.replace(old, new)
    
    return content

def add_data_i18n_to_buttons(content):
    """Add data-i18n to common buttons"""
    button_mappings = [
        ('>До кошика</button>', ' data-i18n="product.add_to_cart">До кошика</button>'),
        ('>Обрати каву</a>', ' data-i18n="hero.cta">Обрати каву</a>'),
    ]
    
    for old, new in button_mappings:
        content = content.replace(old, new)
    
    return content

def process_html_file(filepath, is_subdirectory=False):
    """Process a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Update script reference
    content = update_script_reference(content, is_subdirectory)
    
    # Add data-i18n attributes
    content = add_data_i18n_to_nav(content)
    content = add_data_i18n_to_footer(content)
    content = add_data_i18n_to_cart(content)
    content = add_data_i18n_to_buttons(content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = Path('.')
    
    # Find all HTML files
    html_files = []
    
    # Root level files
    for f in base_dir.glob('*.html'):
        if f.name not in ['footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html']:
            html_files.append((f, False))
    
    # Subdirectory files
    for subdir in ['blog', 'articles']:
        subdir_path = base_dir / subdir
        if subdir_path.exists():
            for f in subdir_path.glob('*.html'):
                if not f.name.startswith('_'):
                    html_files.append((f, True))
    
    print(f"Processing {len(html_files)} HTML files...")
    
    updated = 0
    for filepath, is_sub in html_files:
        if process_html_file(filepath, is_sub):
            print(f"  Updated: {filepath}")
            updated += 1
        else:
            print(f"  No changes: {filepath}")
    
    print(f"\nDone! Updated {updated} files.")


if __name__ == '__main__':
    main()
