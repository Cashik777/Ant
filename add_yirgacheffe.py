#!/usr/bin/env python3
"""Add yirgacheffe article translations to locale files"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

YIRGACHEFFE_UK = {
    "title": "Йіргачеффе: перлина ефіопської кави",
    "subtitle": "Чому цей регіон виробляє одну з найдорожчих кав у світі",
    "intro": "Якщо specialty кава — це найкраща кава у світі, то Yirgacheffe — це \"best of the best\". Цей маленький регіон на півдні Ефіопії виробляє каву, яка регулярно отримує 90+ балів від найвимогливіших експертів.",
    "location_title": "Де знаходиться Йіргачеффе",
    "location_text": "Yirgacheffe — це маленьке містечко і навколишній регіон у зоні Gedeo, що в регіоні Sidamo (SNNPR) південної Ефіопії. Висота — 1700-2200 метрів над рівнем моря, що створює ідеальні умови для повільного дозрівання ягід.",
    "taste_title": "🌸 Смаковий профіль Yirgacheffe",
    "aroma_label": "Аромат:",
    "aroma_value": "жасмин, бергамот, квіткові ноти",
    "taste_label": "Смак:",
    "taste_value": "цитрус (лимон, апельсин), чай, мед",
    "acidity_label": "Кислотність:",
    "acidity_value": "яскрава, соковита (як цитрусовий сік)",
    "body_label": "Тіло:",
    "body_value": "легке, шовковисте, чайне",
    "aftertaste_label": "Післясмак:",
    "aftertaste_value": "тривалий, солодкий, квітковий",
    "unique_title": "Чому Йіргачеффе унікальна?",
    "terroir_title": "Терруар",
    "terroir_text": "Вулканічні ґрунти багаті мінералами, рівномірний клімат з сезонами дощів, висока висота — все це створює унікальний \"терруар\", подібний до відомих винних регіонів.",
    "genetics_title": "Генетика",
    "genetics_text": "Тут росте унікальний підвид арабіки — Ethiopian Heirloom (ефіопський реліктовий). Це не культивований сорт, а дикі різновиди, що збереглися тисячоліттями.",
    "processing_title": "Обробка",
    "processing_text": "Більшість кави Yirgacheffe обробляється митим способом (washed), що підкреслює її чистоту та квіткові ноти. Натурально оброблена трапляється рідше, але має ще інтенсивніший ягідний смак.",
    "quote": "\"Yirgacheffe — це не просто кава. Це парфуми у чашці. Закрий очі — і ти в квітковому саду.\"",
    "brew_title": "Як готувати Yirgacheffe",
    "roast_label": "Обсмажка:",
    "roast_value": "тільки світла або дуже легка середня",
    "method_label": "Спосіб:",
    "method_value": "фільтр (V60, Chemex), аеропрес",
    "not_rec_label": "НЕ рекомендуємо:",
    "not_rec_value": "турку або еспресо — затьмарить ніжні ноти",
    "water_label": "Вода:",
    "water_value": "94-96°C, м'яка, фільтрована",
    "our_title": "Наша Yirgacheffe",
    "our_text": "Ми працюємо напряму з кооперативом у регіоні Kochere (одним з найкращих мікрорегіонів Yirgacheffe). Наша кава має оцінку 88 балів SCA та яскравий профіль: жасмин, бергамот, лимонна цедра.",
    "cta_title": "Спробуйте нашу Yirgacheffe",
    "cta_text": "Квіткова, цитрусова, неймовірно ароматна"
}

YIRGACHEFFE_RU = {
    "title": "Йиргачеффе: жемчужина эфиопского кофе",
    "subtitle": "Почему этот регион производит один из самых дорогих сортов кофе в мире",
    "intro": "Если specialty кофе — это лучший кофе в мире, то Yirgacheffe — это \"best of the best\". Этот маленький регион на юге Эфиопии производит кофе, который регулярно получает 90+ баллов от самых требовательных экспертов.",
    "location_title": "Где находится Йиргачеффе",
    "location_text": "Yirgacheffe — это маленький городок и окружающий регион в зоне Gedeo, что в регионе Sidamo (SNNPR) южной Эфиопии. Высота — 1700-2200 метров над уровнем моря, что создаёт идеальные условия для медленного созревания ягод.",
    "taste_title": "🌸 Вкусовой профиль Yirgacheffe",
    "aroma_label": "Аромат:",
    "aroma_value": "жасмин, бергамот, цветочные ноты",
    "taste_label": "Вкус:",
    "taste_value": "цитрус (лимон, апельсин), чай, мёд",
    "acidity_label": "Кислотность:",
    "acidity_value": "яркая, сочная (как цитрусовый сок)",
    "body_label": "Тело:",
    "body_value": "лёгкое, шелковистое, чайное",
    "aftertaste_label": "Послевкусие:",
    "aftertaste_value": "продолжительное, сладкое, цветочное",
    "unique_title": "Почему Йиргачеффе уникальна?",
    "terroir_title": "Терруар",
    "terroir_text": "Вулканические почвы богаты минералами, равномерный климат с сезонами дождей, большая высота — всё это создаёт уникальный \"терруар\", подобный известным винным регионам.",
    "genetics_title": "Генетика",
    "genetics_text": "Здесь растёт уникальный подвид арабики — Ethiopian Heirloom (эфиопский реликтовый). Это не культивированный сорт, а дикие разновидности, сохранившиеся тысячелетиями.",
    "processing_title": "Обработка",
    "processing_text": "Большинство кофе Yirgacheffe обрабатывается мытым способом (washed), что подчёркивает его чистоту и цветочные ноты. Натурально обработанный встречается реже, но имеет ещё более интенсивный ягодный вкус.",
    "quote": "\"Yirgacheffe — это не просто кофе. Это духи в чашке. Закрой глаза — и ты в цветочном саду.\"",
    "brew_title": "Как готовить Yirgacheffe",
    "roast_label": "Обжарка:",
    "roast_value": "только светлая или очень лёгкая средняя",
    "method_label": "Способ:",
    "method_value": "фильтр (V60, Chemex), аэропресс",
    "not_rec_label": "НЕ рекомендуем:",
    "not_rec_value": "турку или эспрессо — затмит нежные ноты",
    "water_label": "Вода:",
    "water_value": "94-96°C, мягкая, фильтрованная",
    "our_title": "Наша Yirgacheffe",
    "our_text": "Мы работаем напрямую с кооперативом в регионе Kochere (одном из лучших микрорегионов Yirgacheffe). Наш кофе имеет оценку 88 баллов SCA и яркий профиль: жасмин, бергамот, лимонная цедра.",
    "cta_title": "Попробуйте нашу Yirgacheffe",
    "cta_text": "Цветочная, цитрусовая, невероятно ароматная"
}

YIRGACHEFFE_EN = {
    "title": "Yirgacheffe: The Pearl of Ethiopian Coffee",
    "subtitle": "Why this region produces one of the most expensive coffees in the world",
    "intro": "If specialty coffee is the best coffee in the world, then Yirgacheffe is the \"best of the best\". This small region in southern Ethiopia produces coffee that regularly scores 90+ points from the most demanding experts.",
    "location_title": "Where is Yirgacheffe Located",
    "location_text": "Yirgacheffe is a small town and surrounding region in the Gedeo zone, in the Sidamo region (SNNPR) of southern Ethiopia. Altitude — 1700-2200 meters above sea level, creating ideal conditions for slow berry ripening.",
    "taste_title": "🌸 Yirgacheffe Flavor Profile",
    "aroma_label": "Aroma:",
    "aroma_value": "jasmine, bergamot, floral notes",
    "taste_label": "Taste:",
    "taste_value": "citrus (lemon, orange), tea, honey",
    "acidity_label": "Acidity:",
    "acidity_value": "bright, juicy (like citrus juice)",
    "body_label": "Body:",
    "body_value": "light, silky, tea-like",
    "aftertaste_label": "Aftertaste:",
    "aftertaste_value": "lingering, sweet, floral",
    "unique_title": "Why is Yirgacheffe Unique?",
    "terroir_title": "Terroir",
    "terroir_text": "Volcanic soils rich in minerals, even climate with rainy seasons, high altitude — all this creates a unique \"terroir\", similar to famous wine regions.",
    "genetics_title": "Genetics",
    "genetics_text": "A unique subspecies of Arabica grows here — Ethiopian Heirloom. This is not a cultivated variety, but wild varieties that have been preserved for millennia.",
    "processing_title": "Processing",
    "processing_text": "Most Yirgacheffe coffee is processed using the washed method, which emphasizes its clarity and floral notes. Naturally processed is rarer but has an even more intense berry flavor.",
    "quote": "\"Yirgacheffe is not just coffee. It's perfume in a cup. Close your eyes — and you're in a flower garden.\"",
    "brew_title": "How to Brew Yirgacheffe",
    "roast_label": "Roast:",
    "roast_value": "only light or very light medium",
    "method_label": "Method:",
    "method_value": "filter (V60, Chemex), Aeropress",
    "not_rec_label": "NOT recommended:",
    "not_rec_value": "Turkish or espresso — will overshadow delicate notes",
    "water_label": "Water:",
    "water_value": "94-96°C, soft, filtered",
    "our_title": "Our Yirgacheffe",
    "our_text": "We work directly with a cooperative in the Kochere region (one of the best micro-regions of Yirgacheffe). Our coffee has a score of 88 SCA points and a bright profile: jasmine, bergamot, lemon zest.",
    "cta_title": "Try Our Yirgacheffe",
    "cta_text": "Floral, citrusy, incredibly aromatic"
}

def update_locale(lang, translations):
    path = BASE_DIR / "locales" / f"{lang}.json"
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if "articles" not in data:
        data["articles"] = {}
    data["articles"]["yirgacheffe"] = translations
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Updated {path}")

update_locale("uk", YIRGACHEFFE_UK)
update_locale("ru", YIRGACHEFFE_RU)
update_locale("en", YIRGACHEFFE_EN)
print("Done!")
