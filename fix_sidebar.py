#!/usr/bin/env python3
"""
Fix sidebar issues:
1. Replace emojis with professional arrow indicators
2. Fix data-i18n key for "Зміст"
3. Clean up product card
"""

import re

filepath = "articles/ethiopia-coffee-origin.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# New professional TOC HTML without emojis
new_toc = '''        <aside class="article-sidebar-left">
            <div class="toc-widget">
                <h4>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M4 6h16M4 12h16M4 18h7"/>
                    </svg>
                    <span data-i18n="blog.table_of_contents">Зміст статті</span>
                </h4>
                <ul>
                    <li><a href="#section-legend" data-i18n="articles.ethiopia_origin.h2_1">Легенда про Калді</a></li>
                    <li><a href="#section-geography" data-i18n="articles.ethiopia_origin.h2_2">Географія та клімат</a></li>
                    <li><a href="#section-regions" data-i18n="articles.ethiopia_origin.h2_3">Регіони вирощування</a></li>
                    <li><a href="#section-processing" data-i18n="articles.ethiopia_origin.h2_4">Методи обробки</a></li>
                    <li><a href="#section-taste" data-i18n="articles.ethiopia_origin.h2_5">Смакові профілі</a></li>
                    <li><a href="#section-ceremony" data-i18n="articles.ethiopia_origin.h2_6">Кавова церемонія</a></li>
                    <li><a href="#section-today" data-i18n="articles.ethiopia_origin.h2_7">Ефіопія сьогодні</a></li>
                </ul>
                <a href="../blog.html" class="toc-more-link">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                    <span data-i18n="blog.more_articles">Більше історій</span>
                </a>
            </div>
        </aside>'''

# New product HTML without emojis
new_product = '''        <aside class="article-sidebar-right">
            <!-- Product Card -->
            <div class="product-widget">
                <div class="product-widget-label" data-i18n="common.recommended">Рекомендуємо</div>
                <div class="product-widget-image">
                    <img src="https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=400" alt="Ethiopia Yirgacheffe">
                    <span class="product-widget-badge">SCA 86+</span>
                </div>
                <div class="product-widget-content">
                    <h5>Ethiopia Yirgacheffe</h5>
                    <div class="product-rating">
                        <span class="stars">★★★★★</span>
                        <span class="count">(127)</span>
                    </div>
                    <div class="product-meta">
                        <span data-i18n="shop.notes">Ноти:</span> Бергамот, жасмин, персик<br>
                        <span data-i18n="shop.processing">Обробка:</span> Мита
                    </div>
                    <div class="product-price">
                        <span class="price-current">420 ₴</span>
                        <span class="price-old">490 ₴</span>
                    </div>
                    <a href="../shop.html" class="btn-widget">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/>
                            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/>
                        </svg>
                        <span data-i18n="shop.add_to_cart">Додати в кошик</span>
                    </a>
                </div>
            </div>
            
            <!-- Subscription CTA -->
            <div class="subscribe-widget">
                <div class="subscribe-widget-content">
                    <span class="discount-badge">-10%</span>
                    <h5 data-i18n="subscription.sidebar_title">Підписка на каву</h5>
                    <p data-i18n="subscription.sidebar_text">Свіжа обсмажка щомісяця</p>
                    <a href="../subscription.html" class="btn-subscribe">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                            <circle cx="12" cy="7" r="4"/>
                        </svg>
                        <span data-i18n="subscription.subscribe_btn">Оформити</span>
                    </a>
                </div>
            </div>
        </aside>'''

# Also update the CSS to remove emoji-related styles and fix h4 icon
css_fix = '''
        .toc-widget h4 {
            font-family: 'Playfair Display', serif;
            font-size: 13px;
            color: #D4AF37;
            margin-bottom: 18px;
            text-transform: uppercase;
            letter-spacing: 2px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .toc-widget h4 svg {
            stroke: #D4AF37;
        }
        
        .toc-widget h4::before {
            display: none;
        }'''

# Replace old TOC
old_toc_pattern = r'<aside class="article-sidebar-left">.*?</aside>'
content = re.sub(old_toc_pattern, new_toc, content, flags=re.DOTALL)
print("TOC replaced - emojis removed")

# Replace old product
old_product_pattern = r'<aside class="article-sidebar-right">.*?</aside>'
content = re.sub(old_product_pattern, new_product, content, flags=re.DOTALL)
print("Product replaced - cleaned up")

# Fix h4 CSS (remove ::before emoji)
old_h4_css = r"\.toc-widget h4::before \{[^}]+\}"
content = re.sub(old_h4_css, '', content, flags=re.DOTALL)
print("CSS fixed")

# Update h4 styling
old_h4_style = r"(\.toc-widget h4 \{[^}]+gap: 8px;)"
content = re.sub(old_h4_style, '''        .toc-widget h4 {
            font-family: 'Playfair Display', serif;
            font-size: 13px;
            color: #D4AF37;
            margin-bottom: 18px;
            text-transform: uppercase;
            letter-spacing: 2px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .toc-widget h4 svg {
            stroke: #D4AF37;
            flex-shrink: 0;''', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Emojis replaced with SVG icons, translations fixed.")
