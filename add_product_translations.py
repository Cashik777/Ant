#!/usr/bin/env python3
"""Add product_page translations to JSON files"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

PRODUCT_PAGE_TRANS = {
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
        "spec_region": {"uk": "Регіон:", "ru": "Регион:", "en": "Region:"},
        "spec_processing": {"uk": "Обробка:", "ru": "Обработка:", "en": "Processing:"},
        "spec_altitude": {"uk": "Висота вирощування:", "ru": "Высота выращивания:", "en": "Altitude:"},
        "spec_variety": {"uk": "Сорт:", "ru": "Сорт:", "en": "Variety:"},
        "spec_roast": {"uk": "Обсмажка:", "ru": "Обжарка:", "en": "Roast:"},
        "spec_sca": {"uk": "SCA оцінка:", "ru": "SCA оценка:", "en": "SCA Score:"},
        "spec_acidity": {"uk": "Кислотність:", "ru": "Кислотность:", "en": "Acidity:"},
        "spec_body": {"uk": "Тіло:", "ru": "Тело:", "en": "Body:"},
        "spec_weight": {"uk": "Вага:", "ru": "Вес:", "en": "Weight:"},
        "spec_packaging": {"uk": "Упаковка:", "ru": "Упаковка:", "en": "Packaging:"},
        "brewing_title": {"uk": "Рекомендації по заварюванню", "ru": "Рекомендации по завариванию", "en": "Brewing Recommendations"},
        "brewing_dose": {"uk": "Дозування:", "ru": "Дозировка:", "en": "Dosage:"},
        "brewing_grind": {"uk": "Помел:", "ru": "Помол:", "en": "Grind:"},
        "brewing_temp": {"uk": "Температура:", "ru": "Температура:", "en": "Temperature:"},
        "brewing_time": {"uk": "Час:", "ru": "Время:", "en": "Time:"},
        "reviews_based": {"uk": "На основі 24 відгуків", "ru": "На основе 24 отзывов", "en": "Based on 24 reviews"},
        "leave_review": {"uk": "Залишити відгук", "ru": "Оставить отзыв", "en": "Leave Review"},
        "your_rating": {"uk": "Ваша оцінка:", "ru": "Ваша оценка:", "en": "Your Rating:"},
        "your_name": {"uk": "Ваше ім'я:", "ru": "Ваше имя:", "en": "Your Name:"},
        "your_review": {"uk": "Відгук:", "ru": "Отзыв:", "en": "Review:"},
        "submit_review": {"uk": "Надіслати відгук", "ru": "Отправить отзыв", "en": "Submit Review"},
        "verified_purchase": {"uk": "✓ Підтверджена покупка", "ru": "✓ Подтвержденная покупка", "en": "✓ Verified Purchase"},
        "show_all_reviews": {"uk": "Показати всі відгуки", "ru": "Показать все отзывы", "en": "Show All Reviews"},
        "related_products": {"uk": "Схожі товари", "ru": "Похожие товары", "en": "Related Products"}
    },
    "cart": {
        "your_cart": {"uk": "Ваш кошик", "ru": "Ваша корзина", "en": "Your Cart"},
        "checkout": {"uk": "Оформити замовлення", "ru": "Оформить заказ", "en": "Checkout"},
        "empty": {"uk": "Кошик порожній", "ru": "Корзина пуста", "en": "Cart is Empty"},
        "to_catalog": {"uk": "Перейти до каталогу", "ru": "Перейти в каталог", "en": "Go to Catalog"}
    }
}

def update_jsons():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for section, keys in PRODUCT_PAGE_TRANS.items():
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
