#!/usr/bin/env python3
"""Add translations for blog post elements (titles, categories, metadata)"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_TRANSLATIONS = {
    # Blog post titles
    "blog_posts": {
        # Categories
        "cat_coffee": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
        "cat_recipes": {"uk": "Рецепти", "ru": "Рецепты", "en": "Recipes"},
        "cat_equipment": {"uk": "Обладнання", "ru": "Оборудование", "en": "Equipment"},
        "cat_tips": {"uk": "Поради", "ru": "Советы", "en": "Tips"},
        
        # Common blog elements
        "min_read": {"uk": "хв читання", "ru": "мин чтения", "en": "min read"},
        "read_more": {"uk": "Читати далі →", "ru": "Читать далее →", "en": "Read More →"},
        "views": {"uk": "переглядів", "ru": "просмотров", "en": "views"},
        "share": {"uk": "Поділитись", "ru": "Поделиться", "en": "Share"},
        "related": {"uk": "Схожі статті", "ru": "Похожие статьи", "en": "Related Articles"},
        "back_to_blog": {"uk": "← Назад до блогу", "ru": "← Назад в блог", "en": "← Back to Blog"},
        "table_of_contents": {"uk": "Зміст", "ru": "Содержание", "en": "Table of Contents"},
        "author": {"uk": "Автор", "ru": "Автор", "en": "Author"},
        "published": {"uk": "Опубліковано", "ru": "Опубликовано", "en": "Published"},
        
        # Blog post titles
        "arabica_robusta_title": {"uk": "Арабіка проти Робусти: все, що потрібно знати", "ru": "Арабика против Робусты: всё, что нужно знать", "en": "Arabica vs Robusta: Everything You Need to Know"},
        "bean_to_cup_title": {"uk": "Від зерна до чашки: повний шлях кави", "ru": "От зерна до чашки: полный путь кофе", "en": "From Bean to Cup: The Complete Coffee Journey"},
        "brewing_methods_title": {"uk": "Методи заварювання кави: повний гід", "ru": "Методы заваривания кофе: полный гид", "en": "Coffee Brewing Methods: Complete Guide"},
        "coffee_processing_title": {"uk": "Способи обробки кави", "ru": "Способы обработки кофе", "en": "Coffee Processing Methods"},
        "coffee_seasonality_title": {"uk": "Сезонність кави: коли найкраща?", "ru": "Сезонность кофе: когда лучший?", "en": "Coffee Seasonality: When Is It Best?"},
        "coffee_storage_title": {"uk": "Як зберігати каву правильно", "ru": "Как хранить кофе правильно", "en": "How to Store Coffee Properly"},
        "cold_brew_title": {"uk": "Cold Brew: повний гід", "ru": "Cold Brew: полный гид", "en": "Cold Brew: Complete Guide"},
        "espresso_title": {"uk": "Еспресо: секрети ідеального шоту", "ru": "Эспрессо: секреты идеального шота", "en": "Espresso: Secrets of the Perfect Shot"},
        "ethiopia_origins_title": {"uk": "Ефіопія: батьківщина кави", "ru": "Эфиопия: родина кофе", "en": "Ethiopia: The Birthplace of Coffee"},
        "french_press_title": {"uk": "Френч-прес: ідеальний спосіб заваріть каву", "ru": "Френч-пресс: идеальный способ заварить кофе", "en": "French Press: The Perfect Way to Brew Coffee"},
        "sca_grading_title": {"uk": "SCA оцінювання: що означають бали", "ru": "SCA оценка: что означают баллы", "en": "SCA Grading: What the Scores Mean"},
        "specialty_title": {"uk": "Що таке Specialty кава?", "ru": "Что такое Specialty кофе?", "en": "What is Specialty Coffee?"},
        "turka_title": {"uk": "Турка: традиційний спосіб приготування", "ru": "Турка: традиционный способ приготовления", "en": "Turkish Coffee: Traditional Brewing Method"},
        "v60_title": {"uk": "V60: мистецтво фільтр-кави", "ru": "V60: искусство фильтр-кофе", "en": "V60: The Art of Filter Coffee"},
        "yirgacheffe_title": {"uk": "Йіргачеффе: регіон унікального смаку", "ru": "Йиргачеффе: регион уникального вкуса", "en": "Yirgacheffe: Region of Unique Flavor"}
    },
    
    # Index page reviews
    "reviews": {
        "title": {"uk": "Що кажуть наші клієнти", "ru": "Что говорят наши клиенты", "en": "What Our Customers Say"},
        "verified": {"uk": "Підтверджений покупець", "ru": "Подтвержденный покупатель", "en": "Verified Buyer"},
        "review1_text": {"uk": "Найкраща кава, яку я пробував! Аромат неймовірний.", "ru": "Лучший кофе, который я пробовал! Аромат невероятный.", "en": "The best coffee I've ever tried! The aroma is incredible."},
        "review1_author": {"uk": "Олександр К.", "ru": "Александр К.", "en": "Alexander K."},
        "review2_text": {"uk": "Швидка доставка, свіжа кава. Раджу всім!", "ru": "Быстрая доставка, свежий кофе. Рекомендую всем!", "en": "Fast delivery, fresh coffee. Recommend to everyone!"},
        "review2_author": {"uk": "Марина С.", "ru": "Марина С.", "en": "Marina S."},
        "review3_text": {"uk": "Підписка — це геніально. Кава приходить автоматично!", "ru": "Подписка — это гениально. Кофе приходит автоматически!", "en": "Subscription is genius. Coffee arrives automatically!"},
        "review3_author": {"uk": "Ігор М.", "ru": "Игорь М.", "en": "Igor M."}
    }
}

def update_jsons():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for section, keys in BLOG_TRANSLATIONS.items():
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
