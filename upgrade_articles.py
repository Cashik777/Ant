
import os
import re

# Configuration
ARTICLES_DIR = r'C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect\articles'
TEMPLATE_CSS_LINK = '<link rel="stylesheet" href="../css/sidebar-premium.css?v=20260109-13">'
IGNORE_FILES = ['ethiopia-coffee-origin.html']

# HTML Templates (Same as before)
LEFT_SIDEBAR_TEMPLATE = """
            <aside class="article-sidebar-left">
                <div class="related-widget">
                    <h4>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
                            <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
                        </svg>
                        <span data-i18n="blog.related_articles">Читайте також</span>
                    </h4>
                    <ul>
                        <li><a href="yirgacheffe-region.html" data-i18n="articles.yirgacheffe.title">Yirgacheffe: регіон легенд</a></li>
                        <li><a href="sidamo-guide.html" data-i18n="articles.sidamo.title">Sidamo: повний гід</a></li>
                        <li><a href="what-is-specialty.html" data-i18n="articles.specialty.title">Що таке specialty кава?</a></li>
                        <li><a href="natural-vs-washed.html" data-i18n="articles.processing.title">Натуральна vs мита обробка</a></li>
                        <li><a href="aeropress-recipes.html" data-i18n="articles.aeropress_recipes.title">3 рецепти для Аеропреса</a></li>
                    </ul>
                    <a href="../blog.html" class="toc-more-link">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M5 12h14M12 5l7 7-7 7" />
                        </svg>
                        <span data-i18n="blog.all_articles">Усі статті</span>
                    </a>
                </div>
            </aside>
"""

RIGHT_SIDEBAR_TEMPLATE_START = """
            <aside class="article-sidebar-right">
                <div class="toc-widget" id="toc-widget">
                    <h4>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M4 6h16M4 12h16M4 18h7" />
                        </svg>
                        <span data-i18n="blog.table_of_contents">Зміст статті</span>
                    </h4>
                    <ul>
"""

RIGHT_SIDEBAR_TEMPLATE_END = """
                    </ul>
                    <a href="../blog.html" class="toc-more-link">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            <path d="M5 12h14M12 5l7 7-7 7" />
                        </svg>
                        <span data-i18n="blog.more_articles">Більше історій</span>
                    </a>
                </div>
            </aside>
"""

SCROLL_SPY_SCRIPT = """
    <script>
        // Enhanced Scroll Spy for ToC highlighting + Sidebar Footer Collision Prevention
        (function () {
            function initScrollSpy() {
                const sections = document.querySelectorAll('h2[id]');
                const tocLinks = document.querySelectorAll('.toc-widget a[href^="#"]');

                if (!sections.length || !tocLinks.length) return;

                function highlightToc() {
                    let currentSection = '';
                    const scrollPos = window.scrollY + 200;

                    sections.forEach(section => {
                        const sectionTop = section.offsetTop;
                        if (scrollPos >= sectionTop) {
                            currentSection = section.getAttribute('id');
                        }
                    });

                    tocLinks.forEach(link => {
                        link.classList.remove('active');
                        if (link.getAttribute('href') === '#' + currentSection) {
                            link.classList.add('active');
                        }
                    });
                }

                highlightToc();

                let ticking = false;
                window.addEventListener('scroll', function () {
                    if (!ticking) {
                        window.requestAnimationFrame(function () {
                            highlightToc();
                            handleSidebarFooterCollision();
                            ticking = false;
                        });
                        ticking = true;
                    }
                });
            }

            function handleSidebarFooterCollision() {
                const leftSidebar = document.querySelector('.article-sidebar-left');
                const rightSidebar = document.querySelector('.article-sidebar-right');
                const footer = document.querySelector('.footer-pro');

                if (!footer) return;

                const footerTop = footer.getBoundingClientRect().top;
                const minDistance = 50; 

                [leftSidebar, rightSidebar].forEach(sidebar => {
                    if (!sidebar) return;
                    const widget = sidebar.querySelector('.related-widget, .toc-widget');
                    if (!widget) return;

                    const widgetRect = widget.getBoundingClientRect();
                    const widgetBottom = widgetRect.bottom;

                    if (widgetBottom > footerTop - minDistance) {
                        const pullUp = widgetBottom - (footerTop - minDistance);
                        widget.style.transform = `translateY(-${pullUp}px)`;
                    } else {
                        widget.style.transform = 'translateY(0)';
                    }
                });
            }

            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', initScrollSpy);
            } else {
                initScrollSpy();
            }
        })();
    </script>
"""

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Remove inline <style>
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)

    # 2. Add Premium CSS Link
    if 'sidebar-premium.css' not in content:
        content = re.sub(r'(<link rel="stylesheet" href="../css/main.css\?v=[\d-]+">)', r'\1\n    ' + TEMPLATE_CSS_LINK, content)

    # 3. Capture Main Content
    # We look for <main>...</main>
    # Note: re.DOTALL makes . match newlines
    match = re.search(r'<main>\s*(.*?)\s*</main>', content, re.DOTALL)
    if not match:
        print(f"  Skipping: No <main> found.")
        return

    main_inner = match.group(1)

    # Split Header and Body
    # Assuming <section class="article-header">...</section> followed by <article class="article-body">...</article>
    header_match = re.search(r'(<section class="article-header">.*?</section>)', main_inner, re.DOTALL)
    body_match = re.search(r'(<article class="article-body">.*?</article>)', main_inner, re.DOTALL)

    if not header_match or not body_match:
        print(f"  Skipping: Header/Body not found.")
        return

    header_html = header_match.group(1)
    body_html = body_match.group(1)

    # 4. Process Body for TOC
    toc_items = []
    h2_counter = 0
    
    def h2_replacer(match):
        nonlocal h2_counter
        attrs = match.group(1)
        text = match.group(2)
        
        # Check for id
        id_match = re.search(r'id=["\'](.*?)["\']', attrs)
        h2_id = None
        if id_match:
            existing_id = id_match.group(1)
            if existing_id != "section-header":
                h2_id = existing_id
        
        if not h2_id:
            h2_counter += 1
            # Try to derive from i18n
            i18n_match = re.search(r'data-i18n=["\'](.*?)["\']', attrs)
            if i18n_match:
                key_parts = i18n_match.group(1).split('.')
                suffix = key_parts[-1]
                h2_id = f"section-{suffix}"
            else:
                slug = slugify(text)
                if not slug:
                     h2_id = f"section-{h2_counter}"
                else:
                     h2_id = f"section-{slug}"
            
            # Ensure unique ID if simple repetition (minimal check, strictly relying on counter/suffix usually enough for this dataset)
            
            # Remove old ID if it exists (to avoid duplicate attributes)
            attrs = re.sub(r'\s*id=["\'].*?["\']', '', attrs)
            
            attrs = f' id="{h2_id}"' + attrs

        # Check for data-i18n (again for TOC)
        i18n_match = re.search(r'data-i18n=["\'](.*?)["\']', attrs)
        i18n_key = i18n_match.group(1) if i18n_match else None
        
        # Add to TOC
        toc_items.append({'id': h2_id, 'text': text, 'i18n': i18n_key})
        
        return f'<h2{attrs}>{text}</h2>'

    # Regex to find H2 tags properly: <h2 attributes>text</h2>
    new_body_html = re.sub(r'<h2(.*?)>(.*?)</h2>', h2_replacer, body_html, flags=re.DOTALL)

    # Generate TOC HTML
    toc_html_list = ""
    for item in toc_items:
        i18n_attr = f' data-i18n="{item["i18n"]}"' if item['i18n'] else ''
        toc_html_list += f'                        <li><a href="#{item["id"]}"{i18n_attr}>{item["text"]}</a></li>\n'

    # Construct New Main
    new_main_html = f"""
    <main>
        {header_html}

        <div class="article-layout">
            {LEFT_SIDEBAR_TEMPLATE}

            <div class="article-main">
                {new_body_html}
            </div>

            {RIGHT_SIDEBAR_TEMPLATE_START}
{toc_html_list}
            {RIGHT_SIDEBAR_TEMPLATE_END}
        </div>
    </main>"""

    # Replace Main in Content
    content = re.sub(r'<main>.*?</main>', new_main_html, content, flags=re.DOTALL)

    # 5. Add Script
    if "initScrollSpy" not in content:
        content = re.sub(r'</body>', f'{SCROLL_SPY_SCRIPT}\n</body>', content)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"  Updated {filepath}")

def main():
    files = [f for f in os.listdir(ARTICLES_DIR) if f.endswith('.html') and f not in IGNORE_FILES]
    print(f"Found {len(files)} files to upgrade.")
    for filename in files:
        try:
            process_file(os.path.join(ARTICLES_DIR, filename))
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    print("All done.")

if __name__ == "__main__":
    main()
