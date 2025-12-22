#!/usr/bin/env python3
"""Add data-i18n attributes to ALL HTML files for complete translation"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def add_i18n_to_quiz():
    """Fix quiz.html with full i18n"""
    filepath = BASE_DIR / "quiz.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Title and subtitle
    content = re.sub(
        r'<h1([^>]*)>Тест: Яка кава вам підходить\?</h1>',
        '<h1\\1 data-i18n="quiz_page.title">Тест: Яка кава вам підходить?</h1>',
        content
    )
    content = re.sub(
        r'>Відповідайте на 5 простих питань<',
        ' data-i18n="quiz_page.subtitle">Відповідайте на 5 простих питань<',
        content
    )
    content = re.sub(
        r'>Почати тест<',
        ' data-i18n="quiz_page.start_btn">Почати тест<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def add_i18n_to_b2b():
    """Fix b2b.html with full i18n"""
    filepath = BASE_DIR / "b2b.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Title
    content = re.sub(
        r'<h1([^>]*)>B2B рішення</h1>',
        '<h1\\1 data-i18n="b2b_page.title">B2B рішення</h1>',
        content
    )
    content = re.sub(
        r'>Specialty кава для вашого бізнесу<',
        ' data-i18n="b2b_page.subtitle">Specialty кава для вашого бізнесу<',
        content
    )
    content = re.sub(
        r'>Для кав\'ярень<',
        ' data-i18n="b2b_page.cafes_title">Для кав\'ярень<',
        content
    )
    content = re.sub(
        r'>Для ресторанів<',
        ' data-i18n="b2b_page.restaurants_title">Для ресторанів<',
        content
    )
    content = re.sub(
        r'>Для офісів<',
        ' data-i18n="b2b_page.offices_title">Для офісів<',
        content
    )
    content = re.sub(
        r'>Для готелів<',
        ' data-i18n="b2b_page.hotels_title">Для готелів<',
        content
    )
    content = re.sub(
        r'>Чому обирають нас\?<',
        ' data-i18n="b2b_page.benefits_title">Чому обирають нас?<',
        content
    )
    content = re.sub(
        r'>Залишити заявку<',
        ' data-i18n="b2b_page.form_title">Залишити заявку<',
        content
    )
    content = re.sub(
        r'>Надіслати заявку<',
        ' data-i18n="b2b_page.form_submit">Надіслати заявку<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def add_i18n_to_account():
    """Fix account.html with full i18n"""
    filepath = BASE_DIR / "account.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<h1([^>]*)>Особистий кабінет</h1>',
        '<h1\\1 data-i18n="account_page.title">Особистий кабінет</h1>',
        content
    )
    content = re.sub(
        r'>Вхід</h2>',
        ' data-i18n="account_page.login_title">Вхід</h2>',
        content
    )
    content = re.sub(
        r'>Реєстрація</h2>',
        ' data-i18n="account_page.register_title">Реєстрація</h2>',
        content
    )
    content = re.sub(
        r'>Увійти<',
        ' data-i18n="account_page.login_btn">Увійти<',
        content
    )
    content = re.sub(
        r'>Зареєструватися<',
        ' data-i18n="account_page.register_btn">Зареєструватися<',
        content
    )
    content = re.sub(
        r'>Забули пароль\?<',
        ' data-i18n="account_page.forgot_password">Забули пароль?<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def add_i18n_to_contacts():
    """Fix contacts.html with full i18n"""
    filepath = BASE_DIR / "contacts.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<h1([^>]*)>Контакти</h1>',
        '<h1\\1 data-i18n="contacts_page.title">Контакти</h1>',
        content
    )
    content = re.sub(
        r'>Ми завжди раді вам допомогти<',
        ' data-i18n="contacts_page.subtitle">Ми завжди раді вам допомогти<',
        content
    )
    content = re.sub(
        r'>Напишіть нам<',
        ' data-i18n="contacts_page.form_title">Напишіть нам<',
        content
    )
    content = re.sub(
        r'>Надіслати<',
        ' data-i18n="contacts_page.form_submit">Надіслати<',
        content
    )
    content = re.sub(
        r'>Телефон<',
        ' data-i18n="contacts_page.phone_title">Телефон<',
        content
    )
    content = re.sub(
        r'>Графік роботи<',
        ' data-i18n="contacts_page.hours_title">Графік роботи<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def add_i18n_to_faq():
    """Fix faq.html with full i18n"""
    filepath = BASE_DIR / "faq.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<h1([^>]*)>Часті питання</h1>',
        '<h1\\1 data-i18n="faq_page.title">Часті питання</h1>',
        content
    )
    content = re.sub(
        r'>Відповіді на популярні питання<',
        ' data-i18n="faq_page.subtitle">Відповіді на популярні питання<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def add_i18n_to_delivery():
    """Fix delivery.html with full i18n"""
    filepath = BASE_DIR / "delivery.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'<h1([^>]*)>Доставка та оплата</h1>',
        '<h1\\1 data-i18n="delivery_page.title">Доставка та оплата</h1>',
        content
    )
    content = re.sub(
        r'>Швидко, надійно, зручно<',
        ' data-i18n="delivery_page.subtitle">Швидко, надійно, зручно<',
        content
    )
    content = re.sub(
        r'>Способи доставки<',
        ' data-i18n="delivery_page.delivery_title">Способи доставки<',
        content
    )
    content = re.sub(
        r'>Способи оплати<',
        ' data-i18n="delivery_page.payment_title">Способи оплати<',
        content
    )
    content = re.sub(
        r'>Нова Пошта<',
        ' data-i18n="delivery_page.nova_poshta">Нова Пошта<',
        content
    )
    content = re.sub(
        r'>Укрпошта<',
        ' data-i18n="delivery_page.ukrposhta">Укрпошта<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def add_i18n_to_about():
    """Fix about.html with full i18n"""
    filepath = BASE_DIR / "about.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Наші цінності<',
        ' data-i18n="about_page.values_title">Наші цінності<',
        content
    )
    content = re.sub(
        r'>Наш шлях<',
        ' data-i18n="about_page.path_title">Наш шлях<',
        content
    )
    content = re.sub(
        r'>Наш процес<',
        ' data-i18n="about_page.process_title">Наш процес<',
        content
    )
    content = re.sub(
        r'>Наша команда<',
        ' data-i18n="about_page.team_title">Наша команда<',
        content
    )
    content = re.sub(
        r'>Готові спробувати\?<',
        ' data-i18n="about_page.try_title">Готові спробувати?<',
        content
    )
    content = re.sub(
        r'>Обрати каву<',
        ' data-i18n="about_page.try_btn">Обрати каву<',
        content
    )
    content = re.sub(
        r'>Якість<',
        ' data-i18n="about_page.value_quality">Якість<',
        content
    )
    content = re.sub(
        r'>Чесність<',
        ' data-i18n="about_page.value_honesty">Чесність<',
        content
    )
    content = re.sub(
        r'>Сталий розвиток<',
        ' data-i18n="about_page.value_sustainability">Сталий розвиток<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def add_i18n_to_gift():
    """Fix gift-certificates.html with full i18n"""
    filepath = BASE_DIR / "gift-certificates.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Створити сертифікат<',
        ' data-i18n="gift_page.create_btn">Створити сертифікат<',
        content
    )
    content = re.sub(
        r'>Придбати сертифікат<',
        ' data-i18n="gift_page.buy_btn">Придбати сертифікат<',
        content
    )
    # Add placeholders
    content = re.sub(
        r'placeholder="Ім\'я отримувача"',
        'placeholder="Ім\'я отримувача" data-i18n-placeholder="gift_page.recipient_placeholder"',
        content
    )
    content = re.sub(
        r'placeholder="Ваше ім\'я"',
        'placeholder="Ваше ім\'я" data-i18n-placeholder="gift_page.sender_placeholder"',
        content
    )
    content = re.sub(
        r'placeholder="Напишіть побажання\.\.\."',
        'placeholder="Напишіть побажання..." data-i18n-placeholder="gift_page.message_placeholder"',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def add_i18n_to_subscription():
    """Fix subscription.html with full i18n"""
    filepath = BASE_DIR / "subscription.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Weights/month
    content = re.sub(
        r'>250\s*</span>\s*<span[^>]*>г/місяць<',
        '>250</span> <span data-i18n="subscription_page.plan_per_month">г/місяць<',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'>500\s*</span>\s*<span[^>]*>г/місяць<',
        '>500</span> <span data-i18n="subscription_page.plan_per_month">г/місяць<',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'>1000\s*</span>\s*<span[^>]*>г/місяць<',
        '>1000</span> <span data-i18n="subscription_page.plan_per_month">г/місяць<',
        content, flags=re.DOTALL
    )
    
    # How it works
    content = re.sub(
        r'>Як це працює<',
        ' data-i18n="subscription_page.how_it_works">Як це працює<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

if __name__ == "__main__":
    print("Adding data-i18n attributes to all HTML files...")
    add_i18n_to_quiz()
    add_i18n_to_b2b()
    add_i18n_to_account()
    add_i18n_to_contacts()
    add_i18n_to_faq()
    add_i18n_to_delivery()
    add_i18n_to_about()
    add_i18n_to_gift()
    add_i18n_to_subscription()
    print("Done! All HTML files updated with data-i18n attributes.")
