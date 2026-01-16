import re
from pathlib import Path

def read_file_any_encoding(filepath):
    encodings = ['utf-8', 'utf-8-sig', 'cp1251', 'windows-1251', 'latin-1']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read(), enc
        except:
            continue
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        return f.read(), 'utf-8-replace'

filepath = Path('articles/ethiopia-coffee-origin.html')
content, enc = read_file_any_encoding(filepath)

# Find and remove inline <style> blocks that contain sidebar styles
# Keep other style blocks but remove sidebar-related ones

# Pattern to match style blocks containing sidebar-related CSS
pattern = r'<style>\s*(/\*.*?(?:SIDEBAR|Related|Recommended|toc-widget|related-widget).*?\*/.*?|(?:.*?\.toc-widget.*?|.*?\.related-widget.*?|.*?\.article-sidebar.*?)+)</style>'

# Simpler approach: remove specific known problematic style blocks
# The inline styles for .toc-widget, .related-widget, .toc-more-link

lines = content.split('\n')
new_lines = []
in_sidebar_style = False
skip_until_close = False
brace_count = 0

i = 0
while i < len(lines):
    line = lines[i]
    
    # Check if this is a style tag with sidebar content
    if '<style>' in line and '</style>' not in line:
        # Look ahead to see if this style block contains sidebar styles
        j = i + 1
        style_content = [line]
        while j < len(lines) and '</style>' not in lines[j]:
            style_content.append(lines[j])
            j += 1
        if j < len(lines):
            style_content.append(lines[j])
        
        full_style = '\n'.join(style_content)
        
        # If this style block contains toc-widget, related-widget, or toc-more-link, skip it
        if '.toc-widget' in full_style or '.related-widget' in full_style or '.toc-more-link' in full_style:
            print(f"Removing inline sidebar style block at line {i+1}")
            i = j + 1  # Skip past the entire style block
            continue
    
    new_lines.append(line)
    i += 1

new_content = '\n'.join(new_lines)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Cleaned inline styles from {filepath}")
