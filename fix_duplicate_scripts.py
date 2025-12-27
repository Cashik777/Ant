#!/usr/bin/env python3
"""
Remove duplicate i18n.js script tags from HTML pages
"""
import os
import re

def fix_duplicate_scripts(filepath):
    """Remove duplicate i18n.js script tags"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match consecutive i18n.js script tags
        patterns = [
            (r'(<script src="js/i18n\.js"></script>\s*)<script src="js/i18n\.js"></script>', r'\1'),
            (r'(<script src="../js/i18n\.js"></script>\s*)<script src="../js/i18n\.js"></script>', r'\1'),
            (r'(<script src="js/i18n\.js\?v=[\d.]+"></script>\s*)<script src="js/i18n\.js\?v=[\d.]+"></script>', r'\1'),
            (r'(<script src="../js/i18n\.js\?v=[\d.]+"></script>\s*)<script src="../js/i18n\.js\?v=[\d.]+"></script>', r'\1'),
        ]
        
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[FIXED] {filepath}")
            return True
        else:
            return False
            
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return False

def main():
    base_dir = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect'
    
    html_files = []
    for root, dirs, files in os.walk(base_dir):
        if '.git' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    
    fixed = 0
    for filepath in sorted(html_files):
        if fix_duplicate_scripts(filepath):
            fixed += 1
    
    print(f"\nFixed {fixed} files with duplicate script tags")

if __name__ == '__main__':
    main()
