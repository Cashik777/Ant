#!/usr/bin/env python3
"""
Enhance sidebar visuals for better conversion and clickability
- More prominent CTAs
- Better visual hierarchy
- Subscription widget addition
- Animated hover effects
"""

import re

filepath = "articles/ethiopia-coffee-origin.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Enhanced CSS - more visual, better CTAs
enhanced_css = '''
        /* ========================================
           ENHANCED SIDEBAR STYLES - v2
           Focus: Conversion + Visual Appeal
        ======================================== */
        
        /* Article Layout with Sidebars */
        .article-layout {
            display: flex;
            justify-content: center;
            gap: 40px;
            max-width: 1440px;
            margin: 0 auto;
            padding: 50px 30px;
        }
        
        .article-sidebar-left {
            width: 220px;
            flex-shrink: 0;
            position: sticky;
            top: 100px;
            height: fit-content;
            display: none;
        }
        
        .article-sidebar-right {
            width: 300px;
            flex-shrink: 0;
            position: sticky;
            top: 100px;
            height: fit-content;
            display: none;
        }
        
        @media (min-width: 1200px) {
            .article-sidebar-left,
            .article-sidebar-right {
                display: block;
            }
        }
        
        /* ========================================
           TABLE OF CONTENTS - Enhanced
        ======================================== */
        .toc-widget {
            background: linear-gradient(135deg, rgba(42, 31, 10, 0.04), rgba(212, 175, 55, 0.08));
            border-radius: 16px;
            padding: 24px;
            border-left: 4px solid #D4AF37;
            box-shadow: 0 4px 20px rgba(42, 31, 10, 0.06);
            transition: all 0.3s ease;
        }
        
        .toc-widget:hover {
            box-shadow: 0 8px 30px rgba(42, 31, 10, 0.1);
            transform: translateY(-2px);
        }
        
        .toc-widget h4 {
            font-family: 'Playfair Display', serif;
            font-size: 13px;
            color: #D4AF37;
            margin-bottom: 18px;
            text-transform: uppercase;
            letter-spacing: 2px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .toc-widget h4::before {
            content: '📖';
            font-size: 16px;
        }
        
        .toc-widget ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .toc-widget li {
            margin-bottom: 6px;
        }
        
        .toc-widget a {
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: #5a4a2a;
            text-decoration: none;
            display: block;
            padding: 10px 12px;
            transition: all 0.25s ease;
            border-radius: 8px;
            background: transparent;
            position: relative;
            overflow: hidden;
        }
        
        .toc-widget a::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 3px;
            background: #D4AF37;
            transform: scaleY(0);
            transition: transform 0.25s ease;
        }
        
        .toc-widget a:hover {
            color: #2a1f0a;
            background: rgba(212, 175, 55, 0.15);
            padding-left: 16px;
        }
        
        .toc-widget a:hover::before {
            transform: scaleY(1);
        }
        
        /* More Articles Link */
        .toc-more-link {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            margin-top: 20px;
            padding: 12px;
            background: linear-gradient(135deg, #2a1f0a, #3d2d14);
            color: white !important;
            border-radius: 10px;
            font-weight: 500;
            font-size: 13px;
        }
        
        .toc-more-link:hover {
            background: linear-gradient(135deg, #3d2d14, #4a3620) !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(42, 31, 10, 0.3);
        }
        
        /* ========================================
           PRODUCT CARD - Enhanced Premium Look
        ======================================== */
        .product-widget {
            background: linear-gradient(180deg, #fff 0%, #faf8f3 100%);
            border-radius: 20px;
            padding: 0;
            box-shadow: 0 8px 40px rgba(42, 31, 10, 0.12);
            border: 1px solid rgba(212, 175, 55, 0.2);
            overflow: hidden;
            transition: all 0.4s ease;
        }
        
        .product-widget:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 50px rgba(42, 31, 10, 0.18);
        }
        
        .product-widget-label {
            background: linear-gradient(135deg, #D4AF37, #B8962E);
            color: white;
            font-family: 'Inter', sans-serif;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 2px;
            padding: 10px 20px;
            text-align: center;
            font-weight: 600;
        }
        
        .product-widget-image {
            position: relative;
            overflow: hidden;
        }
        
        .product-widget img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            transition: transform 0.5s ease;
        }
        
        .product-widget:hover img {
            transform: scale(1.08);
        }
        
        .product-widget-badge {
            position: absolute;
            top: 12px;
            right: 12px;
            background: rgba(42, 31, 10, 0.9);
            color: #D4AF37;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 600;
            backdrop-filter: blur(10px);
        }
        
        .product-widget-content {
            padding: 20px;
        }
        
        .product-widget h5 {
            font-family: 'Playfair Display', serif;
            font-size: 20px;
            color: #2a1f0a;
            margin-bottom: 8px;
            line-height: 1.3;
        }
        
        .product-widget .product-meta {
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: #8a7a5a;
            margin-bottom: 15px;
            line-height: 1.6;
        }
        
        .product-widget .product-meta strong {
            color: #5a4a2a;
        }
        
        .product-widget .product-rating {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 15px;
        }
        
        .product-widget .product-rating .stars {
            color: #D4AF37;
            font-size: 14px;
            letter-spacing: 2px;
        }
        
        .product-widget .product-rating .count {
            font-size: 12px;
            color: #8a7a5a;
        }
        
        .product-widget .product-price {
            display: flex;
            align-items: baseline;
            gap: 10px;
            margin-bottom: 18px;
        }
        
        .product-widget .price-current {
            font-family: 'Playfair Display', serif;
            font-size: 28px;
            font-weight: 700;
            color: #2a1f0a;
        }
        
        .product-widget .price-old {
            font-size: 16px;
            color: #aaa;
            text-decoration: line-through;
        }
        
        .product-widget .btn-widget {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            padding: 15px 24px;
            background: linear-gradient(135deg, #D4AF37, #B8962E);
            color: white;
            text-align: center;
            border-radius: 12px;
            text-decoration: none;
            font-family: 'Inter', sans-serif;
            font-size: 15px;
            font-weight: 600;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        }
        
        .product-widget .btn-widget:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(212, 175, 55, 0.5);
        }
        
        .product-widget .btn-widget svg,
        .product-widget .btn-widget i {
            font-size: 18px;
        }
        
        /* ========================================
           SUBSCRIPTION WIDGET - Premium CTA
        ======================================== */
        .subscribe-widget {
            margin-top: 25px;
            background: linear-gradient(135deg, #2a1f0a, #3d2d14);
            border-radius: 20px;
            padding: 24px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .subscribe-widget::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(212, 175, 55, 0.1) 0%, transparent 70%);
            animation: pulse-glow 3s ease-in-out infinite;
        }
        
        @keyframes pulse-glow {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        
        .subscribe-widget-content {
            position: relative;
            z-index: 1;
        }
        
        .subscribe-widget .discount-badge {
            display: inline-block;
            background: #D4AF37;
            color: #2a1f0a;
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .subscribe-widget h5 {
            font-family: 'Playfair Display', serif;
            font-size: 18px;
            color: white;
            margin-bottom: 10px;
        }
        
        .subscribe-widget p {
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: rgba(255,255,255,0.7);
            margin-bottom: 18px;
            line-height: 1.5;
        }
        
        .subscribe-widget .btn-subscribe {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            width: 100%;
            padding: 14px 20px;
            background: white;
            color: #2a1f0a;
            border-radius: 12px;
            text-decoration: none;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .subscribe-widget .btn-subscribe:hover {
            background: #D4AF37;
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(212, 175, 55, 0.4);
        }
        
        /* Adjust main article body */
        .article-main {
            max-width: 800px;
            flex-grow: 1;
        }
'''

# Enhanced TOC HTML
toc_html = '''
        <aside class="article-sidebar-left">
            <div class="toc-widget">
                <h4 data-i18n="common.contents">Зміст статті</h4>
                <ul>
                    <li><a href="#section-legend">🏔️ Легенда про Калді</a></li>
                    <li><a href="#section-geography">🌍 Географія та клімат</a></li>
                    <li><a href="#section-regions">📍 Регіони вирощування</a></li>
                    <li><a href="#section-processing">⚙️ Методи обробки</a></li>
                    <li><a href="#section-taste">☕ Смакові профілі</a></li>
                    <li><a href="#section-ceremony">🎭 Кавова церемонія</a></li>
                    <li><a href="#section-today">📈 Ефіопія сьогодні</a></li>
                </ul>
                <a href="../blog.html" class="toc-more-link">
                    📚 <span data-i18n="common.more_articles">Більше історій</span>
                </a>
            </div>
        </aside>
'''

# Enhanced Product + Subscription HTML
product_html = '''
        <aside class="article-sidebar-right">
            <!-- Product Card -->
            <div class="product-widget">
                <div class="product-widget-label">✨ Рекомендуємо спробувати</div>
                <div class="product-widget-image">
                    <img src="https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=400" alt="Ethiopia Yirgacheffe">
                    <span class="product-widget-badge">SCA 86+</span>
                </div>
                <div class="product-widget-content">
                    <h5>Ethiopia Yirgacheffe</h5>
                    <div class="product-rating">
                        <span class="stars">★★★★★</span>
                        <span class="count">(127 відгуків)</span>
                    </div>
                    <div class="product-meta">
                        <strong>Ноти:</strong> Бергамот, жасмин, персик<br>
                        <strong>Обробка:</strong> Мита
                    </div>
                    <div class="product-price">
                        <span class="price-current">420 ₴</span>
                        <span class="price-old">490 ₴</span>
                    </div>
                    <a href="../shop.html" class="btn-widget">
                        <i class="fas fa-shopping-cart"></i>
                        <span data-i18n="common.add_to_cart">Додати в кошик</span>
                    </a>
                </div>
            </div>
            
            <!-- Subscription CTA -->
            <div class="subscribe-widget">
                <div class="subscribe-widget-content">
                    <span class="discount-badge">-10% знижка</span>
                    <h5 data-i18n="subscription.title">Підписка на каву</h5>
                    <p data-i18n="subscription.benefit">Свіжа кава щомісяця прямо до дверей. Безкоштовна доставка!</p>
                    <a href="../subscription.html" class="btn-subscribe">
                        <i class="fas fa-gift"></i>
                        <span data-i18n="common.subscribe">Оформити підписку</span>
                    </a>
                </div>
            </div>
        </aside>
'''

# Remove old sidebar CSS first (between /* Article Layout and .article-main)
old_css_pattern = r'/\* Article Layout with Sidebars \*/.*?/\* Adjust main article body \*/\s*\.article-main \{[^}]+\}'
content = re.sub(old_css_pattern, enhanced_css, content, flags=re.DOTALL)
print("CSS enhanced")

# Remove old sidebars and replace with new
# Find and replace left sidebar
old_toc_pattern = r'<aside class="article-sidebar-left">.*?</aside>'
content = re.sub(old_toc_pattern, toc_html.strip(), content, flags=re.DOTALL)
print("TOC enhanced")

# Find and replace right sidebar
old_product_pattern = r'<aside class="article-sidebar-right">.*?</aside>'
content = re.sub(old_product_pattern, product_html.strip(), content, flags=re.DOTALL)
print("Product widget enhanced")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Enhanced sidebars saved.")
