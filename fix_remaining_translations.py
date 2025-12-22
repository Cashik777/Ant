#!/usr/bin/env python3
"""Fix all remaining translation issues identified in verification"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Additional translations needed based on verification
MISSING_TRANSLATIONS = {
    # Index page stats
    "stats": {
        "clients": {"uk": "Задоволених клієнтів", "ru": "Довольных клиентов", "en": "Happy Customers"},
        "sca": {"uk": "Бали SCA Specialty", "ru": "Баллов SCA Specialty", "en": "SCA Specialty Points"},
        "delivery": {"uk": "Від замовлення до чашки", "ru": "От заказа до чашки", "en": "From Order to Cup"},
        "origin": {"uk": "Пряме походження", "ru": "Прямое происхождение", "en": "Direct Origin"},
        "hours": {"uk": "год", "ru": "час", "en": "hrs"},
        "subscribers": {"uk": "людей оформили підписку", "ru": "человек оформили подписку", "en": "people subscribed"}
    },
    
    # Lead magnet / Newsletter
    "lead_magnet": {
        "title": {"uk": "Безкоштовний гід: 7 секретів ідеальної кави вдома", "ru": "Бесплатный гид: 7 секретов идеального кофе дома", "en": "Free Guide: 7 Secrets to Perfect Coffee at Home"},
        "text": {"uk": "Отримайте PDF з практичними порадами від наших бариста", "ru": "Получите PDF с практическими советами от наших бариста", "en": "Get a PDF with practical tips from our baristas"},
        "email_placeholder": {"uk": "Ваш email", "ru": "Ваш email", "en": "Your email"},
        "btn": {"uk": "Отримати безкоштовно", "ru": "Получить бесплатно", "en": "Get Free Guide"},
        "downloaded": {"uk": "людей вже завантажили", "ru": "человек уже скачали", "en": "people downloaded"}
    },
    
    # Footer
    "footer": {
        "about": {"uk": "Про нас", "ru": "О нас", "en": "About Us"},
        "about_text": {"uk": "Ми імпортуємо найкращу specialty каву безпосередньо з ефіопських ферм", "ru": "Мы импортируем лучший specialty кофе непосредственно с эфиопских ферм", "en": "We import the best specialty coffee directly from Ethiopian farms"},
        "quick_links": {"uk": "Швидкі посилання", "ru": "Быстрые ссылки", "en": "Quick Links"},
        "catalog": {"uk": "Каталог", "ru": "Каталог", "en": "Catalog"},
        "subscription": {"uk": "Підписка", "ru": "Подписка", "en": "Subscription"},
        "about_link": {"uk": "Про нас", "ru": "О нас", "en": "About Us"},
        "contacts": {"uk": "Контакти", "ru": "Контакты", "en": "Contacts"},
        "help": {"uk": "Допомога", "ru": "Помощь", "en": "Help"},
        "delivery": {"uk": "Доставка і оплата", "ru": "Доставка и оплата", "en": "Delivery & Payment"},
        "returns": {"uk": "Повернення", "ru": "Возврат", "en": "Returns"},
        "faq": {"uk": "FAQ", "ru": "FAQ", "en": "FAQ"},
        "privacy": {"uk": "Політика конфіденційності", "ru": "Политика конфиденциальности", "en": "Privacy Policy"},
        "newsletter": {"uk": "Розсилка", "ru": "Рассылка", "en": "Newsletter"},
        "newsletter_text": {"uk": "Новинки та спецпропозиції", "ru": "Новинки и спецпредложения", "en": "New arrivals and special offers"},
        "subscribe_btn": {"uk": "Підписатися", "ru": "Подписаться", "en": "Subscribe"},
        "copyright": {"uk": "Всі права захищені", "ru": "Все права защищены", "en": "All rights reserved"},
        "safe_payment": {"uk": "Безпечна оплата", "ru": "Безопасная оплата", "en": "Secure Payment"}
    },
    
    # About page extra
    "about_page": {
        "hero_badge": {"uk": "НАША ІСТОРІЯ", "ru": "НАША ИСТОРИЯ", "en": "OUR STORY"},
        "hero_title": {"uk": "Від ефіопських гір до вашої чашки", "ru": "От эфиопских гор до вашей чашки", "en": "From Ethiopian Mountains to Your Cup"},
        "hero_text": {"uk": "Ми — команда кавоманів, які побудували прямий ланцюг поставок з Ефіопії", "ru": "Мы — команда кофеманов, которые построили прямую цепочку поставок из Эфиопии", "en": "We are a team of coffee lovers who built a direct supply chain from Ethiopia"},
        "feature_direct": {"uk": "Прямі закупки", "ru": "Прямые закупки", "en": "Direct Purchasing"},
        "feature_fresh": {"uk": "Свіжа обсмажка", "ru": "Свежая обжарка", "en": "Fresh Roasting"},
        "feature_sca": {"uk": "85+ балів SCA", "ru": "85+ баллов SCA", "en": "85+ SCA Points"},
        "stat_clients": {"uk": "Задоволених клієнтів", "ru": "Довольных клиентов", "en": "Happy Customers"},
        "stat_sca": {"uk": "Балів SCA Specialty", "ru": "Баллов SCA Specialty", "en": "SCA Specialty Points"},
        "stat_delivery": {"uk": "Від замовлення до доставки", "ru": "От заказа до доставки", "en": "From Order to Delivery"},
        "stat_direct": {"uk": "Пряме походження", "ru": "Прямое происхождение", "en": "Direct Origin"},
        "values_title": {"uk": "Наші цінності", "ru": "Наши ценности", "en": "Our Values"},
        "value_quality": {"uk": "Якість", "ru": "Качество", "en": "Quality"},
        "value_quality_text": {"uk": "Тільки specialty кава 85+ балів", "ru": "Только specialty кофе 85+ баллов", "en": "Only specialty coffee 85+ points"},
        "value_honesty": {"uk": "Чесність", "ru": "Честность", "en": "Honesty"},
        "value_honesty_text": {"uk": "Прозорі ціни, чесна інформація", "ru": "Прозрачные цены, честная информация", "en": "Transparent prices, honest information"},
        "value_sustainability": {"uk": "Сталий розвиток", "ru": "Устойчивое развитие", "en": "Sustainability"},
        "value_sustainability_text": {"uk": "Справедлива оплата фермерам", "ru": "Справедливая оплата фермерам", "en": "Fair payment to farmers"},
        "why_ethiopia_title": {"uk": "Чому Ефіопія?", "ru": "Почему Эфиопия?", "en": "Why Ethiopia?"},
        "why_ethiopia_text": {"uk": "Батьківщина кави з унікальним терруаром", "ru": "Родина кофе с уникальным терруаром", "en": "Birthplace of coffee with unique terroir"},
        "path_title": {"uk": "Наш шлях", "ru": "Наш путь", "en": "Our Journey"},
        "process_title": {"uk": "Наш процес", "ru": "Наш процесс", "en": "Our Process"},
        "team_title": {"uk": "Наша команда", "ru": "Наша команда", "en": "Our Team"},
        "team_member1_name": {"uk": "Олександр", "ru": "Александр", "en": "Alexander"},
        "team_member1_role": {"uk": "Засновник", "ru": "Основатель", "en": "Founder"},
        "team_member2_name": {"uk": "Марина", "ru": "Марина", "en": "Marina"},
        "team_member2_role": {"uk": "Головний обсмажувач", "ru": "Главный обжарщик", "en": "Head Roaster"},
        "team_member3_name": {"uk": "Ігор", "ru": "Игорь", "en": "Igor"},
        "team_member3_role": {"uk": "Q-грейдер", "ru": "Q-грейдер", "en": "Q-Grader"},
        "try_title": {"uk": "Готові спробувати?", "ru": "Готовы попробовать?", "en": "Ready to Try?"},
        "try_text": {"uk": "Замовте свою першу пачку вже сьогодні", "ru": "Закажите свою первую пачку уже сегодня", "en": "Order your first pack today"},
        "try_btn": {"uk": "Обрати каву", "ru": "Выбрать кофе", "en": "Choose Coffee"},
        "timeline_2018": {"uk": "Перша подорож до Ефіопії", "ru": "Первая поездка в Эфиопию", "en": "First trip to Ethiopia"},
        "timeline_2019": {"uk": "Запуск EthioDirect", "ru": "Запуск EthioDirect", "en": "EthioDirect Launch"},
        "timeline_2020": {"uk": "1000+ клієнтів", "ru": "1000+ клиентов", "en": "1000+ customers"},
        "timeline_2021": {"uk": "Власна обсмажувальня", "ru": "Своя обжарочная", "en": "Own roastery"},
        "timeline_2023": {"uk": "Підписка та B2B", "ru": "Подписка и B2B", "en": "Subscription & B2B"}
    },
    
    # Subscription page extra
    "subscription_page": {
        "plan_popular_badge": {"uk": "⭐ НАЙПОПУЛЯРНІШИЙ", "ru": "⭐ САМЫЙ ПОПУЛЯРНЫЙ", "en": "⭐ MOST POPULAR"},
        "hero_title": {"uk": "Підписка на свіжу каву", "ru": "Подписка на свежий кофе", "en": "Fresh Coffee Subscription"},
        "hero_subtitle": {"uk": "Обирайте план і отримуйте найсвіжішу каву без турбот про замовлення", "ru": "Выбирайте план и получайте свежайший кофе без забот о заказе", "en": "Choose a plan and receive the freshest coffee without ordering hassle"},
        "g_month": {"uk": "г/місяць", "ru": "г/месяц", "en": "g/month"}
    },
    
    # Gift page extra placeholders
    "gift_page": {
        "create_btn": {"uk": "Створити сертифікат", "ru": "Создать сертификат", "en": "Create Certificate"},
        "pay_btn": {"uk": "Сплатити", "ru": "Оплатить", "en": "Pay Now"},
        "name_placeholder": {"uk": "Наприклад: Олена", "ru": "Например: Елена", "en": "e.g.: Elena"},
        "message_placeholder": {"uk": "Напишіть кілька теплих слів...", "ru": "Напишите несколько теплых слов...", "en": "Write a few warm words..."},
        "validity_text": {"uk": "Сертифікат дійсний 1 рік з моменту покупки", "ru": "Сертификат действителен 1 год с момента покупки", "en": "Certificate valid for 1 year from purchase"}
    },
    
    # Blog page
    "blog_page": {
        "hero_title": {"uk": "Кавові історії", "ru": "Кофейные истории", "en": "Coffee Stories"},
        "hero_subtitle": {"uk": "Дізнавайтесь більше про каву, методи заварювання та ефіопську культуру", "ru": "Узнавайте больше о кофе, методах заваривания и эфиопской культуре", "en": "Learn more about coffee, brewing methods, and Ethiopian culture"},
        "all_posts": {"uk": "Всі статті", "ru": "Все статьи", "en": "All Posts"},
        "read_more": {"uk": "Читати далі →", "ru": "Читать далее →", "en": "Read More →"},
        "min_read": {"uk": "хв читання", "ru": "мин чтения", "en": "min read"}
    }
}

def update_jsons():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for section, keys in MISSING_TRANSLATIONS.items():
            if section not in data:
                data[section] = {}
            for key, trans in keys.items():
                data[section][key] = trans[lang]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Updated {lang}.json with missing translations")

if __name__ == "__main__":
    update_jsons()
    print("Done!")
