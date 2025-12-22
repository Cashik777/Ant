#!/usr/bin/env python3
"""Add blog card translations and common i18n elements"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

TRANSLATIONS = {
    "blog": {
        "min_read": {"uk": "хв читання", "ru": "мин чтения", "en": "min read"},
        "read_more": {"uk": "Читати далі →", "ru": "Читать далее →", "en": "Read More →"},
        "views": {"uk": "переглядів", "ru": "просмотров", "en": "views"},
        "cat_about": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
        "cat_recipes": {"uk": "Рецепти", "ru": "Рецепты", "en": "Recipes"},
        "cat_equipment": {"uk": "Обладнання", "ru": "Оборудование", "en": "Equipment"},
        "cat_tips": {"uk": "Поради", "ru": "Советы", "en": "Tips"},
        "cat_all": {"uk": "Усі", "ru": "Все", "en": "All"},
        "related": {"uk": "Схожі статті", "ru": "Похожие статьи", "en": "Related Articles"},
        "share": {"uk": "Поділитись", "ru": "Поделиться", "en": "Share"},
        "published": {"uk": "Опубліковано", "ru": "Опубликовано", "en": "Published"}
    },
    "common": {
        "loading": {"uk": "Завантаження...", "ru": "Загрузка...", "en": "Loading..."},
        "error": {"uk": "Помилка", "ru": "Ошибка", "en": "Error"},
        "success": {"uk": "Успішно", "ru": "Успешно", "en": "Success"},
        "close": {"uk": "Закрити", "ru": "Закрыть", "en": "Close"},
        "back": {"uk": "Назад", "ru": "Назад", "en": "Back"},
        "next": {"uk": "Далі", "ru": "Далее", "en": "Next"},
        "prev": {"uk": "Попередній", "ru": "Предыдущий", "en": "Previous"},
        "see_all": {"uk": "Дивитись всі", "ru": "Смотреть все", "en": "See All"},
        "home": {"uk": "Головна", "ru": "Главная", "en": "Home"},
        "menu": {"uk": "Меню", "ru": "Меню", "en": "Menu"}
    },
    "pages": {
        "blog_title": {"uk": "Історії про каву", "ru": "Истории о кофе", "en": "Coffee Stories"},
        "blog_subtitle": {"uk": "Занурюйтесь у світ specialty кави: від плантацій Ефіопії до вашої чашки", "ru": "Погружайтесь в мир specialty кофе: от плантаций Эфиопии до вашей чашки", "en": "Dive into the world of specialty coffee: from Ethiopian plantations to your cup"}
    },
    "footer": {
        "badge_return_days": {"uk": "14 днів", "ru": "14 дней", "en": "14 days"},
        "badge_return": {"uk": "повернення", "ru": "возврат", "en": "return"},
        "badge_specialty": {"uk": "100% Specialty", "ru": "100% Specialty", "en": "100% Specialty"},
        "badge_quality": {"uk": "якість зерна", "ru": "качество зерна", "en": "bean quality"},
        "badge_free": {"uk": "Безкоштовна", "ru": "Бесплатная", "en": "Free"},
        "badge_shipping": {"uk": "доставка від 500₴", "ru": "доставка от 500₴", "en": "shipping from 500₴"},
        "badge_fresh": {"uk": "Свіжа обсмажка", "ru": "Свежая обжарка", "en": "Fresh Roast"},
        "badge_days": {"uk": "до 3 днів", "ru": "до 3 дней", "en": "up to 3 days"},
        "payment_methods": {"uk": "Способи оплати:", "ru": "Способы оплаты:", "en": "Payment Methods:"},
        "all_rights": {"uk": "Всі права захищені", "ru": "Все права защищены", "en": "All rights reserved"},
        "description": {"uk": "Ми доставляємо справжню specialty каву прямо з ефіопських ферм до вашого дому.", "ru": "Мы доставляем настоящий specialty кофе прямо с эфиопских ферм к вашему дому.", "en": "We deliver authentic specialty coffee directly from Ethiopian farms to your home."},
        "shop_title": {"uk": "Магазин", "ru": "Магазин", "en": "Shop"},
        "catalog": {"uk": "Весь каталог", "ru": "Весь каталог", "en": "Full Catalog"},
        "subscription": {"uk": "Підписка на каву", "ru": "Подписка на кофе", "en": "Coffee Subscription"},
        "b2b": {"uk": "B2B рішення", "ru": "B2B решения", "en": "B2B Solutions"},
        "account": {"uk": "Особистий кабінет", "ru": "Личный кабинет", "en": "My Account"},
        "support_title": {"uk": "Підтримка", "ru": "Поддержка", "en": "Support"},
        "delivery": {"uk": "Доставка та оплата", "ru": "Доставка и оплата", "en": "Delivery & Payment"},
        "return": {"uk": "Повернення та обмін", "ru": "Возврат и обмен", "en": "Returns & Exchange"},
        "faq": {"uk": "Часті питання", "ru": "Частые вопросы", "en": "FAQ"},
        "contacts": {"uk": "Контакти", "ru": "Контакты", "en": "Contacts"},
        "contacts_title": {"uk": "Контакти", "ru": "Контакты", "en": "Contacts"},
        "location": {"uk": "Одеса, Україна", "ru": "Одесса, Украина", "en": "Odessa, Ukraine"},
        "newsletter_title": {"uk": "Підписка на новини", "ru": "Подписка на новости", "en": "Newsletter"},
        "newsletter_text": {"uk": "Отримуйте акції, новинки та поради", "ru": "Получайте акции, новинки и советы", "en": "Get deals, news and tips"},
        "newsletter_placeholder": {"uk": "Ваш email", "ru": "Ваш email", "en": "Your email"},
        "newsletter_cta": {"uk": "Підписатись", "ru": "Подписаться", "en": "Subscribe"},
        "privacy": {"uk": "Політика конфіденційності", "ru": "Политика конфиденциальности", "en": "Privacy Policy"},
        "terms": {"uk": "Умови повернення", "ru": "Условия возврата", "en": "Return Policy"},
        "offer": {"uk": "Публічна оферта", "ru": "Публичная оферта", "en": "Public Offer"}
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

if __name__ == "__main__":
    print("Adding blog and common translations...")
    update_jsons()
    print("Done!")
