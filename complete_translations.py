#!/usr/bin/env python3
"""Complete site translation - adds all missing translations"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Complete translations for ALL pages
TRANSLATIONS = {
    # INDEX PAGE
    "index": {
        "hero_title": {"uk": "Справжня ефіопська кава", "ru": "Настоящий эфиопский кофе", "en": "Authentic Ethiopian Coffee"},
        "hero_subtitle": {"uk": "Від ферм до вашої чашки. Свіжа обсмажка, прямі поставки.", "ru": "От ферм до вашей чашки. Свежая обжарка, прямые поставки.", "en": "From farms to your cup. Fresh roast, direct supply."},
        "hero_cta": {"uk": "Обрати каву", "ru": "Выбрать кофе", "en": "Choose Coffee"},
        "hero_cta_secondary": {"uk": "Дізнатись більше", "ru": "Узнать больше", "en": "Learn More"},
        "featured_title": {"uk": "Наші бестселери", "ru": "Наши бестселлеры", "en": "Our Bestsellers"},
        "featured_subtitle": {"uk": "Найпопулярніші сорти ефіопської кави", "ru": "Самые популярные сорта эфиопского кофе", "en": "Most popular Ethiopian coffee varieties"},
        "view_all": {"uk": "Дивитись всі", "ru": "Смотреть все", "en": "View All"},
        "why_us_title": {"uk": "Чому обирають нас", "ru": "Почему выбирают нас", "en": "Why Choose Us"},
        "why_direct": {"uk": "Прямі поставки", "ru": "Прямые поставки", "en": "Direct Supply"},
        "why_direct_text": {"uk": "Без посередників, напряму з ферм Ефіопії", "ru": "Без посредников, напрямую с ферм Эфиопии", "en": "No intermediaries, directly from Ethiopian farms"},
        "why_fresh": {"uk": "Свіжа обсмажка", "ru": "Свежая обжарка", "en": "Fresh Roast"},
        "why_fresh_text": {"uk": "Обсмажуємо під замовлення, до 3 днів", "ru": "Обжариваем под заказ, до 3 дней", "en": "Roasted to order, up to 3 days"},
        "why_quality": {"uk": "Specialty якість", "ru": "Specialty качество", "en": "Specialty Quality"},
        "why_quality_text": {"uk": "Тільки кава 85+ балів SCA", "ru": "Только кофе 85+ баллов SCA", "en": "Only 85+ SCA score coffee"},
        "why_fair": {"uk": "Чесна ціна", "ru": "Честная цена", "en": "Fair Price"},
        "why_fair_text": {"uk": "Справедлива оплата фермерам", "ru": "Справедливая оплата фермерам", "en": "Fair payment to farmers"},
        "subscription_title": {"uk": "Підписка на каву", "ru": "Подписка на кофе", "en": "Coffee Subscription"},
        "subscription_text": {"uk": "Отримуйте свіжу каву регулярно зі знижкою 10%", "ru": "Получайте свежий кофе регулярно со скидкой 10%", "en": "Get fresh coffee regularly with 10% discount"},
        "subscription_cta": {"uk": "Оформити підписку", "ru": "Оформить подписку", "en": "Subscribe Now"},
        "instagram_title": {"uk": "Слідкуйте за нами", "ru": "Следите за нами", "en": "Follow Us"},
        "reviews_title": {"uk": "Відгуки клієнтів", "ru": "Отзывы клиентов", "en": "Customer Reviews"}
    },
    
    # SHOP PAGE  
    "shop": {
        "title": {"uk": "Каталог кави", "ru": "Каталог кофе", "en": "Coffee Catalog"},
        "subtitle": {"uk": "Оберіть свій ідеальний смак", "ru": "Выберите свой идеальный вкус", "en": "Choose Your Perfect Taste"},
        "filters": {"uk": "Фільтри", "ru": "Фильтры", "en": "Filters"},
        "filter_roast": {"uk": "Обсмажка", "ru": "Обжарка", "en": "Roast"},
        "roast_light": {"uk": "Світла", "ru": "Светлая", "en": "Light"},
        "roast_medium": {"uk": "Середня", "ru": "Средняя", "en": "Medium"},
        "roast_dark": {"uk": "Темна", "ru": "Темная", "en": "Dark"},
        "filter_taste": {"uk": "Смак", "ru": "Вкус", "en": "Taste"},
        "taste_fruity": {"uk": "Фруктовий", "ru": "Фруктовый", "en": "Fruity"},
        "taste_chocolate": {"uk": "Шоколадний", "ru": "Шоколадный", "en": "Chocolate"},
        "taste_floral": {"uk": "Квітковий", "ru": "Цветочный", "en": "Floral"},
        "filter_price": {"uk": "Ціна", "ru": "Цена", "en": "Price"},
        "price_from": {"uk": "від", "ru": "от", "en": "from"},
        "price_to": {"uk": "до", "ru": "до", "en": "to"},
        "sort": {"uk": "Сортування", "ru": "Сортировка", "en": "Sort"},
        "sort_popular": {"uk": "За популярністю", "ru": "По популярности", "en": "By Popularity"},
        "sort_price_asc": {"uk": "Ціна: від низької", "ru": "Цена: от низкой", "en": "Price: Low to High"},
        "sort_price_desc": {"uk": "Ціна: від високої", "ru": "Цена: от высокой", "en": "Price: High to Low"},
        "sort_rating": {"uk": "За рейтингом", "ru": "По рейтингу", "en": "By Rating"},
        "clear_filters": {"uk": "Скинути фільтри", "ru": "Сбросить фильтры", "en": "Clear Filters"},
        "found": {"uk": "Знайдено:", "ru": "Найдено:", "en": "Found:"},
        "products_count": {"uk": "товарів", "ru": "товаров", "en": "products"},
        "nothing_found": {"uk": "Нічого не знайдено", "ru": "Ничего не найдено", "en": "Nothing Found"},
        "try_change_filters": {"uk": "Спробуйте змінити фільтри", "ru": "Попробуйте изменить фильтры", "en": "Try changing filters"}
    },
    
    # PRODUCT PAGE
    "product_page": {
        "add_to_cart": {"uk": "Додати в кошик", "ru": "Добавить в корзину", "en": "Add to Cart"},
        "subscribe": {"uk": "Підписатись", "ru": "Подписаться", "en": "Subscribe"},
        "guarantee_fresh": {"uk": "Гарантія свіжості", "ru": "Гарантия свежести", "en": "Freshness Guarantee"},
        "guarantee_shipping": {"uk": "Безкоштовна доставка від 500₴", "ru": "Бесплатная доставка от 500₴", "en": "Free shipping from 500₴"},
        "guarantee_return": {"uk": "Повернення 14 днів", "ru": "Возврат 14 дней", "en": "14 days return"},
        "tab_description": {"uk": "Опис", "ru": "Описание", "en": "Description"},
        "tab_specs": {"uk": "Характеристики", "ru": "Характеристики", "en": "Specifications"},
        "tab_brewing": {"uk": "Як заварювати", "ru": "Как заваривать", "en": "How to Brew"},
        "tab_reviews": {"uk": "Відгуки", "ru": "Отзывы", "en": "Reviews"},
        "about_coffee": {"uk": "Про цю каву", "ru": "Об этом кофе", "en": "About This Coffee"},
        "specs_title": {"uk": "Детальні характеристики", "ru": "Детальные характеристики", "en": "Detailed Specifications"},
        "spec_region": {"uk": "Регіон", "ru": "Регион", "en": "Region"},
        "spec_processing": {"uk": "Обробка", "ru": "Обработка", "en": "Processing"},
        "spec_altitude": {"uk": "Висота вирощування", "ru": "Высота выращивания", "en": "Altitude"},
        "spec_variety": {"uk": "Сорт", "ru": "Сорт", "en": "Variety"},
        "spec_roast": {"uk": "Обсмажка", "ru": "Обжарка", "en": "Roast"},
        "spec_sca": {"uk": "SCA оцінка", "ru": "SCA оценка", "en": "SCA Score"},
        "spec_acidity": {"uk": "Кислотність", "ru": "Кислотность", "en": "Acidity"},
        "spec_body": {"uk": "Тіло", "ru": "Тело", "en": "Body"},
        "spec_weight": {"uk": "Вага", "ru": "Вес", "en": "Weight"},
        "spec_packaging": {"uk": "Упаковка", "ru": "Упаковка", "en": "Packaging"},
        "brewing_title": {"uk": "Рекомендації по заварюванню", "ru": "Рекомендации по завариванию", "en": "Brewing Recommendations"},
        "brewing_dose": {"uk": "Дозування", "ru": "Дозировка", "en": "Dosage"},
        "brewing_grind": {"uk": "Помел", "ru": "Помол", "en": "Grind"},
        "brewing_temp": {"uk": "Температура", "ru": "Температура", "en": "Temperature"},
        "brewing_time": {"uk": "Час", "ru": "Время", "en": "Time"},
        "reviews_based": {"uk": "На основі", "ru": "На основе", "en": "Based on"},
        "reviews_count": {"uk": "відгуків", "ru": "отзывов", "en": "reviews"},
        "leave_review": {"uk": "Залишити відгук", "ru": "Оставить отзыв", "en": "Leave Review"},
        "your_rating": {"uk": "Ваша оцінка", "ru": "Ваша оценка", "en": "Your Rating"},
        "your_name": {"uk": "Ваше ім'я", "ru": "Ваше имя", "en": "Your Name"},
        "your_review": {"uk": "Відгук", "ru": "Отзыв", "en": "Review"},
        "submit_review": {"uk": "Надіслати відгук", "ru": "Отправить отзыв", "en": "Submit Review"},
        "verified_purchase": {"uk": "Підтверджена покупка", "ru": "Подтвержденная покупка", "en": "Verified Purchase"},
        "show_all_reviews": {"uk": "Показати всі відгуки", "ru": "Показать все отзывы", "en": "Show All Reviews"},
        "related_products": {"uk": "Схожі товари", "ru": "Похожие товары", "en": "Related Products"}
    },
    
    # Add remaining page translations...
    "quiz": {
        "title": {"uk": "Тест: Яка кава вам підходить?", "ru": "Тест: Какой кофе вам подходит?", "en": "Quiz: Which Coffee Suits You?"},
        "subtitle": {"uk": "Відповідайте на питання і ми підберемо ідеальну каву для вас", "ru": "Отвечайте на вопросы и мы подберем идеальный кофе для вас", "en": "Answer questions and we'll find the perfect coffee for you"},
        "start": {"uk": "Почати тест", "ru": "Начать тест", "en": "Start Quiz"},
        "next": {"uk": "Далі", "ru": "Далее", "en": "Next"},
        "result": {"uk": "Ваша ідеальна кава:", "ru": "Ваш идеальный кофе:", "en": "Your Perfect Coffee:"},
        "try_it": {"uk": "Спробувати", "ru": "Попробовать", "en": "Try It"},
        "restart": {"uk": "Пройти тест знову", "ru": "Пройти тест снова", "en": "Take Quiz Again"},
        "q1": {"uk": "Як ви зазвичай п'єте каву?", "ru": "Как вы обычно пьёте кофе?", "en": "How do you usually drink coffee?"},
        "q2": {"uk": "Який смак вам ближче?", "ru": "Какой вкус вам ближе?", "en": "What flavor do you prefer?"},
        "q3": {"uk": "Яку кислотність ви любите?", "ru": "Какую кислотность вы любите?", "en": "What acidity do you prefer?"}
    },
    
    "b2b": {
        "title": {"uk": "B2B рішення", "ru": "B2B решения", "en": "B2B Solutions"},
        "subtitle": {"uk": "Specialty кава для вашого бізнесу", "ru": "Specialty кофе для вашего бизнеса", "en": "Specialty Coffee for Your Business"},
        "cafes": {"uk": "Для кав'ярень", "ru": "Для кофеен", "en": "For Cafes"},
        "restaurants": {"uk": "Для ресторанів", "ru": "Для ресторанов", "en": "For Restaurants"},
        "offices": {"uk": "Для офісів", "ru": "Для офисов", "en": "For Offices"},
        "hotels": {"uk": "Для готелів", "ru": "Для отелей", "en": "For Hotels"},
        "contact_form": {"uk": "Залишити заявку", "ru": "Оставить заявку", "en": "Submit Request"},
        "your_name": {"uk": "Ваше ім'я", "ru": "Ваше имя", "en": "Your Name"},
        "company": {"uk": "Компанія", "ru": "Компания", "en": "Company"},
        "phone": {"uk": "Телефон", "ru": "Телефон", "en": "Phone"},
        "email": {"uk": "Email", "ru": "Email", "en": "Email"},
        "message": {"uk": "Повідомлення", "ru": "Сообщение", "en": "Message"},
        "submit": {"uk": "Надіслати заявку", "ru": "Отправить заявку", "en": "Submit"}
    },
    
    "account": {
        "title": {"uk": "Особистий кабінет", "ru": "Личный кабинет", "en": "My Account"},
        "login": {"uk": "Вхід", "ru": "Вход", "en": "Login"},
        "register": {"uk": "Реєстрація", "ru": "Регистрация", "en": "Register"},
        "email": {"uk": "Email", "ru": "Email", "en": "Email"},
        "password": {"uk": "Пароль", "ru": "Пароль", "en": "Password"},
        "login_btn": {"uk": "Увійти", "ru": "Войти", "en": "Sign In"},
        "register_btn": {"uk": "Зареєструватися", "ru": "Зарегистрироваться", "en": "Sign Up"},
        "forgot": {"uk": "Забули пароль?", "ru": "Забыли пароль?", "en": "Forgot Password?"},
        "my_orders": {"uk": "Мої замовлення", "ru": "Мои заказы", "en": "My Orders"},
        "my_subscription": {"uk": "Моя підписка", "ru": "Моя подписка", "en": "My Subscription"},
        "settings": {"uk": "Налаштування", "ru": "Настройки", "en": "Settings"},
        "logout": {"uk": "Вийти", "ru": "Выйти", "en": "Log Out"}
    },
    
    "contacts": {
        "title": {"uk": "Контакти", "ru": "Контакты", "en": "Contact Us"},
        "subtitle": {"uk": "Ми завжди раді вам допомогти", "ru": "Мы всегда рады вам помочь", "en": "We're Always Happy to Help"},
        "phone": {"uk": "Телефон", "ru": "Телефон", "en": "Phone"},
        "email": {"uk": "Email", "ru": "Email", "en": "Email"},
        "address": {"uk": "Адреса", "ru": "Адрес", "en": "Address"},
        "hours": {"uk": "Графік роботи", "ru": "График работы", "en": "Working Hours"},
        "form_title": {"uk": "Напишіть нам", "ru": "Напишите нам", "en": "Write to Us"},
        "your_name": {"uk": "Ваше ім'я", "ru": "Ваше имя", "en": "Your Name"},
        "subject": {"uk": "Тема", "ru": "Тема", "en": "Subject"},
        "message": {"uk": "Повідомлення", "ru": "Сообщение", "en": "Message"},
        "send": {"uk": "Надіслати", "ru": "Отправить", "en": "Send"}
    },
    
    "faq": {
        "title": {"uk": "Часті питання", "ru": "Частые вопросы", "en": "FAQ"},
        "subtitle": {"uk": "Відповіді на популярні питання", "ru": "Ответы на популярные вопросы", "en": "Answers to Common Questions"},
        "delivery": {"uk": "Доставка", "ru": "Доставка", "en": "Delivery"},
        "payment": {"uk": "Оплата", "ru": "Оплата", "en": "Payment"},
        "product": {"uk": "Продукт", "ru": "Продукт", "en": "Product"}
    },
    
    "delivery": {
        "title": {"uk": "Доставка та оплата", "ru": "Доставка и оплата", "en": "Delivery & Payment"},
        "subtitle": {"uk": "Швидко, надійно, зручно", "ru": "Быстро, надежно, удобно", "en": "Fast, Reliable, Convenient"},
        "methods_title": {"uk": "Способи доставки", "ru": "Способы доставки", "en": "Delivery Methods"},
        "nova_poshta": {"uk": "Нова Пошта", "ru": "Новая Почта", "en": "Nova Poshta"},
        "ukrposhta": {"uk": "Укрпошта", "ru": "Укрпочта", "en": "Ukrposhta"},
        "courier": {"uk": "Кур'єр по Одесі", "ru": "Курьер по Одессе", "en": "Courier in Odessa"},
        "payment_title": {"uk": "Способи оплати", "ru": "Способы оплаты", "en": "Payment Methods"},
        "card": {"uk": "Оплата карткою", "ru": "Оплата картой", "en": "Card Payment"},
        "cod": {"uk": "Накладений платіж", "ru": "Наложенный платеж", "en": "Cash on Delivery"}
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
    update_jsons()
    print("Done!")
