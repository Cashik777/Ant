#!/usr/bin/env python3
"""Fix drawer cart translation in ALL HTML files"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def fix_drawer_in_file(filepath):
    """Add data-i18n to drawer elements"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix drawer header - "Ваш кошик"
        content = re.sub(
            r'<h3><i class="fas fa-shopping-bag"[^>]*></i> Ваш кошик</h3>',
            '<h3><i class="fas fa-shopping-bag" style="margin-right:10px; color:var(--primary);"></i> <span data-i18n="cart.your_cart">Ваш кошик</span></h3>',
            content
        )
        content = re.sub(
            r'<h3>\s*<i class="fas fa-shopping-bag"[^>]*></i>\s*Ваш кошик\s*</h3>',
            '<h3><i class="fas fa-shopping-bag" style="margin-right:10px; color:var(--primary);"></i> <span data-i18n="cart.your_cart">Ваш кошик</span></h3>',
            content, flags=re.DOTALL
        )
        
        # Fix "Разом:" 
        content = re.sub(
            r'>Разом:</span>',
            ' data-i18n="cart.subtotal">Разом:</span>',
            content
        )
        
        # Fix "До безкоштовної доставки:"
        content = re.sub(
            r'>До безкоштовної\s*доставки:',
            ' data-i18n="cart.free_shipping_progress">До безкоштовної доставки:',
            content, flags=re.DOTALL
        )
        
        # Fix "Оформити замовлення" button
        content = re.sub(
            r'>Оформити замовлення<',
            ' data-i18n="cart.checkout">Оформити замовлення<',
            content
        )
        content = re.sub(
            r'>\s*<i class="fas fa-lock"[^>]*></i>\s*Оформити замовлення\s*</button>',
            '><i class="fas fa-lock"></i> <span data-i18n="cart.checkout">Оформити замовлення</span></button>',
            content, flags=re.DOTALL
        )
        
        # Fix safety text
        content = re.sub(
            r'Безпечна оплата',
            '<span data-i18n="cart.safe_payment">Безпечна оплата</span>',
            content
        )
        content = re.sub(
            r'14 днів на повернення',
            '<span data-i18n="cart.return_days">14 днів на повернення</span>',
            content
        )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed drawer: {filepath.name}")
            return True
        return False
    except Exception as e:
        print(f"Error with {filepath}: {e}")
        return False

def main():
    html_files = list(BASE_DIR.glob("*.html"))
    html_files += list(BASE_DIR.glob("blog/*.html"))
    html_files += list(BASE_DIR.glob("articles/*.html"))
    
    fixed = 0
    for f in html_files:
        if fix_drawer_in_file(f):
            fixed += 1
    
    print(f"Fixed {fixed}/{len(html_files)} HTML files")

if __name__ == "__main__":
    main()
