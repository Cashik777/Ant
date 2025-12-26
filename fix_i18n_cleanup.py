import os
import re

base_dir = r'c:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect'

# Extended key mappings
key_mappings = {
    # Delivery keys that were missed
    'delivery_page.nova_poshta': 'delivery.nova_poshta.title',
    'delivery_page.ukrposhta': 'delivery.ukrposhta.title',
    'delivery_page.delivery_title': 'delivery.title',
    'delivery.methods_title': 'delivery.title',
    'delivery.payment_title': 'payment.title',
    
    # B2B keys
    'b2b_page.hero_badge': 'hero.badge',
    'B2B_PAGE.CTA_OFFER': 'cta.button',
    
    # FAQ keys
    'faq_page.not_found_title': 'contact.title',
    'faq_page.not_found_text': 'contact.text',
    'FAQ_PAGE.BTN_TELEGRAM': 'contact.button',
    'FAQ_PAGE.BTN_PHONE': 'contact.button',
}

def clean_duplicate_data_i18n(content):
    """Remove duplicate data-i18n attributes, keeping only the first one"""
    # Pattern to find elements with multiple data-i18n
    # E.g. data-i18n="key1" data-i18n="key2" -> data-i18n="key1"
    pattern = r'(data-i18n="[^"]*")\s*data-i18n="[^"]*"'
    while re.search(pattern, content):
        content = re.sub(pattern, r'\1', content)
    return content

count = 0
files_updated = []

for root, dirs, files in os.walk(base_dir):
    dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'locales']]
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            # Apply key mappings
            for old_key, new_key in key_mappings.items():
                content = content.replace(f'data-i18n="{old_key}"', f'data-i18n="{new_key}"')
                content = content.replace(f"data-i18n='{old_key}'", f"data-i18n='{new_key}'")
            
            # Clean duplicate data-i18n attributes
            content = clean_duplicate_data_i18n(content)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Updated: {filepath}')
                files_updated.append(filepath)
                count += 1

print(f'\nTotal files updated: {count}')
