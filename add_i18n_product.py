#!/usr/bin/env python3
"""Add data-i18n attributes to product.html"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def update_product():
    filepath = BASE_DIR / "product.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Cart drawer
    content = re.sub(
        r'>Ваш кошик<',
        ' data-i18n="cart.your_cart">Ваш кошик<',
        content
    )
    content = re.sub(
        r'>Оформити замовлення<',
        ' data-i18n="cart.checkout">Оформити замовлення<',
        content
    )
    
    # Guarantees
    content = re.sub(
        r'>Гарантія свіжості<',
        ' data-i18n="product_page.guarantee_fresh">Гарантія свіжості<',
        content
    )
    content = re.sub(
        r'>Повернення 14 днів<',
        ' data-i18n="product_page.guarantee_return">Повернення 14 днів<',
        content
    )
    
    # Buttons
    content = re.sub(
        r'>Додати в кошик<',
        ' data-i18n="product_page.add_to_cart">Додати в кошик<',
        content
    )
    content = re.sub(
        r'>Підписатись<',
        ' data-i18n="product_page.subscribe">Підписатись<',
        content
    )
    
    # Tabs
    content = re.sub(
        r'>Опис<',
        ' data-i18n="product_page.tab_description">Опис<',
        content
    )
    content = re.sub(
        r'>Характеристики<',
        ' data-i18n="product_page.tab_specs">Характеристики<',
        content
    )
    content = re.sub(
        r'>Як заварювати<',
        ' data-i18n="product_page.tab_brewing">Як заварювати<',
        content
    )
    content = re.sub(
        r'>Відгуки<',
        ' data-i18n="product_page.tab_reviews">Відгуки<',
        content
    )
    
    # Tab content
    content = re.sub(
        r'>Про цю каву<',
        ' data-i18n="product_page.about_coffee">Про цю каву<',
        content
    )
    content = re.sub(
        r'>Детальні характеристики<',
        ' data-i18n="product_page.specs_title">Детальні характеристики<',
        content
    )
    content = re.sub(
        r'>Рекомендації по заварюванню<',
        ' data-i18n="product_page.brewing_title">Рекомендації по заварюванню<',
        content
    )
    
    # Specs table labels
    content = re.sub(
        r'<strong>Регіон:</strong>',
        '<strong data-i18n="product_page.spec_region">Регіон:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Обробка:</strong>',
        '<strong data-i18n="product_page.spec_processing">Обробка:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Висота вирощування:</strong>',
        '<strong data-i18n="product_page.spec_altitude">Висота вирощування:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Сорт:</strong>',
        '<strong data-i18n="product_page.spec_variety">Сорт:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Обсмажка:</strong>',
        '<strong data-i18n="product_page.spec_roast">Обсмажка:</strong>',
        content
    )
    content = re.sub(
        r'<strong>SCA оцінка:</strong>',
        '<strong data-i18n="product_page.spec_sca">SCA оцінка:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Кислотність:</strong>',
        '<strong data-i18n="product_page.spec_acidity">Кислотність:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Тіло:</strong>',
        '<strong data-i18n="product_page.spec_body">Тіло:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Вага:</strong>',
        '<strong data-i18n="product_page.spec_weight">Вага:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Упаковка:</strong>',
        '<strong data-i18n="product_page.spec_packaging">Упаковка:</strong>',
        content
    )
    
    # Brewing method labels
    content = re.sub(
        r'<strong>Дозування:</strong>',
        '<strong data-i18n="product_page.brewing_dose">Дозування:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Помел:</strong>',
        '<strong data-i18n="product_page.brewing_grind">Помел:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Температура:</strong>',
        '<strong data-i18n="product_page.brewing_temp">Температура:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Час екстракції:</strong>',
        '<strong data-i18n="product_page.brewing_time">Час екстракції:</strong>',
        content
    )
    content = re.sub(
        r'<strong>Час:</strong>',
        '<strong data-i18n="product_page.brewing_time">Час:</strong>',
        content
    )
    
    # Reviews section
    content = re.sub(
        r'>На основі 24 відгуків<',
        ' data-i18n="product_page.reviews_based">На основі 24 відгуків<',
        content
    )
    content = re.sub(
        r'>Залишити відгук<',
        ' data-i18n="product_page.leave_review">Залишити відгук<',
        content
    )
    content = re.sub(
        r'>Ваша оцінка:<',
        ' data-i18n="product_page.your_rating">Ваша оцінка:<',
        content
    )
    content = re.sub(
        r'>Ваше ім\'я:<',
        ' data-i18n="product_page.your_name">Ваше ім\'я:<',
        content
    )
    content = re.sub(
        r'>Відгук:<',
        ' data-i18n="product_page.your_review">Відгук:<',
        content
    )
    content = re.sub(
        r'>Надіслати відгук<',
        ' data-i18n="product_page.submit_review">Надіслати відгук<',
        content
    )
    content = re.sub(
        r'>✓ Підтверджена покупка<',
        ' data-i18n="product_page.verified_purchase">✓ Підтверджена покупка<',
        content
    )
    content = re.sub(
        r'>Показати всі відгуки<',
        ' data-i18n="product_page.show_all_reviews">Показати всі відгуки<',
        content
    )
    
    # Related products
    content = re.sub(
        r'>Схожі товари<',
        ' data-i18n="product_page.related_products">Схожі товари<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

if __name__ == "__main__":
    update_product()
    print("Done!")
