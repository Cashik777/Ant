#!/usr/bin/env python3
"""
Remove ALL emojis from HTML files
"""
import os
import re

base_dir = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect'

# Comprehensive emoji replacements for quiz and other files
emoji_to_icon = {
    '🥛': '<i class="fas fa-glass-whiskey" style="color:#e5e5e5;"></i>',
    '🍬': '<i class="fas fa-candy-cane" style="color:#ff69b4;"></i>',
    '🍓': '<i class="fas fa-apple-alt" style="color:#e74c3c;"></i>',
    '🍫': '<i class="fas fa-cookie" style="color:#8B4513;"></i>',
    '🌸': '<i class="fas fa-spa" style="color:#ff69b4;"></i>',
    '🫖': '<i class="fas fa-mug-hot" style="color:#8B4545;"></i>',
    '🥤': '<i class="fas fa-glass-cheers" style="color:#8B4545;"></i>',
    '🌅': '<i class="fas fa-sun" style="color:#f39c12;"></i>',
    '☀️': '<i class="fas fa-sun" style="color:#f39c12;"></i>',
    '🌙': '<i class="fas fa-moon" style="color:#2c3e50;"></i>',
    '1️⃣': '<i class="fas fa-coffee" style="color:#8B4545;"></i>',
    '2️⃣': '<i class="fas fa-coffee" style="color:#8B4545;"></i>',
    '🫐': '<i class="fas fa-circle" style="color:#4169e1;"></i>',
    '🔥': '<i class="fas fa-fire" style="color:#e74c3c;"></i>',
    '☕': '<i class="fas fa-coffee" style="color:#8B4545;"></i>',
    '⚡': '<i class="fas fa-bolt" style="color:#f39c12;"></i>',
    '🎁': '<i class="fas fa-gift" style="color:#9b59b6;"></i>',
    '⭐': '<i class="fas fa-star" style="color:#f39c12;"></i>',
    '💳': '<i class="fas fa-credit-card"></i>',
    '🚚': '<i class="fas fa-truck"></i>',
    '💰': '<i class="fas fa-tag"></i>',
    '🌍': '<i class="fas fa-globe"></i>',
    '🎉': '<i class="fas fa-gift"></i>',
    '👋': '',
    '✓': '<i class="fas fa-check"></i>',
    '🏢': '<i class="fas fa-building"></i>',
}

def fix_html_file(filepath):
    """Remove/replace emojis in HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        for emoji, replacement in emoji_to_icon.items():
            content = content.replace(emoji, replacement)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[FIXED] {os.path.basename(filepath)}")
            return True
        return False
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return False

# Process all HTML files
html_files = []
for root, dirs, files in os.walk(base_dir):
    # Skip .git and node_modules
    if '.git' in root or 'node_modules' in root:
        continue
    for filename in files:
        if filename.endswith('.html'):
            html_files.append(os.path.join(root, filename))

fixed_count = 0
for filepath in sorted(html_files):
    if fix_html_file(filepath):
        fixed_count += 1

print(f"\nFixed {fixed_count} HTML files")
