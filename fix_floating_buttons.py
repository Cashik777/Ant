#!/usr/bin/env python3
"""
Fix floating buttons - remove data-i18n attribute, keep only data-i18n-title
The data-i18n attribute replaces the inner HTML including the icon, we only want to translate the title attribute
"""
from pathlib import Path
import re

def fix_floating_buttons(html_file):
    """Remove data-i18n from floating buttons, keep data-i18n-title"""
    try:
        content = html_file.read_text(encoding='utf-8')
        
        # Pattern to find float-btn elements with data-i18n
        # We want to remove data-i18n="float_buttons.xxx" but keep data-i18n-title
        pattern = r'(<a[^>]*class="float-btn[^"]*"[^>]*)\s*data-i18n="float_buttons\.[^"]*"'
        
        new_content = re.sub(pattern, r'\1', content)
        
        if new_content != content:
            html_file.write_text(new_content, encoding='utf-8')
            print(f"  [OK] {html_file.name}")
            return True
        else:
            print(f"  [SKIP] {html_file.name} - no floating buttons found")
            return False
            
    except Exception as e:
        print(f"  [ERROR] {html_file.name} - {e}")
        return False

def main():
    base_dir = Path('.')
    
    # Process all HTML files
    html_files = list(base_dir.glob('*.html'))
    html_files.extend(Path('articles').glob('*.html'))
    html_files.extend(Path('blog').glob('*.html'))
    
    print(f"Fixing floating buttons in HTML files\n")
    
    updated = 0
    for html_file in html_files:
        if fix_floating_buttons(html_file):
            updated += 1
    
    print(f"\n[DONE] Fixed {updated} files")

if __name__ == "__main__":
    main()
