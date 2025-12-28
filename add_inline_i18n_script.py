#!/usr/bin/env python3
"""
Add i18n-inline.js script tag to all HTML files
This ensures inline translations are loaded before i18n.js initializes
"""
from pathlib import Path
import re

def add_inline_script(html_file):
    """Add i18n-inline.js script before i18n.js if not already present"""
    try:
        content = html_file.read_text(encoding='utf-8')
        
        # Check if already has inline script
        if 'i18n-inline.js' in content:
            print(f"  [SKIP] {html_file.name} - already has i18n-inline.js")
            return False
        
        # Find where i18n.js is loaded (accounting for potential query params like ?v=2.0)
        pattern = r'(\s*<script src="(?:\.\./)?js/i18n\.js(?:\?.*?)?"><\/script>)'
        match = re.search(pattern, content)
        
        if not match:
            print(f"  [SKIP] {html_file.name} - no i18n.js found")
            return False
        
        # Determine correct path based on file location
        if str(html_file).count('\\') > str(Path.cwd()).count('\\'):
            # File is in subdirectory
            script_path = '../js/i18n-inline.js'
        else:
            script_path = 'js/i18n-inline.js'
        
        # Insert inline script before i18n.js
        inline_script = f'<script src="{script_path}"></script>\n    '
        new_content = content.replace(match.group(0), inline_script + match.group(0))
        
        # Write back
        html_file.write_text(new_content, encoding='utf-8')
        print(f"  [OK] {html_file.name} - added i18n-inline.js")
        return True
        
    except Exception as e:
        print(f"  [ERROR] {html_file.name} - {e}")
        return False

def main():
    base_dir = Path('.')
    
    # Process root HTML files
    html_files = list(base_dir.glob('*.html'))
    # Process articles
    html_files.extend(Path('articles').glob('*.html'))
    # Process blog
    html_files.extend(Path('blog').glob('*.html'))
    
    print(f"Found {len(html_files)} HTML files to process\n")
    
    updated = 0
    for html_file in html_files:
        if add_inline_script(html_file):
            updated += 1
    
    print(f"\n[DONE] Updated {updated} files")

if __name__ == "__main__":
    main()
