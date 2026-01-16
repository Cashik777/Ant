import re
from pathlib import Path

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

# Fix scroll spy script - more robust version
NEW_SCROLL_SPY = '''
    <script>
    // Enhanced Scroll Spy for ToC highlighting
    (function() {
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
            
            // Initial highlight
            highlightToc();
            
            // Throttled scroll handler
            let ticking = false;
            window.addEventListener('scroll', function() {
                if (!ticking) {
                    window.requestAnimationFrame(function() {
                        highlightToc();
                        ticking = false;
                    });
                    ticking = true;
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
'''

filepath = Path('articles/ethiopia-coffee-origin.html')
content, enc = read_file_any_encoding(filepath)

# Remove old scroll spy script
content = re.sub(
    r'<script>\s*//\s*Scroll Spy.*?</script>',
    '',
    content,
    flags=re.DOTALL
)

# Add new scroll spy before </body>
if 'initScrollSpy' not in content:
    content = content.replace('</body>', NEW_SCROLL_SPY + '</body>')
else:
    # Replace existing
    content = re.sub(
        r'<script>\s*//\s*Enhanced Scroll Spy.*?</script>',
        NEW_SCROLL_SPY.strip(),
        content,
        flags=re.DOTALL
    )

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed scroll spy in ethiopia-coffee-origin.html")
