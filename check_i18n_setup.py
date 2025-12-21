"""
Script to ensure ALL HTML pages have:
1. Language buttons (UA/RU/EN) in top-bar
2. i18n.js script included
"""
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Language buttons HTML (should be in top-bar-right)
LANG_BUTTONS = '''<div class="top-bar-right">
                <a href="#" translate="no" class="active" onclick="setLanguage('uk'); return false;">UA</a>
                <a href="#" translate="no" onclick="setLanguage('ru'); return false;">RU</a>
                <a href="#" translate="no" onclick="setLanguage('en'); return false;">EN</a>
            </div>'''

# i18n script tag for root pages
I18N_SCRIPT_ROOT = '<script src="js/i18n.js"></script>'
# i18n script tag for subdirectory pages
I18N_SCRIPT_SUB = '<script src="../js/i18n.js"></script>'

def get_all_html_files():
    """Get all HTML files except templates"""
    files = []
    for path in BASE_DIR.rglob("*.html"):
        # Skip template files
        if 'template' in path.name.lower():
            continue
        files.append(path)
    return files

def check_has_lang_buttons(content):
    """Check if file has language buttons"""
    return 'setLanguage' in content and 'top-bar-right' in content

def check_has_i18n_script(content):
    """Check if file has i18n.js included"""
    return 'i18n.js' in content

def fix_file(filepath):
    """Check and fix a single HTML file"""
    rel_path = filepath.relative_to(BASE_DIR)
    is_subdir = '\\' in str(rel_path) or '/' in str(rel_path)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    issues = []
    
    # Check for language buttons
    if not check_has_lang_buttons(content):
        issues.append("Missing language buttons")
    
    # Check for i18n.js script
    if not check_has_i18n_script(content):
        issues.append("Missing i18n.js script")
        # Try to add it before </body>
        if is_subdir:
            script_tag = I18N_SCRIPT_SUB
        else:
            script_tag = I18N_SCRIPT_ROOT
        
        if '</body>' in content:
            content = content.replace('</body>', f'    {script_tag}\n</body>')
            modified = True
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return issues, modified

def main():
    files = get_all_html_files()
    print(f"Checking {len(files)} HTML files...\n")
    
    files_with_issues = []
    files_fixed = 0
    
    for filepath in sorted(files):
        rel_path = filepath.relative_to(BASE_DIR)
        issues, was_fixed = fix_file(filepath)
        
        if issues:
            files_with_issues.append((rel_path, issues))
            if was_fixed:
                files_fixed += 1
                print(f"[FIXED] {rel_path}")
            else:
                print(f"[ISSUE] {rel_path}: {', '.join(issues)}")
        else:
            print(f"[OK] {rel_path}")
    
    print(f"\n{'='*50}")
    print(f"Total files: {len(files)}")
    print(f"Files with issues: {len(files_with_issues)}")
    print(f"Files fixed: {files_fixed}")
    
    if files_with_issues:
        print(f"\nFiles still needing attention:")
        for path, issues in files_with_issues:
            if "Missing language buttons" in issues:
                print(f"  - {path}: needs language buttons")

if __name__ == "__main__":
    main()
