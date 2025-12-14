import os
import re

# Read footer template
with open('footer-template.html', 'r', encoding='utf-8') as f:
    footer_content = f.read()

# List of files to update (excluding ones that already have footer-pro)
files_to_update = [
    'shop.html',
    'index.html',
    'product.html',
    'about.html', 
    'blog.html',
    'subscription.html',
    'quiz.html',
    'delivery.html',
    'contacts.html',
    'account.html',
    'b2b.html',
    'privacy.html',
    'return.html'
]

updated_count = 0

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f'Skip: {filename} not found')
        continue
        
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already has footer-pro
        # if 'footer-pro' in content:
        #     print(f'Skip: {filename} already has footer-pro')
        #     continue
        
        # Find and replace footer section
        # Pattern: from <footer to </footer>
        footer_pattern = r'<footer[^>]*>.*?</footer>'
        
        if re.search(footer_pattern, content, re.DOTALL):
            new_content = re.sub(footer_pattern, footer_content, content, flags=re.DOTALL)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f'OK: {filename}')
            updated_count += 1
        else:
            # If no footer found, add before </body>
            if '</body>' in content:
                new_content = content.replace('</body>', footer_content + '\n</body>')
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'OK (added): {filename}')
                updated_count += 1
            else:
                print(f'ERROR: {filename} has no footer or </body>')
                
    except Exception as e:
        print(f'ERROR: {filename} - {str(e)}')

print(f'\nTotal updated: {updated_count} files')
