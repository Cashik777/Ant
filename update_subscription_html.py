#!/usr/bin/env python3
"""
Add data-i18n attributes to subscription.html
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Replacements for subscription.html
REPLACEMENTS = [
    # Hero section
    ('-10% НА КОЖНУ ДОСТАВКУ', 'subscription_page.hero_badge', '-10% НА КОЖНУ ДОСТАВКУ'),
    # Plans section - Starter
    ('>Starter<', 'subscription_page.plan_starter', 'Starter'),
    ('>Для знайомства<', 'subscription_page.plan_starter_desc', 'Для знайомства'),
    ('>г/місяць<', 'subscription_page.plan_per_month', 'г/місяць'),
    ('>1 пачка 250г<', 'subscription_page.plan_pack_1', '1 пачка 250г'),
    ('>Раз на місяць<', 'subscription_page.plan_monthly', 'Раз на місяць'),
    ('>Безкоштовна доставка<', 'subscription_page.plan_free_shipping', 'Безкоштовна доставка'),
    # Popular badge
    ('>⭐ НАЙПОПУЛЯРНІШИЙ<', 'subscription_page.plan_popular_badge', '⭐ НАЙПОПУЛЯРНІШИЙ'),
    # Coffee Lover
    ('>Coffee Lover<', 'subscription_page.plan_coffee_lover', 'Coffee Lover'),
    ('>Ідеальний баланс<', 'subscription_page.plan_lover_desc', 'Ідеальний баланс'),
    ('>2 пачки по 250г<', 'subscription_page.plan_packs_2', '2 пачки по 250г'),
    ('>Раз на 2 тижні<', 'subscription_page.plan_biweekly', 'Раз на 2 тижні'),
    ('>Пріоритетна підтримка<', 'subscription_page.plan_priority', 'Пріоритетна підтримка'),
    # Coffee Addict
    ('>Coffee Addict<', 'subscription_page.plan_addict', 'Coffee Addict'),
    ('>Для справжніх цінителів<', 'subscription_page.plan_addict_desc', 'Для справжніх цінителів'),
    ('>4 пачки по 250г<', 'subscription_page.plan_packs_4', '4 пачки по 250г'),
    ('>Щотижня<', 'subscription_page.plan_weekly', 'Щотижня'),
    ('>Ексклюзивні лоти<', 'subscription_page.plan_exclusive', 'Ексклюзивні лоти'),
    # How it works steps
    ('>Оберіть план</h3>', 'subscription_page.step1_title', 'Оберіть план'),
    ('>Визначте, скільки кави вам потрібно</p>', 'subscription_page.step1_text', 'Визначте, скільки кави вам потрібно'),
    ('>Налаштуйте</h3>', 'subscription_page.step2_title', 'Налаштуйте'),
    ('>Обсмажка, помол, частота — все під вас</p>', 'subscription_page.step2_text', 'Обсмажка, помол, частота — все під вас'),
    ('>Отримуйте</h3>', 'subscription_page.step3_title', 'Отримуйте'),
    ('>Свіжа кава приходить автоматично</p>', 'subscription_page.step3_text', 'Свіжа кава приходить автоматично'),
    ('>Насолоджуйтесь!</h3>', 'subscription_page.step4_title', 'Насолоджуйтесь!'),
    ('>Ми дбаємо про вашу каву</p>', 'subscription_page.step4_text', 'Ми дбаємо про вашу каву'),
    # FAQ
    ('>Чи можу я скасувати підписку?<', 'subscription_page.faq_cancel_q', 'Чи можу я скасувати підписку?'),
    ('>Так, ви можете скасувати', 'subscription_page.faq_cancel_a', 'Так, ви можете скасувати або поставити на паузу підписку в будь-який момент з особистого кабінету.'),
    ('>Чи можу я змінити каву?<', 'subscription_page.faq_change_q', 'Чи можу я змінити каву?'),
    ('>Звичайно! Ви можете змінити', 'subscription_page.faq_change_a', 'Звичайно! Ви можете змінити сорт кави, обсмажку та помол перед кожною доставкою.'),
    ('>Коли списуються кошти?<', 'subscription_page.faq_payment_q', 'Коли списуються кошти?'),
    ('>Оплата списується автоматично', 'subscription_page.faq_payment_a', 'Оплата списується автоматично за 2 дні до запланованої доставки.'),
]

def update_subscription():
    filepath = BASE_DIR / "subscription.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add data-i18n to specific elements using regex
    
    # How it works h3 titles
    content = re.sub(
        r'<h3 style="margin-bottom:10px;">Оберіть план</h3>',
        '<h3 style="margin-bottom:10px;" data-i18n="subscription_page.step1_title">Оберіть план</h3>',
        content
    )
    content = re.sub(
        r'<h3 style="margin-bottom:10px;">Налаштуйте</h3>',
        '<h3 style="margin-bottom:10px;" data-i18n="subscription_page.step2_title">Налаштуйте</h3>',
        content
    )
    content = re.sub(
        r'<h3 style="margin-bottom:10px;">Отримуйте</h3>',
        '<h3 style="margin-bottom:10px;" data-i18n="subscription_page.step3_title">Отримуйте</h3>',
        content
    )
    content = re.sub(
        r'<h3 style="margin-bottom:10px;">Насолоджуйтесь!</h3>',
        '<h3 style="margin-bottom:10px;" data-i18n="subscription_page.step4_title">Насолоджуйтесь!</h3>',
        content
    )
    
    # How it works p texts
    content = re.sub(
        r'<p style="color:var\(--text-muted\);">Визначте, скільки кави вам потрібно</p>',
        '<p style="color:var(--text-muted);" data-i18n="subscription_page.step1_text">Визначте, скільки кави вам потрібно</p>',
        content
    )
    content = re.sub(
        r'<p style="color:var\(--text-muted\);">Обсмажка, помол, частота — все під вас</p>',
        '<p style="color:var(--text-muted);" data-i18n="subscription_page.step2_text">Обсмажка, помол, частота — все під вас</p>',
        content
    )
    content = re.sub(
        r'<p style="color:var\(--text-muted\);">Свіжа кава приходить автоматично</p>',
        '<p style="color:var(--text-muted);" data-i18n="subscription_page.step3_text">Свіжа кава приходить автоматично</p>',
        content
    )
    content = re.sub(
        r'<p style="color:var\(--text-muted\);">Ми дбаємо про вашу каву</p>',
        '<p style="color:var(--text-muted);" data-i18n="subscription_page.step4_text">Ми дбаємо про вашу каву</p>',
        content
    )
    
    # Plan names
    content = re.sub(
        r'<h3 style="font-size:1.5rem; margin-bottom:10px;">Starter</h3>',
        '<h3 style="font-size:1.5rem; margin-bottom:10px;" data-i18n="subscription_page.plan_starter">Starter</h3>',
        content
    )
    content = re.sub(
        r'<p style="color:var\(--text-muted\); margin-bottom:20px;">Для знайомства</p>',
        '<p style="color:var(--text-muted); margin-bottom:20px;" data-i18n="subscription_page.plan_starter_desc">Для знайомства</p>',
        content
    )
    content = re.sub(
        r'<h3 style="font-size:1.5rem; margin-bottom:10px; color:white;">Coffee Lover</h3>',
        '<h3 style="font-size:1.5rem; margin-bottom:10px; color:white;" data-i18n="subscription_page.plan_coffee_lover">Coffee Lover</h3>',
        content
    )
    content = re.sub(
        r'<p style="opacity:0.8; margin-bottom:20px;">Ідеальний баланс</p>',
        '<p style="opacity:0.8; margin-bottom:20px;" data-i18n="subscription_page.plan_lover_desc">Ідеальний баланс</p>',
        content
    )
    content = re.sub(
        r'<h3 style="font-size:1.5rem; margin-bottom:10px;">Coffee Addict</h3>',
        '<h3 style="font-size:1.5rem; margin-bottom:10px;" data-i18n="subscription_page.plan_addict">Coffee Addict</h3>',
        content
    )
    content = re.sub(
        r'<p style="color:var\(--text-muted\); margin-bottom:20px;">Для справжніх цінителів</p>',
        '<p style="color:var(--text-muted); margin-bottom:20px;" data-i18n="subscription_page.plan_addict_desc">Для справжніх цінителів</p>',
        content
    )
    
    # Popular badge
    content = re.sub(
        r'>⭐ НАЙПОПУЛЯРНІШИЙ<',
        ' data-i18n="subscription_page.plan_popular_badge">⭐ НАЙПОПУЛЯРНІШИЙ<',
        content
    )
    
    # List items in plans (simplified)
    list_items = [
        ('1 пачка 250г', 'subscription_page.plan_pack_1'),
        ('Раз на місяць', 'subscription_page.plan_monthly'),
        ('2 пачки по 250г', 'subscription_page.plan_packs_2'),
        ('Раз на 2 тижні', 'subscription_page.plan_biweekly'),
        ('Пріоритетна підтримка', 'subscription_page.plan_priority'),
        ('4 пачки по 250г', 'subscription_page.plan_packs_4'),
        ('Щотижня', 'subscription_page.plan_weekly'),
        ('Ексклюзивні лоти', 'subscription_page.plan_exclusive'),
    ]
    
    for text, key in list_items:
        pattern = rf'(<li[^>]*>)\s*(<i[^>]*></i>)\s*{re.escape(text)}\s*(</li>)'
        replacement = rf'\1\2 <span data-i18n="{key}">{text}</span>\3'
        content = re.sub(pattern, replacement, content)
    
    # Bezkoshtovna dostavka - appears multiple times
    content = content.replace(
        '<i class="fas fa-check" style="color:var(--success);"></i> Безкоштовна доставка',
        '<i class="fas fa-check" style="color:var(--success);"></i> <span data-i18n="subscription_page.plan_free_shipping">Безкоштовна доставка</span>'
    )
    content = content.replace(
        '<i class="fas fa-check" style="color:var(--secondary);"></i> Безкоштовна доставка',
        '<i class="fas fa-check" style="color:var(--secondary);"></i> <span data-i18n="subscription_page.plan_free_shipping">Безкоштовна доставка</span>'
    )
    
    # FAQ section
    content = re.sub(
        r'<strong>Чи можу я скасувати підписку\?</strong>',
        '<strong data-i18n="subscription_page.faq_cancel_q">Чи можу я скасувати підписку?</strong>',
        content
    )
    content = re.sub(
        r'<p style="margin:10px 0 0; color:var\(--text-muted\);">Так, ви можете скасувати або поставити на\s+паузу підписку в будь-який момент з особистого кабінету\.</p>',
        '<p style="margin:10px 0 0; color:var(--text-muted);" data-i18n="subscription_page.faq_cancel_a">Так, ви можете скасувати або поставити на паузу підписку в будь-який момент з особистого кабінету.</p>',
        content
    )
    content = re.sub(
        r'<strong>Чи можу я змінити каву\?</strong>',
        '<strong data-i18n="subscription_page.faq_change_q">Чи можу я змінити каву?</strong>',
        content
    )
    content = re.sub(
        r'<p style="margin:10px 0 0; color:var\(--text-muted\);">Звичайно! Ви можете змінити сорт кави,\s+обсмажку та помол перед кожною доставкою\.</p>',
        '<p style="margin:10px 0 0; color:var(--text-muted);" data-i18n="subscription_page.faq_change_a">Звичайно! Ви можете змінити сорт кави, обсмажку та помол перед кожною доставкою.</p>',
        content
    )
    content = re.sub(
        r'<strong>Коли списуються кошти\?</strong>',
        '<strong data-i18n="subscription_page.faq_payment_q">Коли списуються кошти?</strong>',
        content
    )
    content = re.sub(
        r'<p style="margin:10px 0 0; color:var\(--text-muted\);">Оплата списується автоматично за 2 дні до\s+запланованої доставки\.</p>',
        '<p style="margin:10px 0 0; color:var(--text-muted);" data-i18n="subscription_page.faq_payment_a">Оплата списується автоматично за 2 дні до запланованої доставки.</p>',
        content
    )
    
    # Buttons  
    content = re.sub(
        r'<button class="btn btn-outline" style="width:100%;">Обрати план</button>',
        '<button class="btn btn-outline" style="width:100%;" data-i18n="subscription_page.choose_plan">Обрати план</button>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath}")

if __name__ == "__main__":
    update_subscription()
    print("Done!")
