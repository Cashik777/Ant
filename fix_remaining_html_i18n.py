#!/usr/bin/env python3
"""Add data-i18n to all remaining HTML elements across all pages"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def fix_subscription_html():
    filepath = BASE_DIR / "subscription.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix Most Popular badge
    content = re.sub(
        r'>⭐ НАЙПОПУЛЯРНІШИЙ<',
        ' data-i18n="subscription_page.plan_popular_badge">⭐ НАЙПОПУЛЯРНІШИЙ<',
        content
    )
    content = re.sub(
        r'⭐ НАЙПОПУЛЯРНІШИЙ(?!</)',
        '<span data-i18n="subscription_page.plan_popular_badge">⭐ НАЙПОПУЛЯРНІШИЙ</span>',
        content
    )
    
    # Fix g/month
    content = re.sub(
        r'>г/місяць<',
        ' data-i18n="subscription_page.g_month">г/місяць<',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed: {filepath.name}")

def fix_gift_html():
    filepath = BASE_DIR / "gift-certificates.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix create button
    content = re.sub(
        r'>СТВОРИТИ СЕРТИФІКАТ<',
        ' data-i18n="gift_page.create_btn">СТВОРИТИ СЕРТИФІКАТ<',
        content, flags=re.IGNORECASE
    )
    
    # Fix placeholders
    content = re.sub(
        r'placeholder="Наприклад: Олена"',
        'placeholder="Наприклад: Олена" data-i18n-placeholder="gift_page.name_placeholder"',
        content
    )
    content = re.sub(
        r'placeholder="Напишіть кілька теплих слів\.\.\."',
        'placeholder="Напишіть кілька теплих слів..." data-i18n-placeholder="gift_page.message_placeholder"',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed: {filepath.name}")

def fix_about_html():
    filepath = BASE_DIR / "about.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # Add i18n to various elements
    replacements = [
        (r'>Наші цінності<', ' data-i18n="about_page.values_title">Наші цінності<'),
        (r'>Наш шлях<', ' data-i18n="about_page.path_title">Наш шлях<'),
        (r'>Наш процес<', ' data-i18n="about_page.process_title">Наш процес<'),
        (r'>Наша команда<', ' data-i18n="about_page.team_title">Наша команда<'),
        (r'>Готові спробувати\?<', ' data-i18n="about_page.try_title">Готові спробувати?<'),
        (r'>Якість<', ' data-i18n="about_page.value_quality">Якість<'),
        (r'>Чесність<', ' data-i18n="about_page.value_honesty">Чесність<'),
        (r'>Сталий розвиток<', ' data-i18n="about_page.value_sustainability">Сталий розвиток<'),
        (r'>Чому Ефіопія\?<', ' data-i18n="about_page.why_ethiopia_title">Чому Ефіопія?<'),
        (r'>Прямі закупки<', ' data-i18n="about_page.feature_direct">Прямі закупки<'),
        (r'>Свіжа обсмажка<', ' data-i18n="about_page.feature_fresh">Свіжа обсмажка<'),
        (r'>85\+ балів SCA<', ' data-i18n="about_page.feature_sca">85+ балів SCA<'),
        (r'>Обрати каву<', ' data-i18n="about_page.try_btn">Обрати каву<')
    ]
    
    for pattern, replacement in replacements:
        if 'data-i18n' not in content or replacement not in content:
            content = re.sub(pattern, replacement, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath.name}")
    else:
        print(f"No changes: {filepath.name}")

def fix_blog_main():
    filepath = BASE_DIR / "blog.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # Fix hero title and subtitle
    content = re.sub(
        r'<h1([^>]*)>Кавові історії</h1>',
        '<h1\\1 data-i18n="blog_page.hero_title">Кавові історії</h1>',
        content
    )
    
    # Fix category buttons
    content = re.sub(
        r'>Всі статті<',
        ' data-i18n="blog_page.all_posts">Всі статті<',
        content
    )
    
    # Fix read more buttons
    content = re.sub(
        r'>Читати далі →<',
        ' data-i18n="blog_page.read_more">Читати далі →<',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath.name}")
    else:
        print(f"No changes: {filepath.name}")

def fix_index_html():
    filepath = BASE_DIR / "index.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # Fix lead magnet section
    content = re.sub(
        r'>Ваш email<',
        ' data-i18n="lead_magnet.email_placeholder">Ваш email<',
        content
    )
    content = re.sub(
        r'placeholder="Ваш email"',
        'placeholder="Ваш email" data-i18n-placeholder="lead_magnet.email_placeholder"',
        content
    )
    content = re.sub(
        r'>Отримати безкоштовно<',
        ' data-i18n="lead_magnet.btn">Отримати безкоштовно<',
        content
    )
    content = re.sub(
        r'>людей вже завантажили<',
        ' data-i18n="lead_magnet.downloaded">людей вже завантажили<',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath.name}")
    else:
        print(f"No changes: {filepath.name}")

def main():
    fix_subscription_html()
    fix_gift_html()
    fix_about_html()
    fix_blog_main()
    fix_index_html()
    print("All done!")

if __name__ == "__main__":
    main()
