#!/usr/bin/env python3
"""
Add polish.css and ux-enhancements.css links to all HTML pages
"""
import os
import re

def update_html_file(filepath):
    """Add CSS links after main.css in an HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has polish.css
        if 'polish.css' in content:
            print(f"[SKIP] {filepath} - already has polish.css")
            return False
        
        # Determine the correct path prefix
        if '/blog/' in filepath.replace('\\', '/') or '/articles/' in filepath.replace('\\', '/'):
            prefix = '../'
        else:
            prefix = ''
        
        # Pattern to find main.css link
        pattern = r'(<link[^>]*href="' + re.escape(prefix) + r'css/main\.css"[^>]*>)'
        
        replacement = r'\1\n    <link rel="stylesheet" href="' + prefix + r'css/polish.css">\n    <link rel="stylesheet" href="' + prefix + r'css/ux-enhancements.css">'
        
        new_content = re.sub(pattern, replacement, content, count=1)
        
        if new_content == content:
            print(f"[WARN] {filepath} - no main.css link found")
            return False
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"[OK] {filepath}")
        return True
        
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return False

def main():
    base_dir = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect'
    
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        # Skip .git folder
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    updated = 0
    for filepath in sorted(html_files):
        if update_html_file(filepath):
            updated += 1
    
    print(f"\nUpdated {updated}/{len(html_files)} files")

if __name__ == '__main__':
    main()
