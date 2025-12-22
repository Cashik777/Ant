#!/usr/bin/env python3
"""Fix data-i18n-placeholder attributes - add value where missing"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent

def fix_file(filepath):
    """Fix placeholder attributes in a single file"""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return 0
    
    original = content
    changes = 0
    
    # Fix pattern: data-i18n="search.placeholder" data-i18n-placeholder (no value)
    # Should be: data-i18n-placeholder="search.placeholder"
    pattern = r'data-i18n="search\.placeholder"\s+data-i18n-placeholder(?!\s*=)'
    replacement = 'data-i18n-placeholder="search.placeholder"'
    
    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        changes += 1
        content = new_content
    
    if content != original:
        filepath.write_text(content, encoding='utf-8')
        return changes
    return 0


def main():
    print("Fixing data-i18n-placeholder attributes...")
    print("=" * 60)
    
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    total_changes = 0
    files_changed = 0
    
    for filepath in html_files:
        changes = fix_file(filepath)
        if changes:
            rel_path = filepath.relative_to(PROJECT_ROOT)
            print(f"  [+] Fixed {rel_path}")
            total_changes += changes
            files_changed += 1
    
    print("=" * 60)
    print(f"Fixed {total_changes} files")


if __name__ == '__main__':
    main()
