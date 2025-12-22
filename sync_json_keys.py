#!/usr/bin/env python3
"""
Sync JSON translation keys with HTML data-i18n attributes
Extracts actual keys from HTML and creates matching entries in JSON
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Article key mappings
ARTICLE_MAPPINGS = {
    "light-vs-dark-roast.html": {
        "key": "light_vs_dark",
        "content": {
            "uk": {
                "h2_1": "Що відбувається під час обсмажки?",
                "h2_2": "Світла обсмажка (Light Roast)",
                "h2_3": "Середня обсмажка (Medium Roast)",
                "h2_4": "Темна обсмажка (Dark Roast)",
                "h2_5": "Міф про кофеїн",
                "h2_6": "Як обрати?"
            },
            "ru": {
                "h2_1": "Что происходит во время обжарки?",
                "h2_2": "Светлая обжарка (Light Roast)",
                "h2_3": "Средняя обжарка (Medium Roast)",
                "h2_4": "Тёмная обжарка (Dark Roast)",
                "h2_5": "Миф о кофеине",
                "h2_6": "Как выбрать?"
            },
            "en": {
                "h2_1": "What Happens During Roasting?",
                "h2_2": "Light Roast",
                "h2_3": "Medium Roast",
                "h2_4": "Dark Roast",
                "h2_5": "The Caffeine Myth",
                "h2_6": "How to Choose?"
            }
        }
    },
    "how-to-brew-v60.html": {
        "key": "how_to_brew_v60",
        "content": {
            "uk": {
                "h2_1": "Що вам потрібно",
                "h2_2": "Пропорції",
                "h2_3": "Покроковий рецепт",
                "h3_1": "Крок 1",
                "h3_2": "Крок 2",
                "h3_3": "Крок 3",
                "h3_4": "Крок 4",
                "h3_5": "Крок 5",
                "h3_6": "Крок 6"
            },
            "ru": {
                "h2_1": "Что вам нужно",
                "h2_2": "Пропорции",
                "h2_3": "Пошаговый рецепт",
                "h3_1": "Шаг 1",
                "h3_2": "Шаг 2",
                "h3_3": "Шаг 3",
                "h3_4": "Шаг 4",
                "h3_5": "Шаг 5",
                "h3_6": "Шаг 6"
            },
            "en": {
                "h2_1": "What You Need",
                "h2_2": "Ratios",
                "h2_3": "Step-by-Step Recipe",
                "h3_1": "Step 1",
                "h3_2": "Step 2",
                "h3_3": "Step 3",
                "h3_4": "Step 4",
                "h3_5": "Step 5",
                "h3_6": "Step 6"
            }
        }
    },
    "coffee-storage.html": {
        "key": "coffee_storage",
        "content": {
            "uk": {
                "h2_1": "5 ворогів свіжості",
                "h2_2": "Як правильно зберігати",
                "h2_3": "Скільки зберігається кава?",
                "h2_4": "Чи можна зберігати в холодильнику?",
                "h3_1": "Кисень",
                "h3_2": "Волога",
                "h3_3": "Тепло",
                "h3_4": "Світло",
                "h3_5": "Сторонні запахи"
            },
            "ru": {
                "h2_1": "5 врагов свежести",
                "h2_2": "Как правильно хранить",
                "h2_3": "Сколько хранится кофе?",
                "h2_4": "Можно ли хранить в холодильнике?",
                "h3_1": "Кислород",
                "h3_2": "Влага",
                "h3_3": "Тепло",
                "h3_4": "Свет",
                "h3_5": "Посторонние запахи"
            },
            "en": {
                "h2_1": "5 Enemies of Freshness",
                "h2_2": "How to Store Properly",
                "h2_3": "How Long Does Coffee Keep?",
                "h2_4": "Can You Store in the Fridge?",
                "h3_1": "Oxygen",
                "h3_2": "Moisture",
                "h3_3": "Heat",
                "h3_4": "Light",
                "h3_5": "Foreign Odors"
            }
        }
    },
    "natural-vs-washed.html": {
        "key": "natural_vs_washed",
        "content": {
            "uk": {
                "h2_1": "Мита обробка (Washed)",
                "h2_2": "Натуральна обробка (Natural)",
                "h2_3": "Порівняння смаків"
            },
            "ru": {
                "h2_1": "Мытая обработка (Washed)",
                "h2_2": "Натуральная обработка (Natural)",
                "h2_3": "Сравнение вкусов"
            },
            "en": {
                "h2_1": "Washed Processing",
                "h2_2": "Natural Processing",
                "h2_3": "Flavor Comparison"
            }
        }
    },
    "water-for-coffee.html": {
        "key": "water_for_coffee",
        "content": {
            "uk": {
                "h2_1": "Чому вода важлива?",
                "h2_2": "Ідеальна вода за SCA",
                "h2_3": "Яку воду використовувати?",
                "h2_4": "Чого уникати?"
            },
            "ru": {
                "h2_1": "Почему вода важна?",
                "h2_2": "Идеальная вода по SCA",
                "h2_3": "Какую воду использовать?",
                "h2_4": "Чего избегать?"
            },
            "en": {
                "h2_1": "Why Does Water Matter?",
                "h2_2": "Ideal Water per SCA",
                "h2_3": "What Water to Use?",
                "h2_4": "What to Avoid?"
            }
        }
    },
    "grinder-guide.html": {
        "key": "grinder_guide",
        "content": {
            "uk": {
                "h2_1": "Чому потрібна кавомолка?",
                "h2_2": "Типи кавомолок",
                "h2_3": "Ручні кавомолки",
                "h2_4": "Електричні кавомолки",
                "h2_5": "Що обрати?",
                "h3_1": "Ножові кавомолки",
                "h3_2": "Жорнові кавомолки",
                "h3_3": "Плоскі жорна",
                "h3_4": "Конічні жорна"
            },
            "ru": {
                "h2_1": "Зачем нужна кофемолка?",
                "h2_2": "Типы кофемолок",
                "h2_3": "Ручные кофемолки",
                "h2_4": "Электрические кофемолки",
                "h2_5": "Что выбрать?",
                "h3_1": "Ножевые кофемолки",
                "h3_2": "Жерновые кофемолки",
                "h3_3": "Плоские жернова",
                "h3_4": "Конические жернова"
            },
            "en": {
                "h2_1": "Why Do You Need a Grinder?",
                "h2_2": "Types of Grinders",
                "h2_3": "Manual Grinders",
                "h2_4": "Electric Grinders",
                "h2_5": "What to Choose?",
                "h3_1": "Blade Grinders",
                "h3_2": "Burr Grinders",
                "h3_3": "Flat Burrs",
                "h3_4": "Conical Burrs"
            }
        }
    },
    "aeropress-recipes.html": {
        "key": "aeropress_recipes",
        "content": {
            "uk": {
                "h2_1": "Рецепти чемпіонів"
            },
            "ru": {
                "h2_1": "Рецепты чемпионов"
            },
            "en": {
                "h2_1": "Champion Recipes"
            }
        }
    },
    "cold-brew-recipe.html": {
        "key": "cold_brew_recipe",
        "content": {
            "uk": {
                "h2_1": "Що таке Cold Brew?",
                "h2_2": "Обладнання",
                "h2_3": "Рецепт",
                "h2_4": "Поради"
            },
            "ru": {
                "h2_1": "Что такое Cold Brew?",
                "h2_2": "Оборудование",
                "h2_3": "Рецепт",
                "h2_4": "Советы"
            },
            "en": {
                "h2_1": "What is Cold Brew?",
                "h2_2": "Equipment",
                "h2_3": "Recipe",
                "h2_4": "Tips"
            }
        }
    },
    "espresso-mistakes.html": {
        "key": "espresso_mistakes",
        "content": {
            "uk": {
                "h2_1": "Топ помилок",
                "h3_1": "1. Неправильний помел",
                "h3_2": "2. Неточна доза",
                "h3_3": "3. Неправильна температура",
                "h3_4": "4. Несвіжа кава",
                "h3_5": "5. Нерівний темпінг",
                "h3_6": "6. Брудна група",
                "h3_7": "7. Неправильне співвідношення"
            },
            "ru": {
                "h2_1": "Топ ошибок",
                "h3_1": "1. Неправильный помол",
                "h3_2": "2. Неточная доза",
                "h3_3": "3. Неправильная температура",
                "h3_4": "4. Несвежий кофе",
                "h3_5": "5. Неровный темпинг",
                "h3_6": "6. Грязная группа",
                "h3_7": "7. Неправильное соотношение"
            },
            "en": {
                "h2_1": "Top Mistakes",
                "h3_1": "1. Wrong Grind",
                "h3_2": "2. Inaccurate Dose",
                "h3_3": "3. Wrong Temperature",
                "h3_4": "4. Stale Coffee",
                "h3_5": "5. Uneven Tamping",
                "h3_6": "6. Dirty Group Head",
                "h3_7": "7. Wrong Ratio"
            }
        }
    },
    "turka-recipe.html": {
        "key": "turka_recipe",
        "content": {
            "uk": {
                "h2_1": "Історія",
                "h2_2": "Обладнання",
                "h2_3": "Рецепт",
                "h2_4": "Секрети"
            },
            "ru": {
                "h2_1": "История",
                "h2_2": "Оборудование",
                "h2_3": "Рецепт",
                "h2_4": "Секреты"
            },
            "en": {
                "h2_1": "History",
                "h2_2": "Equipment",
                "h2_3": "Recipe",
                "h2_4": "Secrets"
            }
        }
    },
    "caffeine-myths.html": {
        "key": "caffeine_myths",
        "content": {
            "uk": {
                "h2_1": "Популярні міфи",
                "h3_1": "Міф 1: Темна обсмажка міцніша",
                "h3_2": "Міф 2: Еспресо містить найбільше кофеїну",
                "h3_3": "Міф 3: Кофеїн зневоднює",
                "h3_4": "Міф 4: Кофеїн викликає звикання",
                "h3_5": "Міф 5: Декаф без кофеїну"
            },
            "ru": {
                "h2_1": "Популярные мифы",
                "h3_1": "Миф 1: Тёмная обжарка крепче",
                "h3_2": "Миф 2: Эспрессо содержит больше всего кофеина",
                "h3_3": "Миф 3: Кофеин обезвоживает",
                "h3_4": "Миф 4: Кофеин вызывает привыкание",
                "h3_5": "Миф 5: Декаф без кофеина"
            },
            "en": {
                "h2_1": "Popular Myths",
                "h3_1": "Myth 1: Dark Roast is Stronger",
                "h3_2": "Myth 2: Espresso Has the Most Caffeine",
                "h3_3": "Myth 3: Caffeine Dehydrates",
                "h3_4": "Myth 4: Caffeine is Addictive",
                "h3_5": "Myth 5: Decaf is Caffeine-Free"
            }
        }
    }
}

def update_locales():
    """Add synced keys to locale files"""
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "articles" not in data:
            data["articles"] = {}
        
        for filename, mapping in ARTICLE_MAPPINGS.items():
            key = mapping["key"]
            if key not in data["articles"]:
                data["articles"][key] = {}
            
            # Add synced keys
            data["articles"][key].update(mapping["content"][lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path}")

if __name__ == "__main__":
    print("Syncing JSON keys with HTML data-i18n...")
    update_locales()
    print("Done!")
