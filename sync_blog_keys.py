#!/usr/bin/env python3
"""
Sync blog JSON keys with HTML data-i18n attributes
Based on the number of H2/H3 tags found in each blog file
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Extended blog translations with numbered keys
BLOG_SYNCED_KEYS = {
    "arabica_vs_robusta": {
        "uk": {"h2_1": "Порівняльна таблиця", "h2_2": "Arabica: Королева кави", "h2_3": "Robusta: Недооцінений боєць", "h2_4": "Коли обирати Arabica, а коли Robusta?", "h2_5": "Спробуйте справжню Arabica",
               "h3_1": "Умови вирощування", "h3_2": "Смаковий профіль", "h3_3": "Популярні різновиди Arabica", "h3_4": "Чому Robusta дешевша?", "h3_5": "Чи завжди Robusta погана?", "h3_6": "Переваги якісної Robusta", "h3_7": "Обирайте 100% Arabica, якщо:", "h3_8": "Robusta може підійти, якщо:"},
        "ru": {"h2_1": "Сравнительная таблица", "h2_2": "Arabica: Королева кофе", "h2_3": "Robusta: Недооценённый боец", "h2_4": "Когда выбирать Arabica, а когда Robusta?", "h2_5": "Попробуйте настоящую Arabica",
               "h3_1": "Условия выращивания", "h3_2": "Вкусовой профиль", "h3_3": "Популярные разновидности Arabica", "h3_4": "Почему Robusta дешевле?", "h3_5": "Всегда ли Robusta плохая?", "h3_6": "Преимущества качественной Robusta", "h3_7": "Выбирайте 100% Arabica, если:", "h3_8": "Robusta может подойти, если:"},
        "en": {"h2_1": "Comparison Table", "h2_2": "Arabica: The Queen of Coffee", "h2_3": "Robusta: The Underrated Fighter", "h2_4": "When to Choose Arabica, When Robusta?", "h2_5": "Try Real Arabica",
               "h3_1": "Growing Conditions", "h3_2": "Flavor Profile", "h3_3": "Popular Arabica Varieties", "h3_4": "Why is Robusta Cheaper?", "h3_5": "Is Robusta Always Bad?", "h3_6": "Benefits of Quality Robusta", "h3_7": "Choose 100% Arabica if:", "h3_8": "Robusta may work if:"}
    },
    "bean_to_cup": {
        "uk": {"h2_1": "Вирощування", "h2_2": "Збирання врожаю", "h2_3": "Первинна обробка", "h2_4": "Сортування та експорт", "h2_5": "Обсмажка", "h2_6": "Помел", "h2_7": "Заварювання", "h2_8": "Насолода", "h3_1": "Спробуйте результат"},
        "ru": {"h2_1": "Выращивание", "h2_2": "Сбор урожая", "h2_3": "Первичная обработка", "h2_4": "Сортировка и экспорт", "h2_5": "Обжарка", "h2_6": "Помол", "h2_7": "Заваривание", "h2_8": "Наслаждение", "h3_1": "Попробуйте результат"},
        "en": {"h2_1": "Growing", "h2_2": "Harvesting", "h2_3": "Primary Processing", "h2_4": "Sorting and Export", "h2_5": "Roasting", "h2_6": "Grinding", "h2_7": "Brewing", "h2_8": "Enjoyment", "h3_1": "Try the Result"}
    },
    "brewing_methods": {
        "uk": {"h2_1": "Методи занурення", "h2_2": "Крапельні методи", "h2_3": "Методи під тиском", "h2_4": "Методи варіння", "h2_5": "Гібридні методи", "h2_6": "Який метод обрати?", "h2_7": "Спробуйте різні методи",
               "h3_1": "Френч-прес", "h3_2": "Cold Brew", "h3_3": "Cupping", "h3_4": "V60", "h3_5": "Калита", "h3_6": "Кемекс", "h3_7": "Еспресо", "h3_8": "Мока", "h3_9": "Аеропрес", "h3_10": "Турка", "h3_11": "Перколятор"},
        "ru": {"h2_1": "Методы погружения", "h2_2": "Капельные методы", "h2_3": "Методы под давлением", "h2_4": "Методы варки", "h2_5": "Гибридные методы", "h2_6": "Какой метод выбрать?", "h2_7": "Попробуйте разные методы",
               "h3_1": "Френч-пресс", "h3_2": "Cold Brew", "h3_3": "Каппинг", "h3_4": "V60", "h3_5": "Калита", "h3_6": "Кемекс", "h3_7": "Эспрессо", "h3_8": "Мока", "h3_9": "Аэропресс", "h3_10": "Турка", "h3_11": "Перколятор"},
        "en": {"h2_1": "Immersion Methods", "h2_2": "Drip Methods", "h2_3": "Pressure Methods", "h2_4": "Boiling Methods", "h2_5": "Hybrid Methods", "h2_6": "Which Method to Choose?", "h2_7": "Try Different Methods",
               "h3_1": "French Press", "h3_2": "Cold Brew", "h3_3": "Cupping", "h3_4": "V60", "h3_5": "Kalita", "h3_6": "Chemex", "h3_7": "Espresso", "h3_8": "Moka Pot", "h3_9": "Aeropress", "h3_10": "Turkish Pot", "h3_11": "Percolator"}
    },
    "coffee_processing": {
        "uk": {"h2_1": "Натуральна обробка", "h2_2": "Мита обробка", "h2_3": "Медова обробка", "h2_4": "Порівняння методів", "h3_1": "Плюси натуральної", "h3_2": "Мінуси натуральної", "h3_3": "Плюси митої", "h3_4": "Мінуси митої", "h3_5": "Типи медової обробки"},
        "ru": {"h2_1": "Натуральная обработка", "h2_2": "Мытая обработка", "h2_3": "Медовая обработка", "h2_4": "Сравнение методов", "h3_1": "Плюсы натуральной", "h3_2": "Минусы натуральной", "h3_3": "Плюсы мытой", "h3_4": "Минусы мытой", "h3_5": "Типы медовой обработки"},
        "en": {"h2_1": "Natural Processing", "h2_2": "Washed Processing", "h2_3": "Honey Processing", "h2_4": "Method Comparison", "h3_1": "Natural Pros", "h3_2": "Natural Cons", "h3_3": "Washed Pros", "h3_4": "Washed Cons", "h3_5": "Honey Processing Types"}
    },
    "coffee_seasonality": {
        "uk": {"h2_1": "Чому кава сезонна?", "h2_2": "Сезони збору по регіонах", "h2_3": "Ефіопія", "h2_4": "Колумбія", "h2_5": "Бразилія", "h2_6": "Як обрати свіжу каву?", "h3_1": "Поради"},
        "ru": {"h2_1": "Почему кофе сезонный?", "h2_2": "Сезоны сбора по регионам", "h2_3": "Эфиопия", "h2_4": "Колумбия", "h2_5": "Бразилия", "h2_6": "Как выбрать свежий кофе?", "h3_1": "Советы"},
        "en": {"h2_1": "Why is Coffee Seasonal?", "h2_2": "Harvest Seasons by Region", "h2_3": "Ethiopia", "h2_4": "Colombia", "h2_5": "Brazil", "h2_6": "How to Choose Fresh Coffee?", "h3_1": "Tips"}
    },
    "coffee_storage_blog": {
        "uk": {"h2_1": "Вороги свіжості", "h2_2": "Ідеальний контейнер", "h2_3": "Поради щодо зберігання", "h2_4": "Скільки зберігається кава?", "h3_1": "Кисень", "h3_2": "Волога", "h3_3": "Тепло", "h3_4": "Світло", "h3_5": "Сторонні запахи"},
        "ru": {"h2_1": "Враги свежести", "h2_2": "Идеальный контейнер", "h2_3": "Советы по хранению", "h2_4": "Сколько хранится кофе?", "h3_1": "Кислород", "h3_2": "Влага", "h3_3": "Тепло", "h3_4": "Свет", "h3_5": "Посторонние запахи"},
        "en": {"h2_1": "Enemies of Freshness", "h2_2": "The Ideal Container", "h2_3": "Storage Tips", "h2_4": "How Long Does Coffee Keep?", "h3_1": "Oxygen", "h3_2": "Moisture", "h3_3": "Heat", "h3_4": "Light", "h3_5": "Foreign Odors"}
    },
    "cold_brew_guide": {
        "uk": {"h2_1": "Що таке Cold Brew?", "h2_2": "Переваги", "h2_3": "Рецепт", "h2_4": "Поради", "h3_1": "Спробуйте Cold Brew"},
        "ru": {"h2_1": "Что такое Cold Brew?", "h2_2": "Преимущества", "h2_3": "Рецепт", "h2_4": "Советы", "h3_1": "Попробуйте Cold Brew"},
        "en": {"h2_1": "What is Cold Brew?", "h2_2": "Benefits", "h2_3": "Recipe", "h2_4": "Tips", "h3_1": "Try Cold Brew"}
    },
    "espresso_guide": {
        "uk": {"h2_1": "Обладнання", "h2_2": "Помел", "h2_3": "Техніка", "h2_4": "Діагностика проблем", "h3_1": "Машина", "h3_2": "Кавомолка", "h3_3": "Таймер та ваги", "h3_4": "Кислий шот", "h3_5": "Гіркий шот"},
        "ru": {"h2_1": "Оборудование", "h2_2": "Помол", "h2_3": "Техника", "h2_4": "Диагностика проблем", "h3_1": "Машина", "h3_2": "Кофемолка", "h3_3": "Таймер и весы", "h3_4": "Кислый шот", "h3_5": "Горький шот"},
        "en": {"h2_1": "Equipment", "h2_2": "Grind", "h2_3": "Technique", "h2_4": "Troubleshooting", "h3_1": "Machine", "h3_2": "Grinder", "h3_3": "Timer and Scale", "h3_4": "Sour Shot", "h3_5": "Bitter Shot"}
    },
    "ethiopia_origins": {
        "uk": {"h2_1": "Yirgacheffe", "h2_2": "Sidamo", "h2_3": "Guji", "h3_1": "Harrar", "h3_2": "Limu", "h3_3": "Jimma", "h3_4": "Tepi"},
        "ru": {"h2_1": "Yirgacheffe", "h2_2": "Sidamo", "h2_3": "Guji", "h3_1": "Harrar", "h3_2": "Limu", "h3_3": "Jimma", "h3_4": "Tepi"},
        "en": {"h2_1": "Yirgacheffe", "h2_2": "Sidamo", "h2_3": "Guji", "h3_1": "Harrar", "h3_2": "Limu", "h3_3": "Jimma", "h3_4": "Tepi"}
    },
    "french_press_guide": {
        "uk": {"h2_1": "Обладнання", "h2_2": "Рецепт", "h2_3": "Поради", "h3_1": "Спробуйте"},
        "ru": {"h2_1": "Оборудование", "h2_2": "Рецепт", "h2_3": "Советы", "h3_1": "Попробуйте"},
        "en": {"h2_1": "Equipment", "h2_2": "Recipe", "h2_3": "Tips", "h3_1": "Try It"}
    },
    "sca_grading": {
        "uk": {"h2_1": "Що таке SCA?", "h2_2": "Критерії оцінки", "h2_3": "Шкала балів", "h2_4": "Процес каппінгу", "h3_1": "Спробуйте 85+"},
        "ru": {"h2_1": "Что такое SCA?", "h2_2": "Критерии оценки", "h2_3": "Шкала баллов", "h2_4": "Процесс каппинга", "h3_1": "Попробуйте 85+"},
        "en": {"h2_1": "What is SCA?", "h2_2": "Grading Criteria", "h2_3": "Score Scale", "h2_4": "Cupping Process", "h3_1": "Try 85+"}
    },
    "specialty_coffee": {
        "uk": {"h2_1": "Визначення", "h2_2": "Відмінності від комерційної кави", "h2_3": "Ланцюг якості", "h2_4": "Чому дорожче?", "h2_5": "Як знайти?", "h2_6": "Спробуйте", "h3_1": "Зерно", "h3_2": "Обсмажка", "h3_3": "Приготування", "h3_4": "Терруар", "h3_5": "Обробка", "h3_6": "Свіжа обсмажка"},
        "ru": {"h2_1": "Определение", "h2_2": "Отличия от коммерческого кофе", "h2_3": "Цепочка качества", "h2_4": "Почему дороже?", "h2_5": "Как найти?", "h2_6": "Попробуйте", "h3_1": "Зерно", "h3_2": "Обжарка", "h3_3": "Приготовление", "h3_4": "Терруар", "h3_5": "Обработка", "h3_6": "Свежая обжарка"},
        "en": {"h2_1": "Definition", "h2_2": "Differences from Commercial Coffee", "h2_3": "Quality Chain", "h2_4": "Why More Expensive?", "h2_5": "How to Find?", "h2_6": "Try It", "h3_1": "Beans", "h3_2": "Roasting", "h3_3": "Brewing", "h3_4": "Terroir", "h3_5": "Processing", "h3_6": "Fresh Roasting"}
    },
    "turka_guide": {
        "uk": {"h2_1": "Історія", "h2_2": "Обладнання", "h2_3": "Рецепт", "h2_4": "Секрети", "h3_1": "Турка", "h3_2": "Помел", "h3_3": "Вода", "h3_4": "Подача"},
        "ru": {"h2_1": "История", "h2_2": "Оборудование", "h2_3": "Рецепт", "h2_4": "Секреты", "h3_1": "Турка", "h3_2": "Помол", "h3_3": "Вода", "h3_4": "Подача"},
        "en": {"h2_1": "History", "h2_2": "Equipment", "h2_3": "Recipe", "h2_4": "Secrets", "h3_1": "Cezve", "h3_2": "Grind", "h3_3": "Water", "h3_4": "Serving"}
    },
    "v60_guide": {
        "uk": {"h2_1": "Обладнання", "h2_2": "Пропорції", "h2_3": "Техніка заливання", "h2_4": "Рецепт", "h3_1": "Преінфузія", "h3_2": "Перший залив", "h3_3": "Другий залив", "h3_4": "Фінішний залив"},
        "ru": {"h2_1": "Оборудование", "h2_2": "Пропорции", "h2_3": "Техника пролива", "h2_4": "Рецепт", "h3_1": "Преинфузия", "h3_2": "Первый пролив", "h3_3": "Второй пролив", "h3_4": "Финишный пролив"},
        "en": {"h2_1": "Equipment", "h2_2": "Ratios", "h2_3": "Pouring Technique", "h2_4": "Recipe", "h3_1": "Pre-infusion", "h3_2": "First Pour", "h3_3": "Second Pour", "h3_4": "Final Pour"}
    },
    "yirgacheffe_region": {
        "uk": {"h2_1": "Географія", "h2_2": "Клімат", "h2_3": "Смаковий профіль", "h2_4": "Методи обробки", "h2_5": "Чому особлива?", "h3_1": "Мита обробка", "h3_2": "Натуральна обробка", "h3_3": "Спробуйте Yirgacheffe"},
        "ru": {"h2_1": "География", "h2_2": "Климат", "h2_3": "Вкусовой профиль", "h2_4": "Методы обработки", "h2_5": "Почему особенный?", "h3_1": "Мытая обработка", "h3_2": "Натуральная обработка", "h3_3": "Попробуйте Yirgacheffe"},
        "en": {"h2_1": "Geography", "h2_2": "Climate", "h2_3": "Flavor Profile", "h2_4": "Processing Methods", "h2_5": "Why Special?", "h3_1": "Washed Processing", "h3_2": "Natural Processing", "h3_3": "Try Yirgacheffe"}
    }
}

def update_locales():
    """Add synced keys to locale files"""
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "blog" not in data:
            data["blog"] = {}
        
        for blog_key, translations in BLOG_SYNCED_KEYS.items():
            if blog_key not in data["blog"]:
                data["blog"][blog_key] = {}
            data["blog"][blog_key].update(translations[lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path}")

if __name__ == "__main__":
    print("Syncing blog JSON keys with HTML data-i18n...")
    update_locales()
    print("Done!")
