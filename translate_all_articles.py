#!/usr/bin/env python3
"""Add translations for ALL articles and blog posts"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

# All article and blog translations
ALL_CONTENT = {
    "articles": {
        # ETHIOPIA COFFEE ORIGIN
        "ethiopia_origin": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "7 хвилин читання", "ru": "7 минут чтения", "en": "7 min read"},
            "title": {"uk": "Ефіопія — батьківщина кави", "ru": "Эфиопия — родина кофе", "en": "Ethiopia — The Birthplace of Coffee"},
            "subtitle": {"uk": "Дізнайтесь про історію та унікальність ефіопської кави", "ru": "Узнайте об истории и уникальности эфиопского кофе", "en": "Learn about the history and uniqueness of Ethiopian coffee"},
            "intro": {"uk": "Ефіопія — єдина країна у світі, де кава росте дикоросом. Саме тут понад 1000 років тому пастух Калді вперше помітив, як його кози стали енергійнішими після поїдання червоних ягід.", "ru": "Эфиопия — единственная страна в мире, где кофе растет дикорослым. Именно здесь более 1000 лет назад пастух Калди впервые заметил, как его козы стали энергичнее после поедания красных ягод.", "en": "Ethiopia is the only country in the world where coffee grows wild. It was here, over 1000 years ago, that shepherd Kaldi first noticed his goats becoming more energetic after eating red berries."}
        },
        
        # LIGHT VS DARK ROAST
        "light_vs_dark": {
            "category": {"uk": "Обсмажка", "ru": "Обжарка", "en": "Roasting"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Світла vs Темна обсмажка: що обрати?", "ru": "Светлая vs Темная обжарка: что выбрать?", "en": "Light vs Dark Roast: What to Choose?"},
            "subtitle": {"uk": "Розбираємо різницю між світлою та темною обсмажкою", "ru": "Разбираем разницу между светлой и темной обжаркой", "en": "Understanding the difference between light and dark roasts"},
            "intro": {"uk": "Обсмажка — один з найважливіших факторів, що впливає на смак кави. Світла обсмажка зберігає природні характеристики зерна, тоді як темна створює більш насичений, карамельний смак.", "ru": "Обжарка — один из важнейших факторов, влияющих на вкус кофе. Светлая обжарка сохраняет природные характеристики зерна, тогда как темная создает более насыщенный, карамельный вкус.", "en": "Roasting is one of the most important factors affecting coffee taste. Light roast preserves the bean's natural characteristics, while dark roast creates a richer, caramel flavor."}
        },
        
        # WATER FOR COFFEE
        "water_for_coffee": {
            "category": {"uk": "Поради", "ru": "Советы", "en": "Tips"},
            "reading_time": {"uk": "4 хвилини читання", "ru": "4 минуты чтения", "en": "4 min read"},
            "title": {"uk": "Вода для кави: повний гід", "ru": "Вода для кофе: полный гид", "en": "Water for Coffee: Complete Guide"},
            "subtitle": {"uk": "Як вода впливає на смак вашої кави", "ru": "Как вода влияет на вкус вашего кофе", "en": "How water affects your coffee taste"},
            "intro": {"uk": "Кава на 98% складається з води, тому її якість критично важлива. Занадто м'яка вода дасть плоский смак, занадто жорстка — занадто гіркий.", "ru": "Кофе на 98% состоит из воды, поэтому ее качество критически важно. Слишком мягкая вода даст плоский вкус, слишком жесткая — слишком горький.", "en": "Coffee is 98% water, so water quality is critical. Too soft water gives flat taste, too hard — too bitter."}
        },
        
        # AEROPRESS RECIPES
        "aeropress": {
            "category": {"uk": "Рецепти", "ru": "Рецепты", "en": "Recipes"},
            "reading_time": {"uk": "6 хвилин читання", "ru": "6 минут чтения", "en": "6 min read"},
            "title": {"uk": "Аеропрес: 5 найкращих рецептів", "ru": "Аэропресс: 5 лучших рецептов", "en": "AeroPress: 5 Best Recipes"},
            "subtitle": {"uk": "Від класичного до чемпіонського рецепту", "ru": "От классического до чемпионского рецепта", "en": "From classic to championship recipes"},
            "intro": {"uk": "Аеропрес — унікальний девайс, який дозволяє готувати каву безліччю способів. Ось 5 перевірених рецептів для різних смакових профілів.", "ru": "Аэропресс — уникальный девайс, который позволяет готовить кофе множеством способов. Вот 5 проверенных рецептов для разных вкусовых профилей.", "en": "AeroPress is a unique device that allows brewing coffee in countless ways. Here are 5 proven recipes for different flavor profiles."}
        },
        
        # V60 GUIDE
        "v60_guide": {
            "category": {"uk": "Обладнання", "ru": "Оборудование", "en": "Equipment"},
            "reading_time": {"uk": "8 хвилин читання", "ru": "8 минут чтения", "en": "8 min read"},
            "title": {"uk": "V60: мистецтво пуровера", "ru": "V60: искусство пуровера", "en": "V60: The Art of Pour Over"},
            "subtitle": {"uk": "Повний гід по заварюванню на Hario V60", "ru": "Полный гид по завариванию на Hario V60", "en": "Complete guide to brewing with Hario V60"},
            "intro": {"uk": "V60 від Hario — один з найпопулярніших методів альтернативного заварювання у світі. Конічна форма та спіральні ребра дозволяють контролювати екстракцію як ніколи.", "ru": "V60 от Hario — один из самых популярных методов альтернативного заваривания в мире. Коническая форма и спиральные ребра позволяют контролировать экстракцию как никогда.", "en": "V60 by Hario is one of the most popular alternative brewing methods in the world. Its conical shape and spiral ribs allow unprecedented extraction control."}
        },
        
        # ESPRESSO MISTAKES
        "espresso_mistakes": {
            "category": {"uk": "Поради", "ru": "Советы", "en": "Tips"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "7 помилок при приготуванні еспресо", "ru": "7 ошибок при приготовлении эспрессо", "en": "7 Espresso Making Mistakes"},
            "subtitle": {"uk": "Як уникнути типових помилок домашнього бариста", "ru": "Как избежать типичных ошибок домашнего бариста", "en": "How to avoid common home barista mistakes"},
            "intro": {"uk": "Навіть з дорогою кавомашиною можна готувати погану каву. Ось 7 найпоширеніших помилок, які роблять початківці.", "ru": "Даже с дорогой кофемашиной можно готовить плохой кофе. Вот 7 самых распространенных ошибок, которые делают новички.", "en": "Even with an expensive machine, you can make bad coffee. Here are 7 most common mistakes beginners make."}
        },
        
        # COLD BREW
        "cold_brew": {
            "category": {"uk": "Рецепти", "ru": "Рецепты", "en": "Recipes"},
            "reading_time": {"uk": "4 хвилини читання", "ru": "4 минуты чтения", "en": "4 min read"},
            "title": {"uk": "Cold Brew: ідеальний літній напій", "ru": "Cold Brew: идеальный летний напиток", "en": "Cold Brew: Perfect Summer Drink"},
            "subtitle": {"uk": "Як готувати холодну каву вдома", "ru": "Как готовить холодный кофе дома", "en": "How to make cold coffee at home"},
            "intro": {"uk": "Cold brew — це кава холодного заварювання, яка готується 12-24 години. Результат — м'який, солодкий напій без гіркоти.", "ru": "Cold brew — это кофе холодного заваривания, который готовится 12-24 часа. Результат — мягкий, сладкий напиток без горечи.", "en": "Cold brew is coffee brewed cold for 12-24 hours. The result is a smooth, sweet drink without bitterness."}
        },
        
        # COFFEE STORAGE
        "coffee_storage": {
            "category": {"uk": "Поради", "ru": "Советы", "en": "Tips"},
            "reading_time": {"uk": "3 хвилини читання", "ru": "3 минуты чтения", "en": "3 min read"},
            "title": {"uk": "Як правильно зберігати каву", "ru": "Как правильно хранить кофе", "en": "How to Store Coffee Properly"},
            "subtitle": {"uk": "Зберігайте свіжість кави максимально довго", "ru": "Сохраняйте свежесть кофе максимально долго", "en": "Keep your coffee fresh as long as possible"},
            "intro": {"uk": "Кава — це продукт, який швидко втрачає свіжість. Ось найкращі практики зберігання.", "ru": "Кофе — это продукт, который быстро теряет свежесть. Вот лучшие практики хранения.", "en": "Coffee is a product that quickly loses freshness. Here are the best storage practices."}
        },
        
        # GRINDER GUIDE  
        "grinder_guide": {
            "category": {"uk": "Обладнання", "ru": "Оборудование", "en": "Equipment"},
            "reading_time": {"uk": "6 хвилин читання", "ru": "6 минут чтения", "en": "6 min read"},
            "title": {"uk": "Кавомолка: як обрати?", "ru": "Кофемолка: как выбрать?", "en": "Coffee Grinder: How to Choose?"},
            "subtitle": {"uk": "Жорнова vs ножова: повне порівняння", "ru": "Жерновая vs ножевая: полное сравнение", "en": "Burr vs Blade: complete comparison"},
            "intro": {"uk": "Кавомолка — найважливіший інструмент після самої кави. Правильний помел може повністю змінити смак вашого напою.", "ru": "Кофемолка — самый важный инструмент после самого кофе. Правильный помол может полностью изменить вкус вашего напитка.", "en": "A grinder is the most important tool after coffee itself. Proper grinding can completely change your drink's taste."}
        },
        
        # CAFFEINE MYTHS
        "caffeine_myths": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "5 міфів про кофеїн", "ru": "5 мифов о кофеине", "en": "5 Caffeine Myths"},
            "subtitle": {"uk": "Розвінчуємо популярні міфи про каву та кофеїн", "ru": "Развенчиваем популярные мифы о кофе и кофеине", "en": "Debunking popular myths about coffee and caffeine"},
            "intro": {"uk": "Про кофеїн ходить багато легенд. Давайте розберемось, що правда, а що ні.", "ru": "О кофеине ходит много легенд. Давайте разберемся, что правда, а что нет.", "en": "Many legends surround caffeine. Let's figure out what's true and what's not."}
        },
        
        # TURKA RECIPE
        "turka_recipe": {
            "category": {"uk": "Рецепти", "ru": "Рецепты", "en": "Recipes"},
            "reading_time": {"uk": "4 хвилини читання", "ru": "4 минуты чтения", "en": "4 min read"},
            "title": {"uk": "Кава по-турецьки: класичний рецепт", "ru": "Кофе по-турецки: классический рецепт", "en": "Turkish Coffee: Classic Recipe"},
            "subtitle": {"uk": "Традиційний спосіб приготування в турці", "ru": "Традиционный способ приготовления в турке", "en": "Traditional brewing method in cezve"},
            "intro": {"uk": "Кава по-турецьки — один з найстаріших способів приготування кави. Секрет ідеальної чашки в деталях.", "ru": "Кофе по-турецки — один из старейших способов приготовления кофе. Секрет идеальной чашки в деталях.", "en": "Turkish coffee is one of the oldest brewing methods. The secret to a perfect cup is in the details."}
        },
        
        # NATURAL VS WASHED
        "natural_washed": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Натуральна vs Мита обробка", "ru": "Натуральная vs Мытая обработка", "en": "Natural vs Washed Processing"},
            "subtitle": {"uk": "Як спосіб обробки впливає на смак", "ru": "Как способ обработки влияет на вкус", "en": "How processing method affects taste"},
            "intro": {"uk": "Обробка кави — це процес видалення м'якоті з ягоди. Два основних методи — натуральний (сухий) та митий (мокрий) — дають кардинально різні смакові профілі.", "ru": "Обработка кофе — это процесс удаления мякоти из ягоды. Два основных метода — натуральный (сухой) и мытый (мокрый) — дают кардинально разные вкусовые профили.", "en": "Coffee processing is removing pulp from the cherry. Two main methods — natural (dry) and washed (wet) — create drastically different flavor profiles."}
        },
        
        # SIDAMO GUIDE
        "sidamo_guide": {
            "category": {"uk": "Регіони", "ru": "Регионы", "en": "Regions"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Сідамо: регіон ягідної кави", "ru": "Сидамо: регион ягодного кофе", "en": "Sidamo: Region of Berry Coffee"},
            "subtitle": {"uk": "Все про кавовий регіон Сідамо", "ru": "Всё о кофейном регионе Сидамо", "en": "Everything about the Sidamo coffee region"},
            "intro": {"uk": "Сідамо — один з найвідоміших кавових регіонів Ефіопії, відомий своїми ягідними та цитрусовими нотами.", "ru": "Сидамо — один из самых известных кофейных регионов Эфиопии, известный своими ягодными и цитрусовыми нотами.", "en": "Sidamo is one of Ethiopia's most famous coffee regions, known for its berry and citrus notes."}
        },
        
        # YIRGACHEFFE REGION
        "yirgacheffe_region": {
            "category": {"uk": "Регіони", "ru": "Регионы", "en": "Regions"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Йіргачеффе: квітковий рай", "ru": "Йиргачеффе: цветочный рай", "en": "Yirgacheffe: Floral Paradise"},
            "subtitle": {"uk": "Унікальний терруар регіону Йіргачеффе", "ru": "Уникальный терруар региона Йиргачеффе", "en": "The unique terroir of Yirgacheffe region"},
            "intro": {"uk": "Йіргачеффе вважається найпрестижнішим кавовим регіоном Ефіопії. Кава звідси має яскраві квіткові ноти, цитрусову кислотність та чайну текстуру.", "ru": "Йиргачеффе считается самым престижным кофейным регионом Эфиопии. Кофе отсюда имеет яркие цветочные ноты, цитрусовую кислотность и чайную текстуру.", "en": "Yirgacheffe is considered Ethiopia's most prestigious coffee region. Coffee from here has bright floral notes, citrus acidity, and tea-like texture."}
        }
    },
    
    # Common elements for all articles
    "common": {
        "back": {"uk": "Назад", "ru": "Назад", "en": "Back"},
        "back_to_articles": {"uk": "до статей", "ru": "к статьям", "en": "to Articles"},
        "back_to_blog": {"uk": "до блогу", "ru": "в блог", "en": "to Blog"},
        "share_article": {"uk": "Поділитись статтею", "ru": "Поделиться статьей", "en": "Share Article"},
        "read_also": {"uk": "Читайте також", "ru": "Читайте также", "en": "Read Also"},
        "tags": {"uk": "Теги", "ru": "Теги", "en": "Tags"}
    }
}

def update_jsons():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Add articles
        if "articles" not in data:
            data["articles"] = {}
        
        for article_key, article_data in ALL_CONTENT["articles"].items():
            if article_key not in data["articles"]:
                data["articles"][article_key] = {}
            for key, trans in article_data.items():
                data["articles"][article_key][key] = trans[lang]
        
        # Add common
        if "common" not in data:
            data["common"] = {}
        for key, trans in ALL_CONTENT["common"].items():
            data["common"][key] = trans[lang]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Updated {lang}.json with {len(ALL_CONTENT['articles'])} articles")

if __name__ == "__main__":
    update_jsons()
    print("Done!")
