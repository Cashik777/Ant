#!/usr/bin/env python3
"""
Script to replace harsh red colors with softer brown tones.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(r"C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect")

# Color replacements (old -> new)
REPLACEMENTS = {
    '#a52a2a': '#6D4C41',  # Brown instead of red
    '#A52A2A': '#6D4C41',
    '#8B0000': '#5D4037',  # Dark brown instead of dark red
    '#8b0000': '#5D4037',
    '#6B0000': '#4E342E',  # Darker brown for hover
    '#6b0000': '#4E342E',
    '#4a2828': '#3E2723',  # Very dark brown
    '#4A2828': '#3E2723',
    'rgba(139, 0, 0': 'rgba(93, 64, 55',  # rgba primary color
    'rgba(139,0,0': 'rgba(93,64,55',
}

def process_file(filepath):
    """Process a single file and replace colors."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[SKIP] Could not read {filepath}: {e}")
        return False

    original = content
    for old, new in REPLACEMENTS.items():
        content = content.replace(old, new)
    
    if content != original:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Updated {filepath.name}")
            return True
        except Exception as e:
            print(f"[ERROR] Could not write {filepath}: {e}")
            return False
    else:
        print(f"[--] No changes in {filepath.name}")
        return False

def main():
    print("=== Replacing Harsh Red Colors ===")
    print(f"Base directory: {BASE_DIR}")
    print()
    
    # Process HTML files in root
    for html_file in BASE_DIR.glob('*.html'):
        process_file(html_file)
    
    # Process HTML files in articles subdirectory
    articles_dir = BASE_DIR / 'articles'
    if articles_dir.exists():
        for html_file in articles_dir.glob('*.html'):
            process_file(html_file)
    
    # Process CSS files
    css_dir = BASE_DIR / 'css'
    if css_dir.exists():
        for css_file in css_dir.glob('*.css'):
            process_file(css_file)
    
    print()
    print("=== Done ===")

if __name__ == "__main__":
    main()
