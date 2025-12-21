"""
Script to add data-i18n attributes to subscription.html and update locale files
"""
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# New translations to add for subscription page
new_translations = {
    "subscription_page": {
        "hero_badge": "-10% НА КОЖНУ ДОСТАВКУ",
        "hero_title": "Кава, яка приходить сама",
        "hero_subtitle": "Обери смак, частоту, кількість — і насолоджуйся свіжообсмаженою кавою без зайвих клопотів.",
        "choose_plan": "Обрати план",
        "how_it_works": "Як це працює?",
        "benefit_discount": "-10% знижка",
        "benefit_discount_text": "на кожну доставку",
        "benefit_shipping": "Безкоштовна доставка",
        "benefit_shipping_text": "завжди",
        "benefit_flexible": "Гнучке управління",
        "benefit_flexible_text": "пауза будь-коли",
        "benefit_fresh": "Свіжа обсмажка",
        "benefit_fresh_text": "під ваше замовлення",
        "plans_title": "Оберіть свій план",
        "plans_subtitle": "Відміна або пауза в будь-який момент. Без зобов'язань.",
        "plan_starter": "Starter",
        "plan_starter_desc": "Для знайомства",
        "plan_lover": "Coffee Lover",
        "plan_lover_desc": "Ідеальний баланс",
        "plan_addict": "Coffee Addict",
        "plan_addict_desc": "Для справжніх цінителів",
        "plan_popular": "НАЙПОПУЛЯРНІШИЙ",
        "per_month": "г/місяць",
        "pack_1": "1 пачка 250г",
        "pack_2": "2 пачки по 250г",
        "pack_4": "4 пачки по 250г",
        "once_month": "Раз на місяць",
        "twice_month": "Раз на 2 тижні",
        "weekly": "Щотижня",
        "priority_support": "Пріоритетна підтримка",
        "exclusive_lots": "Ексклюзивні лоти",
        "how_step1_title": "Оберіть план",
        "how_step1_text": "Визначте, скільки кави вам потрібно",
        "how_step2_title": "Налаштуйте",
        "how_step2_text": "Обсмажка, помол, частота — все під вас",
        "how_step3_title": "Отримуйте",
        "how_step3_text": "Свіжа кава приходить автоматично",
        "how_step4_title": "Насолоджуйтесь!",
        "how_step4_text": "Ми дбаємо про вашу каву",
        "faq_title": "Часті питання",
        "faq_cancel_q": "Чи можу я скасувати підписку?",
        "faq_cancel_a": "Так, ви можете скасувати або поставити на паузу підписку в будь-який момент з особистого кабінету.",
        "faq_change_q": "Чи можу я змінити каву?",
        "faq_change_a": "Звичайно! Ви можете змінити сорт кави, обсмажку та помол перед кожною доставкою.",
        "faq_payment_q": "Коли списуються кошти?",
        "faq_payment_a": "Оплата списується автоматично за 2 дні до запланованої доставки."
    }
}

# English translations
en_translations = {
    "subscription_page": {
        "hero_badge": "-10% ON EVERY DELIVERY",
        "hero_title": "Coffee that comes to you",
        "hero_subtitle": "Choose taste, frequency, quantity — and enjoy freshly roasted coffee without hassle.",
        "choose_plan": "Choose plan",
        "how_it_works": "How it works?",
        "benefit_discount": "-10% discount",
        "benefit_discount_text": "on every delivery",
        "benefit_shipping": "Free shipping",
        "benefit_shipping_text": "always",
        "benefit_flexible": "Flexible management",
        "benefit_flexible_text": "pause anytime",
        "benefit_fresh": "Fresh roast",
        "benefit_fresh_text": "for your order",
        "plans_title": "Choose your plan",
        "plans_subtitle": "Cancel or pause anytime. No obligations.",
        "plan_starter": "Starter",
        "plan_starter_desc": "For introduction",
        "plan_lover": "Coffee Lover",
        "plan_lover_desc": "Perfect balance",
        "plan_addict": "Coffee Addict",
        "plan_addict_desc": "For true connoisseurs",
        "plan_popular": "MOST POPULAR",
        "per_month": "g/month",
        "pack_1": "1 pack 250g",
        "pack_2": "2 packs of 250g",
        "pack_4": "4 packs of 250g",
        "once_month": "Once a month",
        "twice_month": "Every 2 weeks",
        "weekly": "Weekly",
        "priority_support": "Priority support",
        "exclusive_lots": "Exclusive lots",
        "how_step1_title": "Choose a plan",
        "how_step1_text": "Determine how much coffee you need",
        "how_step2_title": "Customize",
        "how_step2_text": "Roast, grind, frequency — everything for you",
        "how_step3_title": "Receive",
        "how_step3_text": "Fresh coffee comes automatically",
        "how_step4_title": "Enjoy!",
        "how_step4_text": "We take care of your coffee",
        "faq_title": "Frequently Asked Questions",
        "faq_cancel_q": "Can I cancel my subscription?",
        "faq_cancel_a": "Yes, you can cancel or pause your subscription at any time from your personal account.",
        "faq_change_q": "Can I change the coffee?",
        "faq_change_a": "Of course! You can change the coffee variety, roast, and grind before each delivery.",
        "faq_payment_q": "When are funds charged?",
        "faq_payment_a": "Payment is automatically charged 2 days before the scheduled delivery."
    }
}

# Russian translations
ru_translations = {
    "subscription_page": {
        "hero_badge": "-10% НА КАЖДУЮ ДОСТАВКУ",
        "hero_title": "Кофе, который приходит сам",
        "hero_subtitle": "Выбери вкус, частоту, количество — и наслаждайся свежеобжаренным кофе без лишних хлопот.",
        "choose_plan": "Выбрать план",
        "how_it_works": "Как это работает?",
        "benefit_discount": "-10% скидка",
        "benefit_discount_text": "на каждую доставку",
        "benefit_shipping": "Бесплатная доставка",
        "benefit_shipping_text": "всегда",
        "benefit_flexible": "Гибкое управление",
        "benefit_flexible_text": "пауза в любое время",
        "benefit_fresh": "Свежая обжарка",
        "benefit_fresh_text": "под ваш заказ",
        "plans_title": "Выберите свой план",
        "plans_subtitle": "Отмена или пауза в любой момент. Без обязательств.",
        "plan_starter": "Starter",
        "plan_starter_desc": "Для знакомства",
        "plan_lover": "Coffee Lover",
        "plan_lover_desc": "Идеальный баланс",
        "plan_addict": "Coffee Addict",
        "plan_addict_desc": "Для настоящих ценителей",
        "plan_popular": "САМЫЙ ПОПУЛЯРНЫЙ",
        "per_month": "г/месяц",
        "pack_1": "1 пачка 250г",
        "pack_2": "2 пачки по 250г",
        "pack_4": "4 пачки по 250г",
        "once_month": "Раз в месяц",
        "twice_month": "Раз в 2 недели",
        "weekly": "Еженедельно",
        "priority_support": "Приоритетная поддержка",
        "exclusive_lots": "Эксклюзивные лоты",
        "how_step1_title": "Выберите план",
        "how_step1_text": "Определите, сколько кофе вам нужно",
        "how_step2_title": "Настройте",
        "how_step2_text": "Обжарка, помол, частота — всё под вас",
        "how_step3_title": "Получайте",
        "how_step3_text": "Свежий кофе приходит автоматически",
        "how_step4_title": "Наслаждайтесь!",
        "how_step4_text": "Мы заботимся о вашем кофе",
        "faq_title": "Часто задаваемые вопросы",
        "faq_cancel_q": "Могу ли я отменить подписку?",
        "faq_cancel_a": "Да, вы можете отменить или поставить на паузу подписку в любой момент из личного кабинета.",
        "faq_change_q": "Могу ли я изменить кофе?",
        "faq_change_a": "Конечно! Вы можете изменить сорт кофе, обжарку и помол перед каждой доставкой.",
        "faq_payment_q": "Когда списываются средства?",
        "faq_payment_a": "Оплата списывается автоматически за 2 дня до запланированной доставки."
    }
}

def update_locale_file(filename, new_keys):
    filepath = BASE_DIR / "locales" / filename
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for key, value in new_keys.items():
        data[key] = value
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"Updated {filename}")

if __name__ == "__main__":
    update_locale_file("uk.json", new_translations)
    update_locale_file("en.json", en_translations)
    update_locale_file("ru.json", ru_translations)
    print("All locale files updated!")
