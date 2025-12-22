#!/usr/bin/env python3
"""Add complete review translations to JSON"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

REVIEWS = {
    "reviews": {
        "featured_text": {"uk": "\"Це не просто напій, це подорож. Я відчула різницю з першого ковтка. Тепер магазинна кава для мене просто не існує.\"", "ru": "\"Это не просто напиток, это путешествие. Я почувствовала разницу с первого глотка. Теперь магазинный кофе для меня просто не существует.\"", "en": "\"This is not just a drink, it's a journey. I felt the difference from the first sip. Store-bought coffee no longer exists for me.\""},
        "featured_author": {"uk": "— Олена К., Київ • Підписка на Guji Natural", "ru": "— Елена К., Киев • Подписка на Guji Natural", "en": "— Olena K., Kyiv • Guji Natural Subscription"},
        
        "review1_name": {"uk": "Андрій М.", "ru": "Андрей М.", "en": "Andriy M."},
        "review1_city": {"uk": "Львів", "ru": "Львов", "en": "Lviv"},
        "review1_text": {"uk": "Швидка доставка і неймовірний аромат, який наповнює всю квартиру.", "ru": "Быстрая доставка и невероятный аромат, который наполняет всю квартиру.", "en": "Fast delivery and incredible aroma that fills the entire apartment."},
        
        "review2_name": {"uk": "Марина С.", "ru": "Марина С.", "en": "Marina S."},
        "review2_city": {"uk": "Одеса", "ru": "Одесса", "en": "Odessa"},
        "review2_text": {"uk": "Сервіс на висоті. Дуже зручно, що не треба думати, коли замовляти наступну пачку.", "ru": "Сервис на высоте. Очень удобно, что не нужно думать, когда заказывать следующую пачку.", "en": "Excellent service. Very convenient not having to think about when to order the next pack."},
        
        "review3_name": {"uk": "Віктор П.", "ru": "Виктор П.", "en": "Viktor P."},
        "review3_city": {"uk": "Київ", "ru": "Киев", "en": "Kyiv"},
        "review3_text": {"uk": "Дякую за можливість спробувати різні сорти! Харрар — це мій фаворит.", "ru": "Спасибо за возможность попробовать разные сорта! Харрар — мой фаворит.", "en": "Thank you for the opportunity to try different varieties! Harrar is my favorite."},
        
        "join_text": {"uk": "Приєднуйтесь до", "ru": "Присоединяйтесь к", "en": "Join"},
        "coffee_lovers": {"uk": "задоволених кавоманів", "ru": "довольных кофеманов", "en": "happy coffee lovers"},
        "subscribe_cta": {"uk": "Оформити підписку зі знижкою 10%", "ru": "Оформить подписку со скидкой 10%", "en": "Subscribe with 10% off"}
    }
}

def update_jsons():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "reviews" not in data:
            data["reviews"] = {}
        
        for key, trans in REVIEWS["reviews"].items():
            data["reviews"][key] = trans[lang]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Updated {lang}.json with reviews")

if __name__ == "__main__":
    update_jsons()
    print("Done!")
