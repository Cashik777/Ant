import re

with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace category keys
replacements = [
    ('data-i18n="blog.cat_about"', 'data-i18n="categories.about"'),
    ('data-i18n="blog.cat_recipes"', 'data-i18n="categories.recipes"'),
    ('data-i18n="blog.cat_tips"', 'data-i18n="categories.tips"'),
    ('data-i18n="blog.cat_equipment"', 'data-i18n="categories.equipment"'),
    ('data-i18n="blog.read_more"', 'data-i18n="read_more"'),
    ('data-i18n="blog.articles_count"', 'data-i18n="articles_count"'),
    ('data-i18n="blog.newsletter_title"', 'data-i18n="newsletter_title"'),
    ('data-i18n="blog.newsletter_text"', 'data-i18n="newsletter_text"'),
]

for old, new in replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f'Replaced {count} instances: {old} -> {new}')
    else:
        print(f'Not found: {old}')

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')
