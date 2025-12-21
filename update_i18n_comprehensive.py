#!/usr/bin/env python3
"""
Comprehensive i18n updater for EthioDirect website.
Adds data-i18n attributes to all remaining hardcoded text elements.
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

# Skip template files
SKIP_FILES = {'footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html', '_header_template.html'}

def update_subscription_section(content):
    """Update subscription comparison section with i18n keys."""
    
    # Subscription subtitle
    content = re.sub(
        r'<p style="max-width:600px; margin:0 auto; margin-top:20px; color:var\(--text-light\);">[\s\n]*Ваш персональний сомельє\. Кава з\'являється у вас вдома саме тоді, коли потрібна\.[\s\n]*</p>',
        '<p style="max-width:600px; margin:0 auto; margin-top:20px; color:var(--text-light);" data-i18n="subscription.subtitle">Ваш персональний сомельє. Кава з\'являється у вас вдома саме тоді, коли потрібна.</p>',
        content
    )
    
    # Regular purchase title
    content = content.replace(
        '<h4 style="color:var(--text-muted); margin-bottom:15px; font-weight:400;">Разова покупка</h4>',
        '<h4 style="color:var(--text-muted); margin-bottom:15px; font-weight:400;" data-i18n="subscription.regular_title">Разова покупка</h4>'
    )
    
    # Regular purchase items
    content = content.replace(
        '<li style="padding:8px 0;">✗ Повна ціна</li>',
        '<li style="padding:8px 0;" data-i18n="subscription.regular_price">✗ Повна ціна</li>'
    )
    content = content.replace(
        '<li style="padding:8px 0;">✗ Доставка від 500₴</li>',
        '<li style="padding:8px 0;" data-i18n="subscription.regular_delivery">✗ Доставка від 500₴</li>'
    )
    content = content.replace(
        '<li style="padding:8px 0;">✗ Потрібно пам\'ятати замовити</li>',
        '<li style="padding:8px 0;" data-i18n="subscription.regular_remember">✗ Потрібно пам\'ятати замовити</li>'
    )
    
    # Subscription badge
    content = re.sub(
        r'font-weight:700;">[\s\n]*ВИГІДНІШЕ</div>',
        'font-weight:700;" data-i18n="subscription.sub_badge">ВИГІДНІШЕ</div>',
        content
    )
    
    # Subscription title
    content = content.replace(
        '<h4 style="color:var(--primary); margin-bottom:15px; font-weight:700;">Підписка</h4>',
        '<h4 style="color:var(--primary); margin-bottom:15px; font-weight:700;" data-i18n="subscription.sub_title">Підписка</h4>'
    )
    
    # Cancel note
    content = re.sub(
        r'<i class="fas fa-lock" style="margin-right:5px;"></i> Скасувати або змінити можна будь-коли в 1 клік',
        '<i class="fas fa-lock" style="margin-right:5px;"></i> <span data-i18n="subscription.cancel_note">Скасувати або змінити можна будь-коли в 1 клік</span>',
        content
    )
    
    return content

def update_reviews_section(content):
    """Update reviews section with i18n keys."""
    
    # Featured review
    content = re.sub(
        r'<div class="big-quote">"Це не просто напій, це подорож\. Я відчула різницю з першого ковтка\. Тепер[\s\n]*магазинна кава для мене просто не існує\."</div>',
        '<div class="big-quote" data-i18n="reviews.featured_text">"Це не просто напій, це подорож. Я відчула різницю з першого ковтка. Тепер магазинна кава для мене просто не існує."</div>',
        content
    )
    
    # Reviewer meta
    content = re.sub(
        r'<div class="reviewer-meta">— Олена К\., Київ • Підписка на Guji Natural</div>',
        '<div class="reviewer-meta" data-i18n="reviews.featured_author">— Олена К., Київ • Підписка на Guji Natural</div>',
        content
    )
    
    # Join text
    content = re.sub(
        r'Приєднуйтесь до <strong style="color:var\(--primary\);">2500\+</strong> задоволених кавоманів',
        '<span data-i18n="reviews.join_text">Приєднуйтесь до</span> <strong style="color:var(--primary);">2500+</strong> <span data-i18n="reviews.coffee_lovers">задоволених кавоманів</span>',
        content
    )
    
    # Subscribe CTA button
    content = re.sub(
        r'<i class="fas fa-heart"></i>[\s\n]*Оформити підписку зі знижкою 10%',
        '<i class="fas fa-heart"></i> <span data-i18n="reviews.subscribe_cta">Оформити підписку зі знижкою 10%</span>',
        content
    )
    
    return content

def update_lead_section(content):
    """Update lead magnet section with i18n keys."""
    
    # Lead text paragraph
    content = re.sub(
        r'<p>Завантажте наш <strong>безкоштовний PDF-гід</strong> «Як обирати ефіопську каву»\.</p>',
        '<p data-i18n="lead.text">Завантажте наш безкоштовний PDF-гід «Як обирати ефіопську каву».</p>',
        content
    )
    
    # Email placeholder
    content = re.sub(
        r'<input type="email" placeholder="Ваш Email" required>',
        '<input type="email" placeholder="Ваш Email" data-i18n="lead.placeholder" data-i18n-placeholder required>',
        content
    )
    
    return content

def update_footer_section(content):
    """Update footer section with i18n keys."""
    
    # Footer description
    content = re.sub(
        r'<p style="color:#aaa; line-height:1\.8; margin-bottom:20px;">Ми доставляємо справжню specialty каву[\s\n]*прямо[\s\n]*з ефіопських ферм до вашого дому\. Свіжа обсмажка, чесна ціна, любов до кави\.</p>',
        '<p style="color:#aaa; line-height:1.8; margin-bottom:20px;" data-i18n="footer.description">Ми доставляємо справжню specialty каву прямо з ефіопських ферм до вашого дому. Свіжа обсмажка, чесна ціна, любов до кави.</p>',
        content
    )
    
    # Newsletter text
    content = re.sub(
        r'<p style="color:#aaa; margin-bottom:15px; font-size:0\.9rem;">Отримуйте акції, новинки та поради щодо[\s\n]*заварювання</p>',
        '<p style="color:#aaa; margin-bottom:15px; font-size:0.9rem;" data-i18n="footer.newsletter_text">Отримуйте акції, новинки та поради щодо заварювання</p>',
        content
    )
    
    # Newsletter email placeholder
    content = re.sub(
        r'<input type="email" placeholder="Ваш email" required>',
        '<input type="email" placeholder="Ваш email" data-i18n="footer.newsletter_placeholder" data-i18n-placeholder required>',
        content
    )
    
    # Location
    content = re.sub(
        r'<i class="fas fa-map-marker-alt"></i> Одеса, Україна',
        '<i class="fas fa-map-marker-alt"></i> <span data-i18n="footer.location">Одеса, Україна</span>',
        content
    )
    
    # Hours
    content = re.sub(
        r'<li><i class="fas fa-clock"></i> Пн-Пт: 9:00-18:00</li>',
        '<li><i class="fas fa-clock"></i> <span data-i18n="topbar.hours">Пн-Пт: 9:00-18:00</span></li>',
        content
    )
    
    return content

def update_mini_cart(content):
    """Update mini-cart with i18n keys."""
    
    # Cart title
    content = re.sub(
        r'<h4>Ваш кошик</h4>',
        '<h4 data-i18n="cart.title">Ваш кошик</h4>',
        content
    )
    
    # Cart items count
    content = re.sub(
        r'<span class="mini-cart-count" id="mini-cart-count">0 товарів</span>',
        '<span class="mini-cart-count" id="mini-cart-count"><span>0</span> <span data-i18n="cart.items">товарів</span></span>',
        content
    )
    
    # Subtotal
    content = re.sub(
        r'<strong>Разом:</strong>',
        '<strong data-i18n="cart.subtotal">Разом:</strong>',
        content
    )
    
    # Free shipping progress
    content = re.sub(
        r'<i class="fas fa-truck"></i> До безкоштовної доставки: <strong>500 ₴</strong>',
        '<i class="fas fa-truck"></i> <span data-i18n="cart.free_shipping_progress">До безкоштовної доставки:</span> <strong>500 ₴</strong>',
        content
    )
    
    # Checkout button
    content = re.sub(
        r'<i class="fas fa-shopping-cart"></i> Оформити замовлення',
        '<i class="fas fa-shopping-cart"></i> <span data-i18n="cart.checkout">Оформити замовлення</span>',
        content
    )
    
    return content

def update_hero_badge(content):
    """Fix hero badge to properly use i18n."""
    
    content = re.sub(
        r'<div class="premium-badge" data-i18n="hero\.badge">[\s\n]*<i class="fas fa-star"></i>[\s\n]*100% SPECIALTY КАВА[\s\n]*</div>',
        '<div class="premium-badge"><i class="fas fa-star"></i> <span data-i18n="hero.badge">100% SPECIALTY КАВА</span></div>',
        content
    )
    
    return content

def update_html_file(filepath):
    """Update a single HTML file with i18n attributes."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Apply all updates
        content = update_subscription_section(content)
        content = update_reviews_section(content)
        content = update_lead_section(content)
        content = update_footer_section(content)
        content = update_mini_cart(content)
        content = update_hero_badge(content)
        
        # Check if changes were made
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [UPDATED] {filepath.name}")
            return True
        else:
            print(f"  [OK] {filepath.name}")
            return False
            
    except Exception as e:
        print(f"  [ERROR] {filepath.name}: {e}")
        return False

def main():
    print("=" * 60)
    print("Comprehensive i18n Update for All HTML Pages")
    print("=" * 60)
    
    # Find all HTML files
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    html_files = [f for f in html_files if f.name not in SKIP_FILES]
    
    print(f"\nProcessing {len(html_files)} HTML files...\n")
    
    updated = 0
    for filepath in sorted(html_files):
        if update_html_file(filepath):
            updated += 1
    
    print("\n" + "=" * 60)
    print(f"DONE! Updated {updated} files")
    print("=" * 60)

if __name__ == '__main__':
    main()
