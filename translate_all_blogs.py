#!/usr/bin/env python3
"""
Complete translations for all blog posts
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOG_TRANSLATIONS = {
    "arabica_vs_robusta": {
        "uk": {
            "title": "Arabica vs Robusta: вся правда про два види кави",
            "subtitle": "Детальний гід по різниці між двома найпопулярнішими видами кави.",
            "category": "Про каву",
            "reading_time": "8 хвилин читання",
            "intro": "Коли ви обираєте каву в магазині, на упаковці часто написано '100% Arabica'. Але чому це так важливо? І чи справді Robusta така погана?",
            "h2_table": "Порівняльна таблиця",
            "h2_arabica": "Arabica: Королева кави",
            "h3_arabica_conditions": "Умови вирощування",
            "h3_arabica_flavor": "Смаковий профіль",
            "h3_arabica_varieties": "Популярні різновиди Arabica",
            "h2_robusta": "Robusta: Недооцінений боєць",
            "h3_robusta_cheap": "Чому Robusta дешевша?",
            "h3_robusta_quality": "Чи завжди Robusta = погана кава?",
            "h2_when_choose": "Коли обирати Arabica, а коли Robusta?",
            "h3_choose_arabica": "Обирайте 100% Arabica, якщо:",
            "h3_choose_robusta": "Robusta може підійти, якщо:",
            "cta_title": "Спробуйте справжню Arabica з Ефіопії",
            "cta_text": "Ми працюємо лише з 100% Arabica вищого ґатунку",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Arabica vs Robusta: вся правда о двух видах кофе",
            "subtitle": "Детальный гид по разнице между двумя самыми популярными видами кофе.",
            "category": "О кофе",
            "reading_time": "8 минут чтения",
            "intro": "Когда вы выбираете кофе в магазине, на упаковке часто написано '100% Arabica'. Но почему это так важно? И правда ли Robusta такая плохая?",
            "h2_table": "Сравнительная таблица",
            "h2_arabica": "Arabica: Королева кофе",
            "h3_arabica_conditions": "Условия выращивания",
            "h3_arabica_flavor": "Вкусовой профиль",
            "h3_arabica_varieties": "Популярные разновидности Arabica",
            "h2_robusta": "Robusta: Недооценённый боец",
            "h3_robusta_cheap": "Почему Robusta дешевле?",
            "h3_robusta_quality": "Всегда ли Robusta = плохой кофе?",
            "h2_when_choose": "Когда выбирать Arabica, а когда Robusta?",
            "h3_choose_arabica": "Выбирайте 100% Arabica, если:",
            "h3_choose_robusta": "Robusta может подойти, если:",
            "cta_title": "Попробуйте настоящую Arabica из Эфиопии",
            "cta_text": "Мы работаем только с 100% Arabica высшего качества",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Arabica vs Robusta: The Full Truth About Two Coffee Types",
            "subtitle": "A detailed guide to the differences between the two most popular coffee types.",
            "category": "About Coffee",
            "reading_time": "8 min read",
            "intro": "When you choose coffee at the store, the package often says '100% Arabica'. But why is this so important? And is Robusta really that bad?",
            "h2_table": "Comparison Table",
            "h2_arabica": "Arabica: The Queen of Coffee",
            "h3_arabica_conditions": "Growing Conditions",
            "h3_arabica_flavor": "Flavor Profile",
            "h3_arabica_varieties": "Popular Arabica Varieties",
            "h2_robusta": "Robusta: The Underrated Fighter",
            "h3_robusta_cheap": "Why is Robusta Cheaper?",
            "h3_robusta_quality": "Is Robusta Always = Bad Coffee?",
            "h2_when_choose": "When to Choose Arabica, When Robusta?",
            "h3_choose_arabica": "Choose 100% Arabica if:",
            "h3_choose_robusta": "Robusta may work if:",
            "cta_title": "Try Real Arabica from Ethiopia",
            "cta_text": "We work only with 100% premium Arabica",
            "cta_button": "To Catalog"
        }
    },
    "bean_to_cup": {
        "uk": {
            "title": "Від зерна до чашки: шлях кави",
            "subtitle": "Повний цикл виробництва кави — від плантації до вашого столу.",
            "category": "Про каву",
            "reading_time": "6 хвилин читання",
            "intro": "Кожна чашка кави — це результат кропіткої роботи сотень людей на різних континентах. Дізнайтесь, який шлях проходить зерно.",
            "h2_growing": "Вирощування",
            "h2_harvest": "Збирання урожаю",
            "h2_processing": "Обробка",
            "h2_export": "Експорт та імпорт",
            "h2_roasting": "Обсмажка",
            "h2_brewing": "Приготування",
            "cta_title": "Спробуйте результат цього шляху",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "От зерна к чашке: путь кофе",
            "subtitle": "Полный цикл производства кофе — от плантации до вашего стола.",
            "category": "О кофе",
            "reading_time": "6 минут чтения",
            "intro": "Каждая чашка кофе — это результат кропотливой работы сотен людей на разных континентах. Узнайте, какой путь проходит зерно.",
            "h2_growing": "Выращивание",
            "h2_harvest": "Сбор урожая",
            "h2_processing": "Обработка",
            "h2_export": "Экспорт и импорт",
            "h2_roasting": "Обжарка",
            "h2_brewing": "Приготовление",
            "cta_title": "Попробуйте результат этого пути",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "From Bean to Cup: The Journey of Coffee",
            "subtitle": "The complete production cycle — from plantation to your table.",
            "category": "About Coffee",
            "reading_time": "6 min read",
            "intro": "Every cup of coffee is the result of meticulous work by hundreds of people across different continents. Learn the journey of the bean.",
            "h2_growing": "Growing",
            "h2_harvest": "Harvesting",
            "h2_processing": "Processing",
            "h2_export": "Export and Import",
            "h2_roasting": "Roasting",
            "h2_brewing": "Brewing",
            "cta_title": "Try the Result of This Journey",
            "cta_button": "To Catalog"
        }
    },
    "brewing_methods": {
        "uk": {
            "title": "Усі методи заварювання кави: повний гід",
            "subtitle": "Від турки до аеропреса — огляд всіх способів приготування кави.",
            "category": "Рецепти",
            "reading_time": "10 хвилин читання",
            "intro": "Існує безліч способів приготування кави. Кожен метод розкриває різні аспекти смаку зерна.",
            "h2_immersion": "Методи занурення",
            "h2_drip": "Крапельні методи",
            "h2_pressure": "Методи під тиском",
            "h2_boiling": "Методи варіння",
            "cta_title": "Знайдіть свій ідеальний метод",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Все методы заваривания кофе: полный гид",
            "subtitle": "От турки до аэропресса — обзор всех способов приготовления кофе.",
            "category": "Рецепты",
            "reading_time": "10 минут чтения",
            "intro": "Существует множество способов приготовления кофе. Каждый метод раскрывает разные аспекты вкуса зерна.",
            "h2_immersion": "Методы погружения",
            "h2_drip": "Капельные методы",
            "h2_pressure": "Методы под давлением",
            "h2_boiling": "Методы варки",
            "cta_title": "Найдите свой идеальный метод",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "All Coffee Brewing Methods: Complete Guide",
            "subtitle": "From Turkish pot to Aeropress — an overview of all brewing methods.",
            "category": "Recipes",
            "reading_time": "10 min read",
            "intro": "There are countless ways to brew coffee. Each method reveals different aspects of the bean's flavor.",
            "h2_immersion": "Immersion Methods",
            "h2_drip": "Drip Methods",
            "h2_pressure": "Pressure Methods",
            "h2_boiling": "Boiling Methods",
            "cta_title": "Find Your Perfect Method",
            "cta_button": "To Catalog"
        }
    },
    "coffee_processing": {
        "uk": {
            "title": "Обробка кави: від ягоди до зерна",
            "subtitle": "Як сухий, митий та медовий способи обробки впливають на смак.",
            "category": "Обробка",
            "reading_time": "7 хвилин читання",
            "intro": "Після збору врожаю кавова ягода проходить обробку. Саме цей етап критично важливий для кінцевого смаку.",
            "h2_natural": "Натуральна (суха) обробка",
            "h2_washed": "Мита обробка",
            "h2_honey": "Медова обробка",
            "h2_comparison": "Порівняння смаків",
            "cta_title": "Спробуйте різні обробки",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Обработка кофе: от ягоды к зерну",
            "subtitle": "Как сухой, мытый и медовый способы обработки влияют на вкус.",
            "category": "Обработка",
            "reading_time": "7 минут чтения",
            "intro": "После сбора урожая кофейная ягода проходит обработку. Именно этот этап критически важен для конечного вкуса.",
            "h2_natural": "Натуральная (сухая) обработка",
            "h2_washed": "Мытая обработка",
            "h2_honey": "Медовая обработка",
            "h2_comparison": "Сравнение вкусов",
            "cta_title": "Попробуйте разные обработки",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Coffee Processing: From Cherry to Bean",
            "subtitle": "How natural, washed, and honey processing affect taste.",
            "category": "Processing",
            "reading_time": "7 min read",
            "intro": "After harvest, the coffee cherry undergoes processing. This stage is critically important for the final taste.",
            "h2_natural": "Natural (Dry) Processing",
            "h2_washed": "Washed Processing",
            "h2_honey": "Honey Processing",
            "h2_comparison": "Flavor Comparison",
            "cta_title": "Try Different Processing Methods",
            "cta_button": "To Catalog"
        }
    },
    "coffee_seasonality": {
        "uk": {
            "title": "Сезонність кави: коли пити свіжу каву",
            "subtitle": "Чому кава — це сезонний продукт і коли найкращий час для різних регіонів.",
            "category": "Про каву",
            "reading_time": "5 хвилин читання",
            "intro": "Кава — сезонний продукт, як фрукти чи овочі. Кожен регіон має свій сезон збору.",
            "h2_seasons": "Сезони збору",
            "h2_ethiopia": "Ефіопія (листопад-лютий)",
            "h2_freshness": "Як обрати свіжу каву",
            "cta_title": "Замовте свіжу каву сезону",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Сезонность кофе: когда пить свежий кофе",
            "subtitle": "Почему кофе — это сезонный продукт и когда лучшее время для разных регионов.",
            "category": "О кофе",
            "reading_time": "5 минут чтения",
            "intro": "Кофе — сезонный продукт, как фрукты или овощи. У каждого региона свой сезон сбора.",
            "h2_seasons": "Сезоны сбора",
            "h2_ethiopia": "Эфиопия (ноябрь-февраль)",
            "h2_freshness": "Как выбрать свежий кофе",
            "cta_title": "Закажите свежий кофе сезона",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Coffee Seasonality: When to Drink Fresh Coffee",
            "subtitle": "Why coffee is a seasonal product and the best times for different regions.",
            "category": "About Coffee",
            "reading_time": "5 min read",
            "intro": "Coffee is a seasonal product, like fruits or vegetables. Each region has its harvest season.",
            "h2_seasons": "Harvest Seasons",
            "h2_ethiopia": "Ethiopia (November-February)",
            "h2_freshness": "How to Choose Fresh Coffee",
            "cta_title": "Order Fresh Seasonal Coffee",
            "cta_button": "To Catalog"
        }
    },
    "coffee_storage_blog": {
        "uk": {
            "title": "Зберігання кави: поради від професіоналів",
            "subtitle": "Як зберегти свіжість та аромат кави якомога довше.",
            "category": "Поради",
            "reading_time": "4 хвилини читання",
            "intro": "Правильне зберігання — ключ до насолоди смаком кави протягом тривалого часу.",
            "h2_enemies": "Вороги свіжості",
            "h2_containers": "Ідеальний контейнер",
            "h2_tips": "Практичні поради",
            "cta_title": "Замовте свіжообсмажену каву",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Хранение кофе: советы от профессионалов",
            "subtitle": "Как сохранить свежесть и аромат кофе как можно дольше.",
            "category": "Советы",
            "reading_time": "4 минуты чтения",
            "intro": "Правильное хранение — ключ к наслаждению вкусом кофе в течение длительного времени.",
            "h2_enemies": "Враги свежести",
            "h2_containers": "Идеальный контейнер",
            "h2_tips": "Практические советы",
            "cta_title": "Закажите свежеобжаренный кофе",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Coffee Storage: Tips from Professionals",
            "subtitle": "How to preserve coffee freshness and aroma as long as possible.",
            "category": "Tips",
            "reading_time": "4 min read",
            "intro": "Proper storage is key to enjoying coffee flavor for a long time.",
            "h2_enemies": "Enemies of Freshness",
            "h2_containers": "The Ideal Container",
            "h2_tips": "Practical Tips",
            "cta_title": "Order Freshly Roasted Coffee",
            "cta_button": "To Catalog"
        }
    },
    "cold_brew_guide": {
        "uk": {
            "title": "Cold Brew: повний гід по холодному заварюванню",
            "subtitle": "Все, що потрібно знати про приготування ідеального cold brew вдома.",
            "category": "Рецепти",
            "reading_time": "6 хвилин читання",
            "intro": "Cold brew — ідеальний напій для спекотних днів. Він м'який, солодкий і без гіркоти.",
            "h2_what_is": "Що таке Cold Brew?",
            "h2_benefits": "Переваги cold brew",
            "h2_recipe": "Базовий рецепт",
            "h2_tips": "Поради для ідеального результату",
            "cta_title": "Замовте каву для Cold Brew",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Cold Brew: полный гид по холодному завариванию",
            "subtitle": "Всё, что нужно знать о приготовлении идеального cold brew дома.",
            "category": "Рецепты",
            "reading_time": "6 минут чтения",
            "intro": "Cold brew — идеальный напиток для жарких дней. Он мягкий, сладкий и без горечи.",
            "h2_what_is": "Что такое Cold Brew?",
            "h2_benefits": "Преимущества cold brew",
            "h2_recipe": "Базовый рецепт",
            "h2_tips": "Советы для идеального результата",
            "cta_title": "Закажите кофе для Cold Brew",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Cold Brew: Complete Guide to Cold Brewing",
            "subtitle": "Everything you need to know about making perfect cold brew at home.",
            "category": "Recipes",
            "reading_time": "6 min read",
            "intro": "Cold brew is the perfect drink for hot days. It's smooth, sweet, and without bitterness.",
            "h2_what_is": "What is Cold Brew?",
            "h2_benefits": "Benefits of Cold Brew",
            "h2_recipe": "Basic Recipe",
            "h2_tips": "Tips for Perfect Results",
            "cta_title": "Order Coffee for Cold Brew",
            "cta_button": "To Catalog"
        }
    },
    "espresso_guide": {
        "uk": {
            "title": "Еспресо вдома: повний гід для початківців",
            "subtitle": "Від вибору машини до ідеального шота — все, що потрібно знати.",
            "category": "Рецепти",
            "reading_time": "10 хвилин читання",
            "intro": "Еспресо — основа багатьох кавових напоїв. Ось як приготувати його вдома.",
            "h2_equipment": "Необхідне обладнання",
            "h2_grind": "Правильний помел",
            "h2_dose": "Доза та темпінг",
            "h2_extraction": "Екстракція",
            "h2_troubleshoot": "Вирішення проблем",
            "cta_title": "Замовте каву для еспресо",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Эспрессо дома: полный гид для начинающих",
            "subtitle": "От выбора машины до идеального шота — всё, что нужно знать.",
            "category": "Рецепты",
            "reading_time": "10 минут чтения",
            "intro": "Эспрессо — основа многих кофейных напитков. Вот как приготовить его дома.",
            "h2_equipment": "Необходимое оборудование",
            "h2_grind": "Правильный помол",
            "h2_dose": "Доза и темпинг",
            "h2_extraction": "Экстракция",
            "h2_troubleshoot": "Решение проблем",
            "cta_title": "Закажите кофе для эспрессо",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Espresso at Home: Complete Beginner's Guide",
            "subtitle": "From choosing a machine to the perfect shot — everything you need to know.",
            "category": "Recipes",
            "reading_time": "10 min read",
            "intro": "Espresso is the foundation of many coffee drinks. Here's how to make it at home.",
            "h2_equipment": "Required Equipment",
            "h2_grind": "Proper Grind",
            "h2_dose": "Dose and Tamping",
            "h2_extraction": "Extraction",
            "h2_troubleshoot": "Troubleshooting",
            "cta_title": "Order Coffee for Espresso",
            "cta_button": "To Catalog"
        }
    },
    "ethiopia_origins": {
        "uk": {
            "title": "Ефіопія: колиска кави та її регіони",
            "subtitle": "Подорож по найвідоміших кавових регіонах Ефіопії.",
            "category": "Про каву",
            "reading_time": "7 хвилин читання",
            "intro": "Ефіопія — батьківщина кави. Тут росте більше генетичних різновидів арабіки, ніж будь-де у світі.",
            "h2_yirgacheffe": "Yirgacheffe",
            "h2_sidamo": "Sidamo",
            "h2_guji": "Guji",
            "h2_harrar": "Harrar",
            "h2_limu": "Limu",
            "cta_title": "Спробуйте каву з Ефіопії",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Эфиопия: колыбель кофе и её регионы",
            "subtitle": "Путешествие по самым известным кофейным регионам Эфиопии.",
            "category": "О кофе",
            "reading_time": "7 минут чтения",
            "intro": "Эфиопия — родина кофе. Здесь растёт больше генетических разновидностей арабики, чем где-либо в мире.",
            "h2_yirgacheffe": "Yirgacheffe",
            "h2_sidamo": "Sidamo",
            "h2_guji": "Guji",
            "h2_harrar": "Harrar",
            "h2_limu": "Limu",
            "cta_title": "Попробуйте кофе из Эфиопии",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Ethiopia: Cradle of Coffee and Its Regions",
            "subtitle": "A journey through Ethiopia's most famous coffee regions.",
            "category": "About Coffee",
            "reading_time": "7 min read",
            "intro": "Ethiopia is the birthplace of coffee. More genetic varieties of Arabica grow here than anywhere else in the world.",
            "h2_yirgacheffe": "Yirgacheffe",
            "h2_sidamo": "Sidamo",
            "h2_guji": "Guji",
            "h2_harrar": "Harrar",
            "h2_limu": "Limu",
            "cta_title": "Try Coffee from Ethiopia",
            "cta_button": "To Catalog"
        }
    },
    "french_press_guide": {
        "uk": {
            "title": "Френч-прес: ідеальний рецепт",
            "subtitle": "Простий метод для насиченої, ароматної кави щодня.",
            "category": "Рецепти",
            "reading_time": "4 хвилини читання",
            "intro": "Френч-прес — один з найпростіших методів заварювання кави. Ось як отримати найкращий результат.",
            "h2_equipment": "Що потрібно",
            "h2_recipe": "Рецепт",
            "h2_tips": "Поради",
            "cta_title": "Замовте каву для френч-преса",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Френч-пресс: идеальный рецепт",
            "subtitle": "Простой метод для насыщенного, ароматного кофе каждый день.",
            "category": "Рецепты",
            "reading_time": "4 минуты чтения",
            "intro": "Френч-пресс — один из самых простых методов заваривания кофе. Вот как получить лучший результат.",
            "h2_equipment": "Что нужно",
            "h2_recipe": "Рецепт",
            "h2_tips": "Советы",
            "cta_title": "Закажите кофе для френч-пресса",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "French Press: The Perfect Recipe",
            "subtitle": "A simple method for rich, aromatic coffee every day.",
            "category": "Recipes",
            "reading_time": "4 min read",
            "intro": "French press is one of the simplest brewing methods. Here's how to get the best results.",
            "h2_equipment": "What You Need",
            "h2_recipe": "Recipe",
            "h2_tips": "Tips",
            "cta_title": "Order Coffee for French Press",
            "cta_button": "To Catalog"
        }
    },
    "sca_grading": {
        "uk": {
            "title": "Як оцінюють каву: система SCA",
            "subtitle": "Розбираємось у 100-бальній системі оцінки specialty кави.",
            "category": "Про каву",
            "reading_time": "6 хвилин читання",
            "intro": "SCA (Specialty Coffee Association) створила стандартизовану систему оцінки якості кави.",
            "h2_what_is": "Що таке SCA?",
            "h2_criteria": "Критерії оцінки",
            "h2_scores": "Що означають бали",
            "h2_process": "Процес каппінгу",
            "cta_title": "Спробуйте каву 85+",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Как оценивают кофе: система SCA",
            "subtitle": "Разбираемся в 100-балльной системе оценки specialty кофе.",
            "category": "О кофе",
            "reading_time": "6 минут чтения",
            "intro": "SCA (Specialty Coffee Association) создала стандартизированную систему оценки качества кофе.",
            "h2_what_is": "Что такое SCA?",
            "h2_criteria": "Критерии оценки",
            "h2_scores": "Что означают баллы",
            "h2_process": "Процесс каппинга",
            "cta_title": "Попробуйте кофе 85+",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "How Coffee is Graded: The SCA System",
            "subtitle": "Understanding the 100-point specialty coffee grading system.",
            "category": "About Coffee",
            "reading_time": "6 min read",
            "intro": "SCA (Specialty Coffee Association) created a standardized coffee quality grading system.",
            "h2_what_is": "What is SCA?",
            "h2_criteria": "Grading Criteria",
            "h2_scores": "What Scores Mean",
            "h2_process": "The Cupping Process",
            "cta_title": "Try 85+ Coffee",
            "cta_button": "To Catalog"
        }
    },
    "specialty_coffee": {
        "uk": {
            "title": "Що таке specialty кава?",
            "subtitle": "Відмінності specialty від комерційної кави та чому вона коштує дорожче.",
            "category": "Про каву",
            "reading_time": "5 хвилин читання",
            "intro": "Specialty кава — це не маркетингове слово, а чітко визначений термін з конкретними критеріями.",
            "h2_definition": "Визначення",
            "h2_difference": "Різниця з комерційною кавою",
            "h2_why_expensive": "Чому дорожче",
            "h2_how_find": "Як знайти справжню specialty каву",
            "cta_title": "Спробуйте справжню specialty",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Что такое specialty кофе?",
            "subtitle": "Отличия specialty от коммерческого кофе и почему он стоит дороже.",
            "category": "О кофе",
            "reading_time": "5 минут чтения",
            "intro": "Specialty кофе — это не маркетинговое слово, а чётко определённый термин с конкретными критериями.",
            "h2_definition": "Определение",
            "h2_difference": "Разница с коммерческим кофе",
            "h2_why_expensive": "Почему дороже",
            "h2_how_find": "Как найти настоящий specialty кофе",
            "cta_title": "Попробуйте настоящий specialty",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "What is Specialty Coffee?",
            "subtitle": "The differences between specialty and commercial coffee and why it costs more.",
            "category": "About Coffee",
            "reading_time": "5 min read",
            "intro": "Specialty coffee isn't just a marketing term — it's a clearly defined concept with specific criteria.",
            "h2_definition": "Definition",
            "h2_difference": "Difference from Commercial Coffee",
            "h2_why_expensive": "Why It's More Expensive",
            "h2_how_find": "How to Find Real Specialty Coffee",
            "cta_title": "Try Real Specialty",
            "cta_button": "To Catalog"
        }
    },
    "turka_guide": {
        "uk": {
            "title": "Кава в турці: традиційний рецепт",
            "subtitle": "Секрети приготування ідеальної кави по-турецьки.",
            "category": "Рецепти",
            "reading_time": "5 хвилин читання",
            "intro": "Кава в турці — найстаріший метод приготування, якому понад 500 років.",
            "h2_history": "Історія",
            "h2_equipment": "Обладнання",
            "h2_recipe": "Рецепт",
            "h2_secrets": "Секрети",
            "cta_title": "Замовте каву для турки",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Кофе в турке: традиционный рецепт",
            "subtitle": "Секреты приготовления идеального кофе по-турецки.",
            "category": "Рецепты",
            "reading_time": "5 минут чтения",
            "intro": "Кофе в турке — старейший метод приготовления, которому более 500 лет.",
            "h2_history": "История",
            "h2_equipment": "Оборудование",
            "h2_recipe": "Рецепт",
            "h2_secrets": "Секреты",
            "cta_title": "Закажите кофе для турки",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Turkish Coffee: Traditional Recipe",
            "subtitle": "Secrets to making perfect Turkish coffee.",
            "category": "Recipes",
            "reading_time": "5 min read",
            "intro": "Turkish coffee is the oldest brewing method, over 500 years old.",
            "h2_history": "History",
            "h2_equipment": "Equipment",
            "h2_recipe": "Recipe",
            "h2_secrets": "Secrets",
            "cta_title": "Order Coffee for Turkish Brew",
            "cta_button": "To Catalog"
        }
    },
    "v60_guide": {
        "uk": {
            "title": "V60: мистецтво пуровера",
            "subtitle": "Покроковий гід по приготуванню ідеального V60.",
            "category": "Рецепти",
            "reading_time": "6 хвилин читання",
            "intro": "V60 — улюблений метод бариста по всьому світу. Ось як освоїти його вдома.",
            "h2_equipment": "Обладнання",
            "h2_ratio": "Пропорції",
            "h2_technique": "Техніка заливання",
            "h2_recipe": "Покроковий рецепт",
            "cta_title": "Замовте каву для V60",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "V60: искусство пуровера",
            "subtitle": "Пошаговый гид по приготовлению идеального V60.",
            "category": "Рецепты",
            "reading_time": "6 минут чтения",
            "intro": "V60 — любимый метод баристов по всему миру. Вот как освоить его дома.",
            "h2_equipment": "Оборудование",
            "h2_ratio": "Пропорции",
            "h2_technique": "Техника пролива",
            "h2_recipe": "Пошаговый рецепт",
            "cta_title": "Закажите кофе для V60",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "V60: The Art of Pour Over",
            "subtitle": "A step-by-step guide to making the perfect V60.",
            "category": "Recipes",
            "reading_time": "6 min read",
            "intro": "V60 is a favorite method of baristas worldwide. Here's how to master it at home.",
            "h2_equipment": "Equipment",
            "h2_ratio": "Ratios",
            "h2_technique": "Pouring Technique",
            "h2_recipe": "Step-by-Step Recipe",
            "cta_title": "Order Coffee for V60",
            "cta_button": "To Catalog"
        }
    },
    "yirgacheffe_region": {
        "uk": {
            "title": "Yirgacheffe: перлина ефіопської кави",
            "subtitle": "Чому цей регіон виробляє одну з найдорожчих кав у світі.",
            "category": "Про каву",
            "reading_time": "5 хвилин читання",
            "intro": "Yirgacheffe — легендарний регіон Ефіопії, відомий своєю квітковою та цитрусовою кавою.",
            "h2_geography": "Географія та клімат",
            "h2_flavor": "Смаковий профіль",
            "h2_processing": "Методи обробки",
            "h2_why_special": "Чому така особлива",
            "cta_title": "Спробуйте Yirgacheffe",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Yirgacheffe: жемчужина эфиопского кофе",
            "subtitle": "Почему этот регион производит один из самых дорогих сортов кофе в мире.",
            "category": "О кофе",
            "reading_time": "5 минут чтения",
            "intro": "Yirgacheffe — легендарный регион Эфиопии, известный своим цветочным и цитрусовым кофе.",
            "h2_geography": "География и климат",
            "h2_flavor": "Вкусовой профиль",
            "h2_processing": "Методы обработки",
            "h2_why_special": "Почему такой особенный",
            "cta_title": "Попробуйте Yirgacheffe",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Yirgacheffe: The Gem of Ethiopian Coffee",
            "subtitle": "Why this region produces one of the world's most expensive coffees.",
            "category": "About Coffee",
            "reading_time": "5 min read",
            "intro": "Yirgacheffe is a legendary Ethiopian region known for its floral and citrusy coffee.",
            "h2_geography": "Geography and Climate",
            "h2_flavor": "Flavor Profile",
            "h2_processing": "Processing Methods",
            "h2_why_special": "Why It's Special",
            "cta_title": "Try Yirgacheffe",
            "cta_button": "To Catalog"
        }
    }
}

def update_locales():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "blog" not in data:
            data["blog"] = {}
        
        for key, translations in BLOG_TRANSLATIONS.items():
            if key not in data["blog"]:
                data["blog"][key] = {}
            data["blog"][key].update(translations[lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path} with {len(BLOG_TRANSLATIONS)} blog posts")

if __name__ == "__main__":
    print("Adding complete blog translations...")
    update_locales()
    print("Done!")
