#!/usr/bin/env python3
"""
Update what-is-specialty.html with data-i18n attributes for ALL content
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
ARTICLE_PATH = BASE_DIR / "articles" / "what-is-specialty.html"

def update_article():
    with open(ARTICLE_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    key = "articles.what_is_specialty"
    
    # Replace subtitle/lead paragraph
    content = re.sub(
        r'(<p class="article-lead">)Розбираємось, чим відрізняється specialty кава від звичайної, як її оцінюють\s+професіонали та чому вона варта кожної копійки\.(</p>)',
        rf'\1<span data-i18n="{key}.subtitle">Розбираємось, чим відрізняється specialty кава від звичайної, як її оцінюють професіонали та чому вона варта кожної копійки.</span>\2',
        content,
        flags=re.DOTALL
    )
    
    # Replace intro paragraph
    content = re.sub(
        r'<p>Якщо ви коли-небудь замислювались, чому одна пачка кави коштує 100 гривень',
        f'<p data-i18n="{key}.intro">Якщо ви коли-небудь замислювались, чому одна пачка кави коштує 100 гривень',
        content
    )
    
    # Replace H2 headings
    h2_replacements = [
        ('Що означає "Specialty"?', 'h2_what_means'),
        ('Як оцінюють каву професіонали', 'h2_grading'),
        ('Чому specialty кава дорожча?', 'h2_why_expensive'),
        ('Як розпізнати справжню specialty каву', 'h2_recognize'),
        ('Чи варто переплачувати?', 'h2_worth_it'),
    ]
    
    for text, i18n_key in h2_replacements:
        escaped = re.escape(text)
        content = re.sub(
            rf'<h2>({escaped})</h2>',
            rf'<h2 data-i18n="{key}.{i18n_key}">\1</h2>',
            content
        )
    
    # Replace H3 headings
    h3_replacements = [
        ('1. Терруар та клімат', 'h3_terroir'),
        ('2. Ручний збір', 'h3_harvest'),
        ('3. Обробка', 'h3_processing'),
        ('4. Свіжа обсмажка', 'h3_roasting'),
        ('5. Fair Trade', 'h3_fairtrade'),
    ]
    
    for text, i18n_key in h3_replacements:
        escaped = re.escape(text)
        content = re.sub(
            rf'<h3>({escaped})</h3>',
            rf'<h3 data-i18n="{key}.{i18n_key}">\1</h3>',
            content
        )
    
    # Replace key paragraphs (targeting specific content)
    paragraph_replacements = [
        (r'<p>Термін "specialty coffee" офіційно з\'явився', f'<p data-i18n="{key}.p_history">Термін "specialty coffee" офіційно з\'явився'),
        (r'<p><strong>Specialty кава</strong> — це кава, яка отримала', f'<p data-i18n="{key}.p_definition"><strong>Specialty кава</strong> — це кава, яка отримала'),
        (r'<p>Оцінювання кави — це справжня наука', f'<p data-i18n="{key}.p_grading_intro">Оцінювання кави — це справжня наука'),
        (r'<p>Кожен критерій оцінюється від 6 до 10 балів', f'<p data-i18n="{key}.p_grading_note">Кожен критерій оцінюється від 6 до 10 балів'),
        (r'<p>Висока ціна specialty кави', f'<p data-i18n="{key}.p_expensive_intro">Висока ціна specialty кави'),
        (r'<p>Найкраща кава росте на висоті', f'<p data-i18n="{key}.p_terroir">Найкраща кава росте на висоті'),
        (r'<p>На відміну від комерційної кави', f'<p data-i18n="{key}.p_harvest">На відміну від комерційної кави'),
        (r'<p>Кожен етап — від ферментації', f'<p data-i18n="{key}.p_processing">Кожен етап — від ферментації'),
        (r'<p>Specialty кава має пити оптимальний', f'<p data-i18n="{key}.p_roasting">Specialty кава має пити оптимальний'),
        (r'<p>Фермери, які виробляють specialty каву', f'<p data-i18n="{key}.p_fairtrade">Фермери, які виробляють specialty каву'),
        (r'<p>На жаль, не все, що називається', f'<p data-i18n="{key}.p_recognize_intro">На жаль, не все, що називається'),
        (r'<p>Якщо ви п\'єте каву заради кофеїну', f'<p data-i18n="{key}.p_worth_intro">Якщо ви п\'єте каву заради кофеїну'),
        (r'<p>Specialty кава відкриє вам світ смаків', f'<p data-i18n="{key}.p_worth_flavors">Specialty кава відкриє вам світ смаків'),
        (r'<p>Спробуйте хоча б раз', f'<p data-i18n="{key}.p_conclusion">Спробуйте хоча б раз'),
    ]
    
    for pattern, replacement in paragraph_replacements:
        content = re.sub(pattern, replacement, content)
    
    # Replace quotes
    content = re.sub(
        r'(<div class="article-quote">)\s*"Specialty кава — це приблизно 3%',
        rf'\1<span data-i18n="{key}.quote1">"Specialty кава — це приблизно 3%',
        content
    )
    content = re.sub(
        r'(<div class="article-quote">)\s*"Коли я вперше спробував справжню',
        rf'\1<span data-i18n="{key}.quote2">"Коли я вперше спробував справжню',
        content
    )
    
    # Replace CTA
    content = re.sub(
        r'(<div class="article-cta">)\s*<h3>Готові спробувати справжню specialty каву\?</h3>',
        rf'\1\n                <h3 data-i18n="{key}.cta_title">Готові спробувати справжню specialty каву?</h3>',
        content
    )
    content = re.sub(
        r'<p>Замовте наш бестселер — Yirgacheffe з нотами квітів та цитрусів</p>',
        f'<p data-i18n="{key}.cta_text">Замовте наш бестселер — Yirgacheffe з нотами квітів та цитрусів</p>',
        content
    )
    
    # Replace related articles title
    content = re.sub(
        r'<h2 style="text-align:center; margin-bottom:40px;">Схожі статті</h2>',
        f'<h2 style="text-align:center; margin-bottom:40px;" data-i18n="{key}.related_title">Схожі статті</h2>',
        content
    )
    
    # Replace tags/share labels
    content = re.sub(
        r'>Теги:</span>',
        f' data-i18n="{key}.tags_label">Теги:</span>',
        content
    )
    content = re.sub(
        r'>Поділитись:</span>',
        f' data-i18n="{key}.share_label">Поділитись:</span>',
        content
    )
    
    with open(ARTICLE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {ARTICLE_PATH}")

if __name__ == "__main__":
    update_article()
    print("Done!")
