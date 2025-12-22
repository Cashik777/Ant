#!/usr/bin/env python3
"""Add ethiopia_origin article translations"""
import json
from pathlib import Path
BASE_DIR = Path(__file__).parent

ETHIOPIA_UK = {
    "title": "Ефіопія — батьківщина кави: легенда про пастуха Калді",
    "subtitle": "Історія відкриття кави понад 1000 років тому",
    "intro": "Кожного разу, коли ви насолоджуєтесь чашкою кави, ви продовжуєте традицію з ефіопських гір. Легенда про пастуха Калді — невід'ємна частина кавової культури.",
    "legend_title": "Легенда про пастуха Калді",
    "legend_p1": "У IX столітті козопас Калді помітив: його кози, з'ївши червоні ягоди з невідомого куща, стали надзвичайно енергійними — стрибали та не могли заснути.",
    "quote1": "\"Кози танцювали у місячному світлі. Калді зрозумів — ці ягоди мають магічну силу.\"",
    "legend_p2": "Калді спробував ягоди сам і відчув прилив енергії. Він відніс їх до монастиря, де монахи спочатку кинули їх у вогонь. Але неймовірний аромат підсмажених зерен змусив їх передумати — так з'явився перший кавовий напій.",
    "spread_title": "Від Ефіопії до світу",
    "century15": "XV ст.", "century15_text": "— кава потрапила до Ємену",
    "century16": "XVI ст.", "century16_text": "— стала популярною в Османській імперії",
    "century17": "XVII ст.", "century17_text": "— прибула до Європи",
    "century18": "XVIII ст.", "century18_text": "— поширилась на колонії та стала глобальним товаром",
    "special_title": "Чому ефіопська кава особлива?",
    "diversity_label": "Генетичне різноманіття:", "diversity_text": "понад 10,000 сортів арабіки — більше, ніж у всіх інших країнах.",
    "conditions_label": "Ідеальні умови:", "conditions_text": "висота 1500-2200м, вулканічні ґрунти, ідеальний клімат.",
    "traditions_label": "Традиції:", "traditions_text": "більшість кави вирощується у тіні природного лісу, без хімії.",
    "regions_title": "Унікальні регіони Ефіопії",
    "yirgacheffe_desc": "— квіти, цитруси, легке тіло",
    "sidamo_desc": "— шоколад, горіхи, баланс",
    "harrar_desc": "— чорниця, вино, спеції",
    "guji_desc": "— полуниця, манго, тропіки",
    "quote2": "\"В Ефіопії кажуть: 'Buna dabo naw' — 'Кава — це наш хліб'.\"",
    "cta_title": "Спробуйте справжню ефіопську каву"
}

ETHIOPIA_RU = {
    "title": "Эфиопия — родина кофе: легенда о пастухе Калди",
    "subtitle": "История открытия кофе более 1000 лет назад",
    "intro": "Каждый раз, когда вы наслаждаетесь чашкой кофе, вы продолжаете традицию из эфиопских гор. Легенда о пастухе Калди — неотъемлемая часть кофейной культуры.",
    "legend_title": "Легенда о пастухе Калди",
    "legend_p1": "В IX веке козопас Калди заметил: его козы, съев красные ягоды с неизвестного куста, стали чрезвычайно энергичными — прыгали и не могли уснуть.",
    "quote1": "\"Козы танцевали в лунном свете. Калди понял — эти ягоды обладают магической силой.\"",
    "legend_p2": "Калди попробовал ягоды сам и ощутил прилив энергии. Он отнёс их в монастырь, где монахи сначала бросили их в огонь. Но невероятный аромат поджаренных зёрен заставил их передумать — так появился первый кофейный напиток.",
    "spread_title": "От Эфиопии к миру",
    "century15": "XV в.", "century15_text": "— кофе попал в Йемен",
    "century16": "XVI в.", "century16_text": "— стал популярным в Османской империи",
    "century17": "XVII в.", "century17_text": "— прибыл в Европу",
    "century18": "XVIII в.", "century18_text": "— распространился на колонии и стал глобальным товаром",
    "special_title": "Почему эфиопский кофе особенный?",
    "diversity_label": "Генетическое разнообразие:", "diversity_text": "более 10 000 сортов арабики — больше, чем во всех других странах.",
    "conditions_label": "Идеальные условия:", "conditions_text": "высота 1500-2200м, вулканические почвы, идеальный климат.",
    "traditions_label": "Традиции:", "traditions_text": "большинство кофе выращивается в тени природного леса, без химии.",
    "regions_title": "Уникальные регионы Эфиопии",
    "yirgacheffe_desc": "— цветы, цитрусы, лёгкое тело",
    "sidamo_desc": "— шоколад, орехи, баланс",
    "harrar_desc": "— черника, вино, специи",
    "guji_desc": "— клубника, манго, тропики",
    "quote2": "\"В Эфиопии говорят: 'Buna dabo naw' — 'Кофе — это наш хлеб'.\"",
    "cta_title": "Попробуйте настоящий эфиопский кофе"
}

ETHIOPIA_EN = {
    "title": "Ethiopia — The Birthplace of Coffee: The Legend of Kaldi",
    "subtitle": "The history of coffee discovery over 1000 years ago",
    "intro": "Every time you enjoy a cup of coffee, you continue a tradition from the Ethiopian mountains. The legend of the shepherd Kaldi is an integral part of coffee culture.",
    "legend_title": "The Legend of Kaldi",
    "legend_p1": "In the 9th century, goatherd Kaldi noticed: his goats, after eating red berries from an unknown bush, became extremely energetic — jumping and unable to sleep.",
    "quote1": "\"The goats danced in the moonlight. Kaldi understood — these berries have magical power.\"",
    "legend_p2": "Kaldi tried the berries himself and felt a surge of energy. He took them to a monastery, where the monks first threw them into the fire. But the incredible aroma of the roasted beans made them reconsider — thus the first coffee drink was born.",
    "spread_title": "From Ethiopia to the World",
    "century15": "15th c.", "century15_text": "— coffee reached Yemen",
    "century16": "16th c.", "century16_text": "— became popular in the Ottoman Empire",
    "century17": "17th c.", "century17_text": "— arrived in Europe",
    "century18": "18th c.", "century18_text": "— spread to colonies and became a global commodity",
    "special_title": "Why is Ethiopian Coffee Special?",
    "diversity_label": "Genetic diversity:", "diversity_text": "over 10,000 Arabica varieties — more than all other countries combined.",
    "conditions_label": "Ideal conditions:", "conditions_text": "altitude 1500-2200m, volcanic soils, perfect climate.",
    "traditions_label": "Traditions:", "traditions_text": "most coffee is grown in the shade of natural forest, without chemicals.",
    "regions_title": "Unique Ethiopian Regions",
    "yirgacheffe_desc": "— flowers, citrus, light body",
    "sidamo_desc": "— chocolate, nuts, balance",
    "harrar_desc": "— blueberry, wine, spices",
    "guji_desc": "— strawberry, mango, tropics",
    "quote2": "\"In Ethiopia they say: 'Buna dabo naw' — 'Coffee is our bread'.\"",
    "cta_title": "Try Real Ethiopian Coffee"
}

def update_locale(lang, translations):
    path = BASE_DIR / "locales" / f"{lang}.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if "articles" not in data:
        data["articles"] = {}
    data["articles"]["ethiopia_origin"] = translations
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Updated {path}")

update_locale("uk", ETHIOPIA_UK)
update_locale("ru", ETHIOPIA_RU)
update_locale("en", ETHIOPIA_EN)
print("Done!")
