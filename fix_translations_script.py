import os
import re

base_dir = r'c:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect'

patterns_replacements = [
    (r'<script src="js/translations\.js"></script><script src="js/i18n\.js"></script>', '<script src="js/i18n.js"></script>'),
    (r'<script src="js/translations\.js"></script>', '<script src="js/i18n.js"></script>'),
    (r'<script src="\.\./js/translations\.js"></script><script src="\.\./js/i18n\.js"></script>', '<script src="../js/i18n.js"></script>'),
    (r'<script src="\.\./js/translations\.js"></script>', '<script src="../js/i18n.js"></script>'),
]

count = 0
for root, dirs, files in os.walk(base_dir):
    dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules']]
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            for pattern, replacement in patterns_replacements:
                content = re.sub(pattern, replacement, content)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Updated: {filepath}')
                count += 1

print(f'\nTotal files updated: {count}')
