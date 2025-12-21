#!/usr/bin/env python3
"""
i18n Content Audit Script
Finds all untranslated text in HTML files.
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent

# Skip these files
SKIP_FILES = {'footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html'}

# Tags that should not contain translatable text
SKIP_TAGS = {'script', 'style', 'link', 'meta', 'code', 'pre'}

# Inline tags that might contain text
INLINE_TAGS = {'span', 'strong', 'em', 'b', 'i', 'a', 'small', 'mark'}

# Attributes to check for translation
TRANSLATABLE_ATTRS = ['placeholder', 'title', 'alt', 'aria-label']

class I18nAuditor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.issues = []
        self.current_file = ""
        self.tag_stack = []
        self.has_i18n_stack = []
        self.line_offset = 0
        
    def reset_for_file(self, filename):
        self.reset()
        self.issues = []
        self.current_file = filename
        self.tag_stack = []
        self.has_i18n_stack = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Check if this element or ancestor has data-i18n
        has_i18n = 'data-i18n' in attrs_dict
        parent_has_i18n = self.has_i18n_stack[-1] if self.has_i18n_stack else False
        
        self.tag_stack.append(tag)
        self.has_i18n_stack.append(has_i18n or parent_has_i18n)
        
        # Check translatable attributes
        if tag not in SKIP_TAGS:
            for attr in TRANSLATABLE_ATTRS:
                if attr in attrs_dict:
                    value = attrs_dict[attr].strip()
                    # Check if it's NOT using i18n
                    i18n_attr = f'data-i18n-{attr}'
                    if i18n_attr not in attrs_dict and 'data-i18n' not in attrs_dict:
                        # Check if value looks like hardcoded text (not a key or empty)
                        if value and not value.startswith('{') and len(value) > 2:
                            # Skip common non-translatable values
                            if not value.startswith('http') and not value.startswith('#') and not value.startswith('javascript'):
                                self.issues.append({
                                    'type': 'attribute',
                                    'tag': tag,
                                    'attr': attr,
                                    'value': value[:50],
                                    'line': self.getpos()[0]
                                })
    
    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
            self.has_i18n_stack.pop()
    
    def handle_data(self, data):
        text = data.strip()
        
        # Skip empty or whitespace-only
        if not text:
            return
            
        # Skip if inside skip tags
        if self.tag_stack and self.tag_stack[-1] in SKIP_TAGS:
            return
            
        # Skip if ancestor has data-i18n
        if self.has_i18n_stack and self.has_i18n_stack[-1]:
            return
            
        # Skip very short text (likely icons or symbols)
        if len(text) <= 2:
            return
            
        # Skip numbers only
        if text.replace('.', '').replace(',', '').replace(' ', '').replace('₴', '').replace('%', '').replace('+', '').replace('-', '').isdigit():
            return
            
        # Skip common non-translatable patterns
        skip_patterns = [
            r'^[\d\s\.\,\:\-\+₴%]+$',  # Numbers/currency
            r'^[\•\|\—\–]+$',  # Bullets/dividers
            r'^[A-Z]{2,5}$',  # Abbreviations like SCA
            r'^@',  # Email/social handles
            r'^https?://',  # URLs
            r'^EthioDirect$',  # Brand name
            r'^\d+\s*(г|гр|кг|мл|л)$',  # Weights
        ]
        
        for pattern in skip_patterns:
            if re.match(pattern, text):
                return
        
        # This text appears to need translation
        current_tag = self.tag_stack[-1] if self.tag_stack else 'root'
        self.issues.append({
            'type': 'text',
            'tag': current_tag,
            'value': text[:80],
            'line': self.getpos()[0]
        })


def audit_html_file(filepath):
    """Audit a single HTML file for untranslated content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        auditor = I18nAuditor()
        auditor.reset_for_file(filepath.name)
        auditor.feed(content)
        
        return auditor.issues
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return []


def audit_js_file(filepath):
    """Check JS file for hardcoded strings that should be translated."""
    issues = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        # Patterns that indicate hardcoded UI text
        patterns = [
            (r'innerHTML\s*=\s*[\'"`]([^\'"`]+)[\'"`]', 'innerHTML'),
            (r'textContent\s*=\s*[\'"`]([^\'"`]+)[\'"`]', 'textContent'),
            (r'innerText\s*=\s*[\'"`]([^\'"`]+)[\'"`]', 'innerText'),
            (r'insertAdjacentHTML\([^,]+,\s*[\'"`]([^\'"`]+)[\'"`]', 'insertAdjacentHTML'),
            (r'alert\([\'"`]([^\'"`]+)[\'"`]\)', 'alert'),
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern, method in patterns:
                matches = re.findall(pattern, line)
                for match in matches:
                    # Skip if it's using t()
                    if 't(' in line or 'data-i18n' in match:
                        continue
                    # Skip HTML-only content
                    if re.match(r'^<[^>]+>$', match):
                        continue
                    # Skip if it looks like a variable or has Cyrillic
                    if any(c in match for c in 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯіїєґІЇЄҐ'):
                        issues.append({
                            'type': 'js',
                            'method': method,
                            'value': match[:60],
                            'line': line_num
                        })
        
        return issues
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return []


def main():
    print("=" * 70)
    print("i18n CONTENT AUDIT")
    print("=" * 70)
    
    all_issues = defaultdict(list)
    
    # Audit HTML files
    print("\n[HTML] Scanning HTML files...")
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    html_files = [f for f in html_files if f.name not in SKIP_FILES]
    
    for filepath in sorted(html_files):
        issues = audit_html_file(filepath)
        if issues:
            rel_path = filepath.relative_to(PROJECT_ROOT)
            all_issues[str(rel_path)] = issues
    
    # Audit JS files
    print("[JS] Scanning JS files...")
    js_files = list(PROJECT_ROOT.glob('js/*.js'))
    
    for filepath in js_files:
        if filepath.name == 'i18n.js':
            continue
        issues = audit_js_file(filepath)
        if issues:
            rel_path = filepath.relative_to(PROJECT_ROOT)
            all_issues[str(rel_path)].extend(issues)
    
    # Report
    print("\n" + "=" * 70)
    print("AUDIT RESULTS")
    print("=" * 70)
    
    total_issues = 0
    for filepath, issues in sorted(all_issues.items()):
        if issues:
            print(f"\n[FILE] {filepath} ({len(issues)} issues)")
            for issue in issues[:10]:  # Limit output
                if issue['type'] == 'text':
                    print(f"   L{issue['line']:4d} [{issue['tag']:8s}] \"{issue['value']}\"")
                elif issue['type'] == 'attribute':
                    print(f"   L{issue['line']:4d} [{issue['tag']:8s}] {issue['attr']}=\"{issue['value']}\"")
                elif issue['type'] == 'js':
                    print(f"   L{issue['line']:4d} [{issue['method']:12s}] \"{issue['value']}\"")
            if len(issues) > 10:
                print(f"   ... and {len(issues) - 10} more")
            total_issues += len(issues)
    
    print("\n" + "=" * 70)
    print(f"TOTAL: {total_issues} potential issues in {len(all_issues)} files")
    print("=" * 70)
    
    return all_issues


if __name__ == '__main__':
    main()
