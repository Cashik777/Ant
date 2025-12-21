#!/usr/bin/env python3
"""
Update ALL HTML files with static language buttons.
Buttons have translate="no" so Google Translate won't change them.
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

# New static top-bar-right content
NEW_TOP_BAR_RIGHT = '''<div class="top-bar-right">
                <a href="#" translate="no" class="active" onclick="setLanguage('uk'); return false;">UA</a>
                <a href="#" translate="no" onclick="setLanguage('ru'); return false;">RU</a>
                <a href="#" translate="no" onclick="setLanguage('en'); return false;">EN</a>
            </div>'''

def fix_file(filepath):
    """Update a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Replace entire top-bar-right div
        pattern = r'<div class="top-bar-right">.*?</div>'
        content = re.sub(pattern, NEW_TOP_BAR_RIGHT, content, flags=re.DOTALL)
        
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
    print("Updating All HTML with Static Language Buttons")
    print("=" * 60)
    
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    skip = {'footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html', '_header_template.html'}
    html_files = [f for f in html_files if f.name not in skip]
    
    print(f"\nProcessing {len(html_files)} files...\n")
    
    updated = 0
    for f in sorted(html_files):
        if fix_file(f):
            updated += 1
    
    print(f"\n{'=' * 60}")
    print(f"DONE! Updated {updated} files")
    print("=" * 60)

if __name__ == '__main__':
    main()
