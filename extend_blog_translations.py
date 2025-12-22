#!/usr/bin/env python3
"""
Add extended paragraph translations for all blogs p1-p5
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Extended paragraph translations for all blogs
EXTENDED_PARAGRAPHS = {
    "arabica_vs_robusta": {
        "uk": {
            "p1": "\"100% Arabica\" — ви бачили це на кожній другій пачці кави. Але що це насправді означає?",
            "p2": "Arabica — капризна красуня. Їй потрібні особливі умови.",
            "p3": "Arabica славиться складністю смаку з фруктовими нотами.",
            "p4": "Robusta — це стійка рослина, яка витримує складніші умови.",
            "p5": "Якісна Robusta має місце в кавовому світі."
        },
        "ru": {
            "p1": "\"100% Arabica\" — вы видели это на каждой второй пачке кофе. Но что это означает?",
            "p2": "Arabica — капризная красавица. Ей нужны особые условия.",
            "p3": "Arabica славится сложностью вкуса с фруктовыми нотами.",
            "p4": "Robusta — это стойкое растение, которое выдерживает сложные условия.",
            "p5": "Качественная Robusta имеет место в кофейном мире."
        },
        "en": {
            "p1": "\"100% Arabica\" — you've seen this on every other coffee pack. But what does it mean?",
            "p2": "Arabica is a demanding beauty. It needs special conditions.",
            "p3": "Arabica is famous for its complex flavor with fruity notes.",
            "p4": "Robusta is a hardy plant that withstands tougher conditions.",
            "p5": "Quality Robusta has its place in the coffee world."
        }
    },
    "bean_to_cup": {
        "uk": {
            "p1": "Кожна чашка specialty кави проходить довгий шлях від плантації до вашої кухні.",
            "p2": "Все починається з кавового дерева. В Ефіопії кава росте на висоті 1500-2200м.",
            "p3": "Критичні фактори: висота, тінь, ґрунт, догляд.",
            "p4": "Ручний збір лише стиглих червоних ягід.",
            "p5": "Ягоди обробляють митим або натуральним методом."
        },
        "ru": {
            "p1": "Каждая чашка specialty кофе проходит долгий путь от плантации до вашей кухни.",
            "p2": "Всё начинается с кофейного дерева. В Эфиопии кофе растёт на высоте 1500-2200м.",
            "p3": "Критические факторы: высота, тень, почва, уход.",
            "p4": "Ручной сбор только спелых красных ягод.",
            "p5": "Ягоды обрабатывают мытым или натуральным методом."
        },
        "en": {
            "p1": "Each cup of specialty coffee travels a long path from plantation to your kitchen.",
            "p2": "It all starts with the coffee tree. In Ethiopia, coffee grows at 1500-2200m altitude.",
            "p3": "Critical factors: altitude, shade, soil, care.",
            "p4": "Hand-picking only ripe red cherries.",
            "p5": "Cherries are processed using washed or natural methods."
        }
    },
    "brewing_methods": {
        "uk": {
            "p1": "Спосіб заварювання впливає на смак так само сильно, як і сорт кави.",
            "p2": "Кава занурюється у воду, і всі речовини екстрагуються.",
            "p3": "Вода проходить через каву під дією гравітації.",
            "p4": "Під тиском екстракція відбувається швидко.",
            "p5": "Кава і вода варяться разом."
        },
        "ru": {
            "p1": "Способ заваривания влияет на вкус так же сильно, как и сорт кофе.",
            "p2": "Кофе погружается в воду, и все вещества экстрагируются.",
            "p3": "Вода проходит через кофе под действием гравитации.",
            "p4": "Под давлением экстракция происходит быстро.",
            "p5": "Кофе и вода варятся вместе."
        },
        "en": {
            "p1": "The brewing method affects taste just as much as the coffee variety.",
            "p2": "Coffee is immersed in water, and all substances extract.",
            "p3": "Water passes through coffee by gravity.",
            "p4": "Under pressure, extraction happens quickly.",
            "p5": "Coffee and water are boiled together."
        }
    },
    "coffee_processing": {
        "uk": {
            "p1": "Після збору ягоди проходять обробку — один з найважливіших етапів.",
            "p2": "При натуральному методі ягода сушиться цілою.",
            "p3": "Мита обробка передбачає видалення м'якоті.",
            "p4": "Медова обробка — золота середина.",
            "p5": "Кожен метод дає унікальний смаковий профіль."
        },
        "ru": {
            "p1": "После сбора ягоды проходят обработку — один из важнейших этапов.",
            "p2": "При натуральном методе ягода сушится целиком.",
            "p3": "Мытая обработка предполагает удаление мякоти.",
            "p4": "Медовая обработка — золотая середина.",
            "p5": "Каждый метод даёт уникальный вкусовой профиль."
        },
        "en": {
            "p1": "After harvest, cherries undergo processing — one of the most important stages.",
            "p2": "In natural processing, the cherry dries whole.",
            "p3": "Washed processing removes the pulp.",
            "p4": "Honey processing is the golden mean.",
            "p5": "Each method produces a unique flavor profile."
        }
    },
    "coffee_seasonality": {
        "uk": {
            "p1": "Кава — сезонний продукт, як виноград чи яблука.",
            "p2": "Ефіопія: листопад-лютий. Найкраща свіжа кава — з лютого.",
            "p3": "Колумбія має два збори на рік.",
            "p4": "Бразилія: травень-вересень.",
            "p5": "Свіжа кава — це макс 4 тижні після обсмажки."
        },
        "ru": {
            "p1": "Кофе — сезонный продукт, как виноград или яблоки.",
            "p2": "Эфиопия: ноябрь-февраль. Лучший свежий кофе — с февраля.",
            "p3": "Колумбия имеет два сбора в год.",
            "p4": "Бразилия: май-сентябрь.",
            "p5": "Свежий кофе — это макс 4 недели после обжарки."
        },
        "en": {
            "p1": "Coffee is a seasonal product, like grapes or apples.",
            "p2": "Ethiopia: November-February. Best fresh coffee from February.",
            "p3": "Colombia has two harvests per year.",
            "p4": "Brazil: May-September.",
            "p5": "Fresh coffee is max 4 weeks after roasting."
        }
    },
    "coffee_storage_blog": {
        "uk": {
            "p1": "Правильне зберігання — ключ до збереження смаку.",
            "p2": "П'ять головних ворогів: кисень, волога, тепло, світло, запахи.",
            "p3": "Ідеальний контейнер — герметичний, непрозорий.",
            "p4": "Мелена кава зберігається до 2 тижнів.",
            "p5": "Ніколи не зберігайте каву в холодильнику."
        },
        "ru": {
            "p1": "Правильное хранение — ключ к сохранению вкуса.",
            "p2": "Пять главных врагов: кислород, влага, тепло, свет, запахи.",
            "p3": "Идеальный контейнер — герметичный, непрозрачный.",
            "p4": "Молотый кофе хранится до 2 недель.",
            "p5": "Никогда не храните кофе в холодильнике."
        },
        "en": {
            "p1": "Proper storage is key to preserving taste.",
            "p2": "Five main enemies: oxygen, moisture, heat, light, odors.",
            "p3": "The ideal container is airtight, opaque.",
            "p4": "Ground coffee keeps up to 2 weeks.",
            "p5": "Never store coffee in the refrigerator."
        }
    },
    "cold_brew_guide": {
        "uk": {
            "p1": "Cold brew — кава, заварена холодною водою.",
            "p2": "М'який, солодкий смак без гіркоти.",
            "p3": "Співвідношення 1:8, час 12-24 години.",
            "p4": "Можна зберігати в холодильнику до 2 тижнів.",
            "p5": "Подавайте з льодом або розбавте водою."
        },
        "ru": {
            "p1": "Cold brew — кофе, заваренный холодной водой.",
            "p2": "Мягкий, сладкий вкус без горечи.",
            "p3": "Соотношение 1:8, время 12-24 часа.",
            "p4": "Можно хранить в холодильнике до 2 недель.",
            "p5": "Подавайте со льдом или разбавьте водой."
        },
        "en": {
            "p1": "Cold brew is coffee brewed with cold water.",
            "p2": "Smooth, sweet taste without bitterness.",
            "p3": "Ratio 1:8, time 12-24 hours.",
            "p4": "Can be stored in fridge for up to 2 weeks.",
            "p5": "Serve over ice or dilute with water."
        }
    },
    "espresso_guide": {
        "uk": {
            "p1": "Еспресо — основа більшості кавових напоїв.",
            "p2": "Потрібні: машина, кавомолка, свіжа кава.",
            "p3": "18-20г кави, 36-40г напою за 25-30 сек.",
            "p4": "Кислий шот — грубий помел. Гіркий — дрібний.",
            "p5": "Практикуйтесь кожного дня!"
        },
        "ru": {
            "p1": "Эспрессо — основа большинства кофейных напитков.",
            "p2": "Нужны: машина, кофемолка, свежий кофе.",
            "p3": "18-20г кофе, 36-40г напитка за 25-30 сек.",
            "p4": "Кислый шот — грубый помол. Горький — мелкий.",
            "p5": "Практикуйтесь каждый день!"
        },
        "en": {
            "p1": "Espresso is the foundation of most coffee drinks.",
            "p2": "You need: machine, grinder, fresh coffee.",
            "p3": "18-20g coffee, 36-40g drink in 25-30 sec.",
            "p4": "Sour shot — coarse grind. Bitter — fine.",
            "p5": "Practice every day!"
        }
    },
    "ethiopia_origins": {
        "uk": {
            "p1": "Ефіопія — батьківщина кави.",
            "p2": "Yirgacheffe — найвідоміший регіон.",
            "p3": "Sidamo — більший регіон з різноманітними профілями.",
            "p4": "Guji — новий зірковий регіон.",
            "p5": "Harrar — відомий натуральною обробкою."
        },
        "ru": {
            "p1": "Эфиопия — родина кофе.",
            "p2": "Yirgacheffe — самый известный регион.",
            "p3": "Sidamo — больший регион с разнообразными профилями.",
            "p4": "Guji — новый звёздный регион.",
            "p5": "Harrar — известен натуральной обработкой."
        },
        "en": {
            "p1": "Ethiopia is the birthplace of coffee.",
            "p2": "Yirgacheffe is the most famous region.",
            "p3": "Sidamo is a larger region with diverse profiles.",
            "p4": "Guji is a rising star region.",
            "p5": "Harrar is known for natural processing."
        }
    },
    "french_press_guide": {
        "uk": {
            "p1": "Френч-прес — найпростіший метод.",
            "p2": "30г кави, 500мл води, 4 хвилини.",
            "p3": "Відразу перелийте — інакше буде гіркота.",
            "p4": "Грубий помел як морська сіль.",
            "p5": "Температура води — 92-96°C."
        },
        "ru": {
            "p1": "Френч-пресс — самый простой метод.",
            "p2": "30г кофе, 500мл воды, 4 минуты.",
            "p3": "Сразу перелейте — иначе будет горечь.",
            "p4": "Грубый помол как морская соль.",
            "p5": "Температура воды — 92-96°C."
        },
        "en": {
            "p1": "French press is the simplest method.",
            "p2": "30g coffee, 500ml water, 4 minutes.",
            "p3": "Pour immediately — otherwise it becomes bitter.",
            "p4": "Coarse grind like sea salt.",
            "p5": "Water temperature — 92-96°C."
        }
    },
    "sca_grading": {
        "uk": {
            "p1": "SCA створила стандарт оцінки кави.",
            "p2": "100-бальна шкала. 80+ = specialty.",
            "p3": "11 критеріїв оцінки.",
            "p4": "Каппінг — професійна дегустація.",
            "p5": "85+ — відмінна кава."
        },
        "ru": {
            "p1": "SCA создала стандарт оценки кофе.",
            "p2": "100-балльная шкала. 80+ = specialty.",
            "p3": "11 критериев оценки.",
            "p4": "Каппинг — профессиональная дегустация.",
            "p5": "85+ — отличный кофе."
        },
        "en": {
            "p1": "SCA created the coffee grading standard.",
            "p2": "100-point scale. 80+ = specialty.",
            "p3": "11 evaluation criteria.",
            "p4": "Cupping is professional tasting.",
            "p5": "85+ is excellent coffee."
        }
    },
    "specialty_coffee": {
        "uk": {
            "p1": "Specialty — не маркетинг, а чіткий термін.",
            "p2": "80+ балів SCA = specialty.",
            "p3": "Це приблизно 3% всієї кави.",
            "p4": "Якість зерна, свіжість обсмажки, прозорість.",
            "p5": "Вартує кожної копійки."
        },
        "ru": {
            "p1": "Specialty — не маркетинг, а чёткий термин.",
            "p2": "80+ баллов SCA = specialty.",
            "p3": "Это примерно 3% всего кофе.",
            "p4": "Качество зерна, свежесть обжарки, прозрачность.",
            "p5": "Стоит каждой копейки."
        },
        "en": {
            "p1": "Specialty isn't marketing, it's a clear term.",
            "p2": "80+ SCA points = specialty.",
            "p3": "That's about 3% of all coffee.",
            "p4": "Bean quality, roast freshness, transparency.",
            "p5": "Worth every penny."
        }
    },
    "turka_guide": {
        "uk": {
            "p1": "Кава в турці — найстаріший метод.",
            "p2": "Мідна турка з товстим дном.",
            "p3": "Найдрібніший помел, як пудра.",
            "p4": "7г кави на 60мл води.",
            "p5": "Ніколи не кип'ятіть!"
        },
        "ru": {
            "p1": "Кофе в турке — старейший метод.",
            "p2": "Медная турка с толстым дном.",
            "p3": "Самый мелкий помол, как пудра.",
            "p4": "7г кофе на 60мл воды.",
            "p5": "Никогда не кипятите!"
        },
        "en": {
            "p1": "Turkish coffee is the oldest method.",
            "p2": "Copper cezve with thick bottom.",
            "p3": "Finest grind, like powder.",
            "p4": "7g coffee per 60ml water.",
            "p5": "Never boil!"
        }
    },
    "v60_guide": {
        "uk": {
            "p1": "V60 — улюблений метод бариста.",
            "p2": "V60, фільтри, гусячок, ваги.",
            "p3": "15г кави, 250мл води.",
            "p4": "Преінфузія 30мл, 30-45 сек.",
            "p5": "Загальний час — 2:30-3:00."
        },
        "ru": {
            "p1": "V60 — любимый метод баристов.",
            "p2": "V60, фильтры, гусака, весы.",
            "p3": "15г кофе, 250мл воды.",
            "p4": "Преинфузия 30мл, 30-45 сек.",
            "p5": "Общее время — 2:30-3:00."
        },
        "en": {
            "p1": "V60 is baristas' favorite method.",
            "p2": "V60, filters, gooseneck, scale.",
            "p3": "15g coffee, 250ml water.",
            "p4": "Pre-infusion 30ml, 30-45 sec.",
            "p5": "Total time — 2:30-3:00."
        }
    },
    "yirgacheffe_region": {
        "uk": {
            "p1": "Yirgacheffe — легендарний регіон.",
            "p2": "1700-2200м над рівнем моря.",
            "p3": "Квіткові ноти, цитрусова кислотність.",
            "p4": "Мита — чистий смак. Натуральна — солодкий.",
            "p5": "Один з найкращих терруарів у світі."
        },
        "ru": {
            "p1": "Yirgacheffe — легендарный регион.",
            "p2": "1700-2200м над уровнем моря.",
            "p3": "Цветочные ноты, цитрусовая кислотность.",
            "p4": "Мытая — чистый вкус. Натуральная — сладкий.",
            "p5": "Один из лучших терруаров в мире."
        },
        "en": {
            "p1": "Yirgacheffe is a legendary region.",
            "p2": "1700-2200m above sea level.",
            "p3": "Floral notes, citrus acidity.",
            "p4": "Washed — clean taste. Natural — sweet.",
            "p5": "One of the world's best terroirs."
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
        
        for key, translations in EXTENDED_PARAGRAPHS.items():
            if key not in data["blog"]:
                data["blog"][key] = {}
            data["blog"][key].update(translations[lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path}")

if __name__ == "__main__":
    print("Adding extended blog paragraph translations...")
    update_locales()
    print("Done!")
