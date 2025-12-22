#!/usr/bin/env python3
"""Add data-i18n attributes to all blog post HTML files"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent

BLOGS_MAP = {
    "arabica-vs-robusta.html": "arabica_robusta",
    "bean-to-cup.html": "bean_to_cup",
    "brewing-methods.html": "brewing_methods",
    "coffee-processing.html": "coffee_processing",
    "coffee-seasonality.html": "coffee_seasonality",
    "coffee-storage.html": "coffee_storage",
    "cold-brew-guide.html": "cold_brew",
    "espresso-guide.html": "espresso_guide",
    "ethiopia-origins.html": "ethiopia_origins",
    "french-press-guide.html": "french_press",
    "sca-grading.html": "sca_grading",
    "specialty-coffee.html": "specialty_coffee",
    "turka-guide.html": "turka_guide",
    "v60-guide.html": "v60_guide",
    "yirgacheffe-region.html": "yirgacheffe"
}

def add_i18n_to_blog(filepath, blog_key):
    """Add data-i18n attributes to blog HTML"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Add blog key to title
        if f'data-i18n="blog_posts.{blog_key}.title"' not in content:
            content = re.sub(
                r'<h1([^>]*)>([^<]+)</h1>',
                lambda m: f'<h1{m.group(1)} data-i18n="blog_posts.{blog_key}.title">{m.group(2)}</h1>' if 'data-i18n' not in m.group(0) else m.group(0),
                content
            )
        
        # Add to category
        if f'data-i18n="blog_posts.{blog_key}.category"' not in content:
            content = re.sub(
                r'<span class="article-category">([^<]+)</span>',
                lambda m: f'<span class="article-category" data-i18n="blog_posts.{blog_key}.category">{m.group(1)}</span>' if 'data-i18n' not in m.group(0) else m.group(0),
                content
            )
        
        # Add to reading time
        if f'data-i18n="blog_posts.{blog_key}.reading_time"' not in content:
            content = re.sub(
                r'<i class="far fa-clock"></i>\s*(\d+ хвилин[а-я]* читання)',
                lambda m: f'<i class="far fa-clock"></i> <span data-i18n="blog_posts.{blog_key}.reading_time">{m.group(1)}</span>',
                content
            )
        
        # Add to subtitle/lead
        if f'data-i18n="blog_posts.{blog_key}.subtitle"' not in content:
            content = re.sub(
                r'<p class="article-lead">([^<]+)</p>',
                lambda m: f'<p class="article-lead" data-i18n="blog_posts.{blog_key}.subtitle">{m.group(1)}</p>' if 'data-i18n' not in m.group(0) else m.group(0),
                content
            )
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath.name}")
            return True
        else:
            print(f"No changes: {filepath.name}")
            return False
    except Exception as e:
        print(f"Error with {filepath}: {e}")
        return False

def main():
    blog_dir = BASE_DIR / "blog"
    updated = 0
    
    for filename, blog_key in BLOGS_MAP.items():
        filepath = blog_dir / filename
        if filepath.exists():
            if add_i18n_to_blog(filepath, blog_key):
                updated += 1
        else:
            print(f"Not found: {filename}")
    
    print(f"Updated {updated}/{len(BLOGS_MAP)} blog posts")

if __name__ == "__main__":
    main()
