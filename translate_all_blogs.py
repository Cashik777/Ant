#!/usr/bin/env python3
"""Add translations for all blog posts"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_POSTS = {
    "blog_posts": {
        # ARABICA VS ROBUSTA
        "arabica_robusta": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "6 хвилин читання", "ru": "6 минут чтения", "en": "6 min read"},
            "title": {"uk": "Арабіка проти Робусти: повне порівняння", "ru": "Арабика против Робусты: полное сравнение", "en": "Arabica vs Robusta: Complete Comparison"},
            "subtitle": {"uk": "Два найпопулярніших сорти кави у світі", "ru": "Два самых популярных сорта кофе в мире", "en": "The two most popular coffee varieties in the world"},
            "intro": {"uk": "Арабіка і Робуста — два основних комерційних види кави. Хоча Арабіка вважається преміальнішою, Робуста має свої переваги.", "ru": "Арабика и Робуста — два основных коммерческих вида кофе. Хотя Арабика считается более премиальной, Робуста имеет свои преимущества.", "en": "Arabica and Robusta are the two main commercial coffee species. While Arabica is considered more premium, Robusta has its advantages."}
        },
        
        # BEAN TO CUP
        "bean_to_cup": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "8 хвилин читання", "ru": "8 минут чтения", "en": "8 min read"},
            "title": {"uk": "Від зерна до чашки: подорож кави", "ru": "От зерна до чашки: путешествие кофе", "en": "From Bean to Cup: Coffee's Journey"},
            "subtitle": {"uk": "Повний шлях кави від плантації до вашого столу", "ru": "Полный путь кофе от плантации до вашего стола", "en": "Complete coffee journey from plantation to your table"},
            "intro": {"uk": "Від маленького зеленого зерна до ароматної чашки — кава проходить довгий шлях. Давайте розглянемо кожен етап.", "ru": "От маленького зеленого зерна до ароматной чашки — кофе проходит долгий путь. Давайте рассмотрим каждый этап.", "en": "From a small green bean to an aromatic cup — coffee travels a long journey. Let's look at each stage."}
        },
        
        # BREWING METHODS
        "brewing_methods": {
            "category": {"uk": "Методи", "ru": "Методы", "en": "Methods"},
            "reading_time": {"uk": "10 хвилин читання", "ru": "10 минут чтения", "en": "10 min read"},
            "title": {"uk": "Методи заварювання кави: повний гід", "ru": "Методы заваривания кофе: полный гид", "en": "Coffee Brewing Methods: Complete Guide"},
            "subtitle": {"uk": "Від еспресо до колд брю — всі способи", "ru": "От эспрессо до колд брю — все способы", "en": "From espresso to cold brew — all methods"},
            "intro": {"uk": "Кожен метод заварювання розкриває різні грані смаку кави. Ось повний огляд найпопулярніших методів.", "ru": "Каждый метод заваривания раскрывает разные грани вкуса кофе. Вот полный обзор самых популярных методов.", "en": "Each brewing method reveals different flavor dimensions. Here's a complete overview of the most popular methods."}
        },
        
        # COFFEE PROCESSING
        "coffee_processing": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "7 хвилин читання", "ru": "7 минут чтения", "en": "7 min read"},
            "title": {"uk": "Способи обробки кави", "ru": "Способы обработки кофе", "en": "Coffee Processing Methods"},
            "subtitle": {"uk": "Як обробка впливає на смак", "ru": "Как обработка влияет на вкус", "en": "How processing affects taste"},
            "intro": {"uk": "Натуральна, мита, хані — різні способи обробки створюють різні смакові профілі.", "ru": "Натуральная, мытая, хани — разные способы обработки создают разные вкусовые профили.", "en": "Natural, washed, honey — different processing methods create different flavor profiles."}
        },
        
        # COFFEE SEASONALITY
        "coffee_seasonality": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Сезонність кави", "ru": "Сезонность кофе", "en": "Coffee Seasonality"},
            "subtitle": {"uk": "Коли кава найсвіжіша", "ru": "Когда кофе самый свежий", "en": "When coffee is freshest"},
            "intro": {"uk": "Як і фрукти, кава має свої сезони збору. Свіжий урожай — завжди найсмачніший.", "ru": "Как и фрукты, кофе имеет свои сезоны сбора. Свежий урожай — всегда самый вкусный.", "en": "Like fruits, coffee has its harvest seasons. Fresh harvest is always the tastiest."}
        },
        
        # COFFEE STORAGE
        "coffee_storage": {
            "category": {"uk": "Поради", "ru": "Советы", "en": "Tips"},
            "reading_time": {"uk": "4 хвилини читання", "ru": "4 минуты чтения", "en": "4 min read"},
            "title": {"uk": "Як зберігати каву", "ru": "Как хранить кофе", "en": "How to Store Coffee"},
            "subtitle": {"uk": "Секрети збереження свіжості", "ru": "Секреты сохранения свежести", "en": "Secrets to maintaining freshness"},
            "intro": {"uk": "Правильне зберігання — ключ до довготривалої свіжості кави.", "ru": "Правильное хранение — ключ к долговременной свежести кофе.", "en": "Proper storage is the key to long-lasting coffee freshness."}
        },
        
        # COLD BREW GUIDE
        "cold_brew": {
            "category": {"uk": "Рецепти", "ru": "Рецепты", "en": "Recipes"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Cold Brew: повний гід", "ru": "Cold Brew: полный гид", "en": "Cold Brew: Complete Guide"},
            "subtitle": {"uk": "Ідеальний літній напій", "ru": "Идеальный летний напиток", "en": "The perfect summer drink"},
            "intro": {"uk": "Cold brew — це не просто холодна кава. Це окремий метод заварювання з унікальним смаком.", "ru": "Cold brew — это не просто холодный кофе. Это отдельный метод заваривания с уникальным вкусом.", "en": "Cold brew is not just cold coffee. It's a separate brewing method with a unique taste."}
        },
        
        # ESPRESSO GUIDE
        "espresso_guide": {
            "category": {"uk": "Методи", "ru": "Методы", "en": "Methods"},
            "reading_time": {"uk": "8 хвилин читання", "ru": "8 минут чтения", "en": "8 min read"},
            "title": {"uk": "Еспресо: повний гід", "ru": "Эспрессо: полный гид", "en": "Espresso: Complete Guide"},
            "subtitle": {"uk": "Секрети ідеального шоту", "ru": "Секреты идеального шота", "en": "Secrets of the perfect shot"},
            "intro": {"uk": "Еспресо — основа більшості кавових напоїв. Ось як приготувати ідеальний шот.", "ru": "Эспрессо — основа большинства кофейных напитков. Вот как приготовить идеальный шот.", "en": "Espresso is the base of most coffee drinks. Here's how to make the perfect shot."}
        },
        
        # ETHIOPIA ORIGINS
        "ethiopia_origins": {
            "category": {"uk": "Регіони", "ru": "Регионы", "en": "Regions"},
            "reading_time": {"uk": "6 хвилин читання", "ru": "6 минут чтения", "en": "6 min read"},
            "title": {"uk": "Ефіопія: батьківщина кави", "ru": "Эфиопия: родина кофе", "en": "Ethiopia: The Birthplace of Coffee"},
            "subtitle": {"uk": "Історія та регіони", "ru": "История и регионы", "en": "History and regions"},
            "intro": {"uk": "Ефіопія — єдина країна, де кава росте дикоросом. Тут народилась кавова культура.", "ru": "Эфиопия — единственная страна, где кофе растет дикорослым. Здесь родилась кофейная культура.", "en": "Ethiopia is the only country where coffee grows wild. Coffee culture was born here."}
        },
        
        # FRENCH PRESS
        "french_press": {
            "category": {"uk": "Методи", "ru": "Методы", "en": "Methods"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Френч-прес: ідеальний рецепт", "ru": "Френч-пресс: идеальный рецепт", "en": "French Press: Perfect Recipe"},
            "subtitle": {"uk": "Простий спосіб смачної кави", "ru": "Простой способ вкусного кофе", "en": "Simple way to delicious coffee"},
            "intro": {"uk": "Френч-прес — один з найпростіших і найсмачніших методів заварювання.", "ru": "Френч-пресс — один из самых простых и вкусных методов заваривания.", "en": "French press is one of the simplest and tastiest brewing methods."}
        },
        
        # SCA GRADING
        "sca_grading": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "7 хвилин читання", "ru": "7 минут чтения", "en": "7 min read"},
            "title": {"uk": "SCA оцінювання: що означають бали", "ru": "SCA оценка: что означают баллы", "en": "SCA Grading: What the Scores Mean"},
            "subtitle": {"uk": "Як професіонали оцінюють каву", "ru": "Как профессионалы оценивают кофе", "en": "How professionals grade coffee"},
            "intro": {"uk": "SCA — світовий стандарт оцінювання кави. Розбираємо, що означають бали.", "ru": "SCA — мировой стандарт оценки кофе. Разбираем, что означают баллы.", "en": "SCA is the world standard for coffee grading. Let's break down what scores mean."}
        },
        
        # SPECIALTY COFFEE
        "specialty_coffee": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "6 хвилин читання", "ru": "6 минут чтения", "en": "6 min read"},
            "title": {"uk": "Що таке Specialty кава?", "ru": "Что такое Specialty кофе?", "en": "What is Specialty Coffee?"},
            "subtitle": {"uk": "Чому specialty варта переплати", "ru": "Почему specialty стоит переплаты", "en": "Why specialty is worth paying more"},
            "intro": {"uk": "Specialty кава — це топ 3% усієї кави у світі. Дізнайтесь, чим вона особлива.", "ru": "Specialty кофе — это топ 3% всего кофе в мире. Узнайте, чем оно особенное.", "en": "Specialty coffee is the top 3% of all coffee in the world. Learn what makes it special."}
        },
        
        # TURKA GUIDE
        "turka_guide": {
            "category": {"uk": "Методи", "ru": "Методы", "en": "Methods"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Кава в турці: традиційний спосіб", "ru": "Кофе в турке: традиционный способ", "en": "Turkish Coffee: Traditional Method"},
            "subtitle": {"uk": "Класичний рецепт кави по-турецьки", "ru": "Классический рецепт кофе по-турецки", "en": "Classic Turkish coffee recipe"},
            "intro": {"uk": "Кава по-турецьки — один з найстаріших методів приготування, що зберігся до наших днів.", "ru": "Кофе по-турецки — один из старейших методов приготовления, сохранившийся до наших дней.", "en": "Turkish coffee is one of the oldest brewing methods that has survived to this day."}
        },
        
        # V60 GUIDE
        "v60_guide": {
            "category": {"uk": "Методи", "ru": "Методы", "en": "Methods"},
            "reading_time": {"uk": "7 хвилин читання", "ru": "7 минут чтения", "en": "7 min read"},
            "title": {"uk": "V60: мистецтво пуровера", "ru": "V60: искусство пуровера", "en": "V60: The Art of Pour Over"},
            "subtitle": {"uk": "Як готувати каву на V60", "ru": "Как готовить кофе на V60", "en": "How to brew coffee with V60"},
            "intro": {"uk": "Hario V60 — культовий девайс серед любителів альтернативного заварювання.", "ru": "Hario V60 — культовый девайс среди любителей альтернативного заваривания.", "en": "Hario V60 is an iconic device among alternative brewing enthusiasts."}
        },
        
        # YIRGACHEFFE REGION
        "yirgacheffe": {
            "category": {"uk": "Регіони", "ru": "Регионы", "en": "Regions"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Йіргачеффе: квітковий рай", "ru": "Йиргачеффе: цветочный рай", "en": "Yirgacheffe: Floral Paradise"},
            "subtitle": {"uk": "Унікальний регіон Ефіопії", "ru": "Уникальный регион Эфиопии", "en": "Ethiopia's unique region"},
            "intro": {"uk": "Йіргачеффе — найпрестижніший кавовий регіон Ефіопії з унікальними квітковими нотами.", "ru": "Йиргачеффе — самый престижный кофейный регион Эфиопии с уникальными цветочными нотами.", "en": "Yirgacheffe is Ethiopia's most prestigious coffee region with unique floral notes."}
        }
    }
}

def update_jsons():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "blog_posts" not in data:
            data["blog_posts"] = {}
        
        for post_key, post_data in BLOG_POSTS["blog_posts"].items():
            if post_key not in data["blog_posts"]:
                data["blog_posts"][post_key] = {}
            for key, trans in post_data.items():
                data["blog_posts"][post_key][key] = trans[lang]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Updated {lang}.json with {len(BLOG_POSTS['blog_posts'])} blog posts")

if __name__ == "__main__":
    update_jsons()
    print("Done!")
