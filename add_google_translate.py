#!/usr/bin/env python3
"""
Add Google Translate script to all HTML pages in the EthioDirect project.
This script:
1. Finds all HTML files
2. Adds the google-translate.js script tag before </body>
3. Skips files that already have it
"""

import os
import re
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent

# Files to skip
SKIP_FILES = {'footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html', '_header_template.html'}

def add_google_translate_to_file(filepath):
    """Add google-translate.js to a single HTML file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has google-translate.js
        if 'google-translate.js' in content:
            print(f"  [SKIP] Already has google-translate.js: {filepath.name}")
            return False
        
        # Check if file has </body> tag
        if '</body>' not in content:
            print(f"  [SKIP] No </body> tag: {filepath.name}")
            return False
        
        # Insert google-translate.js before </body>
        # Find the position just before </body>
        script_tag = '    <script src="js/google-translate.js"></script>\n'
        
        # Handle files in subdirectories (need relative path adjustment)
        rel_path = filepath.relative_to(PROJECT_ROOT)
        depth = len(rel_path.parts) - 1
        if depth > 0:
            script_tag = f'    <script src="{"../" * depth}js/google-translate.js"></script>\n'
        
        # Insert before </body>
        new_content = content.replace('</body>', script_tag + '</body>')
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"  [ADDED] {filepath.name}")
        return True
        
    except Exception as e:
        print(f"  [ERROR] {filepath.name}: {e}")
        return False

def main():
    print("=" * 60)
    print("Adding Google Translate to all HTML pages")
    print("=" * 60)
    
    # Find all HTML files
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    
    # Filter out skip files
    html_files = [f for f in html_files if f.name not in SKIP_FILES]
    
    print(f"\nFound {len(html_files)} HTML files\n")
    
    added_count = 0
    skipped_count = 0
    
    for filepath in sorted(html_files):
        if add_google_translate_to_file(filepath):
            added_count += 1
        else:
            skipped_count += 1
    
    print("\n" + "=" * 60)
    print(f"DONE! Added to {added_count} files, skipped {skipped_count} files")
    print("=" * 60)

if __name__ == '__main__':
    main()
