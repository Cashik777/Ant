"""
Add language switcher top-bar to all HTML pages that are missing it.
Run from the EthioDirect directory: python add_language_topbar.py
"""

import os
import re
from pathlib import Path

# Standard top-bar for root-level pages
ROOT_TOPBAR = '''    <!-- TOP BAR -->
    <div class="top-bar">
        <div class="container top-bar-inner">
            <div class="top-bar-left">
                <span><i class="fas fa-phone-alt"></i> +380 (50) 123-45-67</span>
                <span class="divider-dot">•</span>
                <span><i class="fas fa-clock"></i> Пн-Пт: 9:00-18:00</span>
            </div>
            <div class="top-bar-center">
                <div class="promo-ticker">
                    <span class="ticker-item">🔥 <strong>АКЦІЯ:</strong> безкоштовна доставка від 500₴</span>
                    <span class="ticker-divider">|</span>
                    <span class="ticker-item">☕ Підписка: <strong>-10%</strong> на кожну доставку</span>
                    <span class="ticker-divider">|</span>
                    <span class="ticker-item">⚡ Свіжа обсмажка <strong>до 3 днів</strong></span>
                </div>
            </div>
            <div class="top-bar-right">
                <a href="#" translate="no" class="active" onclick="setLanguage('uk'); return false;">UA</a>
                <a href="#" translate="no" onclick="setLanguage('ru'); return false;">RU</a>
                <a href="#" translate="no" onclick="setLanguage('en'); return false;">EN</a>
            </div>
        </div>
    </div>
'''

# Top-bar for subdirectory pages (blog/, articles/)
SUB_TOPBAR = '''    <!-- TOP BAR -->
    <div class="top-bar">
        <div class="container top-bar-inner">
            <div class="top-bar-left">
                <span><i class="fas fa-phone-alt"></i> +380 (50) 123-45-67</span>
            </div>
            <div class="top-bar-center">
                <span>🔥 Безкоштовна доставка від 500₴</span>
            </div>
            <div class="top-bar-right">
                <a href="#" translate="no" class="active" onclick="setLanguage('uk'); return false;">UA</a>
                <a href="#" translate="no" onclick="setLanguage('ru'); return false;">RU</a>
                <a href="#" translate="no" onclick="setLanguage('en'); return false;">EN</a>
            </div>
        </div>
    </div>
'''

def has_topbar(content):
    """Check if the page already has a top-bar with language buttons"""
    return 'top-bar-right' in content and 'setLanguage' in content

def add_topbar(filepath, is_subdirectory=False):
    """Add top-bar to an HTML file if missing"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if has_topbar(content):
        return False, "Already has top-bar"
    
    # Find the position to insert (after <body> tag, before first content)
    body_match = re.search(r'<body[^>]*>\s*', content)
    if not body_match:
        return False, "No <body> tag found"
    
    insert_pos = body_match.end()
    
    # Use appropriate top-bar based on directory depth
    topbar = SUB_TOPBAR if is_subdirectory else ROOT_TOPBAR
    
    # Insert the top-bar
    new_content = content[:insert_pos] + '\n' + topbar + '\n' + content[insert_pos:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, "Top-bar added"

def ensure_google_translate_script(filepath, is_subdirectory=False):
    """Ensure the google-translate.js script is included"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'google-translate.js' in content:
        return False, "Already has google-translate.js"
    
    # Find position before </body>
    body_close = content.rfind('</body>')
    if body_close == -1:
        return False, "No </body> tag found"
    
    script_path = '../js/google-translate.js' if is_subdirectory else 'js/google-translate.js'
    script_tag = f'    <script src="{script_path}"></script>\n'
    
    new_content = content[:body_close] + script_tag + content[body_close:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True, "google-translate.js added"


def main():
    base_dir = Path('.')
    
    # Find all HTML files
    html_files = []
    
    # Root level files
    for f in base_dir.glob('*.html'):
        if f.name not in ['footer-template.html', 'seo-meta-template.html', 'structured-data-templates.html']:
            html_files.append((f, False))
    
    # Subdirectory files
    for subdir in ['blog', 'articles']:
        subdir_path = base_dir / subdir
        if subdir_path.exists():
            for f in subdir_path.glob('*.html'):
                if not f.name.startswith('_'):
                    html_files.append((f, True))
    
    print(f"Found {len(html_files)} HTML files to process\n")
    
    for filepath, is_sub in html_files:
        print(f"\nProcessing: {filepath}")
        
        # Add top-bar if missing
        success, msg = add_topbar(filepath, is_sub)
        print(f"  Top-bar: {msg}")
        
        # Ensure google-translate.js is included
        success, msg = ensure_google_translate_script(filepath, is_sub)
        print(f"  Script: {msg}")
    
    print("\n✅ Done! All pages have been processed.")


if __name__ == '__main__':
    main()
