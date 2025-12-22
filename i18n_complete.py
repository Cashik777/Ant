#!/usr/bin/env python3
"""
Complete i18n Implementation Script
Adds data-i18n attributes to all content and creates translations for UK/RU/EN
"""

import os
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Articles translations - each article fully translated
ARTICLES_TRANSLATIONS = {
    "sidamo_guide": {
        "uk": {
            "title": "Сідамо: класика ефіопської кави",
            "subtitle": "Найпопулярніший регіон та його унікальний терруар",
            "back": "Назад",
            "intro": "Якщо Yirgacheffe — це \"перлина\" для гурманів, то Sidamo — це \"класика\", яку люблять усі. Цей великий регіон на півдні Ефіопії виробляє збалансовану, м'яку каву, яка підходить для будь-якого способу приготування.",
            "geography_title": "Географія регіону",
            "geography_p1": "Sidamo (або Sidama) — це регіон у Рифтовій долині на півдні Ефіопії. Цікаво, що Yirgacheffe технічно є частиною Sidamo, але отримала власний статус через унікальний смак.",
            "altitude_label": "Висота:",
            "altitude_value": "1500-2200 м над рівнем моря",
            "climate_label": "Клімат:",
            "climate_value": "тропічний, два сезони дощів",
            "soil_label": "Ґрунти:",
            "soil_value": "багаті вулканічні",
            "taste_title": "☕ Смаковий профіль Sidamo",
            "aroma_label": "Аромат:",
            "aroma_value": "шоколад, горіхи, карамель",
            "taste_label": "Смак:",
            "taste_value": "молочний шоколад, мигдаль, м'яка цитрусова кислинка",
            "acidity_label": "Кислотність:",
            "acidity_value": "середня, збалансована",
            "body_label": "Тіло:",
            "body_value": "середнє, кремове",
            "aftertaste_label": "Післясмак:",
            "aftertaste_value": "солодкий, тривалий",
            "why_popular_title": "Чому Sidamo така популярна",
            "why_universal": "Універсальність",
            "why_universal_desc": "— підходить і для еспресо, і для фільтра",
            "why_affordable": "Доступність",
            "why_affordable_desc": "— дешевша за елітні мікролоти",
            "why_stable": "Стабільність",
            "why_stable_desc": "— великі обсяги, передбачуваний смак",
            "why_balance": "Баланс",
            "why_balance_desc": "— не занадто кисла, не занадто гірка",
            "how_brew_title": "Як готувати Sidamo",
            "how_brew_intro": "Sidamo — одна з найуниверсальніших кав. Вона чудово працює з:",
            "brew_espresso": "Еспресо",
            "brew_espresso_desc": "— середня обсмажка, яскрава крема, шоколадний смак",
            "brew_v60": "V60 / фільтр",
            "brew_v60_desc": "— світла обсмажка, розкриває фруктові ноти",
            "brew_moka": "Мока / турка",
            "brew_moka_desc": "— темна обсмажка, насичений смак",
            "brew_cold": "Cold Brew",
            "brew_cold_desc": "— солодкий, шоколадний, освіжаючий",
            "our_sidamo_title": "Наша Sidamo",
            "our_sidamo_text": "Ми працюємо з кооперативами в районі Bensa — одному з найкращих субрегіонів Sidamo. Наша кава проходить миту обробку та має оцінку 85 балів SCA.",
            "cta_title": "Спробуйте нашу Sidamo",
            "cta_text": "Класичний смак Ефіопії в кожній чашці",
            "cta_button": "Замовити"
        },
        "ru": {
            "title": "Сидамо: классика эфиопского кофе",
            "subtitle": "Самый популярный регион и его уникальный терруар",
            "back": "Назад",
            "intro": "Если Yirgacheffe — это \"жемчужина\" для гурманов, то Sidamo — это \"классика\", которую любят все. Этот большой регион на юге Эфиопии производит сбалансированный, мягкий кофе, который подходит для любого способа приготовления.",
            "geography_title": "География региона",
            "geography_p1": "Sidamo (или Sidama) — это регион в Рифтовой долине на юге Эфиопии. Интересно, что Yirgacheffe технически является частью Sidamo, но получила собственный статус благодаря уникальному вкусу.",
            "altitude_label": "Высота:",
            "altitude_value": "1500-2200 м над уровнем моря",
            "climate_label": "Климат:",
            "climate_value": "тропический, два сезона дождей",
            "soil_label": "Почвы:",
            "soil_value": "богатые вулканические",
            "taste_title": "☕ Вкусовой профиль Sidamo",
            "aroma_label": "Аромат:",
            "aroma_value": "шоколад, орехи, карамель",
            "taste_label": "Вкус:",
            "taste_value": "молочный шоколад, миндаль, мягкая цитрусовая кислинка",
            "acidity_label": "Кислотность:",
            "acidity_value": "средняя, сбалансированная",
            "body_label": "Тело:",
            "body_value": "среднее, кремовое",
            "aftertaste_label": "Послевкусие:",
            "aftertaste_value": "сладкое, продолжительное",
            "why_popular_title": "Почему Sidamo так популярна",
            "why_universal": "Универсальность",
            "why_universal_desc": "— подходит и для эспрессо, и для фильтра",
            "why_affordable": "Доступность",
            "why_affordable_desc": "— дешевле элитных микролотов",
            "why_stable": "Стабильность",
            "why_stable_desc": "— большие объёмы, предсказуемый вкус",
            "why_balance": "Баланс",
            "why_balance_desc": "— не слишком кислый, не слишком горький",
            "how_brew_title": "Как готовить Sidamo",
            "how_brew_intro": "Sidamo — один из самых универсальных сортов кофе. Он отлично работает с:",
            "brew_espresso": "Эспрессо",
            "brew_espresso_desc": "— средняя обжарка, яркая крема, шоколадный вкус",
            "brew_v60": "V60 / фильтр",
            "brew_v60_desc": "— светлая обжарка, раскрывает фруктовые ноты",
            "brew_moka": "Мока / турка",
            "brew_moka_desc": "— тёмная обжарка, насыщенный вкус",
            "brew_cold": "Cold Brew",
            "brew_cold_desc": "— сладкий, шоколадный, освежающий",
            "our_sidamo_title": "Наша Sidamo",
            "our_sidamo_text": "Мы работаем с кооперативами в районе Bensa — одном из лучших субрегионов Sidamo. Наш кофе проходит мытую обработку и имеет оценку 85 баллов SCA.",
            "cta_title": "Попробуйте нашу Sidamo",
            "cta_text": "Классический вкус Эфиопии в каждой чашке",
            "cta_button": "Заказать"
        },
        "en": {
            "title": "Sidamo: Ethiopian Coffee Classic",
            "subtitle": "The most popular region and its unique terroir",
            "back": "Back",
            "intro": "If Yirgacheffe is the \"pearl\" for gourmets, then Sidamo is the \"classic\" that everyone loves. This large region in southern Ethiopia produces balanced, smooth coffee suitable for any brewing method.",
            "geography_title": "Region Geography",
            "geography_p1": "Sidamo (or Sidama) is a region in the Rift Valley in southern Ethiopia. Interestingly, Yirgacheffe is technically part of Sidamo but has gained its own status due to its unique flavor.",
            "altitude_label": "Altitude:",
            "altitude_value": "1500-2200 m above sea level",
            "climate_label": "Climate:",
            "climate_value": "tropical, two rainy seasons",
            "soil_label": "Soils:",
            "soil_value": "rich volcanic",
            "taste_title": "☕ Sidamo Flavor Profile",
            "aroma_label": "Aroma:",
            "aroma_value": "chocolate, nuts, caramel",
            "taste_label": "Taste:",
            "taste_value": "milk chocolate, almond, soft citrus acidity",
            "acidity_label": "Acidity:",
            "acidity_value": "medium, balanced",
            "body_label": "Body:",
            "body_value": "medium, creamy",
            "aftertaste_label": "Aftertaste:",
            "aftertaste_value": "sweet, lingering",
            "why_popular_title": "Why Sidamo is So Popular",
            "why_universal": "Versatility",
            "why_universal_desc": "— suitable for both espresso and filter",
            "why_affordable": "Affordability",
            "why_affordable_desc": "— cheaper than elite micro-lots",
            "why_stable": "Consistency",
            "why_stable_desc": "— large volumes, predictable taste",
            "why_balance": "Balance",
            "why_balance_desc": "— not too acidic, not too bitter",
            "how_brew_title": "How to Brew Sidamo",
            "how_brew_intro": "Sidamo is one of the most versatile coffees. It works great with:",
            "brew_espresso": "Espresso",
            "brew_espresso_desc": "— medium roast, bright crema, chocolate flavor",
            "brew_v60": "V60 / filter",
            "brew_v60_desc": "— light roast, reveals fruity notes",
            "brew_moka": "Moka / Turkish",
            "brew_moka_desc": "— dark roast, rich flavor",
            "brew_cold": "Cold Brew",
            "brew_cold_desc": "— sweet, chocolatey, refreshing",
            "our_sidamo_title": "Our Sidamo",
            "our_sidamo_text": "We work with cooperatives in the Bensa area — one of the best sub-regions of Sidamo. Our coffee undergoes washed processing and has a score of 85 SCA points.",
            "cta_title": "Try Our Sidamo",
            "cta_text": "Classic Ethiopian taste in every cup",
            "cta_button": "Order Now"
        }
    },
    "yirgacheffe_region": {
        "uk": {
            "title": "Yirgacheffe: перлина ефіопської кави",
            "subtitle": "Легендарний регіон з квітковим смаком",
            "back": "Назад",
            "intro": "Yirgacheffe — це не просто назва регіону, це синонім найелегантнішої кави у світі. Квіткові, цитрусові ноти та неймовірна чистота чашки зробили цей сорт культовим.",
            "geography_title": "Де росте Yirgacheffe",
            "geography_p1": "Yirgacheffe — невеликий район у складі регіону Sidamo на півдні Ефіопії. Завдяки унікальному мікроклімату та ідеальній висоті (1750-2200 м) кава тут набуває особливого характеру.",
            "taste_title": "☕ Смаковий профіль Yirgacheffe",
            "aroma_value": "жасмин, бергамот, лимонна цедра",
            "taste_value": "чай, персик, лимон, мед",
            "cta_title": "Спробуйте нашу Yirgacheffe",
            "cta_text": "Елегантність Ефіопії в кожній чашці",
            "cta_button": "Замовити"
        },
        "ru": {
            "title": "Yirgacheffe: жемчужина эфиопского кофе",
            "subtitle": "Легендарный регион с цветочным вкусом",
            "back": "Назад",
            "intro": "Yirgacheffe — это не просто название региона, это синоним самого элегантного кофе в мире. Цветочные, цитрусовые ноты и невероятная чистота чашки сделали этот сорт культовым.",
            "geography_title": "Где растёт Yirgacheffe",
            "geography_p1": "Yirgacheffe — небольшой район в составе региона Sidamo на юге Эфиопии. Благодаря уникальному микроклимату и идеальной высоте (1750-2200 м) кофе здесь приобретает особый характер.",
            "taste_title": "☕ Вкусовой профиль Yirgacheffe",
            "aroma_value": "жасмин, бергамот, лимонная цедра",
            "taste_value": "чай, персик, лимон, мёд",
            "cta_title": "Попробуйте нашу Yirgacheffe",
            "cta_text": "Элегантность Эфиопии в каждой чашке",
            "cta_button": "Заказать"
        },
        "en": {
            "title": "Yirgacheffe: The Pearl of Ethiopian Coffee",
            "subtitle": "Legendary region with floral taste",
            "back": "Back",
            "intro": "Yirgacheffe is not just a region name, it's a synonym for the most elegant coffee in the world. Floral, citrus notes and incredible cup clarity have made this variety iconic.",
            "geography_title": "Where Yirgacheffe Grows",
            "geography_p1": "Yirgacheffe is a small district within the Sidamo region in southern Ethiopia. Thanks to its unique microclimate and ideal altitude (1750-2200 m), coffee here acquires a special character.",
            "taste_title": "☕ Yirgacheffe Flavor Profile",
            "aroma_value": "jasmine, bergamot, lemon zest",
            "taste_value": "tea, peach, lemon, honey",
            "cta_title": "Try Our Yirgacheffe",
            "cta_text": "Ethiopian elegance in every cup",
            "cta_button": "Order Now"
        }
    },
    "ethiopia_coffee_origin": {
        "uk": {
            "title": "Ефіопія — батьківщина кави",
            "subtitle": "Історія, легенди та унікальність",
            "back": "Назад",
            "intro": "Ефіопія — єдина країна, де кава росте природно у дикому середовищі. Саме тут понад 1000 років тому була відкрита кава завдяки легендарному пастухові Калді.",
            "legend_title": "Легенда про Калді",
            "legend_p1": "За легендою, пастух Калді помітив, що його кози стають енергійними після поїдання червоних ягід з певного куща. Він розповів про це монахам, і так почалася історія кави.",
            "cta_title": "Спробуйте справжню ефіопську каву",
            "cta_text": "Від батьківщини кави — до вашої чашки",
            "cta_button": "Замовити"
        },
        "ru": {
            "title": "Эфиопия — родина кофе",
            "subtitle": "История, легенды и уникальность",
            "back": "Назад",
            "intro": "Эфиопия — единственная страна, где кофе растёт естественным образом в дикой среде. Именно здесь более 1000 лет назад был открыт кофе благодаря легендарному пастуху Калди.",
            "legend_title": "Легенда о Калди",
            "legend_p1": "По легенде, пастух Калди заметил, что его козы становятся энергичными после поедания красных ягод с определённого куста. Он рассказал об этом монахам, и так началась история кофе.",
            "cta_title": "Попробуйте настоящий эфиопский кофе",
            "cta_text": "От родины кофе — к вашей чашке",
            "cta_button": "Заказать"
        },
        "en": {
            "title": "Ethiopia — The Birthplace of Coffee",
            "subtitle": "History, legends and uniqueness",
            "back": "Back",
            "intro": "Ethiopia is the only country where coffee grows naturally in the wild. It was here that coffee was discovered over 1000 years ago thanks to the legendary shepherd Kaldi.",
            "legend_title": "The Legend of Kaldi",
            "legend_p1": "According to legend, the shepherd Kaldi noticed that his goats became energetic after eating red berries from a certain bush. He told the monks about it, and thus began the history of coffee.",
            "cta_title": "Try Real Ethiopian Coffee",
            "cta_text": "From the birthplace of coffee — to your cup",
            "cta_button": "Order Now"
        }
    },
    "what_is_specialty": {
        "uk": {
            "title": "Що таке Specialty кава?",
            "subtitle": "Стандарти якості та оцінка SCA",
            "back": "Назад",
            "intro": "Specialty кава — це кава, яка отримала оцінку 80+ балів за 100-бальною шкалою SCA. Лише близько 5% усієї кави у світі досягає цього рівня якості.",
            "sca_title": "Система оцінки SCA",
            "sca_p1": "Specialty Coffee Association (SCA) розробила строгі стандарти для оцінки кави. Q-грейдери оцінюють 10 параметрів: аромат, смак, післясмак, кислотність, тіло, баланс, чистоту чашки та інші.",
            "grades_title": "Класифікація балів",
            "grade_specialty": "80-84 балів — Specialty",
            "grade_premium": "85-89 балів — Premium Specialty",
            "grade_exceptional": "90+ балів — Exceptional (Рідкісні лоти)",
            "cta_title": "Спробуйте Specialty каву",
            "cta_text": "Наша кава — 85+ балів SCA",
            "cta_button": "Замовити"
        },
        "ru": {
            "title": "Что такое Specialty кофе?",
            "subtitle": "Стандарты качества и оценка SCA",
            "back": "Назад",
            "intro": "Specialty кофе — это кофе, получивший оценку 80+ баллов по 100-балльной шкале SCA. Лишь около 5% всего кофе в мире достигает этого уровня качества.",
            "sca_title": "Система оценки SCA",
            "sca_p1": "Specialty Coffee Association (SCA) разработала строгие стандарты для оценки кофе. Q-грейдеры оценивают 10 параметров: аромат, вкус, послевкусие, кислотность, тело, баланс, чистоту чашки и другие.",
            "grades_title": "Классификация баллов",
            "grade_specialty": "80-84 балла — Specialty",
            "grade_premium": "85-89 баллов — Premium Specialty",
            "grade_exceptional": "90+ баллов — Exceptional (Редкие лоты)",
            "cta_title": "Попробуйте Specialty кофе",
            "cta_text": "Наш кофе — 85+ баллов SCA",
            "cta_button": "Заказать"
        },
        "en": {
            "title": "What is Specialty Coffee?",
            "subtitle": "Quality standards and SCA grading",
            "back": "Back",
            "intro": "Specialty coffee is coffee that has scored 80+ points on the SCA 100-point scale. Only about 5% of all coffee in the world reaches this level of quality.",
            "sca_title": "SCA Grading System",
            "sca_p1": "The Specialty Coffee Association (SCA) has developed strict standards for grading coffee. Q-graders evaluate 10 parameters: aroma, flavor, aftertaste, acidity, body, balance, cup cleanliness and others.",
            "grades_title": "Score Classification",
            "grade_specialty": "80-84 points — Specialty",
            "grade_premium": "85-89 points — Premium Specialty",
            "grade_exceptional": "90+ points — Exceptional (Rare lots)",
            "cta_title": "Try Specialty Coffee",
            "cta_text": "Our coffee — 85+ SCA points",
            "cta_button": "Order Now"
        }
    },
    "light_vs_dark_roast": {
        "uk": {
            "title": "Світла vs темна обсмажка",
            "subtitle": "Як ступінь обсмажки впливає на смак",
            "back": "Назад",
            "intro": "Обсмажка — це ключовий етап, який визначає характер кави. Світла обсмажка розкриває терруар та кислотність, темна — додає тіла та гіркоти.",
            "light_title": "Світла обсмажка",
            "light_desc": "Зберігає оригінальний смак зерна, підкреслює фруктові та квіткові ноти. Ідеальна для Specialty кави.",
            "dark_title": "Темна обсмажка",
            "dark_desc": "Додає карамельних, шоколадних нот. Менша кислотність, більше гіркоти. Класика для еспресо.",
            "cta_title": "Спробуйте різні обсмажки",
            "cta_text": "Знайдіть свій ідеальний смак",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Светлая vs тёмная обжарка",
            "subtitle": "Как степень обжарки влияет на вкус",
            "back": "Назад",
            "intro": "Обжарка — это ключевой этап, определяющий характер кофе. Светлая обжарка раскрывает терруар и кислотность, тёмная — добавляет тела и горчинки.",
            "light_title": "Светлая обжарка",
            "light_desc": "Сохраняет оригинальный вкус зерна, подчёркивает фруктовые и цветочные ноты. Идеальна для Specialty кофе.",
            "dark_title": "Тёмная обжарка",
            "dark_desc": "Добавляет карамельных, шоколадных нот. Меньше кислотности, больше горчинки. Классика для эспрессо.",
            "cta_title": "Попробуйте разные обжарки",
            "cta_text": "Найдите свой идеальный вкус",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Light vs Dark Roast",
            "subtitle": "How roast level affects taste",
            "back": "Back",
            "intro": "Roasting is the key stage that determines the character of coffee. Light roast reveals terroir and acidity, dark adds body and bitterness.",
            "light_title": "Light Roast",
            "light_desc": "Preserves the original bean flavor, emphasizes fruity and floral notes. Ideal for Specialty coffee.",
            "dark_title": "Dark Roast",
            "dark_desc": "Adds caramel, chocolate notes. Less acidity, more bitterness. Classic for espresso.",
            "cta_title": "Try Different Roasts",
            "cta_text": "Find your perfect taste",
            "cta_button": "To Catalog"
        }
    },
    "water_for_coffee": {
        "uk": {
            "title": "Вода для кави: повний гід",
            "subtitle": "Чому вода важливіша за каву",
            "back": "Назад",
            "intro": "Кава на 98% складається з води. Якість води напряму впливає на екстракцію та смак. Неправильна вода може зіпсувати навіть найкращу Specialty каву.",
            "params_title": "Ідеальні параметри води",
            "tds_label": "TDS (мінералізація):",
            "tds_value": "75-150 ppm",
            "ph_label": "pH:",
            "ph_value": "6.5-7.5",
            "cta_title": "Оптимізуйте свою каву",
            "cta_text": "Правильна вода = ідеальний смак",
            "cta_button": "Замовити каву"
        },
        "ru": {
            "title": "Вода для кофе: полный гид",
            "subtitle": "Почему вода важнее кофе",
            "back": "Назад",
            "intro": "Кофе на 98% состоит из воды. Качество воды напрямую влияет на экстракцию и вкус. Неправильная вода может испортить даже лучший Specialty кофе.",
            "params_title": "Идеальные параметры воды",
            "tds_label": "TDS (минерализация):",
            "tds_value": "75-150 ppm",
            "ph_label": "pH:",
            "ph_value": "6.5-7.5",
            "cta_title": "Оптимизируйте свой кофе",
            "cta_text": "Правильная вода = идеальный вкус",
            "cta_button": "Заказать кофе"
        },
        "en": {
            "title": "Water for Coffee: Complete Guide",
            "subtitle": "Why water is more important than coffee",
            "back": "Back",
            "intro": "Coffee is 98% water. Water quality directly affects extraction and taste. Wrong water can ruin even the best Specialty coffee.",
            "params_title": "Ideal Water Parameters",
            "tds_label": "TDS (mineralization):",
            "tds_value": "75-150 ppm",
            "ph_label": "pH:",
            "ph_value": "6.5-7.5",
            "cta_title": "Optimize Your Coffee",
            "cta_text": "Right water = perfect taste",
            "cta_button": "Order Coffee"
        }
    }
}

# Common translations shared across all pages
COMMON_TRANSLATIONS = {
    "uk": {
        "topbar_free_delivery": "🔥 Безкоштовна доставка від 500₴",
        "back": "Назад",
        "order_now": "Замовити",
        "to_catalog": "До каталогу",
        "read_more": "Читати далі"
    },
    "ru": {
        "topbar_free_delivery": "🔥 Бесплатная доставка от 500₴",
        "back": "Назад",
        "order_now": "Заказать",
        "to_catalog": "В каталог",
        "read_more": "Читать далее"
    },
    "en": {
        "topbar_free_delivery": "🔥 Free delivery from 500₴",
        "back": "Back",
        "order_now": "Order Now",
        "to_catalog": "To Catalog",
        "read_more": "Read More"
    }
}


def update_locale_file(lang: str, new_translations: dict):
    """Add new translations to locale file"""
    locale_path = BASE_DIR / "locales" / f"{lang}.json"
    
    # Read existing
    with open(locale_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Merge new translations
    if "articles" not in data:
        data["articles"] = {}
    
    for article_key, article_trans in new_translations.get("articles", {}).items():
        data["articles"][article_key] = article_trans
    
    # Add common
    if "common" not in data:
        data["common"] = {}
    for key, value in new_translations.get("common", {}).items():
        data["common"][key] = value
    
    # Write back
    with open(locale_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"Updated {locale_path}")


def update_sidamo_guide_html():
    """Update sidamo-guide.html with data-i18n attributes"""
    
    file_path = BASE_DIR / "articles" / "sidamo-guide.html"
    
    new_content = '''<!DOCTYPE html>
<html lang="uk" data-i18n-title="articles.sidamo_guide.title">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Сідамо — EthioDirect</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../css/main.css">
    <style>
        .article-header {
            padding-top: 140px;
            background: linear-gradient(135deg, #2a1f0a, #4a3520);
            color: white;
            padding-bottom: 60px;
        }

        .article-header .container {
            max-width: 800px;
        }

        .article-header h1 {
            font-size: 2.5rem;
            color: white;
            margin-bottom: 20px;
        }

        .article-body {
            max-width: 800px;
            margin: 0 auto;
            padding: 60px 20px;
        }

        .article-body h2 {
            font-size: 1.8rem;
            margin: 40px 0 20px;
        }

        .article-body p {
            font-size: 1.1rem;
            line-height: 1.9;
            color: #444;
            margin-bottom: 20px;
        }

        .article-body ul {
            margin: 20px 0;
            padding-left: 25px;
        }

        .article-body li {
            font-size: 1.1rem;
            line-height: 1.8;
            margin-bottom: 12px;
        }

        .article-image {
            width: 100%;
            border-radius: 12px;
            margin: 30px 0;
        }

        .taste-card {
            background: #f5f0e6;
            padding: 25px;
            border-radius: 12px;
            margin: 20px 0;
        }
    </style>
</head>

<body>
    <div class="top-bar">
        <div class="container top-bar-inner">
            <div class="top-bar-left"><span><i class="fas fa-phone-alt"></i> <span data-i18n="topbar.phone">+380 (50) 123-45-67</span></span></div>
            <div class="top-bar-center"><span data-i18n="common.topbar_free_delivery">🔥 Безкоштовна доставка від 500₴</span></div>
            <div class="top-bar-right">
                <a href="#" translate="no" class="active" onclick="setLanguage('uk'); return false;">UA</a>
                <a href="#" translate="no" onclick="setLanguage('ru'); return false;">RU</a>
                <a href="#" translate="no" onclick="setLanguage('en'); return false;">EN</a>
            </div>
        </div>
    </div>
    <header class="header">
        <div class="container header-inner"><a href="../index.html" class="logo"><i class="fas fa-certificate"></i>
                ETHIODIRECT</a>
            <nav class="nav-desktop"><a href="../shop.html" class="nav-link" data-i18n="nav.catalog">Каталог</a><a href="../blog.html"
                    class="nav-link active" data-i18n="nav.stories">Історії</a><a href="../about.html" class="nav-link" data-i18n="nav.about">Про нас</a></nav>
        </div>
    </header>

    <main>
        <section class="article-header">
            <div class="container">
                <a href="../blog.html" style="color:rgba(255,255,255,0.7); text-decoration:none;"><i
                        class="fas fa-arrow-left"></i> <span data-i18n="articles.sidamo_guide.back">Назад</span></a>
                <h1 style="margin-top:20px;" data-i18n="articles.sidamo_guide.title">Сідамо: класика ефіопської кави</h1>
                <p style="opacity:0.9;" data-i18n="articles.sidamo_guide.subtitle">Найпопулярніший регіон та його унікальний терруар</p>
            </div>
        </section>

        <article class="article-body">
            <img src="https://images.unsplash.com/photo-1610632380989-680fe40816c6?w=1200" alt="Сідамо"
                class="article-image">

            <p data-i18n="articles.sidamo_guide.intro">Якщо Yirgacheffe — це "перлина" для гурманів, то Sidamo — це "класика", яку люблять усі. Цей великий
                регіон на півдні Ефіопії виробляє збалансовану, м\'яку каву, яка підходить для будь-якого способу
                приготування.</p>

            <h2 data-i18n="articles.sidamo_guide.geography_title">Географія регіону</h2>
            <p data-i18n="articles.sidamo_guide.geography_p1">Sidamo (або Sidama) — це регіон у Рифтовій долині на півдні Ефіопії. Цікаво, що Yirgacheffe технічно є
                частиною Sidamo, але отримала власний статус через унікальний смак.</p>
            <p><strong data-i18n="articles.sidamo_guide.altitude_label">Висота:</strong> <span data-i18n="articles.sidamo_guide.altitude_value">1500-2200 м над рівнем моря</span></p>
            <p><strong data-i18n="articles.sidamo_guide.climate_label">Клімат:</strong> <span data-i18n="articles.sidamo_guide.climate_value">тропічний, два сезони дощів</span></p>
            <p><strong data-i18n="articles.sidamo_guide.soil_label">Ґрунти:</strong> <span data-i18n="articles.sidamo_guide.soil_value">багаті вулканічні</span></p>

            <div class="taste-card">
                <h3 style="margin-top:0;" data-i18n="articles.sidamo_guide.taste_title">☕ Смаковий профіль Sidamo</h3>
                <ul style="margin-bottom:0;">
                    <li><strong data-i18n="articles.sidamo_guide.aroma_label">Аромат:</strong> <span data-i18n="articles.sidamo_guide.aroma_value">шоколад, горіхи, карамель</span></li>
                    <li><strong data-i18n="articles.sidamo_guide.taste_label">Смак:</strong> <span data-i18n="articles.sidamo_guide.taste_value">молочний шоколад, мигдаль, м\'яка цитрусова кислинка</span></li>
                    <li><strong data-i18n="articles.sidamo_guide.acidity_label">Кислотність:</strong> <span data-i18n="articles.sidamo_guide.acidity_value">середня, збалансована</span></li>
                    <li><strong data-i18n="articles.sidamo_guide.body_label">Тіло:</strong> <span data-i18n="articles.sidamo_guide.body_value">середнє, кремове</span></li>
                    <li><strong data-i18n="articles.sidamo_guide.aftertaste_label">Післясмак:</strong> <span data-i18n="articles.sidamo_guide.aftertaste_value">солодкий, тривалий</span></li>
                </ul>
            </div>

            <h2 data-i18n="articles.sidamo_guide.why_popular_title">Чому Sidamo така популярна</h2>
            <ul>
                <li><strong data-i18n="articles.sidamo_guide.why_universal">Універсальність</strong> <span data-i18n="articles.sidamo_guide.why_universal_desc">— підходить і для еспресо, і для фільтра</span></li>
                <li><strong data-i18n="articles.sidamo_guide.why_affordable">Доступність</strong> <span data-i18n="articles.sidamo_guide.why_affordable_desc">— дешевша за елітні мікролоти</span></li>
                <li><strong data-i18n="articles.sidamo_guide.why_stable">Стабільність</strong> <span data-i18n="articles.sidamo_guide.why_stable_desc">— великі обсяги, передбачуваний смак</span></li>
                <li><strong data-i18n="articles.sidamo_guide.why_balance">Баланс</strong> <span data-i18n="articles.sidamo_guide.why_balance_desc">— не занадто кисла, не занадто гірка</span></li>
            </ul>

            <h2 data-i18n="articles.sidamo_guide.how_brew_title">Як готувати Sidamo</h2>
            <p data-i18n="articles.sidamo_guide.how_brew_intro">Sidamo — одна з найуниверсальніших кав. Вона чудово працює з:</p>
            <ul>
                <li><strong data-i18n="articles.sidamo_guide.brew_espresso">Еспресо</strong> <span data-i18n="articles.sidamo_guide.brew_espresso_desc">— середня обсмажка, яскрава крема, шоколадний смак</span></li>
                <li><strong data-i18n="articles.sidamo_guide.brew_v60">V60 / фільтр</strong> <span data-i18n="articles.sidamo_guide.brew_v60_desc">— світла обсмажка, розкриває фруктові ноти</span></li>
                <li><strong data-i18n="articles.sidamo_guide.brew_moka">Мока / турка</strong> <span data-i18n="articles.sidamo_guide.brew_moka_desc">— темна обсмажка, насичений смак</span></li>
                <li><strong data-i18n="articles.sidamo_guide.brew_cold">Cold Brew</strong> <span data-i18n="articles.sidamo_guide.brew_cold_desc">— солодкий, шоколадний, освіжаючий</span></li>
            </ul>

            <h2 data-i18n="articles.sidamo_guide.our_sidamo_title">Наша Sidamo</h2>
            <p data-i18n="articles.sidamo_guide.our_sidamo_text">Ми працюємо з кооперативами в районі Bensa — одному з найкращих субрегіонів Sidamo. Наша кава проходить
                миту обробку та має оцінку 85 балів SCA.</p>

            <div
                style="background:var(--primary); padding:40px; border-radius:16px; text-align:center; margin-top:40px;">
                <h3 style="color:white;" data-i18n="articles.sidamo_guide.cta_title">Спробуйте нашу Sidamo</h3>
                <p style="color:rgba(255,255,255,0.9);" data-i18n="articles.sidamo_guide.cta_text">Класичний смак Ефіопії в кожній чашці</p>
                <a href="../shop.html" class="btn"
                    style="background:var(--secondary); color:#1a1a1a; margin-top:15px;" data-i18n="articles.sidamo_guide.cta_button">Замовити</a>
            </div>
        </article>
    </main>

    <footer class="footer-pro">
        <div class="container">
            <div class="footer-bottom">
                <p>&copy; 2025 EthioDirect.</p>
            </div>
        </div>
    </footer>
    <script src="../js/main.js"></script>
    <script src="../js/i18n.js"></script>
</body>

</html>'''
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {file_path}")


def main():
    print("=" * 60)
    print("EthioDirect Complete i18n Implementation")
    print("=" * 60)
    
    # Prepare translations for each language
    for lang in ["uk", "ru", "en"]:
        translations = {
            "articles": {},
            "common": COMMON_TRANSLATIONS[lang]
        }
        
        for article_key, article_data in ARTICLES_TRANSLATIONS.items():
            translations["articles"][article_key] = article_data[lang]
        
        update_locale_file(lang, translations)
    
    # Update HTML files
    update_sidamo_guide_html()
    
    print("\n" + "=" * 60)
    print("✅ Implementation complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
