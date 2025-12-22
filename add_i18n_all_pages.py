#!/usr/bin/env python3
"""Add data-i18n attributes to index.html"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def update_index():
    filepath = BASE_DIR / "index.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hero section
    content = re.sub(
        r'<h1 class="hero-title">([^<]+)</h1>',
        '<h1 class="hero-title" data-i18n="index.hero_title">\\1</h1>',
        content
    )
    content = re.sub(
        r'<p class="hero-text">([^<]+)</p>',
        '<p class="hero-text" data-i18n="index.hero_subtitle">\\1</p>',
        content
    )
    
    # Featured section
    content = re.sub(
        r'>Наші бестселери<',
        ' data-i18n="index.featured_title">Наші бестселери<',
        content
    )
    content = re.sub(
        r'>Дивитись всі<',
        ' data-i18n="index.view_all">Дивитись всі<',
        content
    )
    
    # Why us section
    content = re.sub(
        r'>Чому обирають нас<',
        ' data-i18n="index.why_us_title">Чому обирають нас<',
        content
    )
    content = re.sub(
        r'>Прямі поставки<',
        ' data-i18n="index.why_direct">Прямі поставки<',
        content
    )
    content = re.sub(
        r'>Свіжа обсмажка<',
        ' data-i18n="index.why_fresh">Свіжа обсмажка<',
        content
    )
    content = re.sub(
        r'>Specialty якість<',
        ' data-i18n="index.why_quality">Specialty якість<',
        content
    )
    content = re.sub(
        r'>Чесна ціна<',
        ' data-i18n="index.why_fair">Чесна ціна<',
        content
    )
    
    # Subscription section
    content = re.sub(
        r'>Підписка на каву<',
        ' data-i18n="index.subscription_title">Підписка на каву<',
        content
    )
    content = re.sub(
        r'>Оформити підписку<',
        ' data-i18n="index.subscription_cta">Оформити підписку<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_shop():
    filepath = BASE_DIR / "shop.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Title
    content = re.sub(
        r'<h1([^>]*)>Каталог кави</h1>',
        '<h1\\1 data-i18n="shop.title">Каталог кави</h1>',
        content
    )
    
    # Filters
    content = re.sub(
        r'>Фільтри<',
        ' data-i18n="shop.filters">Фільтри<',
        content
    )
    content = re.sub(
        r'>Обсмажка<',
        ' data-i18n="shop.filter_roast">Обсмажка<',
        content
    )
    content = re.sub(
        r'>Світла<',
        ' data-i18n="shop.roast_light">Світла<',
        content
    )
    content = re.sub(
        r'>Середня<',
        ' data-i18n="shop.roast_medium">Середня<',
        content
    )
    content = re.sub(
        r'>Темна<',
        ' data-i18n="shop.roast_dark">Темна<',
        content
    )
    content = re.sub(
        r'>Ціна<',
        ' data-i18n="shop.filter_price">Ціна<',
        content
    )
    content = re.sub(
        r'>Скинути фільтри<',
        ' data-i18n="shop.clear_filters">Скинути фільтри<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_quiz():
    filepath = BASE_DIR / "quiz.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Тест: Яка кава вам підходить\?<',
        ' data-i18n="quiz.title">Тест: Яка кава вам підходить?<',
        content
    )
    content = re.sub(
        r'>Почати тест<',
        ' data-i18n="quiz.start">Почати тест<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_b2b():
    filepath = BASE_DIR / "b2b.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>B2B рішення<',
        ' data-i18n="b2b.title">B2B рішення<',
        content
    )
    content = re.sub(
        r'>Specialty кава для вашого бізнесу<',
        ' data-i18n="b2b.subtitle">Specialty кава для вашого бізнесу<',
        content
    )
    content = re.sub(
        r'>Для кав\'ярень<',
        ' data-i18n="b2b.cafes">Для кав\'ярень<',
        content
    )
    content = re.sub(
        r'>Для ресторанів<',
        ' data-i18n="b2b.restaurants">Для ресторанів<',
        content
    )
    content = re.sub(
        r'>Для офісів<',
        ' data-i18n="b2b.offices">Для офісів<',
        content
    )
    content = re.sub(
        r'>Надіслати заявку<',
        ' data-i18n="b2b.submit">Надіслати заявку<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_account():
    filepath = BASE_DIR / "account.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Особистий кабінет<',
        ' data-i18n="account.title">Особистий кабінет<',
        content
    )
    content = re.sub(
        r'>Вхід<',
        ' data-i18n="account.login">Вхід<',
        content
    )
    content = re.sub(
        r'>Реєстрація<',
        ' data-i18n="account.register">Реєстрація<',
        content
    )
    content = re.sub(
        r'>Увійти<',
        ' data-i18n="account.login_btn">Увійти<',
        content
    )
    content = re.sub(
        r'>Забули пароль\?<',
        ' data-i18n="account.forgot">Забули пароль?<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_contacts():
    filepath = BASE_DIR / "contacts.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Контакти<',
        ' data-i18n="contacts.title">Контакти<',
        content
    )
    content = re.sub(
        r'>Напишіть нам<',
        ' data-i18n="contacts.form_title">Напишіть нам<',
        content
    )
    content = re.sub(
        r'>Надіслати<',
        ' data-i18n="contacts.send">Надіслати<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_faq():
    filepath = BASE_DIR / "faq.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Часті питання<',
        ' data-i18n="faq.title">Часті питання<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_delivery():
    filepath = BASE_DIR / "delivery.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Доставка та оплата<',
        ' data-i18n="delivery.title">Доставка та оплата<',
        content
    )
    content = re.sub(
        r'>Способи доставки<',
        ' data-i18n="delivery.methods_title">Способи доставки<',
        content
    )
    content = re.sub(
        r'>Способи оплати<',
        ' data-i18n="delivery.payment_title">Способи оплати<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

if __name__ == "__main__":
    print("Adding data-i18n to all pages...")
    update_index()
    update_shop()
    update_quiz()
    update_b2b()
    update_account()
    update_contacts()
    update_faq()
    update_delivery()
    print("Done!")
