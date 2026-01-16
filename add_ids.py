#!/usr/bin/env python3
"""Add section IDs to H2 headings for TOC anchor links"""

import re

filepath = "articles/ethiopia-coffee-origin.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add IDs to h2 elements based on their data-i18n key
section_map = {
    'h2_1': 'section-legend',
    'h2_2': 'section-geography', 
    'h2_3': 'section-regions',
    'h2_4': 'section-processing',
    'h2_5': 'section-taste',
    'h2_6': 'section-ceremony',
    'h2_7': 'section-today',
}

for key, section_id in section_map.items():
    # Find h2 with this data-i18n key and add id
    pattern = f'<h2 data-i18n="articles\\.ethiopia_origin\\.{key}">'
    replacement = f'<h2 id="{section_id}" data-i18n="articles.ethiopia_origin.{key}">'
    content = re.sub(pattern, replacement, content)
    print(f"Added id={section_id} to {key}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
