#!/usr/bin/env python3
"""
Add translations for all list items in what-is-specialty.html
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# List item translations for what-is-specialty article
LIST_TRANSLATIONS = {
    "what_is_specialty": {
        "uk": {
            # Grading criteria (ol list)
            "li_aroma": "<strong>Аромат</strong> — запах сухого та змоченого зерна",
            "li_flavor": "<strong>Смак</strong> — основний смаковий профіль",
            "li_aftertaste": "<strong>Післясмак</strong> — тривалість та якість смаку",
            "li_acidity": "<strong>Кислотність</strong> — яскравість та характер",
            "li_body": "<strong>Тіло</strong> — щільність напою",
            "li_balance": "<strong>Баланс</strong> — гармонія всіх елементів",
            "li_sweetness": "<strong>Солодкість</strong> — природна солодкість зерна",
            "li_clean_cup": "<strong>Чистота чашки</strong> — відсутність дефектів",
            "li_uniformity": "<strong>Однорідність</strong> — стабільність смаку",
            "li_overall": "<strong>Загальне враження</strong> — суб'єктивна оцінка",
            "li_defects": "<strong>Дефекти</strong> — віднімаються бали за недоліки",
            
            # Recognition tips (ul list)
            "li_roast_date": "<strong>Дата обсмажки</strong> — має бути видрукувана, не \"придатна до\"",
            "li_origin": "<strong>Походження</strong> — вказано регіон, а ще краще — ферма",
            "li_sca_score": "<strong>Оцінка SCA</strong> — якщо вказано 80+ балів, це хороший знак",
            "li_flavor_profile": "<strong>Смаковий профіль</strong> — описані конкретні ноти (не просто \"ароматна\")",
            "li_small_batch": "<strong>Малий обсяг</strong> — specialty рідко продається упаковками по 1 кг"
        },
        "ru": {
            "li_aroma": "<strong>Аромат</strong> — запах сухого и смоченного зерна",
            "li_flavor": "<strong>Вкус</strong> — основной вкусовой профиль",
            "li_aftertaste": "<strong>Послевкусие</strong> — длительность и качество вкуса",
            "li_acidity": "<strong>Кислотность</strong> — яркость и характер",
            "li_body": "<strong>Тело</strong> — плотность напитка",
            "li_balance": "<strong>Баланс</strong> — гармония всех элементов",
            "li_sweetness": "<strong>Сладость</strong> — природная сладость зерна",
            "li_clean_cup": "<strong>Чистота чашки</strong> — отсутствие дефектов",
            "li_uniformity": "<strong>Однородность</strong> — стабильность вкуса",
            "li_overall": "<strong>Общее впечатление</strong> — субъективная оценка",
            "li_defects": "<strong>Дефекты</strong> — вычитаются баллы за недостатки",
            
            "li_roast_date": "<strong>Дата обжарки</strong> — должна быть напечатана, не \"годен до\"",
            "li_origin": "<strong>Происхождение</strong> — указан регион, а ещё лучше — ферма",
            "li_sca_score": "<strong>Оценка SCA</strong> — если указано 80+ баллов, это хороший знак",
            "li_flavor_profile": "<strong>Вкусовой профиль</strong> — описаны конкретные ноты (не просто \"ароматный\")",
            "li_small_batch": "<strong>Малый объём</strong> — specialty редко продаётся упаковками по 1 кг"
        },
        "en": {
            "li_aroma": "<strong>Aroma</strong> — smell of dry and wet beans",
            "li_flavor": "<strong>Flavor</strong> — main taste profile",
            "li_aftertaste": "<strong>Aftertaste</strong> — duration and quality of taste",
            "li_acidity": "<strong>Acidity</strong> — brightness and character",
            "li_body": "<strong>Body</strong> — density of the drink",
            "li_balance": "<strong>Balance</strong> — harmony of all elements",
            "li_sweetness": "<strong>Sweetness</strong> — natural sweetness of the bean",
            "li_clean_cup": "<strong>Clean Cup</strong> — absence of defects",
            "li_uniformity": "<strong>Uniformity</strong> — consistency of taste",
            "li_overall": "<strong>Overall</strong> — subjective assessment",
            "li_defects": "<strong>Defects</strong> — points deducted for flaws",
            
            "li_roast_date": "<strong>Roast Date</strong> — should be printed, not \"best before\"",
            "li_origin": "<strong>Origin</strong> — region specified, even better — farm name",
            "li_sca_score": "<strong>SCA Score</strong> — if 80+ points indicated, it's a good sign",
            "li_flavor_profile": "<strong>Flavor Profile</strong> — specific notes described (not just \"aromatic\")",
            "li_small_batch": "<strong>Small Batch</strong> — specialty rarely sold in 1kg packages"
        }
    }
}

def update_html():
    """Add data-i18n to list items in what-is-specialty.html"""
    filepath = BASE_DIR / "articles" / "what-is-specialty.html"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    key = "articles.what_is_specialty"
    
    # Replace criteria list items (ol)
    replacements = [
        (r'<li><strong>Аромат</strong>', f'<li data-i18n="{key}.li_aroma"><strong>Аромат</strong>'),
        (r'<li><strong>Смак</strong>', f'<li data-i18n="{key}.li_flavor"><strong>Смак</strong>'),
        (r'<li><strong>Післясмак</strong>', f'<li data-i18n="{key}.li_aftertaste"><strong>Післясмак</strong>'),
        (r'<li><strong>Кислотність</strong>', f'<li data-i18n="{key}.li_acidity"><strong>Кислотність</strong>'),
        (r'<li><strong>Тіло</strong>', f'<li data-i18n="{key}.li_body"><strong>Тіло</strong>'),
        (r'<li><strong>Баланс</strong>', f'<li data-i18n="{key}.li_balance"><strong>Баланс</strong>'),
        (r'<li><strong>Солодкість</strong>', f'<li data-i18n="{key}.li_sweetness"><strong>Солодкість</strong>'),
        (r'<li><strong>Чистота чашки</strong>', f'<li data-i18n="{key}.li_clean_cup"><strong>Чистота чашки</strong>'),
        (r'<li><strong>Однорідність</strong>', f'<li data-i18n="{key}.li_uniformity"><strong>Однорідність</strong>'),
        (r'<li><strong>Загальне враження</strong>', f'<li data-i18n="{key}.li_overall"><strong>Загальне враження</strong>'),
        (r'<li><strong>Дефекти</strong>', f'<li data-i18n="{key}.li_defects"><strong>Дефекти</strong>'),
        
        # Recognition tips (ul)
        (r'<li><strong>Дата обсмажки</strong>', f'<li data-i18n="{key}.li_roast_date"><strong>Дата обсмажки</strong>'),
        (r'<li><strong>Походження</strong>', f'<li data-i18n="{key}.li_origin"><strong>Походження</strong>'),
        (r'<li><strong>Оцінка SCA</strong>', f'<li data-i18n="{key}.li_sca_score"><strong>Оцінка SCA</strong>'),
        (r'<li><strong>Смаковий профіль</strong>', f'<li data-i18n="{key}.li_flavor_profile"><strong>Смаковий профіль</strong>'),
        (r'<li><strong>Малий обсяг</strong>', f'<li data-i18n="{key}.li_small_batch"><strong>Малий обсяг</strong>'),
    ]
    
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath}")

def update_locales():
    """Add list translations to locale files"""
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "articles" not in data:
            data["articles"] = {}
        
        for article_key, translations in LIST_TRANSLATIONS.items():
            if article_key not in data["articles"]:
                data["articles"][article_key] = {}
            data["articles"][article_key].update(translations[lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path}")

if __name__ == "__main__":
    print("Adding list item translations...")
    update_html()
    update_locales()
    print("Done!")
