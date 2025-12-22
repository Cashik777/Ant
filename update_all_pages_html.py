#!/usr/bin/env python3
"""
Add data-i18n attributes to all remaining pages
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def update_gift_certificates():
    filepath = BASE_DIR / "gift-certificates.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hero
    content = content.replace(
        '🎁 ІДЕАЛЬНИЙ ПОДАРУНОК',
        '<span data-i18n="gift_page.hero_badge">🎁 ІДЕАЛЬНИЙ ПОДАРУНОК</span>'
    )
    content = re.sub(
        r'<h1 style="font-size:3rem; color:white; margin-bottom:20px; line-height:1\.2;">\s*Подарункові сертифікати\s*</h1>',
        '<h1 style="font-size:3rem; color:white; margin-bottom:20px; line-height:1.2;" data-i18n="gift_page.hero_title">Подарункові сертифікати</h1>',
        content
    )
    content = re.sub(
        r'<p style="font-size:1\.2rem; opacity:0\.9; margin-bottom:30px;">\s*Подаруйте справжню ефіопську каву\. Сертифікат доставляється миттєво на email у красивому\s*PDF-форматі\.\s*</p>',
        '<p style="font-size:1.2rem; opacity:0.9; margin-bottom:30px;" data-i18n="gift_page.hero_text">Подаруйте справжню ефіопську каву. Сертифікат доставляється миттєво на email у красивому PDF-форматі.</p>',
        content
    )
    content = re.sub(
        r'>Створити сертифікат\s*</a>',
        ' data-i18n="gift_page.create_btn">Створити сертифікат</a>',
        content
    )
    
    # Preview
    content = re.sub(
        r'<h3 style="color:white; font-size:1\.3rem; margin-bottom:10px;">Подарунковий сертифікат</h3>',
        '<h3 style="color:white; font-size:1.3rem; margin-bottom:10px;" data-i18n="gift_page.preview_title">Подарунковий сертифікат</h3>',
        content
    )
    content = re.sub(
        r'<h2 class="text-center" style="margin-bottom:50px;">Створіть сертифікат</h2>',
        '<h2 class="text-center" style="margin-bottom:50px;" data-i18n="gift_page.create_title">Створіть сертифікат</h2>',
        content
    )
    
    # Form labels
    content = re.sub(
        r'<label style="display:block; margin-bottom:15px; font-weight:600;">Оберіть номінал:</label>',
        '<label style="display:block; margin-bottom:15px; font-weight:600;" data-i18n="gift_page.amount_label">Оберіть номінал:</label>',
        content
    )
    content = re.sub(
        r'<label style="display:block; margin-bottom:8px; font-weight:600;">Кому \(ім\'я\s*отримувача\):</label>',
        '<label style="display:block; margin-bottom:8px; font-weight:600;" data-i18n="gift_page.recipient_label">Кому (ім\'я отримувача):</label>',
        content
    )
    content = re.sub(
        r'<label style="display:block; margin-bottom:8px; font-weight:600;">Від кого:</label>',
        '<label style="display:block; margin-bottom:8px; font-weight:600;" data-i18n="gift_page.sender_label">Від кого:</label>',
        content
    )
    content = re.sub(
        r'<label style="display:block; margin-bottom:8px; font-weight:600;">Побажання\s*\(опціонально\):</label>',
        '<label style="display:block; margin-bottom:8px; font-weight:600;" data-i18n="gift_page.message_label">Побажання (опціонально):</label>',
        content
    )
    content = re.sub(
        r'<label style="display:block; margin-bottom:8px; font-weight:600;">Email для доставки\s*сертифікату:</label>',
        '<label style="display:block; margin-bottom:8px; font-weight:600;" data-i18n="gift_page.email_label">Email для доставки сертифікату:</label>',
        content
    )
    
    # Preview section
    content = re.sub(
        r'<h3 style="margin-bottom:20px; text-align:center;">Попередній перегляд</h3>',
        '<h3 style="margin-bottom:20px; text-align:center;" data-i18n="gift_page.preview_label">Попередній перегляд</h3>',
        content
    )
    content = re.sub(
        r'<h2 style="color:white; font-size:1\.8rem; margin-bottom:10px;">Подарунковий\s*сертифікат</h2>',
        '<h2 style="color:white; font-size:1.8rem; margin-bottom:10px;" data-i18n="gift_page.preview_title">Подарунковий сертифікат</h2>',
        content
    )
    content = re.sub(
        r'<div style="font-size:1\.5rem; color:white; margin-top:-10px;">гривень</div>',
        '<div style="font-size:1.5rem; color:white; margin-top:-10px;" data-i18n="gift_page.uah">гривень</div>',
        content
    )
    content = re.sub(
        r'<span style="color:#999; font-size:0\.85rem;">Кому:</span>',
        '<span style="color:#999; font-size:0.85rem;" data-i18n="gift_page.to_label">Кому:</span>',
        content
    )
    content = re.sub(
        r'<span style="color:#999; font-size:0\.85rem;">Від:</span>',
        '<span style="color:#999; font-size:0.85rem;" data-i18n="gift_page.from_label">Від:</span>',
        content
    )
    content = re.sub(
        r'<span\s*style="color:#999; font-size:0\.8rem; text-transform:uppercase; letter-spacing:1px;">Код\s*сертифікату</span>',
        '<span style="color:#999; font-size:0.8rem; text-transform:uppercase; letter-spacing:1px;" data-i18n="gift_page.code_label">Код сертифікату</span>',
        content
    )
    
    # Why gift section
    content = re.sub(
        r'<h2 style="margin-bottom:50px;">Чому це ідеальний подарунок\?</h2>',
        '<h2 style="margin-bottom:50px;" data-i18n="gift_page.why_ideal_title">Чому це ідеальний подарунок?</h2>',
        content
    )
    content = re.sub(
        r'<h3 style="margin-bottom:15px;">Для кавоманів</h3>',
        '<h3 style="margin-bottom:15px;" data-i18n="gift_page.ideal_lovers_title">Для кавоманів</h3>',
        content
    )
    content = re.sub(
        r'<p style="color:#666;">Specialty кава 85\+ SCA балів — те, що вони справді оцінять</p>',
        '<p style="color:#666;" data-i18n="gift_page.ideal_lovers_text">Specialty кава 85+ SCA балів — те, що вони справді оцінять</p>',
        content
    )
    content = re.sub(
        r'<h3 style="margin-bottom:15px;">Миттєво</h3>',
        '<h3 style="margin-bottom:15px;" data-i18n="gift_page.ideal_instant_title">Миттєво</h3>',
        content
    )
    content = re.sub(
        r'<p style="color:#666;">PDF сертифікат на email за хвилину — не треба нікуди їхати</p>',
        '<p style="color:#666;" data-i18n="gift_page.ideal_instant_text">PDF сертифікат на email за хвилину — не треба нікуди їхати</p>',
        content
    )
    content = re.sub(
        r'<h3 style="margin-bottom:15px;">Гнучкість</h3>',
        '<h3 style="margin-bottom:15px;" data-i18n="gift_page.ideal_flexible_title">Гнучкість</h3>',
        content
    )
    content = re.sub(
        r'<p style="color:#666;">Дійсний рік, можна використати частинами на кілька покупок</p>',
        '<p style="color:#666;" data-i18n="gift_page.ideal_flexible_text">Дійсний рік, можна використати частинами на кілька покупок</p>',
        content
    )
    content = re.sub(
        r'<h3 style="margin-bottom:15px;">Краса дизайну</h3>',
        '<h3 style="margin-bottom:15px;" data-i18n="gift_page.ideal_design_title">Краса дизайну</h3>',
        content
    )
    content = re.sub(
        r'<p style="color:#666;">Стильний PDF, який приємно дарувати і отримувати</p>',
        '<p style="color:#666;" data-i18n="gift_page.ideal_design_text">Стильний PDF, який приємно дарувати і отримувати</p>',
        content
    )
    
    # CTA section
    content = re.sub(
        r'<h2 style="color:white; margin-bottom:20px;">Залишились питання\?</h2>',
        '<h2 style="color:white; margin-bottom:20px;" data-i18n="gift_page.questions_title">Залишились питання?</h2>',
        content
    )
    content = re.sub(
        r'<p style="color:rgba\(255,255,255,0\.8\); margin-bottom:30px;">Напишіть нам — допоможемо обрати ідеальний\s*подарунок!</p>',
        '<p style="color:rgba(255,255,255,0.8); margin-bottom:30px;" data-i18n="gift_page.questions_text">Напишіть нам — допоможемо обрати ідеальний подарунок!</p>',
        content
    )
    content = re.sub(
        r'>\s*<i class="fas fa-comments" style="margin-right:10px;"></i> Зв\'язатися з нами\s*</a>',
        '><i class="fas fa-comments" style="margin-right:10px;"></i> <span data-i18n="gift_page.contact_btn">Зв\'язатися з нами</span></a>',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_about():
    filepath = BASE_DIR / "about.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Hero section
    content = re.sub(
        r'<span class="hero-badge"><i class="fas fa-heart"></i> НАША ІСТОРІЯ</span>',
        '<span class="hero-badge"><i class="fas fa-heart"></i> <span data-i18n="about_page.hero_badge">НАША ІСТОРІЯ</span></span>',
        content
    )
    content = re.sub(
        r'<h1>Від ефіопських гір до вашої чашки</h1>',
        '<h1 data-i18n="about_page.hero_title">Від ефіопських гір до вашої чашки</h1>',
        content
    )
    content = re.sub(
        r'<p class="hero-text">Ми — команда кавоманів, які побудували прямий ланцюг поставок з Ефіопії,\s*щоб ви могли насолоджуватися справжнім смаком specialty кави без посередників\.</p>',
        '<p class="hero-text" data-i18n="about_page.hero_text">Ми — команда кавоманів, які побудували прямий ланцюг поставок з Ефіопії, щоб ви могли насолоджуватися справжнім смаком specialty кави без посередників.</p>',
        content
    )
    content = content.replace(
        '<div class="hero-feature"><i class="fas fa-check-circle"></i> Прямі закупки</div>',
        '<div class="hero-feature"><i class="fas fa-check-circle"></i> <span data-i18n="about_page.feature_direct">Прямі закупки</span></div>'
    )
    content = content.replace(
        '<div class="hero-feature"><i class="fas fa-check-circle"></i> Свіжа обсмажка</div>',
        '<div class="hero-feature"><i class="fas fa-check-circle"></i> <span data-i18n="about_page.feature_fresh">Свіжа обсмажка</span></div>'
    )
    content = content.replace(
        '<div class="hero-feature"><i class="fas fa-check-circle"></i> 85+ балів SCA</div>',
        '<div class="hero-feature"><i class="fas fa-check-circle"></i> <span data-i18n="about_page.feature_sca">85+ балів SCA</span></div>'
    )
    
    # Stats
    content = re.sub(
        r'<div class="stat-label">Задоволених клієнтів</div>',
        '<div class="stat-label" data-i18n="about_page.stat_clients">Задоволених клієнтів</div>',
        content
    )
    content = re.sub(
        r'<div class="stat-label">Балів SCA Specialty</div>',
        '<div class="stat-label" data-i18n="about_page.stat_sca">Балів SCA Specialty</div>',
        content
    )
    content = re.sub(
        r'<div class="stat-label">Від замовлення до доставки</div>',
        '<div class="stat-label" data-i18n="about_page.stat_delivery">Від замовлення до доставки</div>',
        content
    )
    content = re.sub(
        r'<div class="stat-label">Пряме походження</div>',
        '<div class="stat-label" data-i18n="about_page.stat_direct">Пряме походження</div>',
        content
    )
    
    # Mission
    content = re.sub(
        r'<h2>Чому Ефіопія\?</h2>',
        '<h2 data-i18n="about_page.why_ethiopia_title">Чому Ефіопія?</h2>',
        content
    )
    
    # Tags
    content = content.replace(
        '>🌸 Квіткові\n                                ноти</span>',
        ' data-i18n="about_page.tag_floral">🌸 Квіткові ноти</span>'
    )
    content = content.replace(
        '>🍓 Ягідний\n                                смак</span>',
        ' data-i18n="about_page.tag_berry">🍓 Ягідний смак</span>'
    )
    content = content.replace(
        '>🍫 Шоколадна\n                                солодкість</span>',
        ' data-i18n="about_page.tag_chocolate">🍫 Шоколадна солодкість</span>'
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_quiz():
    filepath = BASE_DIR / "quiz.html"
    if not filepath.exists():
        print(f"Skipping {filepath} - not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Main replacements
    content = re.sub(
        r'>Тест: Яка кава вам підходить\?<',
        ' data-i18n="quiz_page.title">Тест: Яка кава вам підходить?<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_b2b():
    filepath = BASE_DIR / "b2b.html"
    if not filepath.exists():
        print(f"Skipping {filepath} - not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Title
    content = re.sub(
        r'>B2B рішення<',
        ' data-i18n="b2b_page.title">B2B рішення<',
        content
    )
    content = re.sub(
        r'>Specialty кава для вашого бізнесу<',
        ' data-i18n="b2b_page.subtitle">Specialty кава для вашого бізнесу<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_account():
    filepath = BASE_DIR / "account.html"
    if not filepath.exists():
        print(f"Skipping {filepath} - not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Особистий кабінет<',
        ' data-i18n="account_page.title">Особистий кабінет<',
        content
    )
    content = re.sub(
        r'>Вхід<',
        ' data-i18n="account_page.login_title">Вхід<',
        content
    )
    content = re.sub(
        r'>Реєстрація<',
        ' data-i18n="account_page.register_title">Реєстрація<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_contacts():
    filepath = BASE_DIR / "contacts.html"
    if not filepath.exists():
        print(f"Skipping {filepath} - not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Контакти<',
        ' data-i18n="contacts_page.title">Контакти<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_faq():
    filepath = BASE_DIR / "faq.html"
    if not filepath.exists():
        print(f"Skipping {filepath} - not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Часті питання<',
        ' data-i18n="faq_page.title">Часті питання<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

def update_delivery():
    filepath = BASE_DIR / "delivery.html"
    if not filepath.exists():
        print(f"Skipping {filepath} - not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(
        r'>Доставка та оплата<',
        ' data-i18n="delivery_page.title">Доставка та оплата<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

if __name__ == "__main__":
    print("Updating HTML files with data-i18n attributes...")
    update_gift_certificates()
    update_about()
    update_quiz()
    update_b2b()
    update_account()
    update_contacts()
    update_faq()
    update_delivery()
    print("Done!")
