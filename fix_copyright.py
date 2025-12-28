import glob
import os

def fix_copyright():
    # Target string
    target_str = '<p>&copy; 2025 EthioDirect. Всі права захищені.</p>'
    replacement_str = '<p data-i18n="footer.copyright">&copy; 2025 EthioDirect. Всі права захищені.</p>'
    
    # Find all HTML files recursively
    files = glob.glob('**/*.html', recursive=True)
    
    count = 0
    for file_path in files:
        # Skip node_modules or other junk if any (though unlikely in scratches)
        if 'node_modules' in file_path:
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target_str in content:
            # Check if it already has data-i18n (naive check, but target_str doesn't have it)
            # The replacement target includes the <p> so it excludes already fixed ones
            new_content = content.replace(target_str, replacement_str)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Fixed copyright in: {file_path}")
            count += 1
            
    print(f"Total files fixed: {count}")

if __name__ == "__main__":
    fix_copyright()
