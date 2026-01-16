import re
from pathlib import Path

# All articles for cross-linking
ALL_ARTICLES = [
    ("ethiopia-coffee-origin.html", "articles.ethiopia_origin.title", "Ефіопія — батьківщина кави"),
    ("yirgacheffe-region.html", "articles.yirgacheffe.title", "Yirgacheffe: регіон легенд"),
    ("sidamo-guide.html", "articles.sidamo.title", "Sidamo: повний гід"),
    ("what-is-specialty.html", "articles.specialty.title", "Що таке specialty кава?"),
    ("natural-vs-washed.html", "articles.processing.title", "Натуральна vs мита обробка"),
    ("light-vs-dark-roast.html", "articles.roast.title", "Світле vs темне обсмаження"),
    ("how-to-brew-v60.html", "articles.v60.title", "Як заварювати V60"),
    ("aeropress-recipes.html", "articles.aeropress.title", "Рецепти для AeroPress"),
    ("cold-brew-recipe.html", "articles.coldbrew.title", "Cold Brew: повний гід"),
    ("turka-recipe.html", "articles.turka.title", "Кава в турці"),
    ("espresso-mistakes.html", "articles.espresso.title", "Помилки при еспресо"),
    ("grinder-guide.html", "articles.grinder.title", "Як обрати кавомолку"),
    ("water-for-coffee.html", "articles.water.title", "Вода для кави"),
    ("coffee-storage.html", "articles.storage.title", "Як зберігати каву"),
    ("caffeine-myths.html", "articles.caffeine.title", "Міфи про кофеїн"),
]

def get_related_articles(current_file, count=5):
    """Get related articles excluding current file"""
    related = [a for a in ALL_ARTICLES if a[0] != current_file]
    return related[:count]

def create_left_sidebar(current_file):
    """Create related articles sidebar (LEFT)"""
    articles = get_related_articles(current_file)
    links = "\n".join([
        f'                    <li><a href="{a[0]}" data-i18n="{a[1]}">{a[2]}</a></li>'
        for a in articles
    ])
    
    return f'''<aside class="article-sidebar-left">
            <div class="related-widget">
                <h4>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/>
                        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>
                    </svg>
                    <span data-i18n="blog.related_articles">Читайте також</span>
                </h4>
                <ul>
{links}
                </ul>
                <a href="../blog.html" class="toc-more-link">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M5 12h14M12 5l7 7-7 7"/>
                    </svg>
                    <span data-i18n="blog.all_articles">Усі статті</span>
                </a>
            </div>
        </aside>'''

def read_file_any_encoding(filepath):
    encodings = ['utf-8', 'utf-8-sig', 'cp1251', 'windows-1251', 'latin-1']
    for enc in encodings:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return f.read(), enc
        except (UnicodeDecodeError, UnicodeError):
            continue
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        return f.read(), 'utf-8-replace'

def update_article(filepath):
    """Update article sidebars: LEFT=related articles, RIGHT=ToC"""
    try:
        content, enc = read_file_any_encoding(filepath)
        filename = filepath.name
        
        # Extract current ToC content
        toc_match = re.search(
            r'<aside class="article-sidebar-left">\s*<div class="toc-widget">(.*?)</div>\s*</aside>',
            content, re.DOTALL
        )
        
        if not toc_match:
            return "NO_TOC_FOUND"
        
        toc_content = toc_match.group(1)
        
        # Create new LEFT sidebar (related articles)
        new_left = create_left_sidebar(filename)
        
        # Create new RIGHT sidebar (ToC with scroll spy)
        new_right = f'''<aside class="article-sidebar-right">
            <div class="toc-widget" id="toc-widget">
                {toc_content}
            </div>
        </aside>'''
        
        # Replace old left sidebar with new left (related articles)
        content = re.sub(
            r'<aside class="article-sidebar-left">.*?</aside>',
            new_left,
            content,
            flags=re.DOTALL
        )
        
        # Replace old right sidebar with new right (ToC)
        content = re.sub(
            r'<aside class="article-sidebar-right">.*?</aside>',
            new_right,
            content,
            flags=re.DOTALL
        )
        
        # Add scroll spy script before </body> if not present
        if 'scrollSpyToc' not in content:
            scroll_spy_script = '''
    <script>
    // Scroll Spy for ToC highlighting
    function scrollSpyToc() {
        const sections = document.querySelectorAll('h2[id], h3[id]');
        const tocLinks = document.querySelectorAll('.toc-widget a[href^="#"]');
        
        if (!sections.length || !tocLinks.length) return;
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.getAttribute('id');
                    tocLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === '#' + id) {
                            link.classList.add('active');
                        }
                    });
                }
            });
        }, { rootMargin: '-20% 0px -60% 0px' });
        
        sections.forEach(section => observer.observe(section));
    }
    document.addEventListener('DOMContentLoaded', scrollSpyToc);
    </script>
'''
            content = content.replace('</body>', scroll_spy_script + '</body>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return "UPDATED"
        
    except Exception as e:
        return f"ERROR: {e}"

# Process all articles
articles_dir = Path('articles')
html_files = list(articles_dir.glob('*.html'))

print("Updating article sidebars...")
updated = 0
errors = []

for filepath in html_files:
    result = update_article(filepath)
    if result == "UPDATED":
        print(f"OK: {filepath.name}")
        updated += 1
    else:
        print(f"ERR: {filepath.name} - {result}")
        errors.append((filepath.name, result))

print(f"\n=== RESULT ===")
print(f"Updated: {updated}")
print(f"Errors: {len(errors)}")
