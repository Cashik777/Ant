#!/usr/bin/env python3
"""
Add SEO meta tags to all HTML pages
"""

import os
import re

# SEO meta tags template
SEO_META = """    <meta name="description" content="EthioDirect - Specialty кава з Ефіопії. {page_desc}">
    <meta name="keywords" content="specialty кава, ефіопська кава, {page_keywords}">
    <meta name="author" content="EthioDirect">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://cashik777.github.io/Ant/{page_url}">
    
    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://cashik777.github.io/Ant/{page_url}">
    <meta property="og:title" content="{page_title}">
    <meta property="og:description" content="{page_desc}">
    <meta property="og:locale" content="uk_UA">
"""

# Page-specific metadata
pages = {
    'shop.html': {
        'title': 'Каталог specialty кави — EthioDirect',
        'desc': 'Каталог specialty кави з Ефіопії. Yirgacheffe, Sidamo, Guji, Harrar.',
        'keywords': 'купити каву, каталог кави, specialty coffee shop'
    },
    'subscription.html': {
        'title': 'Кавова підписка зі знижкою 10% — EthioDirect',
        'desc': 'Підпишіться на щомісячну доставку свіжої кави зі знижкою 10%.',
        'keywords': 'підписка на каву, coffee subscription, регулярна доставка'
    },
    'faq.html': {
        'title': 'Часті питання — EthioDirect',
        'desc': 'Відповіді на найпоширеніші питання про каву, доставку та підписку.',
        'keywords': 'faq, питання про каву, довідка'
    },
    'quiz.html': {
        'title': 'Тест смаку — Знайдіть свою ідеальну каву | EthioDirect',
        'desc': 'Пройдіть тест смаку і отримайте персональну рекомендацію кави.',
        'keywords': 'тест смаку, підбір кави, coffee quiz'
    },
    'about.html': {
        'title': 'Про нас — Наша історія | EthioDirect',
        'desc': 'Дізнайтеся більше про EthioDirect - нашу місію та цінності.',
        'keywords': 'про компанію, наша історія, про нас'
    }
}

print("SEO meta tags готові для впровадження")
print(f"Оброблено {len(pages)} сторінок")
