import sys, re

# Read footer template
with open('footer-template.html', 'r', encoding='utf-8') as f:
    footer_content = f.read()

# List of files to update
files_to_update = [
    'product.html', 'about.html', 'blog.html', 
    'subscription.html', 'quiz.html', 'delivery.html',
    'contacts.html', 'account.html', 'b2b.html',
    'privacy.html', 'return.html'
]

for filename in files_to_update:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace old footer with new one
        # Pattern matches from <footer class="footer"> to </footer>
        pattern = r'<footer class="footer">.*?</footer>'
        
        if re.search(pattern, content, re.DOTALL):
            new_content = re.sub(pattern, footer_content, content, flags=re.DOTALL)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f'✓ Updated: {filename}')
        else:
            print(f'⚠ Skipped (no old footer found): {filename}')
    except FileNotFoundError:
        print(f'✗ Not found: {filename}')
    except Exception as e:
        print(f'✗ Error in {filename}: {str(e)}')

print('\nFooter update complete!')
