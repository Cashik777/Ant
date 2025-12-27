#!/usr/bin/env python3
"""
Remove data-i18n attributes from blog article content
This ensures actual article text is shown instead of broken translation keys
"""
import os
import re

blog_dir = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect\blog'
articles_dir = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect\articles'

# Pattern to find data-i18n="blog.xxx" or data-i18n="article.xxx" attributes
# We want to remove these entirely but keep the text content
patterns = [
    r' data-i18n="blog\.[^"]*"',
    r' data-i18n="article\.[^"]*"',
    r' data-i18n="articles\.[^"]*"',
]

def fix_html_file(filepath):
    """Remove data-i18n attributes for blog content from HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        for pattern in patterns:
            content = re.sub(pattern, '', content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[FIXED] {os.path.basename(filepath)}")
            return True
        return False
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return False

fixed_count = 0

# Process blog directory
if os.path.exists(blog_dir):
    for filename in os.listdir(blog_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(blog_dir, filename)
            if fix_html_file(filepath):
                fixed_count += 1

# Process articles directory
if os.path.exists(articles_dir):
    for filename in os.listdir(articles_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(articles_dir, filename)
            if fix_html_file(filepath):
                fixed_count += 1

print(f"\nFixed {fixed_count} HTML files")
