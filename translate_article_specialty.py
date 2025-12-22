#!/usr/bin/env python3
"""Add complete article translations to JSON - Part 1: what-is-specialty article"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

ARTICLE_TRANSLATIONS = {
    "articles": {
        # Common article elements
        "back_to_stories": {"uk": "Назад до статей", "ru": "Назад к статьям", "en": "Back to Articles"},
        "min_reading": {"uk": "хвилин читання", "ru": "минут чтения", "en": "min read"},
        "share": {"uk": "Поділитись", "ru": "Поделиться", "en": "Share"},
        "related_articles": {"uk": "Схожі статті", "ru": "Похожие статьи", "en": "Related Articles"},
        
        # WHAT IS SPECIALTY
        "what_is_specialty": {
            "category": {"uk": "Про каву", "ru": "О кофе", "en": "About Coffee"},
            "reading_time": {"uk": "5 хвилин читання", "ru": "5 минут чтения", "en": "5 min read"},
            "title": {"uk": "Що таке Specialty кава і чому вона коштує дорожче", "ru": "Что такое Specialty кофе и почему оно стоит дороже", "en": "What is Specialty Coffee and Why Does It Cost More"},
            "subtitle": {"uk": "Розбираємось, чим відрізняється specialty кава від звичайної, як її оцінюють професіонали та чому вона варта кожної копійки.", "ru": "Разбираемся, чем отличается specialty кофе от обычного, как его оценивают профессионалы и почему оно стоит каждой копейки.", "en": "Understanding what makes specialty coffee different, how professionals grade it, and why it's worth every penny."},
            "intro": {"uk": "Якщо ви коли-небудь замислювались, чому одна пачка кави коштує 100 гривень, а інша — 400, відповідь криється у понятті specialty кави. Це не просто маркетингове слово — за ним стоїть сувора система оцінювання, десятки років досвіду та справжня пристрасть до якості.", "ru": "Если вы когда-нибудь задумывались, почему одна пачка кофе стоит 100 гривен, а другая — 400, ответ кроется в понятии specialty кофе. Это не просто маркетинговое слово — за ним стоит строгая система оценки, десятки лет опыта и настоящая страсть к качеству.", "en": "If you've ever wondered why one bag of coffee costs $5 while another costs $30, the answer lies in the concept of specialty coffee. This isn't just a marketing term — behind it stands a strict grading system, decades of experience, and a true passion for quality."},
            "h2_what_means": {"uk": "Що означає \"Specialty\"?", "ru": "Что означает \"Specialty\"?", "en": "What Does \"Specialty\" Mean?"},
            "p_history": {"uk": "Термін \"specialty coffee\" офіційно з'явився у 1974 році, коли Ерна Кнутсен, одна з піонерок кавової індустрії, вперше використала його для опису кави найвищої якості. З того часу поняття еволюціонувало і сьогодні має чітке визначення.", "ru": "Термин \"specialty coffee\" официально появился в 1974 году, когда Эрна Кнутсен, одна из пионеров кофейной индустрии, впервые использовала его для описания кофе высочайшего качества. С тех пор понятие эволюционировало и сегодня имеет четкое определение.", "en": "The term \"specialty coffee\" officially appeared in 1974 when Erna Knutsen, one of the coffee industry pioneers, first used it to describe the highest quality coffee. Since then, the concept has evolved and now has a clear definition."},
            "p_definition": {"uk": "Specialty кава — це кава, яка отримала оцінку 80 балів або вище за 100-бальною шкалою Specialty Coffee Association (SCA). Для порівняння: звичайна комерційна кава рідко перевищує 70 балів, а все, що нижче 60 — взагалі вважається неякісним.", "ru": "Specialty кофе — это кофе, который получил оценку 80 баллов или выше по 100-балльной шкале Specialty Coffee Association (SCA). Для сравнения: обычный коммерческий кофе редко превышает 70 баллов, а всё, что ниже 60 — вообще считается некачественным.", "en": "Specialty coffee is coffee that has scored 80 points or higher on the Specialty Coffee Association (SCA) 100-point scale. For comparison: regular commercial coffee rarely exceeds 70 points, and anything below 60 is considered low quality."},
            "quote1": {"uk": "\"Specialty кава — це приблизно 3% від усієї кави, що виробляється у світі. Це як порівнювати столове вино з Grand Cru.\"", "ru": "\"Specialty кофе — это примерно 3% от всего кофе, производимого в мире. Это как сравнивать столовое вино с Grand Cru.\"", "en": "\"Specialty coffee represents about 3% of all coffee produced in the world. It's like comparing table wine with Grand Cru.\""},
            "h2_grading": {"uk": "Як оцінюють каву професіонали", "ru": "Как оценивают кофе профессионалы", "en": "How Professionals Grade Coffee"},
            "p_grading_intro": {"uk": "Оцінювання кави — це справжня наука. Сертифіковані Q-грейдери (кавові експерти) аналізують зерно за 11 критеріями:", "ru": "Оценка кофе — это настоящая наука. Сертифицированные Q-грейдеры (кофейные эксперты) анализируют зерно по 11 критериям:", "en": "Coffee grading is a true science. Certified Q-graders (coffee experts) analyze beans using 11 criteria:"},
            "li_aroma": {"uk": "Аромат — запах сухого та змоченого зерна", "ru": "Аромат — запах сухого и смоченного зерна", "en": "Aroma — the smell of dry and wet grounds"},
            "li_flavor": {"uk": "Смак — основний смаковий профіль", "ru": "Вкус — основной вкусовой профиль", "en": "Flavor — the main taste profile"},
            "li_aftertaste": {"uk": "Післясмак — тривалість та якість смаку", "ru": "Послевкусие — длительность и качество вкуса", "en": "Aftertaste — duration and quality of taste"},
            "li_acidity": {"uk": "Кислотність — яскравість та характер", "ru": "Кислотность — яркость и характер", "en": "Acidity — brightness and character"},
            "li_body": {"uk": "Тіло — щільність напою", "ru": "Тело — плотность напитка", "en": "Body — the density of the drink"},
            "li_balance": {"uk": "Баланс — гармонія всіх елементів", "ru": "Баланс — гармония всех элементов", "en": "Balance — harmony of all elements"},
            "li_sweetness": {"uk": "Солодкість — природна солодкість зерна", "ru": "Сладость — естественная сладость зерна", "en": "Sweetness — natural sweetness of the bean"},
            "li_clean_cup": {"uk": "Чистота чашки — відсутність дефектів", "ru": "Чистота чашки — отсутствие дефектов", "en": "Clean cup — absence of defects"},
            "li_uniformity": {"uk": "Однорідність — стабільність смаку", "ru": "Однородность — стабильность вкуса", "en": "Uniformity — consistency of flavor"},
            "li_overall": {"uk": "Загальне враження — суб'єктивна оцінка", "ru": "Общее впечатление — субъективная оценка", "en": "Overall — subjective impression"},
            "li_defects": {"uk": "Дефекти — віднімаються бали за недоліки", "ru": "Дефекты — вычитаются баллы за недостатки", "en": "Defects — points deducted for flaws"},
            "p_grading_note": {"uk": "Кожен критерій оцінюється від 6 до 10 балів. Щоб зерно отримало статус specialty, воно повинно мати не більше 5 дефектів на 350 грамів при візуальному огляді.", "ru": "Каждый критерий оценивается от 6 до 10 баллов. Чтобы зерно получило статус specialty, оно должно иметь не более 5 дефектов на 350 грамм при визуальном осмотре.", "en": "Each criterion is scored from 6 to 10 points. To achieve specialty status, beans must have no more than 5 defects per 350 grams upon visual inspection."},
            "h2_why_expensive": {"uk": "Чому specialty кава дорожча?", "ru": "Почему specialty кофе дороже?", "en": "Why is Specialty Coffee More Expensive?"},
            "p_expensive_intro": {"uk": "Висока ціна specialty кави — це не накрутка маркетологів. За нею стоять реальні витрати на кожному етапі:", "ru": "Высокая цена specialty кофе — это не накрутка маркетологов. За ней стоят реальные затраты на каждом этапе:", "en": "The high price of specialty coffee isn't a marketing markup. Real costs exist at every stage:"},
            "h3_terroir": {"uk": "1. Терруар та клімат", "ru": "1. Терруар и климат", "en": "1. Terroir and Climate"},
            "p_terroir": {"uk": "Найкраща кава росте на висоті 1800-2200 метрів над рівнем моря, в тропічному кліматі з чіткими сезонами. Такі умови є лише в кількох регіонах світу, і Ефіопія — один з них.", "ru": "Лучший кофе растет на высоте 1800-2200 метров над уровнем моря, в тропическом климате с четкими сезонами. Такие условия есть только в нескольких регионах мира, и Эфиопия — один из них.", "en": "The best coffee grows at 1800-2200 meters above sea level, in a tropical climate with distinct seasons. These conditions exist only in a few regions of the world, and Ethiopia is one of them."},
            "h3_harvest": {"uk": "2. Ручний збір", "ru": "2. Ручной сбор", "en": "2. Hand Picking"},
            "p_harvest": {"uk": "На відміну від комерційної кави, яку часто збирають машинами, specialty ягоди збирають вручну, обираючи лише стиглі. Це в 10 разів повільніше, але гарантує якість.", "ru": "В отличие от коммерческого кофе, который часто собирают машинами, specialty ягоды собирают вручную, выбирая только спелые. Это в 10 раз медленнее, но гарантирует качество.", "en": "Unlike commercial coffee that's often machine-harvested, specialty cherries are hand-picked, selecting only ripe ones. It's 10 times slower but guarantees quality."},
            "h3_processing": {"uk": "3. Обробка", "ru": "3. Обработка", "en": "3. Processing"},
            "p_processing": {"uk": "Кожен етап — від ферментації до сушіння — контролюється вручну. Натуральна обробка може тривати до 4 тижнів.", "ru": "Каждый этап — от ферментации до сушки — контролируется вручную. Натуральная обработка может длиться до 4 недель.", "en": "Every step — from fermentation to drying — is manually controlled. Natural processing can take up to 4 weeks."},
            "h3_roasting": {"uk": "4. Свіжа обсмажка", "ru": "4. Свежая обжарка", "en": "4. Fresh Roasting"},
            "p_roasting": {"uk": "Specialty кава має пити оптимальний смак протягом 2-4 тижнів після обсмажки. Ми в EthioDirect смажимо під замовлення.", "ru": "Specialty кофе имеет оптимальный вкус в течение 2-4 недель после обжарки. Мы в EthioDirect обжариваем под заказ.", "en": "Specialty coffee has optimal taste within 2-4 weeks after roasting. At EthioDirect, we roast to order."},
            "h3_fairtrade": {"uk": "5. Fair Trade", "ru": "5. Fair Trade", "en": "5. Fair Trade"},
            "p_fairtrade": {"uk": "Фермери отримують справедливу ціну — часто в 2-3 рази вищу за ринкову.", "ru": "Фермеры получают справедливую цену — часто в 2-3 раза выше рыночной.", "en": "Farmers receive fair prices — often 2-3 times higher than market rates."},
            "h2_recognize": {"uk": "Як розпізнати справжню specialty каву", "ru": "Как распознать настоящий specialty кофе", "en": "How to Recognize Real Specialty Coffee"},
            "p_recognize_intro": {"uk": "Ось на що звертати увагу:", "ru": "Вот на что обращать внимание:", "en": "Here's what to look for:"},
            "li_roast_date": {"uk": "Дата обсмажки — має бути видрукувана", "ru": "Дата обжарки — должна быть напечатана", "en": "Roast date — should be printed"},
            "li_origin": {"uk": "Походження — вказано регіон або ферма", "ru": "Происхождение — указан регион или ферма", "en": "Origin — region or farm specified"},
            "li_sca_score": {"uk": "Оцінка SCA — 80+ балів", "ru": "Оценка SCA — 80+ баллов", "en": "SCA Score — 80+ points"},
            "li_flavor_profile": {"uk": "Смаковий профіль — описані конкретні ноти", "ru": "Вкусовой профиль — описаны конкретные ноты", "en": "Flavor profile — specific notes described"},
            "li_small_batch": {"uk": "Малий обсяг — specialty рідко продається великими упаковками", "ru": "Малый объем — specialty редко продается большими упаковками", "en": "Small batch — specialty rarely sold in large packages"},
            "h2_worth_it": {"uk": "Чи варто переплачувати?", "ru": "Стоит ли переплачивать?", "en": "Is It Worth Paying More?"},
            "p_worth_intro": {"uk": "Якщо для вас кава — це задоволення, ритуал, момент насолоди — однозначно так.", "ru": "Если для вас кофе — это удовольствие, ритуал, момент наслаждения — однозначно да.", "en": "If coffee is a pleasure, ritual, and moment of enjoyment for you — absolutely yes."},
            "cta_title": {"uk": "Готові спробувати справжню specialty каву?", "ru": "Готовы попробовать настоящий specialty кофе?", "en": "Ready to Try Real Specialty Coffee?"},
            "cta_text": {"uk": "Перегляньте нашу колекцію ефіопської кави 85+ SCA", "ru": "Посмотрите нашу коллекцию эфиопского кофе 85+ SCA", "en": "Browse our collection of Ethiopian coffee 85+ SCA"},
            "cta_btn": {"uk": "Перейти до каталогу", "ru": "Перейти в каталог", "en": "Go to Catalog"}
        }
    }
}

def flatten_nested(d, parent_key='', sep='.'):
    """Flatten nested dict with dot notation"""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict) and 'uk' not in v:
            items.extend(flatten_nested(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def update_jsons():
    flat = flatten_nested(ARTICLE_TRANSLATIONS)
    
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Add article translations
        if "articles" not in data:
            data["articles"] = {}
        if "what_is_specialty" not in data["articles"]:
            data["articles"]["what_is_specialty"] = {}
        
        for key, trans in flat.items():
            if isinstance(trans, dict) and lang in trans:
                parts = key.split('.')
                if len(parts) == 2:
                    section, k = parts
                    if section not in data:
                        data[section] = {}
                    data[section][k] = trans[lang]
                elif len(parts) == 3:
                    section, subsection, k = parts
                    if section not in data:
                        data[section] = {}
                    if subsection not in data[section]:
                        data[section][subsection] = {}
                    data[section][subsection][k] = trans[lang]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Updated {lang}.json")

if __name__ == "__main__":
    update_jsons()
    print("Done!")
