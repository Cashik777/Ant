#!/usr/bin/env python3
"""Add data-i18n attributes to return.html and translations to JSON"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

TRANSLATIONS = {
    "return_page": {
        "title": {"uk": "Повернення та обмін", "ru": "Возврат и обмен", "en": "Returns & Exchange"},
        "subtitle": {"uk": "Якщо кава вам не підійшла — ми все виправимо", "ru": "Если кофе вам не подошел — мы все исправим", "en": "If the coffee didn't suit you — we'll fix it"},
        "guarantee_title": {"uk": "Гарантія задоволення 14 днів", "ru": "Гарантия удовлетворения 14 дней", "en": "14-Day Satisfaction Guarantee"},
        "guarantee_text": {"uk": "Якщо кава вам не сподобалась — поверніть гроші або отримайте інший сорт безкоштовно", "ru": "Если кофе вам не понравился — верните деньги или получите другой сорт бесплатно", "en": "If you didn't like the coffee — get a refund or receive another variety for free"},
        "how_to_title": {"uk": "Як повернути товар?", "ru": "Как вернуть товар?", "en": "How to Return?"},
        "step1_title": {"uk": "Зв'яжіться з нами", "ru": "Свяжитесь с нами", "en": "Contact Us"},
        "step1_text": {"uk": "Напишіть нам на email hello@ethiodirect.ua або в Telegram/Viber. Вкажіть номер замовлення та причину повернення.", "ru": "Напишите нам на email hello@ethiodirect.ua или в Telegram/Viber. Укажите номер заказа и причину возврата.", "en": "Write to us at hello@ethiodirect.ua or via Telegram/Viber. Indicate your order number and reason for return."},
        "step2_title": {"uk": "Відправте товар", "ru": "Отправьте товар", "en": "Ship the Product"},
        "step2_text": {"uk": "Упакуйте каву та відправте Новою Поштою за нашими реквізитами.", "ru": "Упакуйте кофе и отправьте Новой Почтой по нашим реквизитам.", "en": "Pack the coffee and ship via Nova Poshta to our address."},
        "step3_title": {"uk": "Отримайте кошти або заміну", "ru": "Получите деньги или замену", "en": "Get Refund or Replacement"},
        "step3_text": {"uk": "Після отримання товару ми повернемо гроші протягом 1-3 робочих днів.", "ru": "После получения товара мы вернем деньги в течение 1-3 рабочих дней.", "en": "After receiving the product, we'll refund within 1-3 business days."},
        "conditions_title": {"uk": "Умови повернення", "ru": "Условия возврата", "en": "Return Conditions"},
        "accept_title": {"uk": "Приймаємо до повернення", "ru": "Принимаем к возврату", "en": "We Accept Returns"},
        "accept_1": {"uk": "Нерозпечатана упаковка", "ru": "Невскрытая упаковка", "en": "Unopened package"},
        "accept_2": {"uk": "Пошкоджена упаковка при доставці", "ru": "Поврежденная упаковка при доставке", "en": "Damaged package on delivery"},
        "accept_3": {"uk": "Невідповідність замовленню", "ru": "Несоответствие заказу", "en": "Order mismatch"},
        "accept_4": {"uk": "Кава не сподобалась за смаком", "ru": "Кофе не понравился по вкусу", "en": "Didn't like the taste"},
        "reject_title": {"uk": "Не приймаємо", "ru": "Не принимаем", "en": "We Don't Accept"},
        "reject_1": {"uk": "Розпечатана упаковка без дефектів", "ru": "Вскрытая упаковка без дефектов", "en": "Opened package without defects"},
        "reject_2": {"uk": "Товар куплений більше 14 днів тому", "ru": "Товар куплен более 14 дней назад", "en": "Product purchased over 14 days ago"},
        "exchange_title": {"uk": "Обмін товару", "ru": "Обмен товара", "en": "Product Exchange"},
        "exchange_text": {"uk": "Якщо ви хочете обміняти каву на інший сорт — це безкоштовно!", "ru": "Если вы хотите обменять кофе на другой сорт — это бесплатно!", "en": "If you want to exchange coffee for another variety — it's free!"},
        "exchange_btn": {"uk": "Зв'язатися для обміну", "ru": "Связаться для обмена", "en": "Contact for Exchange"},
        "questions_title": {"uk": "Маєте питання?", "ru": "Есть вопросы?", "en": "Have Questions?"},
        "questions_text": {"uk": "Ми завжди готові допомогти з поверненням або обміном", "ru": "Мы всегда готовы помочь с возвратом или обменом", "en": "We're always ready to help with returns or exchanges"}
    },
    "privacy_page": {
        "title": {"uk": "Політика конфіденційності", "ru": "Политика конфиденциальности", "en": "Privacy Policy"},
        "subtitle": {"uk": "Як ми захищаємо ваші дані", "ru": "Как мы защищаем ваши данные", "en": "How We Protect Your Data"}
    }
}

def update_jsons():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for section, keys in TRANSLATIONS.items():
            if section not in data:
                data[section] = {}
            for key, trans in keys.items():
                data[section][key] = trans[lang]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Updated {lang}.json")

def update_return():
    filepath = BASE_DIR / "return.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Title and subtitle
    content = re.sub(
        r'<h1([^>]*)>Повернення та обмін</h1>',
        '<h1\\1 data-i18n="return_page.title">Повернення та обмін</h1>',
        content
    )
    content = re.sub(
        r'>Якщо кава вам не підійшла — ми все виправимо<',
        ' data-i18n="return_page.subtitle">Якщо кава вам не підійшла — ми все виправимо<',
        content
    )
    
    # Guarantee banner
    content = re.sub(
        r'>Гарантія задоволення 14 днів<',
        ' data-i18n="return_page.guarantee_title">Гарантія задоволення 14 днів<',
        content
    )
    
    # Steps
    content = re.sub(
        r'>Як повернути товар\?<',
        ' data-i18n="return_page.how_to_title">Як повернути товар?<',
        content
    )
    content = re.sub(
        r'>Зв\'яжіться з нами<',
        ' data-i18n="return_page.step1_title">Зв\'яжіться з нами<',
        content
    )
    content = re.sub(
        r'>Відправте товар<',
        ' data-i18n="return_page.step2_title">Відправте товар<',
        content
    )
    content = re.sub(
        r'>Отримайте кошти або заміну<',
        ' data-i18n="return_page.step3_title">Отримайте кошти або заміну<',
        content
    )
    
    # Conditions
    content = re.sub(
        r'>Умови повернення<',
        ' data-i18n="return_page.conditions_title">Умови повернення<',
        content
    )
    content = re.sub(
        r'>Приймаємо\s*до повернення<',
        ' data-i18n="return_page.accept_title">Приймаємо до повернення<',
        content, flags=re.DOTALL
    )
    content = re.sub(
        r'>Не\s*приймаємо<',
        ' data-i18n="return_page.reject_title">Не приймаємо<',
        content, flags=re.DOTALL
    )
    
    # Exchange
    content = re.sub(
        r'>Обмін товару<',
        ' data-i18n="return_page.exchange_title">Обмін товару<',
        content
    )
    content = re.sub(
        r'>Зв\'язатися для обміну<',
        ' data-i18n="return_page.exchange_btn">Зв\'язатися для обміну<',
        content
    )
    
    # Questions
    content = re.sub(
        r'>Маєте питання\?<',
        ' data-i18n="return_page.questions_title">Маєте питання?<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

if __name__ == "__main__":
    print("Adding return and privacy translations...")
    update_jsons()
    update_return()
    print("Done!")
