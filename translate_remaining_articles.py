#!/usr/bin/env python3
"""
Complete translations for remaining articles
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

REMAINING_ARTICLES = {
    "natural_vs_washed": {
        "uk": {
            "title": "Natural vs Washed: як обробка впливає на смак",
            "subtitle": "Різниця між сухою та митою обробкою зерна і чому це важливо для вашої чашки.",
            "category": "Обробка",
            "reading_time": "5 хвилин читання",
            "intro": "Обробка — один з ключових факторів, що визначає смак вашої кави. Розберемось, чим відрізняються два основних методи.",
            "h2_washed": "Мита обробка (Washed)",
            "p_washed": "При митій обробці м'якоть ягоди видаляється відразу після збору. Зерно проходить ферментацію у воді, потім промивається та сушиться. Результат: чистий, яскравий смак з чіткою кислотністю.",
            "h2_natural": "Натуральна обробка (Natural/Dry)",
            "p_natural": "При натуральній обробці ягода сушиться цілою — разом з м'якоттю. Процес триває 2-4 тижні. Результат: насичений, солодкий смак з фруктовими та ягідними нотами.",
            "h2_difference": "Головні відмінності",
            "p_difference": "Мита кава — більш \"чиста\", з чіткими нотами. Натуральна — більш \"дика\", з глибокими фруктовими смаками. Обидва методи мають своїх прихильників.",
            "cta_title": "Порівняйте самі",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Natural vs Washed: как обработка влияет на вкус",
            "subtitle": "Разница между сухой и мытой обработкой зерна и почему это важно для вашей чашки.",
            "category": "Обработка",
            "reading_time": "5 минут чтения",
            "intro": "Обработка — один из ключевых факторов, определяющих вкус вашего кофе. Разберёмся, чем отличаются два основных метода.",
            "h2_washed": "Мытая обработка (Washed)",
            "p_washed": "При мытой обработке мякоть ягоды удаляется сразу после сбора. Зерно проходит ферментацию в воде, затем промывается и сушится. Результат: чистый, яркий вкус с чёткой кислотностью.",
            "h2_natural": "Натуральная обработка (Natural/Dry)",
            "p_natural": "При натуральной обработке ягода сушится целиком — вместе с мякотью. Процесс длится 2-4 недели. Результат: насыщенный, сладкий вкус с фруктовыми и ягодными нотами.",
            "h2_difference": "Главные отличия",
            "p_difference": "Мытый кофе — более \"чистый\", с чёткими нотами. Натуральный — более \"дикий\", с глубокими фруктовыми вкусами. Оба метода имеют своих поклонников.",
            "cta_title": "Сравните сами",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Natural vs Washed: How Processing Affects Taste",
            "subtitle": "The difference between dry and washed processing and why it matters for your cup.",
            "category": "Processing",
            "reading_time": "5 min read",
            "intro": "Processing is one of the key factors determining your coffee's taste. Let's explore how the two main methods differ.",
            "h2_washed": "Washed Processing",
            "p_washed": "In washed processing, the fruit pulp is removed immediately after harvesting. The bean undergoes fermentation in water, then is washed and dried. Result: clean, bright taste with clear acidity.",
            "h2_natural": "Natural Processing (Dry)",
            "p_natural": "In natural processing, the cherry dries whole — with the pulp. The process takes 2-4 weeks. Result: rich, sweet taste with fruity and berry notes.",
            "h2_difference": "Key Differences",
            "p_difference": "Washed coffee is more \"clean\" with clear notes. Natural is more \"wild\" with deep fruity flavors. Both methods have their fans.",
            "cta_title": "Compare for Yourself",
            "cta_button": "To Catalog"
        }
    },
    "water_for_coffee": {
        "uk": {
            "title": "Яка вода потрібна для ідеальної кави?",
            "subtitle": "98% вашої чашки — це вода. Розбираємось, чому вона важлива та яку обрати.",
            "category": "Поради",
            "reading_time": "5 хвилин читання",
            "intro": "Вода — це 98% вашої чашки кави. Навіть найкраще зерно не розкриє свій потенціал, якщо вода неправильна.",
            "h2_why": "Чому вода важлива?",
            "p_why": "Вода — це розчинник, який екстрагує смакові сполуки з кави. Занадто м'яка вода дасть слабку екстракцію, занадто жорстка — надмірну гіркоту.",
            "h2_ideal": "Ідеальна вода для кави",
            "p_ideal": "За рекомендаціями SCA: TDS (загальна мінералізація) 75-250 ppm, pH 6.5-7.5. Найпростіший варіант — фільтрована вода або якісна бутильована.",
            "h2_avoid": "Чого уникати",
            "p_avoid": "Дистильована вода — занадто м'яка. Вода з-під крана (в більшості міст) — містить хлор та занадто жорстка. Мінеральна з високою мінералізацією — перекриє смак кави.",
            "cta_title": "Спробуйте з правильною водою",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Какая вода нужна для идеального кофе?",
            "subtitle": "98% вашей чашки — это вода. Разбираемся, почему она важна и какую выбрать.",
            "category": "Советы",
            "reading_time": "5 минут чтения",
            "intro": "Вода — это 98% вашей чашки кофе. Даже лучшее зерно не раскроет свой потенциал, если вода неправильная.",
            "h2_why": "Почему вода важна?",
            "p_why": "Вода — это растворитель, который экстрагирует вкусовые соединения из кофе. Слишком мягкая вода даст слабую экстракцию, слишком жёсткая — чрезмерную горечь.",
            "h2_ideal": "Идеальная вода для кофе",
            "p_ideal": "По рекомендациям SCA: TDS (общая минерализация) 75-250 ppm, pH 6.5-7.5. Самый простой вариант — фильтрованная вода или качественная бутилированная.",
            "h2_avoid": "Чего избегать",
            "p_avoid": "Дистиллированная вода — слишком мягкая. Вода из-под крана (в большинстве городов) — содержит хлор и слишком жёсткая. Минеральная с высокой минерализацией — перекроет вкус кофе.",
            "cta_title": "Попробуйте с правильной водой",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "What Water Do You Need for Perfect Coffee?",
            "subtitle": "98% of your cup is water. Understanding why it matters and which to choose.",
            "category": "Tips",
            "reading_time": "5 min read",
            "intro": "Water is 98% of your coffee cup. Even the best beans won't reach their potential with the wrong water.",
            "h2_why": "Why Does Water Matter?",
            "p_why": "Water is the solvent that extracts flavor compounds from coffee. Too soft water gives weak extraction, too hard — excessive bitterness.",
            "h2_ideal": "Ideal Water for Coffee",
            "p_ideal": "Per SCA recommendations: TDS (total dissolved solids) 75-250 ppm, pH 6.5-7.5. Simplest option — filtered water or quality bottled water.",
            "h2_avoid": "What to Avoid",
            "p_avoid": "Distilled water — too soft. Tap water (in most cities) — contains chlorine and is too hard. High-mineral water — will overpower coffee taste.",
            "cta_title": "Try with the Right Water",
            "cta_button": "To Catalog"
        }
    },
    "grinder_guide": {
        "uk": {
            "title": "Як обрати кавомолку: повний гід для початківців",
            "subtitle": "Жорнова чи ножова? Ручна чи електрична? Розбираємось у типах кавомолок та їх перевагах.",
            "category": "Обладнання",
            "reading_time": "7 хвилин читання",
            "intro": "Кавомолка — можливо, найважливіша інвестиція для домашнього бариста. Свіжозмелена кава завжди краща за готову молоту.",
            "h2_types": "Типи кавомолок",
            "p_blade": "<strong>Ножові</strong> — найдешевші, але дають нерівномірний помел. Не рекомендуємо для specialty кави.",
            "p_burr": "<strong>Жорнові</strong> — бувають плоскі та конічні. Дають рівномірний помел, необхідний для правильної екстракції.",
            "h2_manual": "Ручні vs Електричні",
            "p_manual": "Ручні — дешевші, тихі, компактні. Мінус: потрібно крутити 1-2 хвилини. Електричні — швидкі та зручні, але дорожчі.",
            "h2_recommend": "Наші рекомендації",
            "p_recommend": "Для початку: ручна Timemore C2 або Hario Skerton. Для еспресо: Baratza Encore або 1Zpresso JX-Pro.",
            "cta_title": "Є запитання щодо вибору?",
            "cta_button": "Зв'яжіться з нами"
        },
        "ru": {
            "title": "Как выбрать кофемолку: полный гид для начинающих",
            "subtitle": "Жерновая или ножевая? Ручная или электрическая? Разбираемся в типах кофемолок и их преимуществах.",
            "category": "Оборудование",
            "reading_time": "7 минут чтения",
            "intro": "Кофемолка — возможно, самая важная инвестиция для домашнего баристы. Свежемолотый кофе всегда лучше готового молотого.",
            "h2_types": "Типы кофемолок",
            "p_blade": "<strong>Ножевые</strong> — самые дешёвые, но дают неравномерный помол. Не рекомендуем для specialty кофе.",
            "p_burr": "<strong>Жерновые</strong> — бывают плоские и конические. Дают равномерный помол, необходимый для правильной экстракции.",
            "h2_manual": "Ручные vs Электрические",
            "p_manual": "Ручные — дешевле, тихие, компактные. Минус: нужно крутить 1-2 минуты. Электрические — быстрые и удобные, но дороже.",
            "h2_recommend": "Наши рекомендации",
            "p_recommend": "Для начала: ручная Timemore C2 или Hario Skerton. Для эспрессо: Baratza Encore или 1Zpresso JX-Pro.",
            "cta_title": "Есть вопросы по выбору?",
            "cta_button": "Свяжитесь с нами"
        },
        "en": {
            "title": "How to Choose a Coffee Grinder: Complete Beginner's Guide",
            "subtitle": "Burr or blade? Manual or electric? Understanding grinder types and their advantages.",
            "category": "Equipment",
            "reading_time": "7 min read",
            "intro": "A grinder is perhaps the most important investment for a home barista. Freshly ground coffee is always better than pre-ground.",
            "h2_types": "Types of Grinders",
            "p_blade": "<strong>Blade grinders</strong> — cheapest, but give uneven grind. Not recommended for specialty coffee.",
            "p_burr": "<strong>Burr grinders</strong> — come in flat and conical. Give even grind needed for proper extraction.",
            "h2_manual": "Manual vs Electric",
            "p_manual": "Manual — cheaper, quiet, compact. Downside: need to crank 1-2 minutes. Electric — fast and convenient, but more expensive.",
            "h2_recommend": "Our Recommendations",
            "p_recommend": "To start: manual Timemore C2 or Hario Skerton. For espresso: Baratza Encore or 1Zpresso JX-Pro.",
            "cta_title": "Questions About Choosing?",
            "cta_button": "Contact Us"
        }
    },
    "aeropress_recipes": {
        "uk": {
            "title": "3 рецепти для Аеропреса від чемпіонів",
            "subtitle": "Перевірені рецепти переможців чемпіонатів з аеропресу для ідеальної чашки вдома.",
            "category": "Рецепти",
            "reading_time": "5 хвилин читання",
            "intro": "Аеропрес — один з найбільш універсальних методів заварювання. Ось три рецепти від переможців світових чемпіонатів.",
            "h2_classic": "Класичний рецепт",
            "p_classic": "15г кави, 200мл води 85°C. Помел — середній. Час: 1:30. Заливаємо, перемішуємо, віджимаємо.",
            "h2_inverted": "Інвертований метод",
            "p_inverted": "Аеропрес перевернутий. 17г кави, 220мл води 92°C. Настоюємо 2 хвилини, перевертаємо, віджимаємо.",
            "h2_champion": "Рецепт чемпіона 2023",
            "p_champion": "12г кави, 200мл води 78°C. Дуже дрібний помел. Час: 2:00. Результат: насичений, солодкий смак.",
            "cta_title": "Замовте каву для аеропресу",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "3 рецепта для Аэропресса от чемпионов",
            "subtitle": "Проверенные рецепты победителей чемпионатов по аэропрессу для идеальной чашки дома.",
            "category": "Рецепты",
            "reading_time": "5 минут чтения",
            "intro": "Аэропресс — один из самых универсальных методов заваривания. Вот три рецепта от победителей мировых чемпионатов.",
            "h2_classic": "Классический рецепт",
            "p_classic": "15г кофе, 200мл воды 85°C. Помол — средний. Время: 1:30. Заливаем, перемешиваем, отжимаем.",
            "h2_inverted": "Инвертированный метод",
            "p_inverted": "Аэропресс перевёрнут. 17г кофе, 220мл воды 92°C. Настаиваем 2 минуты, переворачиваем, отжимаем.",
            "h2_champion": "Рецепт чемпиона 2023",
            "p_champion": "12г кофе, 200мл воды 78°C. Очень мелкий помол. Время: 2:00. Результат: насыщенный, сладкий вкус.",
            "cta_title": "Закажите кофе для аэропресса",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "3 Aeropress Recipes from Champions",
            "subtitle": "Proven recipes from championship winners for the perfect cup at home.",
            "category": "Recipes",
            "reading_time": "5 min read",
            "intro": "Aeropress is one of the most versatile brewing methods. Here are three recipes from world championship winners.",
            "h2_classic": "Classic Recipe",
            "p_classic": "15g coffee, 200ml water 85°C. Medium grind. Time: 1:30. Pour, stir, press.",
            "h2_inverted": "Inverted Method",
            "p_inverted": "Aeropress inverted. 17g coffee, 220ml water 92°C. Steep 2 minutes, flip, press.",
            "h2_champion": "2023 Champion Recipe",
            "p_champion": "12g coffee, 200ml water 78°C. Very fine grind. Time: 2:00. Result: rich, sweet taste.",
            "cta_title": "Order Coffee for Aeropress",
            "cta_button": "To Catalog"
        }
    },
    "cold_brew_recipe": {
        "uk": {
            "title": "Cold Brew вдома: простий рецепт на 5 літрів",
            "subtitle": "Як приготувати освіжаючу каву холодного заварювання без спеціального обладнання.",
            "category": "Рецепти",
            "reading_time": "4 хвилини читання",
            "intro": "Cold brew — ідеальний напій для спекотних днів. Він м'який, солодкий і майже без гіркоти. А головне — його легко готувати вдома.",
            "h2_what": "Що таке Cold Brew?",
            "p_what": "Cold brew — це кава, заварена холодною водою протягом 12-24 годин. На відміну від айс-кофе (гаряча кава з льодом), cold brew ніколи не нагрівається.",
            "h2_recipe": "Рецепт",
            "p_ratio": "Співвідношення: 1:8 (100г кави на 800мл води). Грубий помел, як для френч-преса.",
            "p_steps": "Змішайте каву з холодною водою в банці. Залиште в холодильнику на 12-24 години. Процідіть через фільтр. Концентрат можна розбавляти водою/молоком 1:1.",
            "h2_tips": "Поради",
            "p_tips": "Використовуйте кави з фруктовими нотами — вони краще розкриваються в cold brew. Зберігайте концентрат до 2 тижнів у холодильнику.",
            "cta_title": "Замовте каву для Cold Brew",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Cold Brew дома: простой рецепт на 5 литров",
            "subtitle": "Как приготовить освежающий кофе холодного заваривания без специального оборудования.",
            "category": "Рецепты",
            "reading_time": "4 минуты чтения",
            "intro": "Cold brew — идеальный напиток для жарких дней. Он мягкий, сладкий и почти без горечи. А главное — его легко готовить дома.",
            "h2_what": "Что такое Cold Brew?",
            "p_what": "Cold brew — это кофе, заваренный холодной водой в течение 12-24 часов. В отличие от айс-кофе (горячий кофе со льдом), cold brew никогда не нагревается.",
            "h2_recipe": "Рецепт",
            "p_ratio": "Соотношение: 1:8 (100г кофе на 800мл воды). Грубый помол, как для френч-пресса.",
            "p_steps": "Смешайте кофе с холодной водой в банке. Оставьте в холодильнике на 12-24 часа. Процедите через фильтр. Концентрат можно разбавлять водой/молоком 1:1.",
            "h2_tips": "Советы",
            "p_tips": "Используйте кофе с фруктовыми нотами — они лучше раскрываются в cold brew. Храните концентрат до 2 недель в холодильнике.",
            "cta_title": "Закажите кофе для Cold Brew",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Cold Brew at Home: Simple Recipe for 5 Liters",
            "subtitle": "How to make refreshing cold-brewed coffee without special equipment.",
            "category": "Recipes",
            "reading_time": "4 min read",
            "intro": "Cold brew is the perfect drink for hot days. It's smooth, sweet, and almost bitter-free. Best of all — it's easy to make at home.",
            "h2_what": "What is Cold Brew?",
            "p_what": "Cold brew is coffee brewed with cold water for 12-24 hours. Unlike iced coffee (hot coffee with ice), cold brew is never heated.",
            "h2_recipe": "Recipe",
            "p_ratio": "Ratio: 1:8 (100g coffee to 800ml water). Coarse grind, like for French press.",
            "p_steps": "Mix coffee with cold water in a jar. Leave in fridge for 12-24 hours. Strain through filter. Concentrate can be diluted with water/milk 1:1.",
            "h2_tips": "Tips",
            "p_tips": "Use coffees with fruity notes — they shine in cold brew. Store concentrate up to 2 weeks in fridge.",
            "cta_title": "Order Coffee for Cold Brew",
            "cta_button": "To Catalog"
        }
    },
    "espresso_mistakes": {
        "uk": {
            "title": "7 помилок при приготуванні еспресо вдома",
            "subtitle": "Чому ваш еспресо гіркий або кислий? Розбираємо типові помилки та як їх уникнути.",
            "category": "Поради",
            "reading_time": "6 хвилин читання",
            "intro": "Покупка кавомашини — лише початок шляху до ідеального еспресо. Ось найчастіші помилки, що заважають насолоджуватись каєю.",
            "h2_grind": "1. Неправильний помел",
            "p_grind": "Занадто грубий — рідкий, кислий шот. Занадто дрібний — гіркий, повільний. Експериментуйте!",
            "h2_dose": "2. Неточна доза",
            "p_dose": "Використовуйте ваги! Стандартна доза — 18-20г кави на подвійний шот.",
            "h2_temp": "3. Неправильна температура",
            "p_temp": "Ідеально: 92-96°C. Прогрівайте машину перед першим шотом мінімум 15 хвилин.",
            "h2_fresh": "4. Несвіжа кава",
            "p_fresh": "Еспресо найкращий з кави 7-21 день після обсмажки. Свіжа обсмажка дає занадто багато газу.",
            "h2_tamp": "5. Нерівний темпінг",
            "p_tamp": "Трамбуйте рівно, з тиском ~15 кг. Нерівний темпінг = нерівна екстракція.",
            "h2_clean": "6. Брудна група",
            "p_clean": "Чистіть групу після кожного приготування. Старі олії = гіркий смак.",
            "h2_ratio": "7. Неправильне співвідношення",
            "p_ratio": "Класика: 1:2 (18г кави = 36г напою) за 25-30 секунд.",
            "cta_title": "Замовте каву для еспресо",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "7 ошибок при приготовлении эспрессо дома",
            "subtitle": "Почему ваш эспрессо горький или кислый? Разбираем типичные ошибки и как их избежать.",
            "category": "Советы",
            "reading_time": "6 минут чтения",
            "intro": "Покупка кофемашины — лишь начало пути к идеальному эспрессо. Вот самые частые ошибки, мешающие наслаждаться кофе.",
            "h2_grind": "1. Неправильный помол",
            "p_grind": "Слишком грубый — жидкий, кислый шот. Слишком мелкий — горький, медленный. Экспериментируйте!",
            "h2_dose": "2. Неточная доза",
            "p_dose": "Используйте весы! Стандартная доза — 18-20г кофе на двойной шот.",
            "h2_temp": "3. Неправильная температура",
            "p_temp": "Идеально: 92-96°C. Прогревайте машину перед первым шотом минимум 15 минут.",
            "h2_fresh": "4. Несвежий кофе",
            "p_fresh": "Эспрессо лучший из кофе 7-21 день после обжарки. Свежая обжарка даёт слишком много газа.",
            "h2_tamp": "5. Неровный темпинг",
            "p_tamp": "Трамбуйте ровно, с давлением ~15 кг. Неровный темпинг = неровная экстракция.",
            "h2_clean": "6. Грязная группа",
            "p_clean": "Чистите группу после каждого приготовления. Старые масла = горький вкус.",
            "h2_ratio": "7. Неправильное соотношение",
            "p_ratio": "Классика: 1:2 (18г кофе = 36г напитка) за 25-30 секунд.",
            "cta_title": "Закажите кофе для эспрессо",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "7 Mistakes When Making Espresso at Home",
            "subtitle": "Why is your espresso bitter or sour? Breaking down common mistakes and how to avoid them.",
            "category": "Tips",
            "reading_time": "6 min read",
            "intro": "Buying an espresso machine is just the start of the journey to perfect espresso. Here are the most common mistakes preventing coffee enjoyment.",
            "h2_grind": "1. Wrong Grind",
            "p_grind": "Too coarse — watery, sour shot. Too fine — bitter, slow. Experiment!",
            "h2_dose": "2. Inaccurate Dose",
            "p_dose": "Use scales! Standard dose — 18-20g coffee for a double shot.",
            "h2_temp": "3. Wrong Temperature",
            "p_temp": "Ideal: 92-96°C. Warm up the machine at least 15 minutes before first shot.",
            "h2_fresh": "4. Stale Coffee",
            "p_fresh": "Espresso is best from coffee 7-21 days after roasting. Fresh roast produces too much gas.",
            "h2_tamp": "5. Uneven Tamping",
            "p_tamp": "Tamp evenly with ~15 kg pressure. Uneven tamping = uneven extraction.",
            "h2_clean": "6. Dirty Group Head",
            "p_clean": "Clean the group after every shot. Old oils = bitter taste.",
            "h2_ratio": "7. Wrong Ratio",
            "p_ratio": "Classic: 1:2 (18g coffee = 36g drink) in 25-30 seconds.",
            "cta_title": "Order Coffee for Espresso",
            "cta_button": "To Catalog"
        }
    },
    "turka_recipe": {
        "uk": {
            "title": "Кава по-турецьки: секрети ідеального джезве",
            "subtitle": "Традиційний метод приготування, який зберігся крізь століття. Покроковий рецепт.",
            "category": "Рецепти",
            "reading_time": "5 хвилин читання",
            "intro": "Кава в турці (джезві) — найстаріший спосіб приготування, якому понад 500 років. Ось як приготувати її правильно.",
            "h2_equipment": "Що потрібно",
            "p_equipment": "Турка (мідна краща), дуже дрібно змелена кава, холодна вода, пісок або повільний вогонь.",
            "h2_recipe": "Класичний рецепт",
            "p_step1": "7г кави на 60мл холодної води. Помел — в пил, дрібніше ніж для еспресо.",
            "p_step2": "Змішайте каву з холодною водою в турці. За бажанням додайте цукор.",
            "p_step3": "Повільно нагрівайте на найменшому вогні. Ніколи не кип'ятіть!",
            "p_step4": "Коли піна почне підніматись — зніміть з вогню. Повторіть 2-3 рази для насиченості.",
            "h2_tips": "Секрети",
            "p_tips": "Не перемішуйте після початку нагрівання. Використовуйте темну обсмажку. Подавайте зі склянкою холодної води.",
            "cta_title": "Замовте каву для турки",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Кофе по-турецки: секреты идеальной джезвы",
            "subtitle": "Традиционный метод приготовления, сохранившийся сквозь века. Пошаговый рецепт.",
            "category": "Рецепты",
            "reading_time": "5 минут чтения",
            "intro": "Кофе в турке (джезве) — старейший способ приготовления, которому более 500 лет. Вот как приготовить его правильно.",
            "h2_equipment": "Что нужно",
            "p_equipment": "Турка (медная лучше), очень мелко молотый кофе, холодная вода, песок или медленный огонь.",
            "h2_recipe": "Классический рецепт",
            "p_step1": "7г кофе на 60мл холодной воды. Помол — в пыль, мельче чем для эспрессо.",
            "p_step2": "Смешайте кофе с холодной водой в турке. По желанию добавьте сахар.",
            "p_step3": "Медленно нагревайте на самом маленьком огне. Никогда не кипятите!",
            "p_step4": "Когда пена начнёт подниматься — снимите с огня. Повторите 2-3 раза для насыщенности.",
            "h2_tips": "Секреты",
            "p_tips": "Не перемешивайте после начала нагрева. Используйте тёмную обжарку. Подавайте со стаканом холодной воды.",
            "cta_title": "Закажите кофе для турки",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Turkish Coffee: Secrets of Perfect Cezve",
            "subtitle": "A traditional brewing method preserved through centuries. Step-by-step recipe.",
            "category": "Recipes",
            "reading_time": "5 min read",
            "intro": "Coffee in a cezve (ibrik) is the oldest brewing method, over 500 years old. Here's how to make it properly.",
            "h2_equipment": "What You Need",
            "p_equipment": "Cezve (copper is best), very finely ground coffee, cold water, sand or low heat.",
            "h2_recipe": "Classic Recipe",
            "p_step1": "7g coffee per 60ml cold water. Grind — powder-fine, finer than espresso.",
            "p_step2": "Mix coffee with cold water in cezve. Add sugar if desired.",
            "p_step3": "Heat slowly on lowest flame. Never boil!",
            "p_step4": "When foam starts to rise — remove from heat. Repeat 2-3 times for richness.",
            "h2_tips": "Secrets",
            "p_tips": "Don't stir after heating starts. Use dark roast. Serve with a glass of cold water.",
            "cta_title": "Order Coffee for Turkish Brew",
            "cta_button": "To Catalog"
        }
    },
    "caffeine_myths": {
        "uk": {
            "title": "5 міфів про кофеїн, у які всі вірять",
            "subtitle": "Чи правда, що темна обсмажка містить більше кофеїну? Розвінчуємо популярні міфи.",
            "category": "Поради",
            "reading_time": "4 хвилини читання",
            "intro": "Навколо кофеїну існує багато міфів. Давайте розберемось, що з цього правда, а що — ні.",
            "h2_myth1": "Міф 1: Темна обсмажка міцніша",
            "p_myth1": "НЕПРАВДА. Кількість кофеїну майже однакова в усіх обсмажках. \"Міцність\" — це смак, не кофеїн.",
            "h2_myth2": "Міф 2: Еспресо містить найбільше кофеїну",
            "p_myth2": "ЧАСТКОВО ПРАВДА. На мілілітр — так. Але в чашці фільтр-кави загалом більше кофеїну, бо об'єм більший.",
            "h2_myth3": "Міф 3: Кофеїн зневоднює",
            "p_myth3": "НЕПРАВДА. Кава на 98% складається з води і є помірним діуретиком. Вона не зневоднює при нормальному споживанні.",
            "h2_myth4": "Міф 4: Кофеїн викликає звикання",
            "p_myth4": "ЧАСТКОВО ПРАВДА. Виникає толерантність, але це не залежність у медичному сенсі. Відміна — легкий дискомфорт 1-2 дні.",
            "h2_myth5": "Міф 5: Кава без кофеїну повністю без кофеїну",
            "p_myth5": "НЕПРАВДА. Декаф містить 2-15 мг кофеїну на чашку (звичайна — 80-100 мг).",
            "cta_title": "Хочете знати більше?",
            "cta_button": "Читати інші статті"
        },
        "ru": {
            "title": "5 мифов о кофеине, в которые все верят",
            "subtitle": "Правда ли, что тёмная обжарка содержит больше кофеина? Развенчиваем популярные мифы.",
            "category": "Советы",
            "reading_time": "4 минуты чтения",
            "intro": "Вокруг кофеина существует много мифов. Давайте разберёмся, что из этого правда, а что — нет.",
            "h2_myth1": "Миф 1: Тёмная обжарка крепче",
            "p_myth1": "НЕПРАВДА. Количество кофеина почти одинаково во всех обжарках. \"Крепость\" — это вкус, не кофеин.",
            "h2_myth2": "Миф 2: Эспрессо содержит больше всего кофеина",
            "p_myth2": "ЧАСТИЧНО ПРАВДА. На миллилитр — да. Но в чашке фильтр-кофе в целом больше кофеина, потому что объём больше.",
            "h2_myth3": "Миф 3: Кофеин обезвоживает",
            "p_myth3": "НЕПРАВДА. Кофе на 98% состоит из воды и является умеренным диуретиком. Он не обезвоживает при нормальном потреблении.",
            "h2_myth4": "Миф 4: Кофеин вызывает привыкание",
            "p_myth4": "ЧАСТИЧНО ПРАВДА. Возникает толерантность, но это не зависимость в медицинском смысле. Отмена — лёгкий дискомфорт 1-2 дня.",
            "h2_myth5": "Миф 5: Кофе без кофеина полностью без кофеина",
            "p_myth5": "НЕПРАВДА. Декаф содержит 2-15 мг кофеина на чашку (обычный — 80-100 мг).",
            "cta_title": "Хотите узнать больше?",
            "cta_button": "Читать другие статьи"
        },
        "en": {
            "title": "5 Caffeine Myths Everyone Believes",
            "subtitle": "Is it true that dark roast has more caffeine? Debunking popular myths.",
            "category": "Tips",
            "reading_time": "4 min read",
            "intro": "There are many myths around caffeine. Let's figure out what's true and what's not.",
            "h2_myth1": "Myth 1: Dark Roast is Stronger",
            "p_myth1": "FALSE. Caffeine content is almost the same across all roasts. \"Strength\" refers to flavor, not caffeine.",
            "h2_myth2": "Myth 2: Espresso Has the Most Caffeine",
            "p_myth2": "PARTLY TRUE. Per milliliter — yes. But a cup of filter coffee has more caffeine overall due to larger volume.",
            "h2_myth3": "Myth 3: Caffeine Dehydrates",
            "p_myth3": "FALSE. Coffee is 98% water and is a mild diuretic. It doesn't dehydrate with normal consumption.",
            "h2_myth4": "Myth 4: Caffeine is Addictive",
            "p_myth4": "PARTLY TRUE. Tolerance develops, but it's not addiction in the medical sense. Withdrawal is mild discomfort for 1-2 days.",
            "h2_myth5": "Myth 5: Decaf is Completely Caffeine-Free",
            "p_myth5": "FALSE. Decaf contains 2-15 mg caffeine per cup (regular has 80-100 mg).",
            "cta_title": "Want to Know More?",
            "cta_button": "Read Other Articles"
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
        
        for key, translations in REMAINING_ARTICLES.items():
            if key not in data["articles"]:
                data["articles"][key] = {}
            data["articles"][key].update(translations[lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path} with {len(REMAINING_ARTICLES)} articles")

if __name__ == "__main__":
    print("Adding complete article translations...")
    update_locales()
    print("Done!")
