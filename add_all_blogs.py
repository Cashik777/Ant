#!/usr/bin/env python3
"""
Batch i18n processor for ALL blog posts
Adds translations to locale files
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# All blog translations
ALL_BLOGS = {
    "arabica_vs_robusta": {
        "uk": {
            "title": "Arabica vs Robusta: Повний гід",
            "category": "BASICS",
            "reading_time": "6 хв читання",
            "intro": "\"100% Arabica\" — ви бачили це на кожній другій пачці кави. Але що це насправді означає? І чому Robusta має таку погану репутацію?",
            "differences_title": "Основні відмінності",
            "arabica_title": "Arabica: Королева кави",
            "growing_title": "Умови вирощування",
            "taste_profile_title": "Смаковий профіль",
            "varieties_title": "Популярні різновиди Arabica",
            "robusta_title": "Robusta: Недооцінений боєць",
            "why_cheaper_title": "Чому Robusta дешевша?",
            "robusta_quality_title": "Чи завжди Robusta = погана кава?",
            "when_choose_title": "Коли обирати Arabica, а коли Robusta?",
            "choose_arabica_title": "Обирайте 100% Arabica, якщо:",
            "choose_robusta_title": "Robusta може підійти, якщо:",
            "cta_title": "Спробуйте справжню Arabica з Ефіопії",
            "cta_text": "Ми працюємо лише з 100% Arabica вищого ґатунку",
            "cta_button": "До каталогу",
            "conclusion_title": "Висновок",
            "tags_label": "Теги:",
            "back_to_blog": "← Всі статті блогу"
        },
        "ru": {
            "title": "Arabica vs Robusta: Полный гид",
            "category": "BASICS",
            "reading_time": "6 мин чтения",
            "intro": "\"100% Arabica\" — вы видели это на каждой второй пачке кофе. Но что это на самом деле означает? И почему Robusta имеет такую плохую репутацию?",
            "differences_title": "Основные отличия",
            "arabica_title": "Arabica: Королева кофе",
            "growing_title": "Условия выращивания",
            "taste_profile_title": "Вкусовой профиль",
            "varieties_title": "Популярные разновидности Arabica",
            "robusta_title": "Robusta: Недооценённый боец",
            "why_cheaper_title": "Почему Robusta дешевле?",
            "robusta_quality_title": "Всегда ли Robusta = плохой кофе?",
            "when_choose_title": "Когда выбирать Arabica, а когда Robusta?",
            "choose_arabica_title": "Выбирайте 100% Arabica, если:",
            "choose_robusta_title": "Robusta может подойти, если:",
            "cta_title": "Попробуйте настоящую Arabica из Эфиопии",
            "cta_text": "Мы работаем только с 100% Arabica высшего качества",
            "cta_button": "В каталог",
            "conclusion_title": "Вывод",
            "tags_label": "Теги:",
            "back_to_blog": "← Все статьи блога"
        },
        "en": {
            "title": "Arabica vs Robusta: Complete Guide",
            "category": "BASICS",
            "reading_time": "6 min read",
            "intro": "\"100% Arabica\" — you've seen this on every other bag of coffee. But what does it actually mean? And why does Robusta have such a bad reputation?",
            "differences_title": "Main Differences",
            "arabica_title": "Arabica: The Queen of Coffee",
            "growing_title": "Growing Conditions",
            "taste_profile_title": "Taste Profile",
            "varieties_title": "Popular Arabica Varieties",
            "robusta_title": "Robusta: The Underrated Fighter",
            "why_cheaper_title": "Why is Robusta Cheaper?",
            "robusta_quality_title": "Is Robusta Always Bad Coffee?",
            "when_choose_title": "When to Choose Arabica vs Robusta?",
            "choose_arabica_title": "Choose 100% Arabica if:",
            "choose_robusta_title": "Robusta may suit you if:",
            "cta_title": "Try Real Arabica from Ethiopia",
            "cta_text": "We work only with 100% premium Arabica",
            "cta_button": "To Catalog",
            "conclusion_title": "Conclusion",
            "tags_label": "Tags:",
            "back_to_blog": "← All Blog Articles"
        }
    },
    "bean_to_cup": {
        "uk": {
            "title": "Шлях кавового зерна: від ферми до чашки",
            "category": "ORIGINS",
            "reading_time": "7 хв читання",
            "intro": "Кожна чашка кави — це результат довгого шляху. Від насадження до обсмажки, кожен етап впливає на смак.",
            "planting_title": "Вирощування",
            "harvesting_title": "Збір урожаю",
            "processing_title": "Обробка",
            "drying_title": "Сушіння",
            "export_title": "Експорт",
            "roasting_title": "Обсмажка",
            "brewing_title": "Заварювання",
            "cta_title": "Спробуйте результат цього шляху",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Путь кофейного зерна: от фермы до чашки",
            "category": "ORIGINS",
            "reading_time": "7 мин чтения",
            "intro": "Каждая чашка кофе — это результат долгого пути. От посадки до обжарки, каждый этап влияет на вкус.",
            "planting_title": "Выращивание",
            "harvesting_title": "Сбор урожая",
            "processing_title": "Обработка",
            "drying_title": "Сушка",
            "export_title": "Экспорт",
            "roasting_title": "Обжарка",
            "brewing_title": "Заваривание",
            "cta_title": "Попробуйте результат этого пути",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Coffee Bean Journey: From Farm to Cup",
            "category": "ORIGINS",
            "reading_time": "7 min read",
            "intro": "Every cup of coffee is the result of a long journey. From planting to roasting, each stage affects the taste.",
            "planting_title": "Growing",
            "harvesting_title": "Harvesting",
            "processing_title": "Processing",
            "drying_title": "Drying",
            "export_title": "Export",
            "roasting_title": "Roasting",
            "brewing_title": "Brewing",
            "cta_title": "Try the Result of This Journey",
            "cta_button": "To Catalog"
        }
    },
    "brewing_methods": {
        "uk": {
            "title": "Методи заварювання кави: повний гід",
            "category": "BREWING",
            "reading_time": "10 хв читання",
            "intro": "Від турки до аеропресу — кожен метод заварювання розкриває каву по-різному. Розбираємось у всіх популярних методах.",
            "pour_over_title": "Пуровер (Pour Over)",
            "v60_title": "V60",
            "chemex_title": "Chemex",
            "immersion_title": "Імерсійні методи",
            "french_press_title": "Френч-прес",
            "aeropress_title": "Аеропрес",
            "pressure_title": "Методи під тиском",
            "espresso_title": "Еспресо",
            "moka_title": "Мока (гейзерна кавоварка)",
            "cold_title": "Холодні методи",
            "cold_brew_title": "Cold Brew",
            "comparison_title": "Порівняння методів",
            "cta_title": "Знайдіть каву для свого методу",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Методы заваривания кофе: полный гид",
            "category": "BREWING",
            "reading_time": "10 мин чтения",
            "intro": "От турки до аэропресса — каждый метод заваривания раскрывает кофе по-разному. Разбираемся во всех популярных методах.",
            "pour_over_title": "Пуровер (Pour Over)",
            "v60_title": "V60",
            "chemex_title": "Chemex",
            "immersion_title": "Иммерсионные методы",
            "french_press_title": "Френч-пресс",
            "aeropress_title": "Аэропресс",
            "pressure_title": "Методы под давлением",
            "espresso_title": "Эспрессо",
            "moka_title": "Мока (гейзерная кофеварка)",
            "cold_title": "Холодные методы",
            "cold_brew_title": "Cold Brew",
            "comparison_title": "Сравнение методов",
            "cta_title": "Найдите кофе для своего метода",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Coffee Brewing Methods: Complete Guide",
            "category": "BREWING",
            "reading_time": "10 min read",
            "intro": "From Turkish coffee to Aeropress — each brewing method reveals coffee differently. Let's explore all popular methods.",
            "pour_over_title": "Pour Over",
            "v60_title": "V60",
            "chemex_title": "Chemex",
            "immersion_title": "Immersion Methods",
            "french_press_title": "French Press",
            "aeropress_title": "Aeropress",
            "pressure_title": "Pressure Methods",
            "espresso_title": "Espresso",
            "moka_title": "Moka Pot",
            "cold_title": "Cold Methods",
            "cold_brew_title": "Cold Brew",
            "comparison_title": "Methods Comparison",
            "cta_title": "Find Coffee for Your Method",
            "cta_button": "To Catalog"
        }
    },
    "coffee_processing": {
        "uk": {
            "title": "Обробка кави: як вона впливає на смак",
            "category": "PROCESSING",
            "reading_time": "6 хв читання",
            "intro": "Метод обробки кавової ягоди — один з найважливіших факторів, що визначає смак кави.",
            "natural_title": "Натуральна (суха) обробка",
            "washed_title": "Мита обробка",
            "honey_title": "Хані обробка",
            "comparison_title": "Порівняння методів",
            "cta_title": "Спробуйте різні обробки",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Обработка кофе: как она влияет на вкус",
            "category": "PROCESSING",
            "reading_time": "6 мин чтения",
            "intro": "Метод обработки кофейной ягоды — один из важнейших факторов, определяющих вкус кофе.",
            "natural_title": "Натуральная (сухая) обработка",
            "washed_title": "Мытая обработка",
            "honey_title": "Хани обработка",
            "comparison_title": "Сравнение методов",
            "cta_title": "Попробуйте разные обработки",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Coffee Processing: How It Affects Taste",
            "category": "PROCESSING",
            "reading_time": "6 min read",
            "intro": "The coffee cherry processing method is one of the most important factors determining coffee taste.",
            "natural_title": "Natural (Dry) Processing",
            "washed_title": "Washed Processing",
            "honey_title": "Honey Processing",
            "comparison_title": "Methods Comparison",
            "cta_title": "Try Different Processing Methods",
            "cta_button": "To Catalog"
        }
    },
    "coffee_seasonality": {
        "uk": {
            "title": "Сезонність кави: коли найсвіжіша?",
            "category": "ORIGINS",
            "reading_time": "5 хв читання",
            "intro": "Кава — сезонний продукт. Розуміння сезонності допомагає обирати найсвіжішу каву.",
            "harvest_title": "Сезони збору в різних країнах",
            "ethiopia_title": "Ефіопія",
            "freshness_title": "Як це впливає на свіжість",
            "tips_title": "Поради щодо вибору",
            "cta_title": "Замовте свіжу сезонну каву",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Сезонность кофе: когда самый свежий?",
            "category": "ORIGINS",
            "reading_time": "5 мин чтения",
            "intro": "Кофе — сезонный продукт. Понимание сезонности помогает выбирать самый свежий кофе.",
            "harvest_title": "Сезоны сбора в разных странах",
            "ethiopia_title": "Эфиопия",
            "freshness_title": "Как это влияет на свежесть",
            "tips_title": "Советы по выбору",
            "cta_title": "Закажите свежий сезонный кофе",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Coffee Seasonality: When is it Freshest?",
            "category": "ORIGINS",
            "reading_time": "5 min read",
            "intro": "Coffee is a seasonal product. Understanding seasonality helps choose the freshest coffee.",
            "harvest_title": "Harvest Seasons in Different Countries",
            "ethiopia_title": "Ethiopia",
            "freshness_title": "How It Affects Freshness",
            "tips_title": "Selection Tips",
            "cta_title": "Order Fresh Seasonal Coffee",
            "cta_button": "To Catalog"
        }
    },
    "blog_coffee_storage": {
        "uk": {
            "title": "Як правильно зберігати каву",
            "category": "TIPS",
            "reading_time": "4 хв читання",
            "intro": "Правильне зберігання — ключ до збереження смаку та аромату кави.",
            "enemies_title": "Вороги свіжості",
            "containers_title": "Правильна тара",
            "tips_title": "Поради зберігання",
            "cta_title": "Замовте свіжу каву",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Как правильно хранить кофе",
            "category": "TIPS",
            "reading_time": "4 мин чтения",
            "intro": "Правильное хранение — ключ к сохранению вкуса и аромата кофе.",
            "enemies_title": "Враги свежести",
            "containers_title": "Правильная тара",
            "tips_title": "Советы по хранению",
            "cta_title": "Закажите свежий кофе",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "How to Store Coffee Properly",
            "category": "TIPS",
            "reading_time": "4 min read",
            "intro": "Proper storage is key to preserving coffee's taste and aroma.",
            "enemies_title": "Enemies of Freshness",
            "containers_title": "Proper Containers",
            "tips_title": "Storage Tips",
            "cta_title": "Order Fresh Coffee",
            "cta_button": "To Catalog"
        }
    },
    "cold_brew_guide": {
        "uk": {
            "title": "Cold Brew: повний гід",
            "category": "BREWING",
            "reading_time": "5 хв читання",
            "intro": "Cold Brew — освіжаючий спосіб насолодитись кавою влітку. Менше кислотності, більше солодкості.",
            "what_is_title": "Що таке Cold Brew?",
            "recipe_title": "Базовий рецепт",
            "ratio_title": "Пропорції",
            "serving_title": "Як подавати",
            "cta_title": "Замовте каву для Cold Brew",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Cold Brew: полный гид",
            "category": "BREWING",
            "reading_time": "5 мин чтения",
            "intro": "Cold Brew — освежающий способ насладиться кофе летом. Меньше кислотности, больше сладости.",
            "what_is_title": "Что такое Cold Brew?",
            "recipe_title": "Базовый рецепт",
            "ratio_title": "Пропорции",
            "serving_title": "Как подавать",
            "cta_title": "Закажите кофе для Cold Brew",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Cold Brew: Complete Guide",
            "category": "BREWING",
            "reading_time": "5 min read",
            "intro": "Cold Brew — a refreshing way to enjoy coffee in summer. Less acidity, more sweetness.",
            "what_is_title": "What is Cold Brew?",
            "recipe_title": "Basic Recipe",
            "ratio_title": "Ratios",
            "serving_title": "How to Serve",
            "cta_title": "Order Coffee for Cold Brew",
            "cta_button": "To Catalog"
        }
    },
    "espresso_guide": {
        "uk": {
            "title": "Еспресо вдома: повний гід",
            "category": "BREWING",
            "reading_time": "8 хв читання",
            "intro": "Приготування ідеального еспресо вдома — це мистецтво. Ось все, що вам потрібно знати.",
            "equipment_title": "Необхідне обладнання",
            "grind_title": "Помел",
            "recipe_title": "Базовий рецепт",
            "troubleshooting_title": "Вирішення проблем",
            "cta_title": "Замовте каву для еспресо",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Эспрессо дома: полный гид",
            "category": "BREWING",
            "reading_time": "8 мин чтения",
            "intro": "Приготовление идеального эспрессо дома — это искусство. Вот всё, что вам нужно знать.",
            "equipment_title": "Необходимое оборудование",
            "grind_title": "Помол",
            "recipe_title": "Базовый рецепт",
            "troubleshooting_title": "Решение проблем",
            "cta_title": "Закажите кофе для эспрессо",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Espresso at Home: Complete Guide",
            "category": "BREWING",
            "reading_time": "8 min read",
            "intro": "Making perfect espresso at home is an art. Here's everything you need to know.",
            "equipment_title": "Required Equipment",
            "grind_title": "Grind",
            "recipe_title": "Basic Recipe",
            "troubleshooting_title": "Troubleshooting",
            "cta_title": "Order Coffee for Espresso",
            "cta_button": "To Catalog"
        }
    },
    "ethiopia_origins": {
        "uk": {
            "title": "Ефіопія — батьківщина кави",
            "category": "ORIGINS",
            "reading_time": "6 хв читання",
            "intro": "Ефіопія — єдина країна, де кава росте в дикій природі. Це батьківщина арабіки.",
            "history_title": "Історія відкриття",
            "regions_title": "Основні регіони",
            "yirgacheffe_title": "Yirgacheffe",
            "sidamo_title": "Sidamo",
            "guji_title": "Guji",
            "taste_title": "Чому ефіопська кава особлива?",
            "cta_title": "Спробуйте справжню ефіопську каву",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Эфиопия — родина кофе",
            "category": "ORIGINS",
            "reading_time": "6 мин чтения",
            "intro": "Эфиопия — единственная страна, где кофе растёт в дикой природе. Это родина арабики.",
            "history_title": "История открытия",
            "regions_title": "Основные регионы",
            "yirgacheffe_title": "Yirgacheffe",
            "sidamo_title": "Sidamo",
            "guji_title": "Guji",
            "taste_title": "Почему эфиопский кофе особенный?",
            "cta_title": "Попробуйте настоящий эфиопский кофе",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Ethiopia — The Birthplace of Coffee",
            "category": "ORIGINS",
            "reading_time": "6 min read",
            "intro": "Ethiopia is the only country where coffee grows wild. It's the birthplace of Arabica.",
            "history_title": "Discovery History",
            "regions_title": "Main Regions",
            "yirgacheffe_title": "Yirgacheffe",
            "sidamo_title": "Sidamo",
            "guji_title": "Guji",
            "taste_title": "Why is Ethiopian Coffee Special?",
            "cta_title": "Try Real Ethiopian Coffee",
            "cta_button": "To Catalog"
        }
    },
    "french_press_guide": {
        "uk": {
            "title": "Френч-прес: простий та смачний",
            "category": "BREWING",
            "reading_time": "4 хв читання",
            "intro": "Френч-прес — один з найпростіших методів заварювання з повним тілом та насиченим смаком.",
            "equipment_title": "Що вам потрібно",
            "recipe_title": "Рецепт",
            "tips_title": "Поради",
            "cta_title": "Замовте каву для френч-пресу",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Френч-пресс: просто и вкусно",
            "category": "BREWING",
            "reading_time": "4 мин чтения",
            "intro": "Френч-пресс — один из простейших методов заваривания с полным телом и насыщенным вкусом.",
            "equipment_title": "Что вам нужно",
            "recipe_title": "Рецепт",
            "tips_title": "Советы",
            "cta_title": "Закажите кофе для френч-пресса",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "French Press: Simple and Delicious",
            "category": "BREWING",
            "reading_time": "4 min read",
            "intro": "French Press is one of the simplest brewing methods with full body and rich taste.",
            "equipment_title": "What You Need",
            "recipe_title": "Recipe",
            "tips_title": "Tips",
            "cta_title": "Order Coffee for French Press",
            "cta_button": "To Catalog"
        }
    },
    "sca_grading": {
        "uk": {
            "title": "Оцінка SCA: що означають бали",
            "category": "SPECIALTY",
            "reading_time": "5 хв читання",
            "intro": "SCA (Specialty Coffee Association) — світовий стандарт оцінки якості кави. Що означають ці бали?",
            "scale_title": "Шкала оцінювання",
            "criteria_title": "Критерії оцінки",
            "specialty_title": "Що таке Specialty?",
            "cta_title": "Спробуйте каву 85+ балів",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Оценка SCA: что означают баллы",
            "category": "SPECIALTY",
            "reading_time": "5 мин чтения",
            "intro": "SCA (Specialty Coffee Association) — мировой стандарт оценки качества кофе. Что означают эти баллы?",
            "scale_title": "Шкала оценивания",
            "criteria_title": "Критерии оценки",
            "specialty_title": "Что такое Specialty?",
            "cta_title": "Попробуйте кофе 85+ баллов",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "SCA Grading: What the Scores Mean",
            "category": "SPECIALTY",
            "reading_time": "5 min read",
            "intro": "SCA (Specialty Coffee Association) is the world standard for coffee quality assessment. What do these scores mean?",
            "scale_title": "Grading Scale",
            "criteria_title": "Evaluation Criteria",
            "specialty_title": "What is Specialty?",
            "cta_title": "Try 85+ Score Coffee",
            "cta_button": "To Catalog"
        }
    },
    "specialty_coffee": {
        "uk": {
            "title": "Що таке Specialty кава?",
            "category": "SPECIALTY",
            "reading_time": "7 хв читання",
            "intro": "Specialty кава — це вершина якості в кавовому світі. Але що саме робить каву \"specialty\"?",
            "definition_title": "Визначення",
            "grading_title": "Система оцінювання",
            "difference_title": "Відмінності від комерційної кави",
            "why_expensive_title": "Чому specialty дорожча?",
            "worth_it_title": "Чи варто переплачувати?",
            "cta_title": "Спробуйте справжню specialty каву",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Что такое Specialty кофе?",
            "category": "SPECIALTY",
            "reading_time": "7 мин чтения",
            "intro": "Specialty кофе — это вершина качества в кофейном мире. Но что именно делает кофе \"specialty\"?",
            "definition_title": "Определение",
            "grading_title": "Система оценивания",
            "difference_title": "Отличия от коммерческого кофе",
            "why_expensive_title": "Почему specialty дороже?",
            "worth_it_title": "Стоит ли переплачивать?",
            "cta_title": "Попробуйте настоящий specialty кофе",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "What is Specialty Coffee?",
            "category": "SPECIALTY",
            "reading_time": "7 min read",
            "intro": "Specialty coffee is the pinnacle of quality in the coffee world. But what exactly makes coffee \"specialty\"?",
            "definition_title": "Definition",
            "grading_title": "Grading System",
            "difference_title": "Differences from Commercial Coffee",
            "why_expensive_title": "Why is Specialty More Expensive?",
            "worth_it_title": "Is It Worth the Price?",
            "cta_title": "Try Real Specialty Coffee",
            "cta_button": "To Catalog"
        }
    },
    "turka_guide": {
        "uk": {
            "title": "Кава в турці: традиційний метод",
            "category": "BREWING",
            "reading_time": "5 хв читання",
            "intro": "Турка — один з найдавніших методів приготування кави. Густий, ароматний напій з багатою історією.",
            "history_title": "Історія",
            "equipment_title": "Вибір турки",
            "recipe_title": "Класичний рецепт",
            "tips_title": "Секрети майстрів",
            "cta_title": "Замовте каву для турки",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Кофе в турке: традиционный метод",
            "category": "BREWING",
            "reading_time": "5 мин чтения",
            "intro": "Турка — один из древнейших методов приготовления кофе. Густой, ароматный напиток с богатой историей.",
            "history_title": "История",
            "equipment_title": "Выбор турки",
            "recipe_title": "Классический рецепт",
            "tips_title": "Секреты мастеров",
            "cta_title": "Закажите кофе для турки",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Turkish Coffee: Traditional Method",
            "category": "BREWING",
            "reading_time": "5 min read",
            "intro": "Turkish coffee pot is one of the oldest coffee brewing methods. A thick, aromatic drink with rich history.",
            "history_title": "History",
            "equipment_title": "Choosing a Cezve",
            "recipe_title": "Classic Recipe",
            "tips_title": "Master's Secrets",
            "cta_title": "Order Coffee for Turkish",
            "cta_button": "To Catalog"
        }
    },
    "v60_guide": {
        "uk": {
            "title": "V60: мистецтво пуроверу",
            "category": "BREWING",
            "reading_time": "6 хв читання",
            "intro": "Hario V60 — один з найпопулярніших методів альтернативного заварювання. Чистий, яскравий смак.",
            "equipment_title": "Обладнання",
            "recipe_title": "Базовий рецепт",
            "technique_title": "Техніка заливки",
            "troubleshooting_title": "Вирішення проблем",
            "cta_title": "Замовте каву для V60",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "V60: искусство пуровера",
            "category": "BREWING",
            "reading_time": "6 мин чтения",
            "intro": "Hario V60 — один из самых популярных методов альтернативного заваривания. Чистый, яркий вкус.",
            "equipment_title": "Оборудование",
            "recipe_title": "Базовый рецепт",
            "technique_title": "Техника пролива",
            "troubleshooting_title": "Решение проблем",
            "cta_title": "Закажите кофе для V60",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "V60: The Art of Pour Over",
            "category": "BREWING",
            "reading_time": "6 min read",
            "intro": "Hario V60 is one of the most popular alternative brewing methods. Clean, bright taste.",
            "equipment_title": "Equipment",
            "recipe_title": "Basic Recipe",
            "technique_title": "Pouring Technique",
            "troubleshooting_title": "Troubleshooting",
            "cta_title": "Order Coffee for V60",
            "cta_button": "To Catalog"
        }
    },
    "blog_yirgacheffe": {
        "uk": {
            "title": "Yirgacheffe: найвідоміший регіон Ефіопії",
            "category": "ORIGINS",
            "reading_time": "5 хв читання",
            "intro": "Yirgacheffe — легендарний регіон на півдні Ефіопії, відомий своєю квітковою та цитрусовою кавою.",
            "geography_title": "Географія та клімат",
            "taste_title": "Смаковий профіль",
            "processing_title": "Методи обробки",
            "cta_title": "Спробуйте Yirgacheffe",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Yirgacheffe: самый известный регион Эфиопии",
            "category": "ORIGINS",
            "reading_time": "5 мин чтения",
            "intro": "Yirgacheffe — легендарный регион на юге Эфиопии, известный своим цветочным и цитрусовым кофе.",
            "geography_title": "География и климат",
            "taste_title": "Вкусовой профиль",
            "processing_title": "Методы обработки",
            "cta_title": "Попробуйте Yirgacheffe",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Yirgacheffe: Ethiopia's Most Famous Region",
            "category": "ORIGINS",
            "reading_time": "5 min read",
            "intro": "Yirgacheffe is a legendary region in southern Ethiopia, known for its floral and citrus coffee.",
            "geography_title": "Geography and Climate",
            "taste_title": "Taste Profile",
            "processing_title": "Processing Methods",
            "cta_title": "Try Yirgacheffe",
            "cta_button": "To Catalog"
        }
    }
}

def update_all_locales():
    """Add all blog translations to locale files"""
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "blog" not in data:
            data["blog"] = {}
        
        for blog_key, blog_langs in ALL_BLOGS.items():
            data["blog"][blog_key] = blog_langs[lang]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path} with {len(ALL_BLOGS)} blog translations")

if __name__ == "__main__":
    print("Adding all blog translations...")
    update_all_locales()
    print("Done! All blog translations added to locale files.")
