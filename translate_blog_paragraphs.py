#!/usr/bin/env python3
"""
Add data-i18n to paragraphs in all blog posts and add translations
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Blog paragraph translations (intro and key paragraphs for each blog)
BLOG_PARAGRAPHS = {
    "arabica_vs_robusta": {
        "uk": {
            "intro": "\"100% Arabica\" — ви бачили це на кожній другій пачці кави. Але що це насправді означає? І чому Robusta має таку погану репутацію? Розбираємось у двох основних видах кави детально.",
            "p1": "Arabica — капризна красуня. Їй потрібні особливі умови вирощування і ретельний догляд.",
            "p2": "Arabica славиться складністю смаку з фруктовими, квітковими та солодкими нотами.",
            "p3": "Robusta — це стійка рослина, яка витримує складніші умови і дає більший урожай.",
            "p4": "Якісна Robusta має місце в кавовому світі і може бути дуже смачною.",
            "p5": "Проблема не в Robusta як такій, а в тому, що її часто використовують низької якості — для здешевлення сумішей."
        },
        "ru": {
            "intro": "\"100% Arabica\" — вы видели это на каждой второй пачке кофе. Но что это на самом деле означает? И почему Robusta имеет такую плохую репутацию? Разбираемся в двух основных видах кофе детально.",
            "p1": "Arabica — капризная красавица. Ей нужны особые условия выращивания и тщательный уход.",
            "p2": "Arabica славится сложностью вкуса с фруктовыми, цветочными и сладкими нотами.",
            "p3": "Robusta — это стойкое растение, которое выдерживает более сложные условия и даёт больший урожай.",
            "p4": "Качественная Robusta имеет место в кофейном мире и может быть очень вкусной.",
            "p5": "Проблема не в Robusta как таковой, а в том, что её часто используют низкого качества — для удешевления смесей."
        },
        "en": {
            "intro": "\"100% Arabica\" — you've seen this on every other coffee pack. But what does it really mean? And why does Robusta have such a bad reputation? Let's explore the two main coffee types in detail.",
            "p1": "Arabica is a demanding beauty. It needs special growing conditions and careful attention.",
            "p2": "Arabica is famous for its complex flavor with fruity, floral, and sweet notes.",
            "p3": "Robusta is a hardy plant that withstands tougher conditions and yields more coffee.",
            "p4": "Quality Robusta has its place in the coffee world and can be very tasty.",
            "p5": "The problem isn't Robusta itself, but that low-quality Robusta is often used to cheapen blends."
        }
    },
    "bean_to_cup": {
        "uk": {
            "intro": "Кожна чашка кави — це результат подорожі, яка починається в далеких тропічних країнах. Дізнайтесь про всі етапи цього захопливого шляху.",
            "p1": "Кава росте лише в \"кавовому поясі\" — регіоні між тропіками Рака і Козерога.",
            "p2": "Збирання врожаю — кропітка робота, особливо для specialty кави, яку збирають вручну.",
            "p3": "Після збору ягоди обробляють — митим або натуральним способом.",
            "p4": "Обсмажка — момент, коли зелене зерно перетворюється на ароматну каву."
        },
        "ru": {
            "intro": "Каждая чашка кофе — это результат путешествия, которое начинается в далёких тропических странах. Узнайте обо всех этапах этого захватывающего пути.",
            "p1": "Кофе растёт только в \"кофейном поясе\" — регионе между тропиками Рака и Козерога.",
            "p2": "Сбор урожая — кропотливая работа, особенно для specialty кофе, который собирают вручную.",
            "p3": "После сбора ягоды обрабатывают — мытым или натуральным способом.",
            "p4": "Обжарка — момент, когда зелёное зерно превращается в ароматный кофе."
        },
        "en": {
            "intro": "Each cup of coffee is the result of a journey that begins in distant tropical countries. Learn about all the stages of this fascinating path.",
            "p1": "Coffee grows only in the \"coffee belt\" — the region between the Tropics of Cancer and Capricorn.",
            "p2": "Harvesting is meticulous work, especially for specialty coffee picked by hand.",
            "p3": "After harvesting, the cherries are processed — either washed or naturally.",
            "p4": "Roasting is the moment when green beans transform into aromatic coffee."
        }
    },
    "brewing_methods": {
        "uk": {
            "intro": "Існує безліч способів приготування кави, і кожен з них розкриває різні аспекти смаку. Розберемо всі популярні методи.",
            "p1": "Методи занурення (френч-прес, cold brew) дають насичений, повнотілий смак.",
            "p2": "Крапельні методи (V60, Калита, Кемекс) створюють чистий, яскравий смак.",
            "p3": "Методи під тиском (еспресо, мока) дають концентрований, інтенсивний напій.",
            "p4": "Вибір методу залежить від ваших уподобань та часу, який ви готові витратити."
        },
        "ru": {
            "intro": "Существует множество способов приготовления кофе, и каждый из них раскрывает разные аспекты вкуса. Разберём все популярные методы.",
            "p1": "Методы погружения (френч-пресс, cold brew) дают насыщенный, полнотелый вкус.",
            "p2": "Капельные методы (V60, Калита, Кемекс) создают чистый, яркий вкус.",
            "p3": "Методы под давлением (эспрессо, мока) дают концентрированный, интенсивный напиток.",
            "p4": "Выбор метода зависит от ваших предпочтений и времени, которое вы готовы потратить."
        },
        "en": {
            "intro": "There are countless ways to brew coffee, and each reveals different aspects of flavor. Let's break down all popular methods.",
            "p1": "Immersion methods (French press, cold brew) give a rich, full-bodied taste.",
            "p2": "Drip methods (V60, Kalita, Chemex) create a clean, bright taste.",
            "p3": "Pressure methods (espresso, moka) produce a concentrated, intense drink.",
            "p4": "The choice of method depends on your preferences and time you're willing to spend."
        }
    },
    "coffee_processing": {
        "uk": {
            "intro": "Обробка — один з найважливіших етапів, який визначає кінцевий смак кави. Розберемо три основні методи.",
            "p1": "При натуральній обробці ягода сушиться цілою. Це дає солодкий, фруктовий смак.",
            "p2": "Мита обробка передбачає видалення м'якоті перед сушінням. Результат — чистий, яскравий смак.",
            "p3": "Медова обробка — це золота середина між двома методами."
        },
        "ru": {
            "intro": "Обработка — один из важнейших этапов, определяющих конечный вкус кофе. Разберём три основных метода.",
            "p1": "При натуральной обработке ягода сушится целиком. Это даёт сладкий, фруктовый вкус.",
            "p2": "Мытая обработка предполагает удаление мякоти перед сушкой. Результат — чистый, яркий вкус.",
            "p3": "Медовая обработка — это золотая середина между двумя методами."
        },
        "en": {
            "intro": "Processing is one of the most important stages that determines the final taste of coffee. Let's break down three main methods.",
            "p1": "In natural processing, the cherry dries whole. This gives a sweet, fruity taste.",
            "p2": "Washed processing removes the pulp before drying. Result — a clean, bright taste.",
            "p3": "Honey processing is a golden mean between the two methods."
        }
    },
    "coffee_seasonality": {
        "uk": {
            "intro": "Кава — сезонний продукт, як фрукти чи овочі. Кожен регіон має свій сезон збору врожаю.",
            "p1": "Ефіопія: листопад-лютий. Найкраща свіжа кава доступна з лютого по травень.",
            "p2": "Колумбія має два збори на рік: жовтень-лютий та квітень-червень.",
            "p3": "Бразилія: травень-вересень. Найбільший виробник кави у світі."
        },
        "ru": {
            "intro": "Кофе — сезонный продукт, как фрукты или овощи. У каждого региона свой сезон сбора урожая.",
            "p1": "Эфиопия: ноябрь-февраль. Лучший свежий кофе доступен с февраля по май.",
            "p2": "Колумбия имеет два сбора в год: октябрь-февраль и апрель-июнь.",
            "p3": "Бразилия: май-сентябрь. Крупнейший производитель кофе в мире."
        },
        "en": {
            "intro": "Coffee is a seasonal product, like fruits or vegetables. Each region has its own harvest season.",
            "p1": "Ethiopia: November-February. Best fresh coffee available from February to May.",
            "p2": "Colombia has two harvests per year: October-February and April-June.",
            "p3": "Brazil: May-September. The world's largest coffee producer."
        }
    },
    "coffee_storage_blog": {
        "uk": {
            "intro": "Правильне зберігання — ключ до збереження смаку і аромату кави. Ось що потрібно знати.",
            "p1": "П'ять головних ворогів кави: кисень, волога, тепло, світло та сторонні запахи.",
            "p2": "Ідеальний контейнер — непрозорий, герметичний, з клапаном для виходу газів.",
            "p3": "Мелена кава зберігається до 2 тижнів, зерно — до 4 тижнів після обсмажки."
        },
        "ru": {
            "intro": "Правильное хранение — ключ к сохранению вкуса и аромата кофе. Вот что нужно знать.",
            "p1": "Пять главных врагов кофе: кислород, влага, тепло, свет и посторонние запахи.",
            "p2": "Идеальный контейнер — непрозрачный, герметичный, с клапаном для выхода газов.",
            "p3": "Молотый кофе хранится до 2 недель, зерно — до 4 недель после обжарки."
        },
        "en": {
            "intro": "Proper storage is key to preserving coffee taste and aroma. Here's what you need to know.",
            "p1": "Five main enemies of coffee: oxygen, moisture, heat, light, and foreign odors.",
            "p2": "The ideal container — opaque, airtight, with a one-way valve for gas release.",
            "p3": "Ground coffee keeps up to 2 weeks, beans — up to 4 weeks after roasting."
        }
    },
    "cold_brew_guide": {
        "uk": {
            "intro": "Cold brew — ідеальний напій для спекотних днів. Він м'який, солодкий і майже без гіркоти.",
            "p1": "Cold brew — це кава, заварена холодною водою протягом 12-24 годин.",
            "p2": "На відміну від айс-кофе, cold brew ніколи не нагрівається, що дає м'якший смак.",
            "p3": "Співвідношення для cold brew: 1:8 (кава до води). Помел — грубий, як для френч-преса."
        },
        "ru": {
            "intro": "Cold brew — идеальный напиток для жарких дней. Он мягкий, сладкий и почти без горечи.",
            "p1": "Cold brew — это кофе, заваренный холодной водой в течение 12-24 часов.",
            "p2": "В отличие от айс-кофе, cold brew никогда не нагревается, что даёт более мягкий вкус.",
            "p3": "Соотношение для cold brew: 1:8 (кофе к воде). Помол — грубый, как для френч-пресса."
        },
        "en": {
            "intro": "Cold brew is the perfect drink for hot days. It's smooth, sweet, and almost bitter-free.",
            "p1": "Cold brew is coffee brewed with cold water for 12-24 hours.",
            "p2": "Unlike iced coffee, cold brew is never heated, giving a smoother taste.",
            "p3": "Ratio for cold brew: 1:8 (coffee to water). Grind — coarse, like for French press."
        }
    },
    "espresso_guide": {
        "uk": {
            "intro": "Еспресо — основа більшості кавових напоїв. Ось як приготувати його вдома як професіонал.",
            "p1": "Для еспресо потрібна якісна машина, хороша кавомолка та свіжа кава.",
            "p2": "Стандартний рецепт: 18-20г кави, 36-40г напою за 25-30 секунд.",
            "p3": "Якщо шот кислий — помел занадто грубий. Гіркий — занадто дрібний."
        },
        "ru": {
            "intro": "Эспрессо — основа большинства кофейных напитков. Вот как приготовить его дома как профессионал.",
            "p1": "Для эспрессо нужна качественная машина, хорошая кофемолка и свежий кофе.",
            "p2": "Стандартный рецепт: 18-20г кофе, 36-40г напитка за 25-30 секунд.",
            "p3": "Если шот кислый — помол слишком грубый. Горький — слишком мелкий."
        },
        "en": {
            "intro": "Espresso is the foundation of most coffee drinks. Here's how to make it at home like a pro.",
            "p1": "For espresso you need a quality machine, good grinder, and fresh coffee.",
            "p2": "Standard recipe: 18-20g coffee, 36-40g drink in 25-30 seconds.",
            "p3": "If shot is sour — grind is too coarse. Bitter — too fine."
        }
    },
    "ethiopia_origins": {
        "uk": {
            "intro": "Ефіопія — батьківщина кави і досі виробляє одну з найкращих кав у світі. Дізнайтесь про її легендарні регіони.",
            "p1": "Yirgacheffe — найвідоміший регіон, славиться квітковим, цитрусовим смаком.",
            "p2": "Sidamo — більший регіон з різноманітними профілями, від ягідних до шоколадних.",
            "p3": "Guji — новий зірковий регіон з яскравими фруктовими нотами.",
            "p4": "Harrar — відомий натуральною обробкою та ягідними, винними нотами."
        },
        "ru": {
            "intro": "Эфиопия — родина кофе и до сих пор производит один из лучших сортов кофе в мире. Узнайте о её легендарных регионах.",
            "p1": "Yirgacheffe — самый известный регион, славится цветочным, цитрусовым вкусом.",
            "p2": "Sidamo — больший регион с разнообразными профилями, от ягодных до шоколадных.",
            "p3": "Guji — новый звёздный регион с яркими фруктовыми нотами.",
            "p4": "Harrar — известен натуральной обработкой и ягодными, винными нотами."
        },
        "en": {
            "intro": "Ethiopia is the birthplace of coffee and still produces some of the world's best. Learn about its legendary regions.",
            "p1": "Yirgacheffe — the most famous region, known for floral, citrus taste.",
            "p2": "Sidamo — a larger region with diverse profiles, from berry to chocolate.",
            "p3": "Guji — a rising star region with bright fruity notes.",
            "p4": "Harrar — known for natural processing and berry, wine notes."
        }
    },
    "french_press_guide": {
        "uk": {
            "intro": "Френч-прес — найпростіший спосіб приготувати смачну каву вдома. Ось покроковий рецепт.",
            "p1": "Вам потрібно: френч-прес, 30г кави грубого помелу, 500мл води 94°C.",
            "p2": "Засипте каву, залийте воду, зачекайте 4 хвилини, повільно опустіть поршень.",
            "p3": "Відразу перелийте каву в чашки — інакше вона продовжить екстрагуватись і стане гіркою."
        },
        "ru": {
            "intro": "Френч-пресс — самый простой способ приготовить вкусный кофе дома. Вот пошаговый рецепт.",
            "p1": "Вам нужно: френч-пресс, 30г кофе грубого помола, 500мл воды 94°C.",
            "p2": "Засыпьте кофе, залейте воду, подождите 4 минуты, медленно опустите поршень.",
            "p3": "Сразу перелейте кофе в чашки — иначе он продолжит экстрагироваться и станет горьким."
        },
        "en": {
            "intro": "French press is the simplest way to make delicious coffee at home. Here's a step-by-step recipe.",
            "p1": "You need: French press, 30g coarse ground coffee, 500ml water at 94°C.",
            "p2": "Add coffee, pour water, wait 4 minutes, slowly press the plunger.",
            "p3": "Pour immediately into cups — otherwise it will keep extracting and become bitter."
        }
    },
    "sca_grading": {
        "uk": {
            "intro": "SCA (Specialty Coffee Association) створила стандартизовану систему оцінки якості кави. Ось як вона працює.",
            "p1": "Каву оцінюють за 100-бальною шкалою. Specialty статус отримують зерна з оцінкою 80+.",
            "p2": "Оцінюють 11 критеріїв: аромат, смак, післясмак, кислотність, тіло, баланс, солодкість та інші.",
            "p3": "Каппінг — це професійний процес дегустації, де оцінюють кожен аспект смаку."
        },
        "ru": {
            "intro": "SCA (Specialty Coffee Association) создала стандартизированную систему оценки качества кофе. Вот как она работает.",
            "p1": "Кофе оценивают по 100-балльной шкале. Статус specialty получают зёрна с оценкой 80+.",
            "p2": "Оценивают 11 критериев: аромат, вкус, послевкусие, кислотность, тело, баланс, сладость и другие.",
            "p3": "Каппинг — это профессиональный процесс дегустации, где оценивают каждый аспект вкуса."
        },
        "en": {
            "intro": "SCA (Specialty Coffee Association) created a standardized coffee quality grading system. Here's how it works.",
            "p1": "Coffee is graded on a 100-point scale. Beans scoring 80+ receive specialty status.",
            "p2": "11 criteria are evaluated: aroma, flavor, aftertaste, acidity, body, balance, sweetness, and more.",
            "p3": "Cupping is the professional tasting process where each flavor aspect is evaluated."
        }
    },
    "specialty_coffee": {
        "uk": {
            "intro": "Specialty кава — це не маркетингове слово, а чітко визначений термін з конкретними критеріями.",
            "p1": "Specialty — це кава з оцінкою SCA 80 балів або вище. Це приблизно 3% всієї кави у світі.",
            "p2": "Різниця з комерційною кавою — в якості зерна, свіжості обсмажки та прозорості походження.",
            "p3": "Specialty коштує дорожче, бо вимагає ручного збору, ретельної обробки та свіжої обсмажки."
        },
        "ru": {
            "intro": "Specialty кофе — это не маркетинговое слово, а чётко определённый термин с конкретными критериями.",
            "p1": "Specialty — это кофе с оценкой SCA 80 баллов или выше. Это примерно 3% всего кофе в мире.",
            "p2": "Разница с коммерческим кофе — в качестве зерна, свежести обжарки и прозрачности происхождения.",
            "p3": "Specialty стоит дороже, потому что требует ручного сбора, тщательной обработки и свежей обжарки."
        },
        "en": {
            "intro": "Specialty coffee isn't a marketing term — it's a clearly defined concept with specific criteria.",
            "p1": "Specialty is coffee with an SCA score of 80 points or higher. That's about 3% of all coffee worldwide.",
            "p2": "The difference from commercial coffee is in bean quality, roast freshness, and origin transparency.",
            "p3": "Specialty costs more because it requires hand-picking, careful processing, and fresh roasting."
        }
    },
    "turka_guide": {
        "uk": {
            "intro": "Кава в турці (джезві) — найстаріший метод приготування кави, якому понад 500 років.",
            "p1": "Турка має бути мідною з товстим дном для рівномірного нагрівання.",
            "p2": "Помел — найдрібніший, як пудра. Пропорція: 7г кави на 60мл холодної води.",
            "p3": "Нагрівайте повільно, ніколи не кип'ятіть. Коли піна почне підніматись — знімайте з вогню."
        },
        "ru": {
            "intro": "Кофе в турке (джезве) — старейший метод приготовления кофе, которому более 500 лет.",
            "p1": "Турка должна быть медной с толстым дном для равномерного нагрева.",
            "p2": "Помол — самый мелкий, как пудра. Пропорция: 7г кофе на 60мл холодной воды.",
            "p3": "Нагревайте медленно, никогда не кипятите. Когда пена начнёт подниматься — снимайте с огня."
        },
        "en": {
            "intro": "Turkish coffee (cezve) is the oldest brewing method, over 500 years old.",
            "p1": "The cezve should be copper with a thick bottom for even heating.",
            "p2": "Grind — finest possible, like powder. Ratio: 7g coffee per 60ml cold water.",
            "p3": "Heat slowly, never boil. When foam starts to rise — remove from heat."
        }
    },
    "v60_guide": {
        "uk": {
            "intro": "V60 — улюблений метод бариста по всьому світу. Він дає чистий, яскравий смак і дозволяє контролювати кожен аспект заварювання.",
            "p1": "Вам потрібно: V60, паперові фільтри, гусячок, ваги, 15г кави, 250мл води 94°C.",
            "p2": "Преінфузія: залийте 30мл води на каву і зачекайте 30-45 секунд.",
            "p3": "Продовжуйте заливати воду по колу, кругами від центру до країв. Загальний час: 2:30-3:00."
        },
        "ru": {
            "intro": "V60 — любимый метод баристов по всему миру. Он даёт чистый, яркий вкус и позволяет контролировать каждый аспект заваривания.",
            "p1": "Вам нужно: V60, бумажные фильтры, гусака, весы, 15г кофе, 250мл воды 94°C.",
            "p2": "Преинфузия: залейте 30мл воды на кофе и подождите 30-45 секунд.",
            "p3": "Продолжайте заливать воду кругами от центра к краям. Общее время: 2:30-3:00."
        },
        "en": {
            "intro": "V60 is a favorite method of baristas worldwide. It gives a clean, bright taste and lets you control every aspect of brewing.",
            "p1": "You need: V60, paper filters, gooseneck kettle, scale, 15g coffee, 250ml water at 94°C.",
            "p2": "Pre-infusion: pour 30ml water over coffee and wait 30-45 seconds.",
            "p3": "Continue pouring water in circles from center to edges. Total time: 2:30-3:00."
        }
    },
    "yirgacheffe_region": {
        "uk": {
            "intro": "Yirgacheffe — легендарний регіон Ефіопії, відомий своєю квітковою та цитрусовою кавою найвищої якості.",
            "p1": "Регіон розташований на висоті 1700-2200 метрів у зоні Gedeo на півдні Ефіопії.",
            "p2": "Смаковий профіль: яскраві квіткові ноти (жасмин, бергамот), цитрусова кислотність, чайне тіло.",
            "p3": "Мита обробка дає чистий, яскравий смак. Натуральна — більш солодкий, ягідний.",
            "p4": "Yirgacheffe вважається одним з найкращих терруарів у світі для вирощування кави."
        },
        "ru": {
            "intro": "Yirgacheffe — легендарный регион Эфиопии, известный своим цветочным и цитрусовым кофе высшего качества.",
            "p1": "Регион расположен на высоте 1700-2200 метров в зоне Gedeo на юге Эфиопии.",
            "p2": "Вкусовой профиль: яркие цветочные ноты (жасмин, бергамот), цитрусовая кислотность, чайное тело.",
            "p3": "Мытая обработка даёт чистый, яркий вкус. Натуральная — более сладкий, ягодный.",
            "p4": "Yirgacheffe считается одним из лучших терруаров в мире для выращивания кофе."
        },
        "en": {
            "intro": "Yirgacheffe is a legendary Ethiopian region known for its floral and citrusy coffee of the highest quality.",
            "p1": "The region is located at 1700-2200 meters in the Gedeo zone of southern Ethiopia.",
            "p2": "Flavor profile: bright floral notes (jasmine, bergamot), citrus acidity, tea-like body.",
            "p3": "Washed processing gives clean, bright taste. Natural — sweeter, more berry-like.",
            "p4": "Yirgacheffe is considered one of the world's best terroirs for growing coffee."
        }
    }
}

def update_locales():
    """Add paragraph translations to locale files"""
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "blog" not in data:
            data["blog"] = {}
        
        for blog_key, translations in BLOG_PARAGRAPHS.items():
            if blog_key not in data["blog"]:
                data["blog"][blog_key] = {}
            data["blog"][blog_key].update(translations[lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path} with {len(BLOG_PARAGRAPHS)} blog paragraphs")

if __name__ == "__main__":
    print("Adding blog paragraph translations...")
    update_locales()
    print("Done!")
