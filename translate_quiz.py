#!/usr/bin/env python3
"""Add full quiz page translations"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

QUIZ_TRANSLATIONS = {
    "quiz_page": {
        # Hero
        "badge": {"uk": "5 ПИТАНЬ • 2 ХВИЛИНИ", "ru": "5 ВОПРОСОВ • 2 МИНУТЫ", "en": "5 QUESTIONS • 2 MINUTES"},
        "hero_title": {"uk": "Знайдіть свою<br>ідеальну каву", "ru": "Найдите свой<br>идеальный кофе", "en": "Find your<br>perfect coffee"},
        "hero_text": {"uk": "Відповідайте на прості питання — і ми підберемо сорт, який точно вам сподобається", "ru": "Ответьте на простые вопросы — и мы подберем сорт, который точно вам понравится", "en": "Answer simple questions — and we'll find a variety you'll definitely love"},
        "benefit_discount": {"uk": "Знижка -10% на результат", "ru": "Скидка -10% на результат", "en": "-10% discount on result"},
        "benefit_instant": {"uk": "Миттєва рекомендація", "ru": "Мгновенная рекомендация", "en": "Instant recommendation"},
        "benefit_accuracy": {"uk": "98% точність", "ru": "98% точность", "en": "98% accuracy"},
        
        # Progress steps
        "step_way": {"uk": "Спосіб", "ru": "Способ", "en": "Way"},
        "step_taste": {"uk": "Смак", "ru": "Вкус", "en": "Taste"},
        "step_method": {"uk": "Метод", "ru": "Метод", "en": "Method"},
        "step_strength": {"uk": "Міцність", "ru": "Крепость", "en": "Strength"},
        "step_volume": {"uk": "Обсяг", "ru": "Объем", "en": "Volume"},
        
        # Question 1
        "q1_title": {"uk": "Як ви зазвичай п'єте каву?", "ru": "Как вы обычно пьёте кофе?", "en": "How do you usually drink coffee?"},
        "q1_subtitle": {"uk": "Оберіть найближчий варіант", "ru": "Выберите ближайший вариант", "en": "Choose the closest option"},
        "q1_opt1_title": {"uk": "Чорна, без нічого", "ru": "Чёрный, без ничего", "en": "Black, nothing added"},
        "q1_opt1_desc": {"uk": "Максимальний смак зерна", "ru": "Максимальный вкус зерна", "en": "Maximum bean flavor"},
        "q1_opt2_title": {"uk": "З молоком", "ru": "С молоком", "en": "With milk"},
        "q1_opt2_desc": {"uk": "Капучіно, лате, флет-вайт", "ru": "Капучино, латте, флэт-уайт", "en": "Cappuccino, latte, flat white"},
        "q1_opt3_title": {"uk": "З молоком і цукром", "ru": "С молоком и сахаром", "en": "With milk and sugar"},
        "q1_opt3_desc": {"uk": "Солодко та ніжно", "ru": "Сладко и нежно", "en": "Sweet and gentle"},
        
        # Question 2
        "q2_title": {"uk": "Які смаки вам подобаються?", "ru": "Какие вкусы вам нравятся?", "en": "What flavors do you like?"},
        "q2_subtitle": {"uk": "Оберіть улюблений профіль", "ru": "Выберите любимый профиль", "en": "Choose your favorite profile"},
        "q2_opt1_title": {"uk": "Фруктові, ягідні", "ru": "Фруктовые, ягодные", "en": "Fruity, berry"},
        "q2_opt1_desc": {"uk": "Яскрава кислинка, свіжість", "ru": "Яркая кислинка, свежесть", "en": "Bright acidity, freshness"},
        "q2_opt2_title": {"uk": "Шоколадні, горіхові", "ru": "Шоколадные, ореховые", "en": "Chocolate, nutty"},
        "q2_opt2_desc": {"uk": "Класичний, насичений смак", "ru": "Классический, насыщенный вкус", "en": "Classic, rich flavor"},
        "q2_opt3_title": {"uk": "Квіткові, чайні", "ru": "Цветочные, чайные", "en": "Floral, tea-like"},
        "q2_opt3_desc": {"uk": "Ніжний, делікатний аромат", "ru": "Нежный, деликатный аромат", "en": "Gentle, delicate aroma"},
        
        # Question 3
        "q3_title": {"uk": "Як ви готуєте каву вдома?", "ru": "Как вы готовите кофе дома?", "en": "How do you brew coffee at home?"},
        "q3_subtitle": {"uk": "Від цього залежить рекомендація обсмажки", "ru": "От этого зависит рекомендация обжарки", "en": "This affects the roast recommendation"},
        "q3_opt1_title": {"uk": "Еспресо-машина", "ru": "Эспрессо-машина", "en": "Espresso machine"},
        "q3_opt1_desc": {"uk": "Автомат або ріжкова", "ru": "Автомат или рожковая", "en": "Automatic or portafilter"},
        "q3_opt2_title": {"uk": "Пуровер / Кемекс", "ru": "Пуровер / Кемекс", "en": "Pour over / Chemex"},
        "q3_opt2_desc": {"uk": "Фільтр-методи", "ru": "Фильтр-методы", "en": "Filter methods"},
        "q3_opt3_title": {"uk": "Турка / Мока", "ru": "Турка / Мока", "en": "Turkish / Moka"},
        "q3_opt3_desc": {"uk": "Традиційний спосіб", "ru": "Традиционный способ", "en": "Traditional method"},
        "q3_opt4_title": {"uk": "Френч-прес", "ru": "Френч-пресс", "en": "French press"},
        "q3_opt4_desc": {"uk": "Імерсійне заварювання", "ru": "Иммерсионное заваривание", "en": "Immersion brewing"},
        
        # Question 4
        "q4_title": {"uk": "Наскільки міцну каву ви любите?", "ru": "Насколько крепкий кофе вы любите?", "en": "How strong do you like your coffee?"},
        "q4_subtitle": {"uk": "Це вплине на рекомендацію обсмажки", "ru": "Это повлияет на рекомендацию обжарки", "en": "This affects roast recommendation"},
        "q4_opt1_title": {"uk": "Легка", "ru": "Легкий", "en": "Light"},
        "q4_opt1_desc": {"uk": "М'яка, чайна", "ru": "Мягкий, чайный", "en": "Mild, tea-like"},
        "q4_opt2_title": {"uk": "Середня", "ru": "Средний", "en": "Medium"},
        "q4_opt2_desc": {"uk": "Збалансована", "ru": "Сбалансированный", "en": "Balanced"},
        "q4_opt3_title": {"uk": "Міцна", "ru": "Крепкий", "en": "Strong"},
        "q4_opt3_desc": {"uk": "Насичена, інтенсивна", "ru": "Насыщенный, интенсивный", "en": "Rich, intense"},
        
        # Question 5
        "q5_title": {"uk": "Скільки кави вам потрібно?", "ru": "Сколько кофе вам нужно?", "en": "How much coffee do you need?"},
        "q5_subtitle": {"uk": "Оберіть обсяг пакування", "ru": "Выберите объем упаковки", "en": "Choose package size"},
        "q5_opt1_title": {"uk": "250 грам", "ru": "250 грамм", "en": "250 grams"},
        "q5_opt1_desc": {"uk": "На 1-2 тижні для одного", "ru": "На 1-2 недели для одного", "en": "1-2 weeks for one person"},
        "q5_opt2_title": {"uk": "500 грам", "ru": "500 грамм", "en": "500 grams"},
        "q5_opt2_desc": {"uk": "Оптимально для пари", "ru": "Оптимально для пары", "en": "Optimal for a couple"},
        "q5_opt3_title": {"uk": "1 кілограм", "ru": "1 килограмм", "en": "1 kilogram"},
        "q5_opt3_desc": {"uk": "Для сім'ї або офісу", "ru": "Для семьи или офиса", "en": "For family or office"},
        
        # Navigation
        "btn_next": {"uk": "Далі", "ru": "Далее", "en": "Next"},
        "btn_back": {"uk": "Назад", "ru": "Назад", "en": "Back"},
        
        # Result
        "result_title": {"uk": "Ваша ідеальна кава:", "ru": "Ваш идеальный кофе:", "en": "Your perfect coffee:"},
        "result_btn_order": {"uk": "Замовити зі знижкою -10%", "ru": "Заказать со скидкой -10%", "en": "Order with -10% discount"},
        "result_btn_restart": {"uk": "Пройти тест ще раз", "ru": "Пройти тест ещё раз", "en": "Take the quiz again"},
        "result_discount": {"uk": "Ваш промокод:", "ru": "Ваш промокод:", "en": "Your promo code:"},
        "why_perfect_title": {"uk": "Чому саме цей сорт?", "ru": "Почему именно этот сорт?", "en": "Why this variety?"}
    }
}

def update_jsons():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "quiz_page" not in data:
            data["quiz_page"] = {}
        
        for key, trans in QUIZ_TRANSLATIONS["quiz_page"].items():
            data["quiz_page"][key] = trans[lang]
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Updated {lang}.json with quiz translations")

if __name__ == "__main__":
    update_jsons()
    print("Done!")
