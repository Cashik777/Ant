#!/usr/bin/env python3
"""
Complete translation for what-is-specialty.html article
Adds data-i18n to ALL content and creates full translations
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Complete article content translations
ARTICLE_CONTENT = {
    "what_is_specialty": {
        "uk": {
            # Header section
            "title": "Що таке Specialty кава і чому вона коштує дорожче",
            "subtitle": "Розбираємось, чим відрізняється specialty кава від звичайної, як її оцінюють професіонали та чому вона варта кожної копійки.",
            "category": "Про каву",
            "reading_time": "5 хвилин читання",
            
            # Body paragraphs
            "intro": "Якщо ви коли-небудь замислювались, чому одна пачка кави коштує 100 гривень, а інша — 400, відповідь криється у понятті <strong>specialty кави</strong>. Це не просто маркетингове слово — за ним стоїть сувора система оцінювання, десятки років досвіду та справжня пристрасть до якості.",
            
            "h2_what_means": "Що означає \"Specialty\"?",
            "p_history": "Термін \"specialty coffee\" офіційно з'явився у 1974 році, коли Ерна Кнутсен, одна з піонерок кавової індустрії, вперше використала його для опису кави найвищої якості. З того часу поняття еволюціонувало і сьогодні має чітке визначення.",
            "p_definition": "<strong>Specialty кава</strong> — це кава, яка отримала оцінку <strong>80 балів або вище</strong> за 100-бальною шкалою Specialty Coffee Association (SCA). Для порівняння: звичайна комерційна кава рідко перевищує 70 балів, а все, що нижче 60 — взагалі вважається неякісним.",
            "quote1": "\"Specialty кава — це приблизно 3% від усієї кави, що виробляється у світі. Це як порівнювати столове вино з Grand Cru.\"",
            
            "h2_grading": "Як оцінюють каву професіонали",
            "p_grading_intro": "Оцінювання кави — це справжня наука. Сертифіковані Q-грейдери (кавові експерти) аналізують зерно за 11 критеріями:",
            "criteria_aroma": "<strong>Аромат</strong> — запах сухого та змоченого зерна",
            "criteria_flavor": "<strong>Смак</strong> — основний смаковий профіль",
            "criteria_aftertaste": "<strong>Післясмак</strong> — тривалість та якість смаку",
            "criteria_acidity": "<strong>Кислотність</strong> — яскравість та характер",
            "criteria_body": "<strong>Тіло</strong> — щільність напою",
            "criteria_balance": "<strong>Баланс</strong> — гармонія всіх елементів",
            "criteria_sweetness": "<strong>Солодкість</strong> — природна солодкість зерна",
            "criteria_clean_cup": "<strong>Чистота чашки</strong> — відсутність дефектів",
            "criteria_uniformity": "<strong>Однорідність</strong> — стабільність смаку",
            "criteria_overall": "<strong>Загальне враження</strong> — суб'єктивна оцінка",
            "criteria_defects": "<strong>Дефекти</strong> — віднімаються бали за недоліки",
            "p_grading_note": "Кожен критерій оцінюється від 6 до 10 балів. Щоб зерно отримало статус specialty, воно повинно мати <strong>не більше 5 дефектів на 350 грамів</strong> при візуальному огляді.",
            
            "h2_why_expensive": "Чому specialty кава дорожча?",
            "p_expensive_intro": "Висока ціна specialty кави — це не накрутка маркетологів. За нею стоять реальні витрати на кожному етапі:",
            "h3_terroir": "1. Терруар та клімат",
            "p_terroir": "Найкраща кава росте на висоті 1800-2200 метрів над рівнем моря, в тропічному кліматі з чіткими сезонами. Такі умови є лише в кількох регіонах світу, і Ефіопія — один з них.",
            "h3_harvest": "2. Ручний збір",
            "p_harvest": "На відміну від комерційної кави, яку часто збирають машинами, specialty ягоди збирають вручну, обираючи лише стиглі. Це в 10 разів повільніше, але гарантує якість.",
            "h3_processing": "3. Обробка",
            "p_processing": "Кожен етап — від ферментації до сушіння — контролюється вручну. Натуральна обробка (коли ягода сушиться цілком) може тривати до 4 тижнів.",
            "h3_roasting": "4. Свіжа обсмажка",
            "p_roasting": "Specialty кава має пити оптимальний смак протягом 2-4 тижнів після обсмажки. Ми в EthioDirect смажимо під замовлення, щоб ви отримали найсвіжіший продукт.",
            "h3_fairtrade": "5. Fair Trade",
            "p_fairtrade": "Фермери, які виробляють specialty каву, отримують справедливу ціну — часто в 2-3 рази вищу за ринкову. Це дозволяє їм інвестувати у покращення якості.",
            
            "h2_recognize": "Як розпізнати справжню specialty каву",
            "p_recognize_intro": "На жаль, не все, що називається \"premium\" або \"specialty\" на полицях супермаркетів, таким є. Ось на що звертати увагу:",
            "tip_date": "<strong>Дата обсмажки</strong> — має бути видрукувана, не \"придатна до\"",
            "tip_origin": "<strong>Походження</strong> — вказано регіон, а ще краще — ферма",
            "tip_sca": "<strong>Оцінка SCA</strong> — якщо вказано 80+ балів, це хороший знак",
            "tip_profile": "<strong>Смаковий профіль</strong> — описані конкретні ноти (не просто \"ароматна\")",
            "tip_volume": "<strong>Малий обсяг</strong> — specialty рідко продається упаковками по 1 кг",
            
            "h2_worth_it": "Чи варто переплачувати?",
            "p_worth_intro": "Якщо ви п'єте каву заради кофеїну вранці — можливо, ні. Але якщо для вас кава — це задоволення, ритуал, момент насолоди — <strong>однозначно так</strong>.",
            "p_worth_flavors": "Specialty кава відкриє вам світ смаків, про які ви навіть не підозрювали: від квіткових нот жасмину до ягідної солодкості чорниці, від цитрусової свіжості до шоколадної глибини. Це зовсім інший досвід.",
            "quote2": "\"Коли я вперше спробував справжню ефіопську Yirgacheffe, я зрозумів, що до цього пив не каву, а лише гірку рідину з кофеїном.\"",
            "p_conclusion": "Спробуйте хоча б раз — і ви зрозумієте, про що ми говоримо. А наша кава з оцінкою 85+ балів — чудовий старт цієї подорожі.",
            
            # CTA section
            "cta_title": "Готові спробувати справжню specialty каву?",
            "cta_text": "Замовте наш бестселер — Yirgacheffe з нотами квітів та цитрусів",
            "cta_button": "Перейти до каталогу",
            
            # Tags and related
            "tags_label": "Теги:",
            "share_label": "Поділитись:",
            "related_title": "Схожі статті"
        },
        "ru": {
            "title": "Что такое Specialty кофе и почему он дороже",
            "subtitle": "Разбираемся, чем отличается specialty кофе от обычного, как его оценивают профессионалы и почему он стоит каждой копейки.",
            "category": "О кофе",
            "reading_time": "5 минут чтения",
            
            "intro": "Если вы когда-нибудь задумывались, почему одна пачка кофе стоит 100 гривен, а другая — 400, ответ кроется в понятии <strong>specialty кофе</strong>. Это не просто маркетинговое слово — за ним стоит строгая система оценивания, десятки лет опыта и настоящая страсть к качеству.",
            
            "h2_what_means": "Что означает \"Specialty\"?",
            "p_history": "Термин \"specialty coffee\" официально появился в 1974 году, когда Эрна Кнутсен, одна из пионерок кофейной индустрии, впервые использовала его для описания кофе высшего качества. С того времени понятие эволюционировало и сегодня имеет чёткое определение.",
            "p_definition": "<strong>Specialty кофе</strong> — это кофе, получивший оценку <strong>80 баллов или выше</strong> по 100-балльной шкале Specialty Coffee Association (SCA). Для сравнения: обычный коммерческий кофе редко превышает 70 баллов, а всё, что ниже 60 — вообще считается некачественным.",
            "quote1": "\"Specialty кофе — это примерно 3% всего кофе в мире. Это как сравнивать столовое вино с Grand Cru.\"",
            
            "h2_grading": "Как оценивают кофе профессионалы",
            "p_grading_intro": "Оценка кофе — это настоящая наука. Сертифицированные Q-грейдеры (кофейные эксперты) анализируют зерно по 11 критериям:",
            "criteria_aroma": "<strong>Аромат</strong> — запах сухого и смоченного зерна",
            "criteria_flavor": "<strong>Вкус</strong> — основной вкусовой профиль",
            "criteria_aftertaste": "<strong>Послевкусие</strong> — длительность и качество вкуса",
            "criteria_acidity": "<strong>Кислотность</strong> — яркость и характер",
            "criteria_body": "<strong>Тело</strong> — плотность напитка",
            "criteria_balance": "<strong>Баланс</strong> — гармония всех элементов",
            "criteria_sweetness": "<strong>Сладость</strong> — природная сладость зерна",
            "criteria_clean_cup": "<strong>Чистота чашки</strong> — отсутствие дефектов",
            "criteria_uniformity": "<strong>Однородность</strong> — стабильность вкуса",
            "criteria_overall": "<strong>Общее впечатление</strong> — субъективная оценка",
            "criteria_defects": "<strong>Дефекты</strong> — вычитаются баллы за недостатки",
            "p_grading_note": "Каждый критерий оценивается от 6 до 10 баллов. Чтобы зерно получило статус specialty, оно должно иметь <strong>не более 5 дефектов на 350 грамм</strong> при визуальном осмотре.",
            
            "h2_why_expensive": "Почему specialty кофе дороже?",
            "p_expensive_intro": "Высокая цена specialty кофе — это не накрутка маркетологов. За ней стоят реальные затраты на каждом этапе:",
            "h3_terroir": "1. Терруар и климат",
            "p_terroir": "Лучший кофе растёт на высоте 1800-2200 метров над уровнем моря, в тропическом климате с чёткими сезонами. Такие условия есть лишь в нескольких регионах мира, и Эфиопия — один из них.",
            "h3_harvest": "2. Ручной сбор",
            "p_harvest": "В отличие от коммерческого кофе, который часто собирают машинами, specialty ягоды собирают вручную, выбирая только спелые. Это в 10 раз медленнее, но гарантирует качество.",
            "h3_processing": "3. Обработка",
            "p_processing": "Каждый этап — от ферментации до сушки — контролируется вручную. Натуральная обработка (когда ягода сушится целиком) может длиться до 4 недель.",
            "h3_roasting": "4. Свежая обжарка",
            "p_roasting": "Specialty кофе имеет оптимальный вкус в течение 2-4 недель после обжарки. Мы в EthioDirect обжариваем под заказ, чтобы вы получили самый свежий продукт.",
            "h3_fairtrade": "5. Fair Trade",
            "p_fairtrade": "Фермеры, производящие specialty кофе, получают справедливую цену — часто в 2-3 раза выше рыночной. Это позволяет им инвестировать в улучшение качества.",
            
            "h2_recognize": "Как распознать настоящий specialty кофе",
            "p_recognize_intro": "К сожалению, не всё, что называется \"premium\" или \"specialty\" на полках супермаркетов, таковым является. Вот на что обращать внимание:",
            "tip_date": "<strong>Дата обжарки</strong> — должна быть напечатана, не \"годен до\"",
            "tip_origin": "<strong>Происхождение</strong> — указан регион, а ещё лучше — ферма",
            "tip_sca": "<strong>Оценка SCA</strong> — если указано 80+ баллов, это хороший знак",
            "tip_profile": "<strong>Вкусовой профиль</strong> — описаны конкретные ноты (не просто \"ароматный\")",
            "tip_volume": "<strong>Малый объём</strong> — specialty редко продаётся упаковками по 1 кг",
            
            "h2_worth_it": "Стоит ли переплачивать?",
            "p_worth_intro": "Если вы пьёте кофе ради кофеина утром — возможно, нет. Но если для вас кофе — это удовольствие, ритуал, момент наслаждения — <strong>однозначно да</strong>.",
            "p_worth_flavors": "Specialty кофе откроет вам мир вкусов, о которых вы даже не подозревали: от цветочных нот жасмина до ягодной сладости черники, от цитрусовой свежести до шоколадной глубины. Это совсем другой опыт.",
            "quote2": "\"Когда я впервые попробовал настоящий эфиопский Yirgacheffe, я понял, что до этого пил не кофе, а лишь горькую жидкость с кофеином.\"",
            "p_conclusion": "Попробуйте хотя бы раз — и вы поймёте, о чём мы говорим. А наш кофе с оценкой 85+ баллов — отличный старт этого путешествия.",
            
            "cta_title": "Готовы попробовать настоящий specialty кофе?",
            "cta_text": "Закажите наш бестселлер — Yirgacheffe с нотами цветов и цитрусов",
            "cta_button": "Перейти в каталог",
            
            "tags_label": "Теги:",
            "share_label": "Поделиться:",
            "related_title": "Похожие статьи"
        },
        "en": {
            "title": "What is Specialty Coffee and Why Does It Cost More",
            "subtitle": "Understanding how specialty coffee differs from regular coffee, how professionals grade it, and why it's worth every penny.",
            "category": "About Coffee",
            "reading_time": "5 min read",
            
            "intro": "If you've ever wondered why one bag of coffee costs 100 hryvnias while another costs 400, the answer lies in the concept of <strong>specialty coffee</strong>. This isn't just a marketing buzzword — behind it stands a rigorous grading system, decades of expertise, and a genuine passion for quality.",
            
            "h2_what_means": "What Does \"Specialty\" Mean?",
            "p_history": "The term \"specialty coffee\" officially appeared in 1974 when Erna Knutsen, one of the pioneers of the coffee industry, first used it to describe coffee of the highest quality. Since then, the concept has evolved and today has a clear definition.",
            "p_definition": "<strong>Specialty coffee</strong> is coffee that has scored <strong>80 points or higher</strong> on the Specialty Coffee Association (SCA) 100-point scale. For comparison: regular commercial coffee rarely exceeds 70 points, and anything below 60 is considered poor quality.",
            "quote1": "\"Specialty coffee is about 3% of all coffee produced worldwide. It's like comparing table wine to Grand Cru.\"",
            
            "h2_grading": "How Professionals Grade Coffee",
            "p_grading_intro": "Coffee grading is a real science. Certified Q-graders (coffee experts) analyze beans across 11 criteria:",
            "criteria_aroma": "<strong>Aroma</strong> — smell of dry and wet beans",
            "criteria_flavor": "<strong>Flavor</strong> — main taste profile",
            "criteria_aftertaste": "<strong>Aftertaste</strong> — duration and quality of taste",
            "criteria_acidity": "<strong>Acidity</strong> — brightness and character",
            "criteria_body": "<strong>Body</strong> — density of the drink",
            "criteria_balance": "<strong>Balance</strong> — harmony of all elements",
            "criteria_sweetness": "<strong>Sweetness</strong> — natural sweetness of the bean",
            "criteria_clean_cup": "<strong>Clean Cup</strong> — absence of defects",
            "criteria_uniformity": "<strong>Uniformity</strong> — consistency of taste",
            "criteria_overall": "<strong>Overall</strong> — subjective assessment",
            "criteria_defects": "<strong>Defects</strong> — points deducted for flaws",
            "p_grading_note": "Each criterion is scored from 6 to 10 points. For beans to achieve specialty status, they must have <strong>no more than 5 defects per 350 grams</strong> during visual inspection.",
            
            "h2_why_expensive": "Why is Specialty Coffee More Expensive?",
            "p_expensive_intro": "The high price of specialty coffee isn't just marketing markup. Behind it are real costs at every stage:",
            "h3_terroir": "1. Terroir and Climate",
            "p_terroir": "The best coffee grows at 1800-2200 meters above sea level, in tropical climates with distinct seasons. These conditions exist in only a few regions worldwide, and Ethiopia is one of them.",
            "h3_harvest": "2. Hand Picking",
            "p_harvest": "Unlike commercial coffee, which is often machine-harvested, specialty cherries are picked by hand, selecting only ripe ones. This is 10 times slower but guarantees quality.",
            "h3_processing": "3. Processing",
            "p_processing": "Every stage — from fermentation to drying — is controlled manually. Natural processing (when the cherry dries whole) can take up to 4 weeks.",
            "h3_roasting": "4. Fresh Roasting",
            "p_roasting": "Specialty coffee has optimal taste within 2-4 weeks after roasting. At EthioDirect, we roast to order so you receive the freshest product.",
            "h3_fairtrade": "5. Fair Trade",
            "p_fairtrade": "Farmers producing specialty coffee receive fair prices — often 2-3 times higher than market rate. This allows them to invest in quality improvement.",
            
            "h2_recognize": "How to Recognize Real Specialty Coffee",
            "p_recognize_intro": "Unfortunately, not everything labeled \"premium\" or \"specialty\" on supermarket shelves actually is. Here's what to look for:",
            "tip_date": "<strong>Roast Date</strong> — should be printed, not \"best before\"",
            "tip_origin": "<strong>Origin</strong> — region specified, even better — farm name",
            "tip_sca": "<strong>SCA Score</strong> — if 80+ points are indicated, it's a good sign",
            "tip_profile": "<strong>Flavor Profile</strong> — specific notes described (not just \"aromatic\")",
            "tip_volume": "<strong>Small Volume</strong> — specialty is rarely sold in 1kg packages",
            
            "h2_worth_it": "Is It Worth the Extra Cost?",
            "p_worth_intro": "If you drink coffee just for morning caffeine — maybe not. But if coffee for you is pleasure, ritual, a moment of enjoyment — <strong>absolutely yes</strong>.",
            "p_worth_flavors": "Specialty coffee will open a world of flavors you never suspected: from floral jasmine notes to berry sweetness of blueberry, from citrus freshness to chocolate depth. It's an entirely different experience.",
            "quote2": "\"When I first tried real Ethiopian Yirgacheffe, I realized that until then I hadn't been drinking coffee — just bitter caffeinated liquid.\"",
            "p_conclusion": "Try it at least once — and you'll understand what we're talking about. And our 85+ point coffee is a perfect start to this journey.",
            
            "cta_title": "Ready to Try Real Specialty Coffee?",
            "cta_text": "Order our bestseller — Yirgacheffe with floral and citrus notes",
            "cta_button": "Go to Catalog",
            
            "tags_label": "Tags:",
            "share_label": "Share:",
            "related_title": "Related Articles"
        }
    }
}

def update_locales():
    """Add complete article content to locale files"""
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "articles" not in data:
            data["articles"] = {}
        
        # Merge the complete content
        for article_key, translations in ARTICLE_CONTENT.items():
            if article_key not in data["articles"]:
                data["articles"][article_key] = {}
            data["articles"][article_key].update(translations[lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path}")

if __name__ == "__main__":
    print("Adding complete article translations...")
    update_locales()
    print("Done!")
