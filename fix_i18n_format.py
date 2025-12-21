"""
Fix i18n attributes to use dot notation and expand translation coverage.
Changes: hero_title -> hero.title, hero_subtitle -> hero.subtitle, etc.
"""

import os
import re
from pathlib import Path

def fix_i18n_attributes(content):
    """Convert underscore notation to dot notation for i18n keys."""
    # Hero section fixes
    replacements = [
        ('data-i18n="hero_badge"', 'data-i18n="hero.badge"'),
        ('data-i18n="hero_title"', 'data-i18n="hero.title"'),
        ('data-i18n="hero_subtitle"', 'data-i18n="hero.subtitle"'),
        ('data-i18n="hero_text"', 'data-i18n="hero.text"'),
        ('data-i18n="hero_cta"', 'data-i18n="hero.cta"'),
        ('data-i18n="hero_secondary"', 'data-i18n="hero.quiz_text"'),
        ('data-i18n="hero_quiz_link"', 'data-i18n="hero.quiz_link"'),
        ('data-i18n="trust_farmers"', 'data-i18n="trust.farmers"'),
        ('data-i18n="trust_specialty"', 'data-i18n="trust.specialty"'),
        ('data-i18n="about_stats_clients"', 'data-i18n="trust.clients"'),
        # Fix duplicate data-i18n attributes (only keep first one)
        (' data-i18n="footer.certificates"', ''),
        (' data-i18n="footer.about"', ''),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    return content

def add_philosophy_i18n(content):
    """Add data-i18n to Philosophy section."""
    # Philosophy title
    content = content.replace(
        '<h2>Це більше, ніж кава. <span>Це — Шлях.</span></h2>',
        '<h2><span data-i18n="philosophy.title">Це більше, ніж кава.</span> <span data-i18n="philosophy.subtitle">Це — Шлях.</span></h2>'
    )
    
    # Philosophy cards
    content = content.replace(
        '<h3>Specialty 85+</h3>',
        '<h3 data-i18n="philosophy.specialty_title">Specialty 85+</h3>'
    )
    content = content.replace(
        '<p>Тільки добірне зерно класу Specialty. Ніяких компромісів з якістю.</p>',
        '<p data-i18n="philosophy.specialty_text">Тільки добірне зерно класу Specialty. Ніяких компромісів з якістю.</p>'
    )
    content = content.replace(
        '<h3>Вогонь Обсмажки</h3>',
        '<h3 data-i18n="philosophy.roast_title">Вогонь Обсмажки</h3>'
    )
    content = content.replace(
        '<p>Смажимо лише під ваше замовлення. Ви отримуєте її на піку смаку.</p>',
        '<p data-i18n="philosophy.roast_text">Смажимо лише під ваше замовлення. Ви отримуєте її на піку смаку.</p>'
    )
    content = content.replace(
        '<h3>Чесна Ціна</h3>',
        '<h3 data-i18n="philosophy.price_title">Чесна Ціна</h3>'
    )
    content = content.replace(
        '<p>Прямий імпорт без посередників. Ви платите фермеру, а не перекупнику.</p>',
        '<p data-i18n="philosophy.price_text">Прямий імпорт без посередників. Ви платите фермеру, а не перекупнику.</p>'
    )
    
    # Philosophy CTA
    content = content.replace(
        'Обрати свій сорт\n                </a>',
        '<span data-i18n="philosophy.cta">Обрати свій сорт</span>\n                </a>'
    )
    
    return content

def add_collection_i18n(content):
    """Add data-i18n to Collection section."""
    content = content.replace(
        '<h2>Найкраще з ефіопських висот</h2>',
        '<h2 data-i18n="collection.title">Найкраще з ефіопських висот</h2>'
    )
    content = content.replace(
        '>Всі лоти</button>',
        ' data-i18n="collection.filter_all">Всі лоти</button>'
    )
    content = content.replace(
        '>Фруктові</button>',
        ' data-i18n="collection.filter_fruity">Фруктові</button>'
    )
    content = content.replace(
        '>Шоколадні</button>',
        ' data-i18n="collection.filter_chocolate">Шоколадні</button>'
    )
    content = content.replace(
        '>Квіткові</button>',
        ' data-i18n="collection.filter_floral">Квіткові</button>'
    )
    content = content.replace(
        '>Всі сорти в наявності</a>',
        ' data-i18n="collection.view_all">Всі сорти в наявності</a>'
    )
    
    return content

def add_subscription_i18n(content):
    """Add data-i18n to Subscription section."""
    content = content.replace(
        '<h2>Кавовий <span>Клуб</span></h2>',
        '<h2><span data-i18n="subscription.title">Кавовий Клуб</span></h2>'
    )
    
    # Subscription steps
    content = content.replace(
        '<h4>1. Тест смаку</h4>',
        '<h4 data-i18n="subscription.step1_title">1. Тест смаку</h4>'
    )
    content = content.replace(
        '<p>Відповідайте на 5 питань про ваші вподобання. Алгоритм підбере ідеальний сорт.</p>',
        '<p data-i18n="subscription.step1_text">Відповідайте на 5 питань про ваші вподобання. Алгоритм підбере ідеальний сорт.</p>'
    )
    content = content.replace(
        '<h4>2. Персоналізація</h4>',
        '<h4 data-i18n="subscription.step2_title">2. Персоналізація</h4>'
    )
    content = content.replace(
        '<p>Обираєте частоту (1-4 рази на місяць) та обсяг. Перша доставка — через 3 дні.</p>',
        '<p data-i18n="subscription.step2_text">Обираєте частоту (1-4 рази на місяць) та обсяг. Перша доставка — через 3 дні.</p>'
    )
    content = content.replace(
        '<h4>3. Ритуал</h4>',
        '<h4 data-i18n="subscription.step3_title">3. Ритуал</h4>'
    )
    content = content.replace(
        '<p>Кава приходить автоматично. Скасувати можна в 1 клік. Знижка 10% на підписку.</p>',
        '<p data-i18n="subscription.step3_text">Кава приходить автоматично. Скасувати можна в 1 клік. Знижка 10% на підписку.</p>'
    )
    
    # Subscription CTA
    content = content.replace(
        'Розпочати тест смаку\n                </a>',
        '<span data-i18n="subscription.cta">Розпочати тест смаку</span>\n                </a>'
    )
    
    return content

def add_stats_i18n(content):
    """Add data-i18n to Stats section."""
    content = content.replace(
        '<div class="stat-label">Задоволених клієнтів</div>',
        '<div class="stat-label" data-i18n="stats.clients">Задоволених клієнтів</div>'
    )
    content = content.replace(
        '<div class="stat-label">Бали SCA Specialty</div>',
        '<div class="stat-label" data-i18n="stats.sca">Бали SCA Specialty</div>'
    )
    content = content.replace(
        '<div class="stat-label">Від замовлення до чашки</div>',
        '<div class="stat-label" data-i18n="stats.delivery">Від замовлення до чашки</div>'
    )
    content = content.replace(
        '<div class="stat-label">Пряме походження</div>',
        '<div class="stat-label" data-i18n="stats.origin">Пряме походження</div>'
    )
    
    return content

def add_lead_i18n(content):
    """Add data-i18n to Lead Magnet section."""
    content = content.replace(
        '<h3>Почніть свій шлях у світі Specialty</h3>',
        '<h3 data-i18n="lead.title">Почніть свій шлях у світі Specialty</h3>'
    )
    content = content.replace(
        '>Отримати гід</button>',
        ' data-i18n="lead.cta">Отримати гід</button>'
    )
    
    return content

def process_file(filepath):
    """Process a single HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Fix existing i18n attributes
    content = fix_i18n_attributes(content)
    
    # Add new i18n attributes to sections (only for index.html)
    if 'index.html' in str(filepath):
        content = add_philosophy_i18n(content)
        content = add_collection_i18n(content)
        content = add_subscription_i18n(content)
        content = add_stats_i18n(content)
        content = add_lead_i18n(content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = Path('.')
    
    # Find all HTML files
    html_files = list(base_dir.glob('*.html'))
    html_files += list(base_dir.glob('blog/*.html'))
    html_files += list(base_dir.glob('articles/*.html'))
    
    print(f"Processing {len(html_files)} HTML files...")
    
    updated = 0
    for f in html_files:
        if process_file(f):
            print(f"  Updated: {f}")
            updated += 1
    
    print(f"\nDone! Updated {updated} files.")

if __name__ == '__main__':
    main()
