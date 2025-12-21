#!/usr/bin/env python3
"""
Fix translation system on all HTML pages:
1. Remove references to translations.js
2. Update top-bar-right to have lang-btn class (not lang-switch)
3. Ensure google-translate.js is loaded
4. Remove onclick handlers from language buttons (handled by new script)
"""

import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

# Skip template files
SKIP_FILES = {'footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html', '_header_template.html'}

def fix_html_file(filepath):
    """Fix a single HTML file for new translation system."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # 1. Remove translations.js script tag
        content = re.sub(r'\s*<script src="[^"]*translations\.js"></script>', '', content)
        content = re.sub(r'\s*<script src="[^"]*translations\.js"\s*>\s*</script>', '', content)
        
        # 2. Replace old lang-switch buttons with new structure
        # The new google-translate.js will create buttons dynamically
        # Just ensure top-bar-right exists
        
        # 3. Remove old onclick handlers from language buttons
        content = re.sub(
            r'onclick="switchLang\([\'"]?\w+[\'"]?\);\s*return false;"',
            '',
            content
        )
        
        # 4. Replace lang-switch class with lang-btn notranslate
        content = content.replace('class="lang-switch active"', 'class="lang-btn notranslate"')
        content = content.replace('class="lang-switch"', 'class="lang-btn notranslate"')
        
        # 5. Ensure google-translate.js is present (should already be from previous script)
        if 'google-translate.js' not in content and '</body>' in content:
            # Get relative path
            rel_path = filepath.relative_to(PROJECT_ROOT)
            depth = len(rel_path.parts) - 1
            prefix = '../' * depth if depth > 0 else ''
            script_tag = f'    <script src="{prefix}js/google-translate.js"></script>\n'
            content = content.replace('</body>', script_tag + '</body>')
        
        # Check if changes were made
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  [FIXED] {filepath.name}")
            return True
        else:
            print(f"  [OK] {filepath.name}")
            return False
            
    except Exception as e:
        print(f"  [ERROR] {filepath.name}: {e}")
        return False

def main():
    print("=" * 60)
    print("Fixing Translation System on All HTML Pages")
    print("=" * 60)
    
    # Find all HTML files
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    html_files = [f for f in html_files if f.name not in SKIP_FILES]
    
    print(f"\nProcessing {len(html_files)} HTML files...\n")
    
    fixed = 0
    for filepath in sorted(html_files):
        if fix_html_file(filepath):
            fixed += 1
    
    print("\n" + "=" * 60)
    print(f"DONE! Fixed {fixed} files")
    print("=" * 60)

if __name__ == '__main__':
    main()
