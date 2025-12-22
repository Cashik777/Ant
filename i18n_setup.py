#!/usr/bin/env python3
"""
EthioDirect - Complete i18n Setup Script
Scans all HTML files and ensures they have proper i18n attributes.
Generates/updates translation JSON files with all text content.
"""

import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser
from collections import defaultdict

# Configuration
PROJECT_ROOT = Path(__file__).parent
HTML_PATTERNS = ['*.html']
EXCLUDE_DIRS = ['node_modules', '.git', 'dist', 'build']
LOCALES_DIR = PROJECT_ROOT / 'locales'

# Elements to skip translation
SKIP_ELEMENTS = {'script', 'style', 'code', 'pre', 'svg', 'path', 'noscript', 'template'}
SKIP_CLASSES = {'notranslate', 'no-translate', 'lang-btn'}
TRANSLATE_NO_ELEMENTS = set()  # Elements with translate="no"

# Track all found text for translation
all_texts = defaultdict(dict)


class HTMLTextExtractor(HTMLParser):
    """Extract translatable text from HTML"""
    
    def __init__(self, filepath):
        super().__init__()
        self.filepath = filepath
        self.current_element = []
        self.skip_depth = 0
        self.texts = []
        self.has_i18n = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        self.current_element.append((tag, attrs_dict))
        
        # Skip certain elements
        if tag in SKIP_ELEMENTS:
            self.skip_depth += 1
            
        # Skip elements with translate="no"
        if attrs_dict.get('translate') == 'no':
            self.skip_depth += 1
            
        # Skip elements with certain classes
        classes = attrs_dict.get('class', '').split()
        if any(c in SKIP_CLASSES for c in classes):
            self.skip_depth += 1
    
    def handle_endtag(self, tag):
        if self.current_element and self.current_element[-1][0] == tag:
            _, attrs = self.current_element.pop()
            
            if tag in SKIP_ELEMENTS:
                self.skip_depth = max(0, self.skip_depth - 1)
            if attrs.get('translate') == 'no':
                self.skip_depth = max(0, self.skip_depth - 1)
            classes = attrs.get('class', '').split()
            if any(c in SKIP_CLASSES for c in classes):
                self.skip_depth = max(0, self.skip_depth - 1)
    
    def handle_data(self, data):
        text = data.strip()
        if not text or self.skip_depth > 0:
            return
            
        # Skip empty or whitespace-only
        if not text or len(text) < 2:
            return
            
        # Skip numbers only, prices, etc
        if re.match(r'^[\d\s\+\-\(\)₴€\$\.,:%]+$', text):
            return
            
        # Skip URLs and emails
        if re.match(r'^(https?://|www\.|[\w\.-]+@)', text, re.I):
            return
            
        # Get current element info
        if self.current_element:
            tag, attrs = self.current_element[-1]
            has_i18n = 'data-i18n' in attrs
            self.texts.append({
                'text': text,
                'tag': tag,
                'has_i18n': has_i18n,
                'i18n_key': attrs.get('data-i18n', ''),
                'line': self.getpos()[0]
            })


def find_html_files():
    """Find all HTML files in project"""
    files = []
    for pattern in HTML_PATTERNS:
        for filepath in PROJECT_ROOT.rglob(pattern):
            # Skip excluded directories
            if any(ex in str(filepath) for ex in EXCLUDE_DIRS):
                continue
            files.append(filepath)
    return sorted(files)


def analyze_html_file(filepath):
    """Analyze HTML file for translatable text"""
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return []
    
    parser = HTMLTextExtractor(filepath)
    try:
        parser.feed(content)
    except Exception as e:
        print(f"  Parse error in {filepath}: {e}")
        return []
    
    return parser.texts


def check_i18n_script(filepath):
    """Check if file includes i18n.js"""
    try:
        content = filepath.read_text(encoding='utf-8')
    except:
        return False
    return 'i18n.js' in content


def check_language_buttons(filepath):
    """Check if file has language buttons"""
    try:
        content = filepath.read_text(encoding='utf-8')
    except:
        return False
    return "setLanguage('uk')" in content or "setLanguage('en')" in content


def add_i18n_script_to_file(filepath):
    """Add i18n.js script to HTML file if missing"""
    try:
        content = filepath.read_text(encoding='utf-8')
    except:
        return False
    
    if 'i18n.js' in content:
        return True  # Already has it
    
    # Find </body> and add script before it
    if '</body>' in content:
        # Determine relative path to js folder
        rel_path = os.path.relpath(PROJECT_ROOT / 'js', filepath.parent)
        script_path = rel_path.replace('\\', '/') + '/i18n.js'
        script_tag = f'\n    <script src="{script_path}"></script>\n'
        
        content = content.replace('</body>', script_tag + '</body>')
        filepath.write_text(content, encoding='utf-8')
        return True
    
    return False


def add_language_buttons(filepath):
    """Add language buttons to top-bar if missing"""
    try:
        content = filepath.read_text(encoding='utf-8')
    except:
        return False
    
    if "setLanguage(" in content:
        return True  # Already has buttons
    
    # Look for top-bar-right div
    if 'class="top-bar-right"' in content and '</div>' in content:
        buttons_html = '''
                <a href="#" translate="no" class="active" onclick="setLanguage('uk'); return false;">UA</a>
                <a href="#" translate="no" onclick="setLanguage('ru'); return false;">RU</a>
                <a href="#" translate="no" onclick="setLanguage('en'); return false;">EN</a>
            '''
        
        # Find top-bar-right and insert buttons
        pattern = r'(class="top-bar-right"[^>]*>)\s*'
        if re.search(pattern, content):
            content = re.sub(pattern, r'\1' + buttons_html, content, count=1)
            filepath.write_text(content, encoding='utf-8')
            return True
    
    return False


def generate_key_from_text(text, context=''):
    """Generate a translation key from text content"""
    # Clean and shorten
    clean = re.sub(r'[^\w\s]', '', text.lower())
    words = clean.split()[:4]
    key = '_'.join(words)
    
    if context:
        key = context + '.' + key
    
    return key[:50]  # Limit length


def count_issues():
    """Count and report i18n issues"""
    files = find_html_files()
    
    stats = {
        'total_files': len(files),
        'missing_script': 0,
        'missing_buttons': 0,
        'files_with_issues': []
    }
    
    print(f"\n{'='*60}")
    print(f"EthioDirect i18n Audit Report")
    print(f"{'='*60}\n")
    print(f"Total HTML files: {len(files)}\n")
    
    for filepath in files:
        rel_path = filepath.relative_to(PROJECT_ROOT)
        has_script = check_i18n_script(filepath)
        has_buttons = check_language_buttons(filepath)
        
        issues = []
        if not has_script:
            issues.append("missing i18n.js")
            stats['missing_script'] += 1
        if not has_buttons:
            issues.append("missing language buttons")
            stats['missing_buttons'] += 1
            
        if issues:
            stats['files_with_issues'].append((rel_path, issues))
            print(f"[!] {rel_path}")
            for issue in issues:
                print(f"    - {issue}")
    
    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"{'='*60}")
    print(f"Files missing i18n.js script: {stats['missing_script']}")
    print(f"Files missing language buttons: {stats['missing_buttons']}")
    print(f"Files OK: {stats['total_files'] - len(stats['files_with_issues'])}")
    
    return stats


def fix_all_files():
    """Fix all HTML files - add i18n.js and language buttons"""
    files = find_html_files()
    fixed_script = 0
    fixed_buttons = 0
    
    print("\nFixing HTML files...")
    
    for filepath in files:
        rel_path = filepath.relative_to(PROJECT_ROOT)
        
        # Add i18n.js if missing
        if not check_i18n_script(filepath):
            if add_i18n_script_to_file(filepath):
                print(f"  [+] Added i18n.js to {rel_path}")
                fixed_script += 1
        
        # Add language buttons if missing
        if not check_language_buttons(filepath):
            if add_language_buttons(filepath):
                print(f"  [+] Added language buttons to {rel_path}")
                fixed_buttons += 1
    
    print(f"\nFixed: {fixed_script} scripts, {fixed_buttons} button sets")


def main():
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--fix':
        fix_all_files()
        print("\nRe-running audit...")
        count_issues()
    else:
        stats = count_issues()
        if stats['missing_script'] > 0 or stats['missing_buttons'] > 0:
            print(f"\nRun with --fix to automatically fix these issues:")
            print(f"  python {sys.argv[0]} --fix")


if __name__ == '__main__':
    main()
