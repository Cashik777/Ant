#!/usr/bin/env python3
"""
Script to update all HTML pages with:
1. translations.js script link
2. Language switcher in top bar
3. data-i18n attributes for translatable content
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect")

# Standard top bar with all 3 languages
TOP_BAR_LANG = '''            <div class="top-bar-right">
                <a href="#" class="lang-switch active" onclick="switchLang('uk'); return false;">UA</a>
                <a href="#" class="lang-switch" onclick="switchLang('ru'); return false;">RU</a>
                <a href="#" class="lang-switch" onclick="switchLang('en'); return false;">EN</a>
            </div>'''

# Translations script tag to add before </body>
TRANSLATIONS_SCRIPT = '    <script src="js/translations.js"></script>'

def update_page(filepath):
    """Update a single HTML page with translation support."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[SKIP] Could not read {filepath}: {e}")
        return False

    original = content
    filename = filepath.name
    
    # 1. Add translations.js before </body> if not already present
    if 'translations.js' not in content:
        if '</body>' in content:
            content = content.replace('</body>', f'{TRANSLATIONS_SCRIPT}\n</body>')
    
    # 2. Ensure top bar has all 3 language switches with onclick
    # Pattern to find existing top-bar-right
    top_bar_patterns = [
        r'<div class="top-bar-right">.*?</div>',
    ]
    
    for pattern in top_bar_patterns:
        matches = re.findall(pattern, content, re.DOTALL)
        for match in matches:
            # Check if it has all 3 languages and onclick
            if 'switchLang' not in match or 'EN' not in match:
                content = content.replace(match, TOP_BAR_LANG)
    
    # 3. Ensure onclick handlers use switchLang properly
    content = re.sub(
        r'onclick="switchLang\(\'uk\'\)"',
        'onclick="switchLang(\'uk\'); return false;"',
        content
    )
    content = re.sub(
        r'onclick="switchLang\(\'ru\'\)"',
        'onclick="switchLang(\'ru\'); return false;"',
        content
    )
    content = re.sub(
        r'onclick="switchLang\(\'en\'\)"',
        'onclick="switchLang(\'en\'); return false;"',
        content
    )
    
    # Check if changes were made
    if content != original:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated {filename}")
            return True
        except Exception as e:
            print(f"[ERROR] Could not write {filepath}: {e}")
            return False
    else:
        print(f"[--] No changes in {filename}")
        return False

def main():
    print("=== Adding Translation Support to All Pages ===")
    print(f"Base directory: {BASE_DIR}")
    print()
    
    # Process all HTML files in root
    html_files = list(BASE_DIR.glob('*.html'))
    
    for html_file in html_files:
        update_page(html_file)
    
    # Also check articles directory
    articles_dir = BASE_DIR / 'articles'
    if articles_dir.exists():
        for html_file in articles_dir.glob('*.html'):
            update_page(html_file)
    
    print()
    print("=== Done ===")

if __name__ == "__main__":
    main()
