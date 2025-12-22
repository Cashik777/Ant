#!/usr/bin/env python3
"""
Batch i18n processor for ALL remaining articles
Adds data-i18n attributes and creates translations
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# All article translations
ALL_ARTICLES = {
    "what_is_specialty": {
        "uk": {
            "title": "Що таке Specialty кава і чому вона коштує дорожче",
            "subtitle": "Розбираємось, чим відрізняється specialty кава від звичайної",
            "category": "Про каву",
            "reading_time": "5 хвилин читання",
            "back_to_articles": "Назад до статей",
            "intro": "Якщо ви коли-небудь замислювались, чому одна пачка кави коштує 100 гривень, а інша — 400, відповідь криється у понятті specialty кави.",
            "what_means_title": "Що означає \"Specialty\"?",
            "definition": "Specialty кава — це кава, яка отримала оцінку 80 балів або вище за 100-бальною шкалою SCA.",
            "quote1": "Specialty кава — це приблизно 3% від усієї кави, що виробляється у світі. Це як порівнювати столове вино з Grand Cru.",
            "grading_title": "Як оцінюють каву професіонали",
            "grading_intro": "Оцінювання кави — це справжня наука. Сертифіковані Q-грейдери аналізують зерно за 11 критеріями.",
            "why_expensive_title": "Чому specialty кава дорожча?",
            "recognize_title": "Як розпізнати справжню specialty каву",
            "worth_it_title": "Чи варто переплачувати?",
            "cta_title": "Готові спробувати справжню specialty каву?",
            "cta_text": "Замовте наш бестселер — Yirgacheffe з нотами квітів та цитрусів",
            "cta_button": "Перейти до каталогу",
            "tags_label": "Теги:",
            "share_label": "Поділитись:",
            "related_title": "Схожі статті"
        },
        "ru": {
            "title": "Что такое Specialty кофе и почему он дороже",
            "subtitle": "Разбираемся, чем отличается specialty кофе от обычного",
            "category": "О кофе",
            "reading_time": "5 минут чтения",
            "back_to_articles": "Назад к статьям",
            "intro": "Если вы когда-нибудь задумывались, почему одна пачка кофе стоит 100 гривен, а другая — 400, ответ кроется в понятии specialty кофе.",
            "what_means_title": "Что означает \"Specialty\"?",
            "definition": "Specialty кофе — это кофе, получивший оценку 80 баллов или выше по 100-балльной шкале SCA.",
            "quote1": "Specialty кофе — это примерно 3% всего кофе в мире. Это как сравнивать столовое вино с Grand Cru.",
            "grading_title": "Как оценивают кофе профессионалы",
            "grading_intro": "Оценка кофе — это настоящая наука. Сертифицированные Q-грейдеры анализируют зерно по 11 критериям.",
            "why_expensive_title": "Почему specialty кофе дороже?",
            "recognize_title": "Как распознать настоящий specialty кофе",
            "worth_it_title": "Стоит ли переплачивать?",
            "cta_title": "Готовы попробовать настоящий specialty кофе?",
            "cta_text": "Закажите наш бестселлер — Yirgacheffe с нотами цветов и цитрусов",
            "cta_button": "Перейти в каталог",
            "tags_label": "Теги:",
            "share_label": "Поделиться:",
            "related_title": "Похожие статьи"
        },
        "en": {
            "title": "What is Specialty Coffee and Why Does It Cost More",
            "subtitle": "Understanding what makes specialty coffee different from regular",
            "category": "About Coffee",
            "reading_time": "5 min read",
            "back_to_articles": "Back to articles",
            "intro": "If you've ever wondered why one bag of coffee costs 100 hryvnias while another costs 400, the answer lies in the concept of specialty coffee.",
            "what_means_title": "What Does \"Specialty\" Mean?",
            "definition": "Specialty coffee is coffee that has scored 80 points or higher on the SCA 100-point scale.",
            "quote1": "Specialty coffee is about 3% of all coffee produced worldwide. It's like comparing table wine to Grand Cru.",
            "grading_title": "How Professionals Grade Coffee",
            "grading_intro": "Coffee grading is a real science. Certified Q-graders analyze beans across 11 criteria.",
            "why_expensive_title": "Why is Specialty Coffee More Expensive?",
            "recognize_title": "How to Recognize Real Specialty Coffee",
            "worth_it_title": "Is It Worth the Price?",
            "cta_title": "Ready to Try Real Specialty Coffee?",
            "cta_text": "Order our bestseller — Yirgacheffe with floral and citrus notes",
            "cta_button": "Go to Catalog",
            "tags_label": "Tags:",
            "share_label": "Share:",
            "related_title": "Related Articles"
        }
    },
    "light_vs_dark": {
        "uk": {
            "title": "Світла чи темна обсмажка: що обрати?",
            "subtitle": "Порівняння смаків, кофеїну та рекомендації",
            "intro": "Один з найчастіших питань: яка обсмажка краща? Відповідь: це залежить від ваших уподобань та способу приготування.",
            "process_title": "Що відбувається під час обсмажки?",
            "process_text": "Обсмажка — це термічна обробка зеленого зерна при температурі 180-230°C.",
            "table_characteristic": "Характеристика",
            "table_light": "Світла",
            "table_medium": "Середня",
            "table_dark": "Темна",
            "light_title": "Світла обсмажка (Light Roast)",
            "medium_title": "Середня обсмажка (Medium Roast)",
            "dark_title": "Темна обсмажка (Dark Roast)",
            "caffeine_myth_title": "Міф про кофеїн",
            "caffeine_myth_text": "Багато хто вважає, що темна обсмажка \"міцніша\" та містить більше кофеїну. Насправді це міф!",
            "how_to_choose_title": "Як обрати?",
            "cta_title": "Спробуйте різні обсмажки",
            "cta_text": "У нас є кава від світлої до темної — знайдіть свою!",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Светлая или тёмная обжарка: что выбрать?",
            "subtitle": "Сравнение вкусов, кофеина и рекомендации",
            "intro": "Один из самых частых вопросов: какая обжарка лучше? Ответ: это зависит от ваших предпочтений и способа приготовления.",
            "process_title": "Что происходит во время обжарки?",
            "process_text": "Обжарка — это термическая обработка зелёного зерна при температуре 180-230°C.",
            "table_characteristic": "Характеристика",
            "table_light": "Светлая",
            "table_medium": "Средняя",
            "table_dark": "Тёмная",
            "light_title": "Светлая обжарка (Light Roast)",
            "medium_title": "Средняя обжарка (Medium Roast)",
            "dark_title": "Тёмная обжарка (Dark Roast)",
            "caffeine_myth_title": "Миф о кофеине",
            "caffeine_myth_text": "Многие считают, что тёмная обжарка \"крепче\" и содержит больше кофеина. На самом деле это миф!",
            "how_to_choose_title": "Как выбрать?",
            "cta_title": "Попробуйте разные обжарки",
            "cta_text": "У нас есть кофе от светлой до тёмной — найдите свой!",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Light or Dark Roast: What to Choose?",
            "subtitle": "Comparing tastes, caffeine and recommendations",
            "intro": "One of the most common questions: which roast is better? Answer: it depends on your preferences and brewing method.",
            "process_title": "What Happens During Roasting?",
            "process_text": "Roasting is the thermal processing of green beans at 180-230°C.",
            "table_characteristic": "Characteristic",
            "table_light": "Light",
            "table_medium": "Medium",
            "table_dark": "Dark",
            "light_title": "Light Roast",
            "medium_title": "Medium Roast",
            "dark_title": "Dark Roast",
            "caffeine_myth_title": "The Caffeine Myth",
            "caffeine_myth_text": "Many believe that dark roast is \"stronger\" and contains more caffeine. This is actually a myth!",
            "how_to_choose_title": "How to Choose?",
            "cta_title": "Try Different Roasts",
            "cta_text": "We have coffee from light to dark — find yours!",
            "cta_button": "To Catalog"
        }
    },
    "natural_vs_washed": {
        "uk": {
            "title": "Натуральна vs мита обробка кави",
            "subtitle": "Як метод обробки впливає на смак",
            "intro": "Метод обробки кавової ягоди — один з найважливіших факторів, що визначає смак кави.",
            "natural_title": "Натуральна (суха) обробка",
            "natural_text": "Ягоди сушать цілком під сонцем 2-4 тижні. М'якоть ферментується та передає зерну солодкість.",
            "washed_title": "Мита обробка",
            "washed_text": "М'якоть видаляють одразу, зерно ферментується у воді. Чистий, яскравий смак.",
            "honey_title": "Хані (напів-мита) обробка",
            "honey_text": "Часткове видалення м'якоті. Баланс між натуральною та митою.",
            "cta_title": "Спробуйте різні обробки",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Натуральная vs мытая обработка кофе",
            "subtitle": "Как метод обработки влияет на вкус",
            "intro": "Метод обработки кофейной ягоды — один из важнейших факторов, определяющих вкус кофе.",
            "natural_title": "Натуральная (сухая) обработка",
            "natural_text": "Ягоды сушат целиком под солнцем 2-4 недели. Мякоть ферментируется и передаёт зерну сладость.",
            "washed_title": "Мытая обработка",
            "washed_text": "Мякоть удаляют сразу, зерно ферментируется в воде. Чистый, яркий вкус.",
            "honey_title": "Хани (полу-мытая) обработка",
            "honey_text": "Частичное удаление мякоти. Баланс между натуральной и мытой.",
            "cta_title": "Попробуйте разные обработки",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Natural vs Washed Coffee Processing",
            "subtitle": "How processing method affects taste",
            "intro": "The coffee cherry processing method is one of the most important factors determining coffee taste.",
            "natural_title": "Natural (Dry) Processing",
            "natural_text": "Cherries are dried whole under the sun for 2-4 weeks. The pulp ferments and imparts sweetness to the bean.",
            "washed_title": "Washed Processing",
            "washed_text": "Pulp is removed immediately, beans ferment in water. Clean, bright taste.",
            "honey_title": "Honey (Semi-washed) Processing",
            "honey_text": "Partial pulp removal. Balance between natural and washed.",
            "cta_title": "Try Different Processing Methods",
            "cta_button": "To Catalog"
        }
    },
    "water_for_coffee": {
        "uk": {
            "title": "Вода для кави: повний гід",
            "subtitle": "98% вашої чашки — це вода. Ось як її обрати правильно",
            "intro": "Кава на 98% складається з води. Якість води напряму впливає на екстракцію та смак.",
            "why_important_title": "Чому вода така важлива?",
            "ideal_params_title": "Ідеальні параметри води",
            "tds_label": "TDS (мінералізація):",
            "tds_value": "75-150 ppm",
            "recommendations_title": "Рекомендації",
            "cta_title": "Оптимізуйте свою каву",
            "cta_button": "Замовити каву"
        },
        "ru": {
            "title": "Вода для кофе: полный гид",
            "subtitle": "98% вашей чашки — это вода. Вот как её выбрать правильно",
            "intro": "Кофе на 98% состоит из воды. Качество воды напрямую влияет на экстракцию и вкус.",
            "why_important_title": "Почему вода так важна?",
            "ideal_params_title": "Идеальные параметры воды",
            "tds_label": "TDS (минерализация):",
            "tds_value": "75-150 ppm",
            "recommendations_title": "Рекомендации",
            "cta_title": "Оптимизируйте свой кофе",
            "cta_button": "Заказать кофе"
        },
        "en": {
            "title": "Water for Coffee: Complete Guide",
            "subtitle": "98% of your cup is water. Here's how to choose it right",
            "intro": "Coffee is 98% water. Water quality directly affects extraction and taste.",
            "why_important_title": "Why is Water So Important?",
            "ideal_params_title": "Ideal Water Parameters",
            "tds_label": "TDS (mineralization):",
            "tds_value": "75-150 ppm",
            "recommendations_title": "Recommendations",
            "cta_title": "Optimize Your Coffee",
            "cta_button": "Order Coffee"
        }
    },
    "grinder_guide": {
        "uk": {
            "title": "Як обрати кавомолку: повний гід",
            "subtitle": "Жорнова vs ножова, ручна vs електрична",
            "intro": "Кавомолка — найважливіший інвестиція після самої кави. Свіжомелене зерно розкриває весь потенціал смаку.",
            "burr_vs_blade_title": "Жорнова vs ножова",
            "manual_vs_electric_title": "Ручна vs електрична",
            "grind_size_title": "Розмір помелу для різних методів",
            "recommendations_title": "Наші рекомендації",
            "cta_title": "Замовте каву для своєї нової кавомолки",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Как выбрать кофемолку: полный гид",
            "subtitle": "Жерновая vs ножевая, ручная vs электрическая",
            "intro": "Кофемолка — важнейшая инвестиция после самого кофе. Свежемолотое зерно раскрывает весь потенциал вкуса.",
            "burr_vs_blade_title": "Жерновая vs ножевая",
            "manual_vs_electric_title": "Ручная vs электрическая",
            "grind_size_title": "Размер помола для разных методов",
            "recommendations_title": "Наши рекомендации",
            "cta_title": "Закажите кофе для своей новой кофемолки",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "How to Choose a Coffee Grinder: Complete Guide",
            "subtitle": "Burr vs blade, manual vs electric",
            "intro": "A grinder is the most important investment after coffee itself. Freshly ground beans unlock the full flavor potential.",
            "burr_vs_blade_title": "Burr vs Blade",
            "manual_vs_electric_title": "Manual vs Electric",
            "grind_size_title": "Grind Size for Different Methods",
            "recommendations_title": "Our Recommendations",
            "cta_title": "Order Coffee for Your New Grinder",
            "cta_button": "To Catalog"
        }
    },
    "aeropress_recipes": {
        "uk": {
            "title": "5 рецептів для аеропресу",
            "subtitle": "Від класики до чемпіонських рецептів",
            "intro": "Аеропрес — один з найуніверсальніших методів заварювання. Ось 5 рецептів для будь-якого настрою.",
            "classic_title": "Класичний рецепт",
            "inverted_title": "Інвертований метод",
            "champion_title": "Рецепт чемпіона",
            "cold_title": "Холодний аеропрес",
            "espresso_title": "Еспресо-стайл",
            "cta_title": "Замовте каву для аеропресу",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "5 рецептов для аэропресса",
            "subtitle": "От классики до чемпионских рецептов",
            "intro": "Аэропресс — один из самых универсальных методов заваривания. Вот 5 рецептов для любого настроения.",
            "classic_title": "Классический рецепт",
            "inverted_title": "Инвертированный метод",
            "champion_title": "Рецепт чемпиона",
            "cold_title": "Холодный аэропресс",
            "espresso_title": "Эспрессо-стайл",
            "cta_title": "Закажите кофе для аэропресса",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "5 Aeropress Recipes",
            "subtitle": "From classic to championship recipes",
            "intro": "Aeropress is one of the most versatile brewing methods. Here are 5 recipes for any mood.",
            "classic_title": "Classic Recipe",
            "inverted_title": "Inverted Method",
            "champion_title": "Championship Recipe",
            "cold_title": "Cold Aeropress",
            "espresso_title": "Espresso-style",
            "cta_title": "Order Coffee for Aeropress",
            "cta_button": "To Catalog"
        }
    },
    "cold_brew_recipe": {
        "uk": {
            "title": "Cold Brew в домашніх умовах",
            "subtitle": "Простий рецепт для спекотного літа",
            "intro": "Cold Brew — це кава холодної екстракції. Менше кислотності, більше солодкості, ідеально для літа.",
            "what_is_title": "Що таке Cold Brew?",
            "recipe_title": "Базовий рецепт",
            "tips_title": "Поради",
            "serving_title": "Як подавати",
            "cta_title": "Замовте каву для Cold Brew",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Cold Brew в домашних условиях",
            "subtitle": "Простой рецепт для жаркого лета",
            "intro": "Cold Brew — это кофе холодной экстракции. Меньше кислотности, больше сладости, идеально для лета.",
            "what_is_title": "Что такое Cold Brew?",
            "recipe_title": "Базовый рецепт",
            "tips_title": "Советы",
            "serving_title": "Как подавать",
            "cta_title": "Закажите кофе для Cold Brew",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Cold Brew at Home",
            "subtitle": "Simple recipe for hot summer",
            "intro": "Cold Brew is cold extraction coffee. Less acidity, more sweetness, perfect for summer.",
            "what_is_title": "What is Cold Brew?",
            "recipe_title": "Basic Recipe",
            "tips_title": "Tips",
            "serving_title": "How to Serve",
            "cta_title": "Order Coffee for Cold Brew",
            "cta_button": "To Catalog"
        }
    },
    "espresso_mistakes": {
        "uk": {
            "title": "10 помилок при приготуванні еспресо",
            "subtitle": "Як уникнути гіркого або кислого еспресо",
            "intro": "Еспресо — найвибагливіший метод приготування. Ось 10 найпоширеніших помилок та як їх виправити.",
            "mistake1_title": "1. Несвіже зерно",
            "mistake2_title": "2. Неправильний помел",
            "mistake3_title": "3. Неправильна температура",
            "conclusion_title": "Висновок",
            "cta_title": "Замовте свіжу каву для еспресо",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "10 ошибок при приготовлении эспрессо",
            "subtitle": "Как избежать горького или кислого эспрессо",
            "intro": "Эспрессо — самый требовательный метод приготовления. Вот 10 самых распространённых ошибок и как их исправить.",
            "mistake1_title": "1. Несвежее зерно",
            "mistake2_title": "2. Неправильный помол",
            "mistake3_title": "3. Неправильная температура",
            "conclusion_title": "Вывод",
            "cta_title": "Закажите свежий кофе для эспрессо",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "10 Espresso Mistakes",
            "subtitle": "How to avoid bitter or sour espresso",
            "intro": "Espresso is the most demanding brewing method. Here are 10 most common mistakes and how to fix them.",
            "mistake1_title": "1. Stale Beans",
            "mistake2_title": "2. Wrong Grind Size",
            "mistake3_title": "3. Wrong Temperature",
            "conclusion_title": "Conclusion",
            "cta_title": "Order Fresh Coffee for Espresso",
            "cta_button": "To Catalog"
        }
    },
    "turka_recipe": {
        "uk": {
            "title": "Кава в турці: секрети ідеального приготування",
            "subtitle": "Традиційний метод, що витримав століття",
            "intro": "Турка (джезва, ібрік) — один з найдавніших методів приготування кави. Ось як приготувати ідеальну чашку.",
            "history_title": "Коротка історія",
            "equipment_title": "Що вам потрібно",
            "recipe_title": "Класичний рецепт",
            "tips_title": "Секрети майстрів",
            "cta_title": "Замовте каву для турки",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Кофе в турке: секреты идеального приготовления",
            "subtitle": "Традиционный метод, выдержавший века",
            "intro": "Турка (джезва, ибрик) — один из древнейших методов приготовления кофе. Вот как приготовить идеальную чашку.",
            "history_title": "Краткая история",
            "equipment_title": "Что вам нужно",
            "recipe_title": "Классический рецепт",
            "tips_title": "Секреты мастеров",
            "cta_title": "Закажите кофе для турки",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Turkish Coffee: Secrets of Perfect Brewing",
            "subtitle": "Traditional method that has stood the test of time",
            "intro": "Turka (cezve, ibrik) is one of the oldest coffee brewing methods. Here's how to make the perfect cup.",
            "history_title": "Brief History",
            "equipment_title": "What You Need",
            "recipe_title": "Classic Recipe",
            "tips_title": "Master's Secrets",
            "cta_title": "Order Coffee for Turkish",
            "cta_button": "To Catalog"
        }
    },
    "how_to_brew_v60": {
        "uk": {
            "title": "Як заварювати каву в V60",
            "subtitle": "Покроковий рецепт для ідеальної чашки",
            "intro": "V60 — один з найпопулярніших методів приготування фільтр-кави. Ось покроковий рецепт.",
            "equipment_title": "Що вам потрібно",
            "recipe_title": "Рецепт (для 250 мл)",
            "technique_title": "Техніка заливки",
            "troubleshooting_title": "Вирішення проблем",
            "cta_title": "Замовте каву для V60",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Как заваривать кофе в V60",
            "subtitle": "Пошаговый рецепт для идеальной чашки",
            "intro": "V60 — один из самых популярных методов приготовления фильтр-кофе. Вот пошаговый рецепт.",
            "equipment_title": "Что вам нужно",
            "recipe_title": "Рецепт (для 250 мл)",
            "technique_title": "Техника пролива",
            "troubleshooting_title": "Решение проблем",
            "cta_title": "Закажите кофе для V60",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "How to Brew Coffee with V60",
            "subtitle": "Step-by-step recipe for the perfect cup",
            "intro": "V60 is one of the most popular filter coffee brewing methods. Here's a step-by-step recipe.",
            "equipment_title": "What You Need",
            "recipe_title": "Recipe (for 250 ml)",
            "technique_title": "Pouring Technique",
            "troubleshooting_title": "Troubleshooting",
            "cta_title": "Order Coffee for V60",
            "cta_button": "To Catalog"
        }
    },
    "coffee_storage": {
        "uk": {
            "title": "Як правильно зберігати каву",
            "subtitle": "5 ворогів свіжості та як їх перемогти",
            "intro": "Навіть найкраща кава може втратити смак через неправильне зберігання. Ось 5 ворогів свіжості.",
            "enemies_title": "5 ворогів свіжості",
            "enemy1": "1. Кисень",
            "enemy2": "2. Волога",
            "enemy3": "3. Тепло",
            "enemy4": "4. Світло",
            "enemy5": "5. Сторонні запахи",
            "recommendations_title": "Наші рекомендації",
            "cta_title": "Замовте свіжообсмажену каву",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Как правильно хранить кофе",
            "subtitle": "5 врагов свежести и как их победить",
            "intro": "Даже лучший кофе может потерять вкус при неправильном хранении. Вот 5 врагов свежести.",
            "enemies_title": "5 врагов свежести",
            "enemy1": "1. Кислород",
            "enemy2": "2. Влага",
            "enemy3": "3. Тепло",
            "enemy4": "4. Свет",
            "enemy5": "5. Посторонние запахи",
            "recommendations_title": "Наши рекомендации",
            "cta_title": "Закажите свежеобжаренный кофе",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "How to Store Coffee Properly",
            "subtitle": "5 enemies of freshness and how to defeat them",
            "intro": "Even the best coffee can lose flavor with improper storage. Here are 5 enemies of freshness.",
            "enemies_title": "5 Enemies of Freshness",
            "enemy1": "1. Oxygen",
            "enemy2": "2. Moisture",
            "enemy3": "3. Heat",
            "enemy4": "4. Light",
            "enemy5": "5. Foreign Odors",
            "recommendations_title": "Our Recommendations",
            "cta_title": "Order Freshly Roasted Coffee",
            "cta_button": "To Catalog"
        }
    },
    "caffeine_myths": {
        "uk": {
            "title": "10 міфів про кофеїн",
            "subtitle": "Правда та вигадки про найпопулярніший стимулятор",
            "intro": "Кофеїн оточений міфами. Давайте розберемось, що правда, а що ні.",
            "myth1_title": "Міф 1: Кава зневоднює",
            "myth2_title": "Міф 2: Темна обсмажка міцніша",
            "myth3_title": "Міф 3: Кава шкодить серцю",
            "conclusion_title": "Висновок",
            "cta_title": "Насолоджуйтесь кавою без страху",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "10 мифов о кофеине",
            "subtitle": "Правда и выдумки о самом популярном стимуляторе",
            "intro": "Кофеин окружён мифами. Давайте разберёмся, что правда, а что нет.",
            "myth1_title": "Миф 1: Кофе обезвоживает",
            "myth2_title": "Миф 2: Тёмная обжарка крепче",
            "myth3_title": "Миф 3: Кофе вредит сердцу",
            "conclusion_title": "Вывод",
            "cta_title": "Наслаждайтесь кофе без страха",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "10 Caffeine Myths",
            "subtitle": "Truth and fiction about the most popular stimulant",
            "intro": "Caffeine is surrounded by myths. Let's figure out what's true and what's not.",
            "myth1_title": "Myth 1: Coffee Dehydrates",
            "myth2_title": "Myth 2: Dark Roast is Stronger",
            "myth3_title": "Myth 3: Coffee Harms the Heart",
            "conclusion_title": "Conclusion",
            "cta_title": "Enjoy Coffee Without Fear",
            "cta_button": "To Catalog"
        }
    }
}

def update_all_locales():
    """Add all article translations to locale files"""
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "articles" not in data:
            data["articles"] = {}
        
        for article_key, article_langs in ALL_ARTICLES.items():
            data["articles"][article_key] = article_langs[lang]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path} with {len(ALL_ARTICLES)} article translations")

if __name__ == "__main__":
    print("Adding all article translations...")
    update_all_locales()
    print("Done! All translations added to locale files.")
