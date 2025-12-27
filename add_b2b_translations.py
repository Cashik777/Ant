#!/usr/bin/env python3
"""
Add missing B2B form, FAQ, and review translations
"""
import json
import os

base_dir = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect\locales'

# B2B extra translations for form, FAQ, reviews
b2b_extra_uk = {
    # Form
    "form_subtitle": "Заповніть форму — і ми зв'яжемося протягом 2 годин",
    "form_name_label": "Ваше ім'я *",
    "form_name_placeholder": "Олександр",
    "form_phone_label": "Телефон *",
    "form_phone_placeholder": "+380 50 123 45 67",
    "form_company_label": "Назва компанії / закладу",
    "form_company_placeholder": "Coffee House",
    "form_type_label": "Тип бізнесу",
    "form_type_cafe": "Кав'ярня",
    "form_type_rest": "Ресторан",
    "form_type_office": "Офіс",
    "form_type_hotel": "Готель",
    "form_type_other": "Інше",
    "form_volume_label": "Орієнтовний обсяг (кг/місяць)",
    "form_volume_5": "до 5 кг",
    "form_volume_10": "5-10 кг",
    "form_volume_20": "10-20 кг",
    "form_volume_50": "20-50 кг",
    "form_volume_50plus": "50+ кг",
    "form_comment_label": "Коментар",
    "form_comment_placeholder": "Розкажіть про ваші потреби...",
    # FAQ
    "faq_title": "Часті питання B2B",
    "faq_q1": "Який мінімальний обсяг замовлення?",
    "faq_a1": "Мінімальне замовлення — 2 кг на місяць. Цього достатньо для невеликої кав'ярні чи офісу.",
    "faq_q2": "Чи можна замовити зразки для дегустації?",
    "faq_a2": "Так! Надсилаємо до 3 зразків по 100г безкоштовно. Це допоможе обрати ідеальний сорт для вашого закладу.",
    "faq_q3": "Як працює навчання бариста?",
    "faq_a3": "Для партнерів рівня \"Бізнес\" і вище — безкоштовний 3-годинний майстер-клас: налаштування обладнання, техніка приготування, латте-арт.",
    "faq_q4": "Які документи ви надаєте?",
    "faq_a4": "Повний пакет для ФОП та ТОВ: рахунок-фактура, видаткова накладна, акт виконаних робіт, сертифікати на продукцію.",
    # Reviews
    "reviews_title": "Що кажуть наші партнери",
    "review_cafe_name": "Coffee Room",
    "review_cafe_desc": "Кав'ярня, Київ",
    "review_cafe_text": "\"Працюємо з EthioDirect вже 2 роки. Якість стабільна, менеджер завжди на зв'язку. Наші гості помітили різницю одразу!\"",
    "review_rest_name": "Gastro House",
    "review_rest_desc": "Ресторан, Одеса",
    "review_rest_text": "\"Команда пройшла навчання від EthioDirect — тепер наша команда готує еспресо на рівні спеціалізованих кав'ярень.\"",
    "review_office_name": "Tech Hub",
    "review_office_desc": "IT-офіс, Львів",
    "review_office_text": "\"150 людей в офісі — і всі задоволені кавою. Доставка як годинник, документи завжди в порядку.\"",
    "toast_success": "Заявку надіслано! Ми зв'яжемося найближчим часом."
}

b2b_extra_en = {
    # Form
    "form_subtitle": "Fill out the form and we'll contact you within 2 hours",
    "form_name_label": "Your name *",
    "form_name_placeholder": "John",
    "form_phone_label": "Phone *",
    "form_phone_placeholder": "+380 50 123 45 67",
    "form_company_label": "Company / Venue name",
    "form_company_placeholder": "Coffee House",
    "form_type_label": "Business type",
    "form_type_cafe": "Cafe",
    "form_type_rest": "Restaurant",
    "form_type_office": "Office",
    "form_type_hotel": "Hotel",
    "form_type_other": "Other",
    "form_volume_label": "Estimated volume (kg/month)",
    "form_volume_5": "up to 5 kg",
    "form_volume_10": "5-10 kg",
    "form_volume_20": "10-20 kg",
    "form_volume_50": "20-50 kg",
    "form_volume_50plus": "50+ kg",
    "form_comment_label": "Comment",
    "form_comment_placeholder": "Tell us about your needs...",
    # FAQ
    "faq_title": "B2B FAQ",
    "faq_q1": "What is the minimum order volume?",
    "faq_a1": "Minimum order is 2 kg per month. This is enough for a small cafe or office.",
    "faq_q2": "Can I order samples for tasting?",
    "faq_a2": "Yes! We send up to 3 samples of 100g for free. This helps you choose the perfect variety for your venue.",
    "faq_q3": "How does barista training work?",
    "faq_a3": "For Business tier partners and above — free 3-hour workshop: equipment setup, brewing technique, latte art.",
    "faq_q4": "What documents do you provide?",
    "faq_a4": "Full package for businesses: invoice, delivery note, completion act, product certificates.",
    # Reviews
    "reviews_title": "What our partners say",
    "review_cafe_name": "Coffee Room",
    "review_cafe_desc": "Cafe, Kyiv",
    "review_cafe_text": "\"We've been working with EthioDirect for 2 years. Quality is consistent, manager is always in touch. Our guests noticed the difference right away!\"",
    "review_rest_name": "Gastro House",
    "review_rest_desc": "Restaurant, Odesa",
    "review_rest_text": "\"Our team was trained by EthioDirect — now we make espresso on par with specialty cafes.\"",
    "review_office_name": "Tech Hub",
    "review_office_desc": "IT Office, Lviv",
    "review_office_text": "\"150 people in the office — and everyone's happy with the coffee. Delivery like clockwork, documents always in order.\"",
    "toast_success": "Request sent! We'll contact you shortly."
}

b2b_extra_ru = {
    # Form
    "form_subtitle": "Заполните форму — и мы свяжемся в течение 2 часов",
    "form_name_label": "Ваше имя *",
    "form_name_placeholder": "Александр",
    "form_phone_label": "Телефон *",
    "form_phone_placeholder": "+380 50 123 45 67",
    "form_company_label": "Название компании / заведения",
    "form_company_placeholder": "Coffee House",
    "form_type_label": "Тип бизнеса",
    "form_type_cafe": "Кофейня",
    "form_type_rest": "Ресторан",
    "form_type_office": "Офис",
    "form_type_hotel": "Отель",
    "form_type_other": "Другое",
    "form_volume_label": "Ориентировочный объем (кг/месяц)",
    "form_volume_5": "до 5 кг",
    "form_volume_10": "5-10 кг",
    "form_volume_20": "10-20 кг",
    "form_volume_50": "20-50 кг",
    "form_volume_50plus": "50+ кг",
    "form_comment_label": "Комментарий",
    "form_comment_placeholder": "Расскажите о ваших потребностях...",
    # FAQ
    "faq_title": "Частые вопросы B2B",
    "faq_q1": "Какой минимальный объем заказа?",
    "faq_a1": "Минимальный заказ — 2 кг в месяц. Этого достаточно для небольшой кофейни или офиса.",
    "faq_q2": "Можно ли заказать образцы для дегустации?",
    "faq_a2": "Да! Отправляем до 3 образцов по 100г бесплатно. Это поможет выбрать идеальный сорт для вашего заведения.",
    "faq_q3": "Как работает обучение бариста?",
    "faq_a3": "Для партнеров уровня \"Бизнес\" и выше — бесплатный 3-часовой мастер-класс: настройка оборудования, техника приготовления, латте-арт.",
    "faq_q4": "Какие документы вы предоставляете?",
    "faq_a4": "Полный пакет для ФЛП и ООО: счет-фактура, расходная накладная, акт выполненных работ, сертификаты на продукцию.",
    # Reviews
    "reviews_title": "Что говорят наши партнеры",
    "review_cafe_name": "Coffee Room",
    "review_cafe_desc": "Кофейня, Киев",
    "review_cafe_text": "\"Работаем с EthioDirect уже 2 года. Качество стабильное, менеджер всегда на связи. Наши гости заметили разницу сразу!\"",
    "review_rest_name": "Gastro House",
    "review_rest_desc": "Ресторан, Одесса",
    "review_rest_text": "\"Команда прошла обучение от EthioDirect — теперь готовим эспрессо на уровне специализированных кофеен.\"",
    "review_office_name": "Tech Hub",
    "review_office_desc": "IT-офис, Львов",
    "review_office_text": "\"150 человек в офисе — и все довольны кофе. Доставка как часы, документы всегда в порядке.\"",
    "toast_success": "Заявка отправлена! Мы свяжемся в ближайшее время."
}

def update_json_file(filepath, key, additions):
    """Add new translations to existing JSON file under specific key"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if key in data:
            data[key].update(additions)
        else:
            data[key] = additions
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"[OK] Updated {filepath}")
        return True
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return False

# Update all files
update_json_file(os.path.join(base_dir, 'uk', 'b2b.json'), 'b2b_page', b2b_extra_uk)
update_json_file(os.path.join(base_dir, 'en', 'b2b.json'), 'b2b_page', b2b_extra_en)
update_json_file(os.path.join(base_dir, 'ru', 'b2b.json'), 'b2b_page', b2b_extra_ru)

print("\nDone!")
