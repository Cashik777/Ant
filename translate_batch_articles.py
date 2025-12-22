#!/usr/bin/env python3
"""
Complete translations for multiple articles at once
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

# All remaining articles with full translations
ALL_ARTICLES = {
    "light_vs_dark": {
        "uk": {
            "title": "Світла чи темна обсмажка: що обрати?",
            "subtitle": "Порівняння смакових профілів, рівнів кофеїну та рекомендації для різних способів приготування.",
            "category": "Обсмажка",
            "reading_time": "6 хвилин читання",
            "intro": "Один з найчастіших питань від покупців: яка обсмажка краща — світла чи темна? Коротка відповідь: це залежить від ваших уподобань. Довга відповідь — у цій статті.",
            "h2_process": "Що відбувається під час обсмажки?",
            "p_process": "Обсмажка — це термічна обробка зеленого кавового зерна при температурі 180-230°C. Під час цього процесу зерно проходить хімічні реакції, які формують смак, аромат та колір кави.",
            "h2_light": "Світла обсмажка (Light Roast)",
            "p_light": "Зерно обсмажується до першого \"кряку\" (crack) — характерного звуку, коли зерно тріскається від внутрішнього тиску. Колір — світло-коричневий.",
            "h2_medium": "Середня обсмажка (Medium Roast)",
            "p_medium": "Обсмажка триває трохи довше після першого кряку. Колір — насичений коричневий. Це найпопулярніший вибір для більшості споживачів.",
            "h2_dark": "Темна обсмажка (Dark Roast)",
            "p_dark": "Обсмажка продовжується до другого кряку і далі. Колір — темно-коричневий до майже чорного, часто з маслянистою поверхнею.",
            "h2_caffeine": "Міф про кофеїн",
            "p_caffeine": "Багато хто вважає, що темна обсмажка \"міцніша\" і містить більше кофеїну. Насправді це міф! Кількість кофеїну майже однакова в усіх обсмажках, а іноді світла містить навіть трохи більше.",
            "h2_choose": "Як обрати?",
            "p_choose": "Для альтернативи (V60, аеропрес) краще підходить світла обсмажка. Для еспресо — середня або темна. Для турки — темна. Але найголовніше — експериментуйте!",
            "cta_title": "Спробуйте різні обсмажки",
            "cta_text": "У нашому каталозі є кава від світлої до темної обсмажки",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Светлая или тёмная обжарка: что выбрать?",
            "subtitle": "Сравнение вкусовых профилей, уровней кофеина и рекомендации для разных способов приготовления.",
            "category": "Обжарка",
            "reading_time": "6 минут чтения",
            "intro": "Один из самых частых вопросов от покупателей: какая обжарка лучше — светлая или тёмная? Короткий ответ: это зависит от ваших предпочтений. Длинный ответ — в этой статье.",
            "h2_process": "Что происходит во время обжарки?",
            "p_process": "Обжарка — это термическая обработка зелёного кофейного зерна при температуре 180-230°C. Во время этого процесса зерно проходит химические реакции, которые формируют вкус, аромат и цвет кофе.",
            "h2_light": "Светлая обжарка (Light Roast)",
            "p_light": "Зерно обжаривается до первого \"крэка\" (crack) — характерного звука, когда зерно трескается от внутреннего давления. Цвет — светло-коричневый.",
            "h2_medium": "Средняя обжарка (Medium Roast)",
            "p_medium": "Обжарка длится чуть дольше после первого крэка. Цвет — насыщенный коричневый. Это самый популярный выбор для большинства потребителей.",
            "h2_dark": "Тёмная обжарка (Dark Roast)",
            "p_dark": "Обжарка продолжается до второго крэка и дальше. Цвет — тёмно-коричневый до почти чёрного, часто с маслянистой поверхностью.",
            "h2_caffeine": "Миф о кофеине",
            "p_caffeine": "Многие считают, что тёмная обжарка \"крепче\" и содержит больше кофеина. На самом деле это миф! Количество кофеина почти одинаково во всех обжарках, а иногда светлая содержит даже чуть больше.",
            "h2_choose": "Как выбрать?",
            "p_choose": "Для альтернативы (V60, аэропресс) лучше подходит светлая обжарка. Для эспрессо — средняя или тёмная. Для турки — тёмная. Но самое главное — экспериментируйте!",
            "cta_title": "Попробуйте разные обжарки",
            "cta_text": "В нашем каталоге есть кофе от светлой до тёмной обжарки",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Light or Dark Roast: What to Choose?",
            "subtitle": "Comparing flavor profiles, caffeine levels, and recommendations for different brewing methods.",
            "category": "Roasting",
            "reading_time": "6 min read",
            "intro": "One of the most common questions from buyers: which roast is better — light or dark? Short answer: it depends on your preferences. Long answer — in this article.",
            "h2_process": "What Happens During Roasting?",
            "p_process": "Roasting is the thermal processing of green coffee beans at 180-230°C. During this process, the bean undergoes chemical reactions that form the taste, aroma, and color of coffee.",
            "h2_light": "Light Roast",
            "p_light": "The bean is roasted until the first \"crack\" — a characteristic sound when the bean cracks from internal pressure. Color — light brown.",
            "h2_medium": "Medium Roast",
            "p_medium": "Roasting continues slightly longer after the first crack. Color — rich brown. This is the most popular choice for most consumers.",
            "h2_dark": "Dark Roast",
            "p_dark": "Roasting continues until the second crack and beyond. Color — dark brown to almost black, often with an oily surface.",
            "h2_caffeine": "The Caffeine Myth",
            "p_caffeine": "Many believe that dark roast is \"stronger\" and contains more caffeine. Actually, this is a myth! The caffeine content is almost the same across all roasts, and sometimes light roast even contains slightly more.",
            "h2_choose": "How to Choose?",
            "p_choose": "For alternative methods (V60, Aeropress) light roast works better. For espresso — medium or dark. For Turkish coffee — dark. But most importantly — experiment!",
            "cta_title": "Try Different Roasts",
            "cta_text": "Our catalog has coffee from light to dark roast",
            "cta_button": "To Catalog"
        }
    },
    "yirgacheffe": {
        "uk": {
            "title": "Йіргачеффе: перлина ефіопської кави",
            "subtitle": "Чому цей регіон виробляє одну з найдорожчих кав у світі та які смаки в ній шукати.",
            "category": "Про каву",
            "reading_time": "5 хвилин читання",
            "intro": "Yirgacheffe (вимовляється \"Їр-ґа-чеф-фе\") — легендарний регіон на півдні Ефіопії, який виробляє одну з найбільш впізнаваних кав у світі.",
            "h2_geography": "Географія та клімат",
            "p_geography": "Регіон розташований на висоті 1700-2200 метрів над рівнем моря, в зоні Gedeo. Це ідеальні умови для арабіки: прохолодні ночі, помірні дні, достатньо опадів та багаті вулканічні ґрунти.",
            "h2_taste": "Смаковий профіль",
            "p_taste": "Yirgacheffe славиться своїм унікальним смаком: яскраві квіткові ноти (жасмин, бергамот), цитрусова кислотність (лимон, апельсин), чайне тіло і довгий солодкий післясмак.",
            "h2_processing": "Методи обробки",
            "p_processing": "Традиційно Yirgacheffe обробляють митим способом, що дає чистий, яскравий смак. Але останнім часом натуральна обробка стає все популярнішою — вона додає солодкості та ягідних нот.",
            "cta_title": "Спробуйте Yirgacheffe",
            "cta_text": "Замовте наш Yirgacheffe з оцінкою 85+ балів",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Иргачеффе: жемчужина эфиопского кофе",
            "subtitle": "Почему этот регион производит один из самых дорогих сортов кофе в мире и какие вкусы в нём искать.",
            "category": "О кофе",
            "reading_time": "5 минут чтения",
            "intro": "Yirgacheffe (произносится \"Ир-гачеф-фе\") — легендарный регион на юге Эфиопии, производящий один из самых узнаваемых сортов кофе в мире.",
            "h2_geography": "География и климат",
            "p_geography": "Регион расположен на высоте 1700-2200 метров над уровнем моря, в зоне Gedeo. Это идеальные условия для арабики: прохладные ночи, умеренные дни, достаточно осадков и богатые вулканические почвы.",
            "h2_taste": "Вкусовой профиль",
            "p_taste": "Yirgacheffe славится своим уникальным вкусом: яркие цветочные ноты (жасмин, бергамот), цитрусовая кислотность (лимон, апельсин), чайное тело и долгое сладкое послевкусие.",
            "h2_processing": "Методы обработки",
            "p_processing": "Традиционно Yirgacheffe обрабатывают мытым способом, что даёт чистый, яркий вкус. Но в последнее время натуральная обработка становится всё популярнее — она добавляет сладости и ягодных нот.",
            "cta_title": "Попробуйте Yirgacheffe",
            "cta_text": "Закажите наш Yirgacheffe с оценкой 85+ баллов",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Yirgacheffe: The Gem of Ethiopian Coffee",
            "subtitle": "Why this region produces one of the world's most expensive coffees and what flavors to look for.",
            "category": "About Coffee",
            "reading_time": "5 min read",
            "intro": "Yirgacheffe (pronounced \"Yeer-ga-chef-eh\") is a legendary region in southern Ethiopia that produces one of the world's most recognizable coffees.",
            "h2_geography": "Geography and Climate",
            "p_geography": "The region is located at 1700-2200 meters above sea level, in the Gedeo zone. These are ideal conditions for Arabica: cool nights, moderate days, adequate rainfall, and rich volcanic soils.",
            "h2_taste": "Flavor Profile",
            "p_taste": "Yirgacheffe is famous for its unique taste: bright floral notes (jasmine, bergamot), citrus acidity (lemon, orange), tea-like body, and a long sweet aftertaste.",
            "h2_processing": "Processing Methods",
            "p_processing": "Traditionally, Yirgacheffe is washed, giving a clean, bright taste. But lately, natural processing is becoming more popular — it adds sweetness and berry notes.",
            "cta_title": "Try Yirgacheffe",
            "cta_text": "Order our 85+ point Yirgacheffe",
            "cta_button": "To Catalog"
        }
    },
    "sidamo_guide": {
        "uk": {
            "title": "Сідамо: класика ефіопської кави",
            "subtitle": "Все про найпопулярніший регіон виробництва кави в Ефіопії та його унікальний терруар.",
            "category": "Про каву",
            "reading_time": "4 хвилини читання",
            "intro": "Sidamo — один з найбільших та найвідоміших кавових регіонів Ефіопії. Саме тут виробляється більша частина ефіопської кави, що експортується.",
            "h2_region": "Про регіон",
            "p_region": "Sidamo розташований на півдні Ефіопії, на висоті 1500-2200 метрів. Регіон має ідеальний клімат для вирощування арабіки: достатньо дощів, помірні температури та родючі ґрунти.",
            "h2_taste": "Смаковий профіль",
            "p_taste": "Кава Sidamo відрізняється збалансованим смаком з нотами ягід, шоколаду та спецій. Кислотність — помірна до яскравої, тіло — середнє.",
            "cta_title": "Спробуйте Sidamo",
            "cta_text": "Замовте справжню каву з регіону Sidamo",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Сидамо: классика эфиопского кофе",
            "subtitle": "Всё о самом популярном регионе производства кофе в Эфиопии и его уникальном терруаре.",
            "category": "О кофе",
            "reading_time": "4 минуты чтения",
            "intro": "Sidamo — один из крупнейших и самых известных кофейных регионов Эфиопии. Именно здесь производится большая часть эфиопского кофе, идущего на экспорт.",
            "h2_region": "О регионе",
            "p_region": "Sidamo расположен на юге Эфиопии, на высоте 1500-2200 метров. Регион имеет идеальный климат для выращивания арабики: достаточно дождей, умеренные температуры и плодородные почвы.",
            "h2_taste": "Вкусовой профиль",
            "p_taste": "Кофе Sidamo отличается сбалансированным вкусом с нотами ягод, шоколада и специй. Кислотность — умеренная до яркой, тело — среднее.",
            "cta_title": "Попробуйте Sidamo",
            "cta_text": "Закажите настоящий кофе из региона Sidamo",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Sidamo: Classic Ethiopian Coffee",
            "subtitle": "Everything about Ethiopia's most popular coffee production region and its unique terroir.",
            "category": "About Coffee",
            "reading_time": "4 min read",
            "intro": "Sidamo is one of Ethiopia's largest and most famous coffee regions. Most of Ethiopia's exported coffee is produced here.",
            "h2_region": "About the Region",
            "p_region": "Sidamo is located in southern Ethiopia, at 1500-2200 meters elevation. The region has an ideal climate for growing Arabica: sufficient rainfall, moderate temperatures, and fertile soils.",
            "h2_taste": "Flavor Profile",
            "p_taste": "Sidamo coffee is known for its balanced taste with notes of berries, chocolate, and spices. Acidity ranges from moderate to bright, body is medium.",
            "cta_title": "Try Sidamo",
            "cta_text": "Order authentic coffee from the Sidamo region",
            "cta_button": "To Catalog"
        }
    },
    "how_to_brew_v60": {
        "uk": {
            "title": "Ідеальний V60: покроковий рецепт від бариста",
            "subtitle": "Детальна інструкція з приготування кави методом пуровер. Пропорції, температура, техніка заливання.",
            "category": "Рецепти",
            "reading_time": "4 хвилини читання",
            "intro": "V60 — один з найпопулярніших методів приготування фільтр-кави. Ось покроковий рецепт, який використовують професійні бариста.",
            "h2_equipment": "Що вам потрібно",
            "p_equipment": "Пуровер V60, паперові фільтри, кавомолка, чайник з гусачком, ваги, таймер, 15г кави, 250мл води (94°C).",
            "h2_ratio": "Пропорції",
            "p_ratio": "Класична пропорція для V60: 1:16.6 (15г кави на 250мл води). Для міцнішої кави використовуйте 1:15, для легшої — 1:17.",
            "h2_recipe": "Рецепт",
            "p_step1": "Промийте фільтр гарячою водою. Це прибере паперовий присмак та прогріє пуровер.",
            "p_step2": "Засипте змелену каву (помел як морська сіль) та зробіть заглибину у центрі.",
            "p_step3": "Почніть з преінфузії: залийте 30мл води, почекайте 30-45 секунд поки кава \"цвіте\".",
            "p_step4": "Продовжуйте заливати воду по колу, від центру до країв. Загальний час заварювання: 2:30-3:00.",
            "cta_title": "Замовте каву для V60",
            "cta_text": "Рекомендуємо світлу обсмажку для найкращого смаку",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Идеальный V60: пошаговый рецепт от баристы",
            "subtitle": "Детальная инструкция по приготовлению кофе методом пуровер. Пропорции, температура, техника пролива.",
            "category": "Рецепты",
            "reading_time": "4 минуты чтения",
            "intro": "V60 — один из самых популярных методов приготовления фильтр-кофе. Вот пошаговый рецепт, который используют профессиональные баристы.",
            "h2_equipment": "Что вам нужно",
            "p_equipment": "Пуровер V60, бумажные фильтры, кофемолка, чайник с гусаком, весы, таймер, 15г кофе, 250мл воды (94°C).",
            "h2_ratio": "Пропорции",
            "p_ratio": "Классическая пропорция для V60: 1:16.6 (15г кофе на 250мл воды). Для более крепкого кофе используйте 1:15, для более лёгкого — 1:17.",
            "h2_recipe": "Рецепт",
            "p_step1": "Промойте фильтр горячей водой. Это уберёт бумажный привкус и прогреет пуровер.",
            "p_step2": "Засыпьте молотый кофе (помол как морская соль) и сделайте углубление в центре.",
            "p_step3": "Начните с преинфузии: залейте 30мл воды, подождите 30-45 секунд пока кофе \"цветёт\".",
            "p_step4": "Продолжайте заливать воду по кругу, от центра к краям. Общее время заваривания: 2:30-3:00.",
            "cta_title": "Закажите кофе для V60",
            "cta_text": "Рекомендуем светлую обжарку для лучшего вкуса",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Perfect V60: Step-by-Step Recipe from a Barista",
            "subtitle": "Detailed instructions for brewing coffee with pour-over. Ratios, temperature, pouring technique.",
            "category": "Recipes",
            "reading_time": "4 min read",
            "intro": "V60 is one of the most popular filter coffee brewing methods. Here's a step-by-step recipe used by professional baristas.",
            "h2_equipment": "What You Need",
            "p_equipment": "V60 dripper, paper filters, coffee grinder, gooseneck kettle, scale, timer, 15g coffee, 250ml water (94°C).",
            "h2_ratio": "Ratios",
            "p_ratio": "Classic V60 ratio: 1:16.6 (15g coffee to 250ml water). For stronger coffee use 1:15, for lighter — 1:17.",
            "h2_recipe": "Recipe",
            "p_step1": "Rinse the filter with hot water. This removes paper taste and preheats the dripper.",
            "p_step2": "Add ground coffee (medium-fine, like sea salt) and make a well in the center.",
            "p_step3": "Start with pre-infusion: pour 30ml water, wait 30-45 seconds while coffee \"blooms.\"",
            "p_step4": "Continue pouring water in circles, from center to edges. Total brew time: 2:30-3:00.",
            "cta_title": "Order Coffee for V60",
            "cta_text": "We recommend light roast for the best flavor",
            "cta_button": "To Catalog"
        }
    },
    "coffee_storage": {
        "uk": {
            "title": "Як правильно зберігати каву: 5 головних правил",
            "subtitle": "Ворогі свіжості кави та прості правила, які допоможуть зберегти аромат надовго.",
            "category": "Поради",
            "reading_time": "3 хвилини читання",
            "intro": "Навіть найкраща кава може втратити свій смак через неправильне зберігання. Ось 5 головних правил, яких варто дотримуватись.",
            "h2_enemies": "5 ворогів свіжості",
            "p_oxygen": "<strong>Кисень</strong> — окислює ароматичні олії",
            "p_moisture": "<strong>Волога</strong> — призводить до появи цвілі",
            "p_heat": "<strong>Тепло</strong> — прискорює старіння",
            "p_light": "<strong>Світло</strong> — руйнує смакові сполуки",
            "p_smells": "<strong>Сторонні запахи</strong> — кава легко їх вбирає",
            "h2_tips": "Поради щодо зберігання",
            "p_tips": "Тримайте каву в герметичній упаковці, в темному прохолодному місці. Не в холодильнику! Мелена кава зберігається 2 тижні, зерно — до місяця після обсмажки.",
            "cta_title": "Замовте свіжу каву",
            "cta_text": "Ми смажимо під замовлення — ви отримаєте найсвіжішу каву",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Как правильно хранить кофе: 5 главных правил",
            "subtitle": "Враги свежести кофе и простые правила, которые помогут сохранить аромат надолго.",
            "category": "Советы",
            "reading_time": "3 минуты чтения",
            "intro": "Даже лучший кофе может потерять свой вкус из-за неправильного хранения. Вот 5 главных правил, которых стоит придерживаться.",
            "h2_enemies": "5 врагов свежести",
            "p_oxygen": "<strong>Кислород</strong> — окисляет ароматические масла",
            "p_moisture": "<strong>Влага</strong> — приводит к появлению плесени",
            "p_heat": "<strong>Тепло</strong> — ускоряет старение",
            "p_light": "<strong>Свет</strong> — разрушает вкусовые соединения",
            "p_smells": "<strong>Посторонние запахи</strong> — кофе легко их впитывает",
            "h2_tips": "Советы по хранению",
            "p_tips": "Храните кофе в герметичной упаковке, в тёмном прохладном месте. Не в холодильнике! Молотый кофе хранится 2 недели, зерно — до месяца после обжарки.",
            "cta_title": "Закажите свежий кофе",
            "cta_text": "Мы обжариваем под заказ — вы получите самый свежий кофе",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "How to Store Coffee Properly: 5 Key Rules",
            "subtitle": "Enemies of coffee freshness and simple rules to preserve aroma longer.",
            "category": "Tips",
            "reading_time": "3 min read",
            "intro": "Even the best coffee can lose its flavor due to improper storage. Here are 5 key rules to follow.",
            "h2_enemies": "5 Enemies of Freshness",
            "p_oxygen": "<strong>Oxygen</strong> — oxidizes aromatic oils",
            "p_moisture": "<strong>Moisture</strong> — leads to mold growth",
            "p_heat": "<strong>Heat</strong> — accelerates aging",
            "p_light": "<strong>Light</strong> — destroys flavor compounds",
            "p_smells": "<strong>Foreign odors</strong> — coffee easily absorbs them",
            "h2_tips": "Storage Tips",
            "p_tips": "Keep coffee in airtight packaging, in a dark cool place. Not in the fridge! Ground coffee keeps 2 weeks, beans — up to a month after roasting.",
            "cta_title": "Order Fresh Coffee",
            "cta_text": "We roast to order — you'll receive the freshest coffee",
            "cta_button": "To Catalog"
        }
    }
}

def update_locales():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "articles" not in data:
            data["articles"] = {}
        
        for key, translations in ALL_ARTICLES.items():
            if key not in data["articles"]:
                data["articles"][key] = {}
            data["articles"][key].update(translations[lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path} with {len(ALL_ARTICLES)} articles")

if __name__ == "__main__":
    print("Adding complete article translations...")
    update_locales()
    print("Done!")
