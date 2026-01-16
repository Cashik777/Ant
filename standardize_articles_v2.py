import os
import re

# Directory containing the articles
articles_dir = r"C:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect\articles"

# Shared Sidebar Content (HTML)
# Left Sidebar (ToC placeholder - will be generated per article)
left_sidebar_template = """            <aside class="article-sidebar-left">
                <div class="toc-widget">
                    <h4>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2">
                            <path d="M4 6h16M4 12h16M4 18h7" />
                        </svg>
                        <span data-i18n="blog.table_of_contents">Зміст статті</span>
                    </h4>
                    <ul>
{toc_items}
                    </ul>
                    <a href="../blog.html" class="toc-more-link">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2">
                            <path d="M5 12h14M12 5l7 7-7 7" />
                        </svg>
                        <span data-i18n="blog.more_articles">Більше історій</span>
                    </a>
                </div>
            </aside>"""

# Right Sidebar (Sommelier + Recommended)
right_sidebar_content = """            <aside class="article-sidebar-right">
                <div class="sommelier-card">
                    <div class="sommelier-header">
                        <span class="sommelier-tag" data-i18n="articles.sommelier.tag">Expert Selection</span>
                        <h3 class="sommelier-title" data-i18n="articles.sommelier.title">Guatamala Antigua Review</h3>
                    </div>

                    <div class="sca-score-seal">
                        <span class="sca-label">SCA SCORE</span>
                        <span class="sca-value">89.5</span>
                    </div>

                    <div class="radar-chart-container">
                        <svg viewBox="0 0 100 100">
                            <circle cx="50" cy="50" r="40" fill="none" stroke="rgba(201,169,98,0.1)"
                                stroke-width="0.5" />
                            <circle cx="50" cy="50" r="30" fill="none" stroke="rgba(201,169,98,0.1)"
                                stroke-width="0.5" />
                            <circle cx="50" cy="50" r="20" fill="none" stroke="rgba(201,169,98,0.1)"
                                stroke-width="0.5" />
                            <circle cx="50" cy="50" r="10" fill="none" stroke="rgba(201,169,98,0.1)"
                                stroke-width="0.5" />
                            <line x1="50" y1="10" x2="50" y2="90" stroke="rgba(201,169,98,0.1)" stroke-width="0.5" />
                            <line x1="15" y1="30" x2="85" y2="70" stroke="rgba(201,169,98,0.1)" stroke-width="0.5" />
                            <line x1="15" y1="70" x2="85" y2="30" stroke="rgba(201,169,98,0.1)" stroke-width="0.5" />
                            <polygon points="50,15 80,35 75,65 50,85 25,65 20,35" fill="rgba(201,169,98,0.4)"
                                stroke="#C9A962" stroke-width="1.5" />
                        </svg>
                    </div>

                    <div class="flavor-notes">
                        <div class="note-item">
                            <span class="note-label" data-i18n="articles.sommelier.altitude">Altitude</span>
                            <span class="note-value">2100m</span>
                        </div>
                        <div class="note-item">
                            <span class="note-label" data-i18n="articles.sommelier.process">Process</span>
                            <span class="note-value">Slow Natural</span>
                        </div>
                        <div class="note-item">
                            <span class="note-label" data-i18n="articles.sommelier.acidity">Acidity</span>
                            <span class="note-value" data-i18n="articles.sommelier.complex">Complex</span>
                        </div>
                        <div class="note-item">
                            <span class="note-label" data-i18n="articles.sommelier.body">Body</span>
                            <span class="note-value" data-i18n="articles.sommelier.velvety">Velvety</span>
                        </div>
                    </div>

                    <p class="sommelier-quote" data-i18n="articles.sommelier.quote">
                        A breathtaking explosion of jasmine and bergamot, leading to a long, honeyed finish. True
                        Ethiopian excellence.
                    </p>

                    <div class="sommelier-cta">
                        <a href="../subscription.html" class="sommelier-btn"
                            data-i18n="subscription.subscribe_btn">Subscribe & Taste</a>
                    </div>
                </div>

                <!-- RECOMMENDED STORIES WIDGET -->
                <div class="recommended-stories-widget">
                    <h4 data-i18n="blog.other_stories">Інші історії</h4>

                    <a href="water-for-coffee.html" class="story-card-sm">
                        <div class="story-img">
                            <img src="https://images.unsplash.com/photo-1517701604599-bb29b565090c?w=600" alt="Water">
                        </div>
                        <div class="story-info">
                            <span class="story-title" data-i18n="blog.articles.article_13.title">Яка вода потрібна для
                                ідеальної кави?</span>
                            <span class="story-desc" data-i18n="blog.recommended_desc_water">Як мінеральний склад води
                                впливає на смак вашої чашки.</span>
                        </div>
                    </a>

                    <a href="coffee-storage.html" class="story-card-sm">
                        <div class="story-img">
                            <img src="https://images.unsplash.com/photo-1610632380989-680fe40816c6?w=600" alt="Storage">
                        </div>
                        <div class="story-info">
                            <span class="story-title" data-i18n="blog.articles.article_5.title">Як правильно зберігати
                                каву</span>
                            <span class="story-desc" data-i18n="blog.recommended_desc_storage">Секрети збереження
                                свіжості та аромату обсмаженого зерна.</span>
                        </div>
                    </a>

                    <a href="how-to-brew-v60.html" class="story-card-sm">
                        <div class="story-img">
                            <img src="https://images.unsplash.com/photo-1434494878577-86c23bcb06b9?w=600" alt="V60">
                        </div>
                        <div class="story-info">
                            <span class="story-title" data-i18n="blog.articles.article_3.title">Ідеальний V60:
                                покроковий рецепт</span>
                            <span class="story-desc" data-i18n="blog.recommended_desc_v60">Покрокова інструкція
                                приготування ідеального пуроверу V60.</span>
                        </div>
                    </a>
                </div>
            </aside>"""

# New CSS styles to be added
new_styles = """
        /* RECOMMENDED STORIES WIDGET */
        .recommended-stories-widget {
            margin-top: 30px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .recommended-stories-widget h4 {
            font-family: 'Playfair Display', serif;
            font-size: 13px;
            color: #D4AF37;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 5px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .recommended-stories-widget h4::after {
            content: '';
            flex-grow: 1;
            height: 1px;
            background: rgba(212, 175, 55, 0.2);
        }

        .story-card-sm {
            display: flex;
            gap: 15px;
            text-decoration: none;
            /* transition */
            transition: all 0.3s ease;
            padding: 10px;
            margin: -10px;
            border-radius: 12px;
        }

        .story-card-sm:hover {
            background: rgba(212, 175, 55, 0.05);
            transform: translateX(5px);
        }

        .story-card-sm .story-img {
            width: 70px;
            height: 70px;
            flex-shrink: 0;
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid rgba(212, 175, 55, 0.2);
        }

        .story-card-sm .story-img img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }

        .story-card-sm:hover .story-img img {
            transform: scale(1.1);
        }

        .story-card-sm .story-info {
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 4px;
        }

        .story-card-sm .story-title {
            font-family: 'Playfair Display', serif;
            font-size: 15px;
            color: #2a1f0a;
            line-height: 1.3;
            transition: color 0.3s ease;
        }

        .story-card-sm:hover .story-title {
            color: #D4AF37;
        }

        .story-card-sm .story-desc {
            font-size: 11px;
            color: #8a7a5a;
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
    """

def process_file(file_path):
    print(f"Processing {file_path}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update CSS
    if ".recommended-stories-widget" not in content:
        # Find the end of the style block
        content = content.replace("    </style>", new_styles + "    </style>")

    # 2. Add IDs to H2 tags and collect TOC items
    toc_items = []
    h2_pattern = re.compile(r'<h2(.*?)data-i18n="(.*?)"(.*?)>(.*?)</h2>', re.IGNORECASE)
    
    section_count = 1
    def replace_h2(match):
        nonlocal section_count
        attrs1, i18n_key, attrs2, existing_content = match.groups()
        section_id = f"section-{section_count}"
        
        # Prepare TOC item
        toc_items.append(f'                        <li><a href="#{section_id}" data-i18n="{i18n_key}">{existing_content}</a></li>')
        
        new_h2 = f'<h2 id="{section_id}"{attrs1}data-i18n="{i18n_key}"{attrs2}>{existing_content}</h2>'
        section_count += 1
        return new_h2

    new_content = h2_pattern.sub(replace_h2, content)

    # 3. Wrap article-body in layout
    if "article-layout" not in new_content:
        # Find the article-body start and end
        # We look for <article class="article-body">...</article>
        article_match = re.search(r'(<article class="article-body">.*?</article>)', new_content, re.DOTALL)
        if article_match:
            original_article = article_match.group(1)
            
            # Construct the new layout
            toc_html = left_sidebar_template.format(toc_items="\n".join(toc_items))
            
            new_layout = f"""        <div class="article-layout">
{toc_html}
            <div class="article-main">
                {original_article}
            </div>
{right_sidebar_content}
        </div>"""
            
            new_content = new_content.replace(original_article, new_layout)
        else:
            print(f"Skipping {file_path}: <article class=\"article-body\"> not found.")
            return

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Done: {file_path}")

# Iterate through files
for filename in os.listdir(articles_dir):
    if filename.endswith(".html") and filename != "ethiopia-coffee-origin.html":
        process_file(os.path.join(articles_dir, filename))
