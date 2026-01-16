#!/usr/bin/env python3
"""Debug cta pattern"""
import re

filepath = "articles/ethiopia-coffee-origin.html"

with open(filepath, 'rb') as f:
    content = f.read().decode('latin1')

# Find any class with cta
print("Looking for CTA patterns...")
for pattern in ['cta-box', 'cta_box', 'cta', 'CTA', 'call-to-action']:
    if pattern.lower() in content.lower():
        idx = content.lower().find(pattern.lower())
        print(f"Found '{pattern}' at {idx}")
        # Show context
        context = content[idx-50:idx+150]
        with open('debug_output.txt', 'w', encoding='utf-8') as f:
            f.write(f"Pattern: {pattern}\nContext:\n{repr(context)}")
        break

# Also look for h3 with cta_title
if 'cta_title' in content.lower():
    idx = content.lower().find('cta_title')
    print(f"Found cta_title at {idx}")

# Look for order/shop button patterns
patterns_to_try = ['order', 'shop', '</article']
for p in patterns_to_try:
    if p.lower() in content.lower():
        idx = content.lower().find(p.lower())
        print(f"Found '{p}' at {idx}")

# Find where content ends
article_match = re.search(r'</article>', content, re.IGNORECASE)
if article_match:
    print(f"</article> found at {article_match.start()}")
    context = content[article_match.start()-300:article_match.end()]
    with open('debug_output.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n\nBefore </article>:\n{repr(context)}")
