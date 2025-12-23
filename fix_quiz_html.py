#!/usr/bin/env python3
"""Add data-i18n to quiz.html for all questions and options"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

def fix_quiz_html():
    filepath = BASE_DIR / "quiz.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    
    # Hero badge
    content = re.sub(
        r'>5 ПИТАНЬ • 2 ХВИЛИНИ<',
        ' data-i18n="quiz_page.badge">5 ПИТАНЬ • 2 ХВИЛИНИ<',
        content
    )
    
    # Hero title
    content = re.sub(
        r'<h1>Знайдіть свою<br>ідеальну каву</h1>',
        '<h1 data-i18n="quiz_page.hero_title">Знайдіть свою<br>ідеальну каву</h1>',
        content
    )
    
    # Hero text
    content = re.sub(
        r'<p>Відповідайте на прості питання — і ми підберемо сорт, який точно вам сподобається</p>',
        '<p data-i18n="quiz_page.hero_text">Відповідайте на прості питання — і ми підберемо сорт, який точно вам сподобається</p>',
        content
    )
    
    # Benefit pills
    content = re.sub(
        r'>Знижка -10% на результат<',
        ' data-i18n="quiz_page.benefit_discount">Знижка -10% на результат<',
        content
    )
    content = re.sub(
        r'>Миттєва рекомендація<',
        ' data-i18n="quiz_page.benefit_instant">Миттєва рекомендація<',
        content
    )
    content = re.sub(
        r'>98% точність<',
        ' data-i18n="quiz_page.benefit_accuracy">98% точність<',
        content
    )
    
    # Progress steps
    content = re.sub(
        r'>Спосіб<',
        ' data-i18n="quiz_page.step_way">Спосіб<',
        content
    )
    content = re.sub(
        r'>Смак<',
        ' data-i18n="quiz_page.step_taste">Смак<',
        content
    )
    content = re.sub(
        r'>Метод<',
        ' data-i18n="quiz_page.step_method">Метод<',
        content
    )
    content = re.sub(
        r'>Міцність<',
        ' data-i18n="quiz_page.step_strength">Міцність<',
        content
    )
    content = re.sub(
        r'>Обсяг<',
        ' data-i18n="quiz_page.step_volume">Обсяг<',
        content
    )
    
    # Q1
    content = re.sub(
        r'<h2>Як ви зазвичай п\'єте каву\?</h2>',
        '<h2 data-i18n="quiz_page.q1_title">Як ви зазвичай п\'єте каву?</h2>',
        content
    )
    content = re.sub(
        r'<p>Оберіть найближчий варіант</p>',
        '<p data-i18n="quiz_page.q1_subtitle">Оберіть найближчий варіант</p>',
        content
    )
    content = re.sub(
        r'<h4>Чорна, без нічого</h4>',
        '<h4 data-i18n="quiz_page.q1_opt1_title">Чорна, без нічого</h4>',
        content
    )
    content = re.sub(
        r'<p>Максимальний смак зерна</p>',
        '<p data-i18n="quiz_page.q1_opt1_desc">Максимальний смак зерна</p>',
        content
    )
    content = re.sub(
        r'<h4>З молоком</h4>',
        '<h4 data-i18n="quiz_page.q1_opt2_title">З молоком</h4>',
        content
    )
    content = re.sub(
        r'<p>Капучіно, лате, флет-вайт</p>',
        '<p data-i18n="quiz_page.q1_opt2_desc">Капучіно, лате, флет-вайт</p>',
        content
    )
    content = re.sub(
        r'<h4>З молоком і цукром</h4>',
        '<h4 data-i18n="quiz_page.q1_opt3_title">З молоком і цукром</h4>',
        content
    )
    content = re.sub(
        r'<p>Солодко та ніжно</p>',
        '<p data-i18n="quiz_page.q1_opt3_desc">Солодко та ніжно</p>',
        content
    )
    
    # Q2
    content = re.sub(
        r'<h2>Які смаки вам подобаються\?</h2>',
        '<h2 data-i18n="quiz_page.q2_title">Які смаки вам подобаються?</h2>',
        content
    )
    content = re.sub(
        r'<p>Оберіть улюблений профіль</p>',
        '<p data-i18n="quiz_page.q2_subtitle">Оберіть улюблений профіль</p>',
        content
    )
    content = re.sub(
        r'<h4>Фруктові, ягідні</h4>',
        '<h4 data-i18n="quiz_page.q2_opt1_title">Фруктові, ягідні</h4>',
        content
    )
    content = re.sub(
        r'<p>Яскрава кислинка, свіжість</p>',
        '<p data-i18n="quiz_page.q2_opt1_desc">Яскрава кислинка, свіжість</p>',
        content
    )
    content = re.sub(
        r'<h4>Шоколадні, горіхові</h4>',
        '<h4 data-i18n="quiz_page.q2_opt2_title">Шоколадні, горіхові</h4>',
        content
    )
    content = re.sub(
        r'<p>Класичний, насичений смак</p>',
        '<p data-i18n="quiz_page.q2_opt2_desc">Класичний, насичений смак</p>',
        content
    )
    content = re.sub(
        r'<h4>Квіткові, чайні</h4>',
        '<h4 data-i18n="quiz_page.q2_opt3_title">Квіткові, чайні</h4>',
        content
    )
    content = re.sub(
        r'<p>Ніжний, делікатний аромат</p>',
        '<p data-i18n="quiz_page.q2_opt3_desc">Ніжний, делікатний аромат</p>',
        content
    )
    
    # Q3  
    content = re.sub(
        r'<h2>Як ви готуєте каву вдома\?</h2>',
        '<h2 data-i18n="quiz_page.q3_title">Як ви готуєте каву вдома?</h2>',
        content
    )
    content = re.sub(
        r'<p>Від цього залежить рекомендація обсмажки</p>',
        '<p data-i18n="quiz_page.q3_subtitle">Від цього залежить рекомендація обсмажки</p>',
        content
    )
    content = re.sub(
        r'<h4>Еспресо-машина</h4>',
        '<h4 data-i18n="quiz_page.q3_opt1_title">Еспресо-машина</h4>',
        content
    )
    content = re.sub(
        r'<p>Автомат або ріжкова</p>',
        '<p data-i18n="quiz_page.q3_opt1_desc">Автомат або ріжкова</p>',
        content
    )
    content = re.sub(
        r'<h4>Пуровер / Кемекс</h4>',
        '<h4 data-i18n="quiz_page.q3_opt2_title">Пуровер / Кемекс</h4>',
        content
    )
    content = re.sub(
        r'<p>Фільтр-методи</p>',
        '<p data-i18n="quiz_page.q3_opt2_desc">Фільтр-методи</p>',
        content
    )
    content = re.sub(
        r'<h4>Турка / Мока</h4>',
        '<h4 data-i18n="quiz_page.q3_opt3_title">Турка / Мока</h4>',
        content
    )
    content = re.sub(
        r'<p>Традиційний спосіб</p>',
        '<p data-i18n="quiz_page.q3_opt3_desc">Традиційний спосіб</p>',
        content
    )
    content = re.sub(
        r'<h4>Френч-прес</h4>',
        '<h4 data-i18n="quiz_page.q3_opt4_title">Френч-прес</h4>',
        content
    )
    content = re.sub(
        r'<p>Імерсійне заварювання</p>',
        '<p data-i18n="quiz_page.q3_opt4_desc">Імерсійне заварювання</p>',
        content
    )
    
    # Q4
    content = re.sub(
        r'<h2>Наскільки міцну каву ви любите\?</h2>',
        '<h2 data-i18n="quiz_page.q4_title">Наскільки міцну каву ви любите?</h2>',
        content
    )
    content = re.sub(
        r'<p>Це вплине на рекомендацію обсмажки</p>',
        '<p data-i18n="quiz_page.q4_subtitle">Це вплине на рекомендацію обсмажки</p>',
        content
    )
    
    # Navigation buttons  
    content = re.sub(
        r'>Далі <',
        ' data-i18n="quiz_page.btn_next">Далі <',
        content
    )
    content = re.sub(
        r'>\s*Назад</button>',
        ' data-i18n="quiz_page.btn_back">Назад</button>',
        content
    )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated quiz.html")
    else:
        print("No changes to quiz.html")

if __name__ == "__main__":
    fix_quiz_html()
