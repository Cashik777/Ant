#!/usr/bin/env python3
"""
Add sidebar layout to ethiopia-coffee-origin.html
- Left: Sticky Table of Contents
- Right: Recommended Product Card
"""

import re

filepath = "articles/ethiopia-coffee-origin.html"

# Read file
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# CSS for sidebar layout
sidebar_css = '''
        /* Article Layout with Sidebars */
        .article-layout {
            display: flex;
            justify-content: center;
            gap: 30px;
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        
        .article-sidebar-left {
            width: 200px;
            flex-shrink: 0;
            position: sticky;
            top: 100px;
            height: fit-content;
            display: none;
        }
        
        .article-sidebar-right {
            width: 280px;
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
        
        /* Table of Contents */
        .toc-widget {
            background: rgba(42, 31, 10, 0.03);
            border-radius: 12px;
            padding: 20px;
            border-left: 3px solid #D4AF37;
        }
        
        .toc-widget h4 {
            font-family: 'Playfair Display', serif;
            font-size: 14px;
            color: #2a1f0a;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .toc-widget ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        
        .toc-widget li {
            margin-bottom: 10px;
        }
        
        .toc-widget a {
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            color: #5a4a2a;
            text-decoration: none;
            display: block;
            padding: 5px 0;
            transition: all 0.2s ease;
            border-left: 2px solid transparent;
            padding-left: 10px;
            margin-left: -10px;
        }
        
        .toc-widget a:hover {
            color: #D4AF37;
            border-left-color: #D4AF37;
        }
        
        /* Product Card Widget */
        .product-widget {
            background: white;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 4px 20px rgba(42, 31, 10, 0.08);
            border: 1px solid rgba(42, 31, 10, 0.08);
        }
        
        .product-widget-label {
            font-family: 'Inter', sans-serif;
            font-size: 11px;
            color: #D4AF37;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
        }
        
        .product-widget img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 12px;
            margin-bottom: 15px;
        }
        
        .product-widget h5 {
            font-family: 'Playfair Display', serif;
            font-size: 18px;
            color: #2a1f0a;
            margin-bottom: 8px;
        }
        
        .product-widget .product-meta {
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            color: #8a7a5a;
            margin-bottom: 12px;
        }
        
        .product-widget .product-price {
            font-family: 'Inter', sans-serif;
            font-size: 20px;
            font-weight: 600;
            color: #2a1f0a;
            margin-bottom: 15px;
        }
        
        .product-widget .btn-widget {
            display: block;
            width: 100%;
            padding: 12px 20px;
            background: linear-gradient(135deg, #D4AF37, #B8962E);
            color: white;
            text-align: center;
            border-radius: 8px;
            text-decoration: none;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        .product-widget .btn-widget:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4);
        }
        
        /* Adjust main article body */
        .article-main {
            max-width: 800px;
            flex-grow: 1;
        }
'''

# HTML for left sidebar (TOC)
toc_html = '''
        <aside class="article-sidebar-left">
            <div class="toc-widget">
                <h4 data-i18n="common.contents">Зміст</h4>
                <ul>
                    <li><a href="#section-legend" data-i18n="articles.ethiopia_origin.h2_1">Легенда про Калді</a></li>
                    <li><a href="#section-geography" data-i18n="articles.ethiopia_origin.h2_2">Географія та клімат</a></li>
                    <li><a href="#section-regions" data-i18n="articles.ethiopia_origin.h2_3">Регіони вирощування</a></li>
                    <li><a href="#section-processing" data-i18n="articles.ethiopia_origin.h2_4">Методи обробки</a></li>
                    <li><a href="#section-taste" data-i18n="articles.ethiopia_origin.h2_5">Смакові профілі</a></li>
                    <li><a href="#section-ceremony" data-i18n="articles.ethiopia_origin.h2_6">Кавова церемонія</a></li>
                    <li><a href="#section-today" data-i18n="articles.ethiopia_origin.h2_7">Ефіопія сьогодні</a></li>
                </ul>
            </div>
        </aside>
'''

# HTML for right sidebar (Product Card)
product_html = '''
        <aside class="article-sidebar-right">
            <div class="product-widget">
                <div class="product-widget-label" data-i18n="common.recommended">Рекомендуємо</div>
                <img src="https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=400" alt="Yirgacheffe Coffee">
                <h5>Ethiopia Yirgacheffe</h5>
                <div class="product-meta">
                    <span data-i18n="product.region">Регіон:</span> Yirgacheffe<br>
                    <span data-i18n="product.notes">Ноти:</span> Бергамот, жасмин, персик
                </div>
                <div class="product-price">420 ₴</div>
                <a href="../shop.html" class="btn-widget" data-i18n="common.order_now">Замовити</a>
            </div>
        </aside>
'''

# Find where to insert CSS (before </style>)
style_end = content.find('</style>')
if style_end != -1:
    content = content[:style_end] + sidebar_css + "\n    " + content[style_end:]
    print("CSS added")

# Find <article class="article-body"> and wrap it in layout
article_pattern = r'(<article class="article-body">)'
article_match = re.search(article_pattern, content)
if article_match:
    # Insert layout wrapper before article
    insertion_point = article_match.start()
    
    # Find </article> to close the wrapper
    article_end = content.find('</article>', insertion_point)
    if article_end != -1:
        # Extract article content
        article_content = content[insertion_point:article_end + len('</article>')]
        
        # Wrap in new layout
        new_layout = f'''
        <div class="article-layout">
{toc_html}
            <div class="article-main">
{article_content}
            </div>
{product_html}
        </div>
'''
        # Replace
        content = content[:insertion_point] + new_layout + content[article_end + len('</article>'):]
        print("Layout structure added")

# Save file
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! File updated:", filepath)
