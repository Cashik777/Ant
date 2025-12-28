from pathlib import Path

def fix_paths():
    base_dir = Path('.')
    # Target directories
    dirs = ['articles', 'blog']
    
    count = 0
    
    for d in dirs:
        dir_path = base_dir / d
        if not dir_path.exists():
            continue
            
        print(f"Scanning {d}...")
        for html_file in dir_path.glob('*.html'):
            try:
                content = html_file.read_text(encoding='utf-8')
                
                # Incorrect path pattern
                wrong_tag = '<script src="js/i18n-inline.js"></script>'
                correct_tag = '<script src="../js/i18n-inline.js"></script>'
                
                if wrong_tag in content:
                    new_content = content.replace(wrong_tag, correct_tag)
                    html_file.write_text(new_content, encoding='utf-8')
                    print(f"  [FIXED] {html_file.name}")
                    count += 1
                elif correct_tag in content:
                    print(f"  [OK] {html_file.name}")
                else:
                    print(f"  [SKIP] {html_file.name} - tag not found")
                    
            except Exception as e:
                print(f"  [ERROR] {html_file.name}: {e}")

    print(f"\nFixed {count} files.")

if __name__ == "__main__":
    fix_paths()
