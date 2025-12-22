#!/usr/bin/env python3
"""
Add data-i18n attributes to specific paragraphs in blog HTML files
More targeted approach based on actual content structure
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent / "blog"

# Specific paragraph patterns to match and replace
BLOG_P_PATTERNS = {
    "arabica-vs-robusta": [
        ("Arabica — капризна красуня. Їй потрібні:", "p1"),
        ("Arabica славиться складністю смаку:", "p2"),
        ("Robusta — це стійка рослина, яка:", "p3"),
        ("<strong>Ні!</strong> Якісна Robusta має місце", "p4"),
        ("Проблема не в Robusta як такій", "p5"),
    ],
    "bean-to-cup": [
        ("Кава народжується як маленьке зерно", "p1"),
        ("Більшість specialty кави збирають вручну", "p1"),
        ("росте лише в", "p1"),
    ],
    "brewing-methods": [
        ("Кожен метод заварювання", "p1"),
        ("Методи занурення", "p1"),
    ],
    "coffee-processing": [
        ("Після збору ягоди проходять", "p1"),
        ("При натуральній обробці", "p1"),
    ],
    "coffee-seasonality": [
        ("Кава — сезонний продукт", "p1"),
        ("Ефіопія:", "p1"),
    ],
    "coffee-storage": [
        ("Правильне зберігання", "p1"),
        ("П'ять головних ворогів", "p1"),
    ],
    "cold-brew-guide": [
        ("Cold brew — це кава", "p1"),
        ("На відміну від айс-кофе", "p2"),
    ],
    "espresso-guide": [
        ("Для еспресо потрібна", "p1"),
        ("Стандартний рецепт:", "p2"),
    ],
    "ethiopia-origins": [
        ("Ефіопія — батьківщина", "p1"),
        ("Yirgacheffe — найвідоміший", "p1"),
    ],
    "french-press-guide": [
        ("Вам потрібно:", "p1"),
        ("Засипте каву", "p2"),
    ],
    "sca-grading": [
        ("SCA створила", "p1"),
        ("Каву оцінюють за", "p1"),
    ],
    "specialty-coffee": [
        ("Specialty — це кава", "p1"),
        ("Різниця з комерційною", "p2"),
    ],
    "turka-guide": [
        ("Турка має бути", "p1"),
        ("Помел — найдрібніший", "p2"),
    ],
    "v60-guide": [
        ("Вам потрібно:", "p1"),
        ("Преінфузія:", "p2"),
    ],
    "yirgacheffe-region": [
        ("Регіон розташований", "p1"),
        ("Смаковий профіль:", "p2"),
    ],
}

BLOG_MAPPINGS = {
    "arabica-vs-robusta": "arabica_vs_robusta",
    "bean-to-cup": "bean_to_cup",
    "brewing-methods": "brewing_methods",
    "coffee-processing": "coffee_processing",
    "coffee-seasonality": "coffee_seasonality",
    "coffee-storage": "coffee_storage_blog",
    "cold-brew-guide": "cold_brew_guide",
    "espresso-guide": "espresso_guide",
    "ethiopia-origins": "ethiopia_origins",
    "french-press-guide": "french_press_guide",
    "sca-grading": "sca_grading",
    "specialty-coffee": "specialty_coffee",
    "turka-guide": "turka_guide",
    "v60-guide": "v60_guide",
    "yirgacheffe-region": "yirgacheffe_region"
}

def add_p_i18n(filename, key):
    """Add data-i18n to specific paragraphs"""
    filepath = BASE_DIR / f"{filename}.html"
    
    if not filepath.exists():
        print(f"Skipping {filename} - file not found")
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    prefix = f"blog.{key}"
    modified = False
    patterns = BLOG_P_PATTERNS.get(filename, [])
    
    for text_pattern, p_key in patterns:
        # Find paragraph containing this text
        pattern = rf'<p([^>]*)>([^<]*{re.escape(text_pattern)}[^<]*(?:<[^>]+>[^<]*)*)</p>'
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            attrs = match.group(1)
            # Skip if already has data-i18n
            if 'data-i18n=' in attrs:
                continue
            old_p = match.group(0)
            new_p = old_p.replace('<p', f'<p data-i18n="{prefix}.{p_key}"', 1)
            content = content.replace(old_p, new_p, 1)
            modified = True
            print(f"  Added {p_key} for: {text_pattern[:30]}...")
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}")

def main():
    print("Adding targeted data-i18n to blog paragraphs...")
    for filename, key in BLOG_MAPPINGS.items():
        add_p_i18n(filename, key)
    print("Done!")

if __name__ == "__main__":
    main()
