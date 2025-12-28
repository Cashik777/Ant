import json
import os

root = r"c:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect\locales"
langs = ["uk", "ru", "en"]

for lang in langs:
    blog_path = os.path.join(root, lang, "blog.json")
    articles_path = os.path.join(root, lang, "articles.json")
    
    if os.path.exists(blog_path):
        with open(blog_path, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
        
        if "articles" in data:
            articles_data = data["articles"]
            
            # Write articles.json
            with open(articles_path, 'w', encoding='utf-8') as f:
                json.dump(articles_data, f, indent=4, ensure_ascii=False)
            print(f"Created {articles_path}")
        else:
            print(f"No articles in {blog_path}")
    else:
        print(f"Missing {blog_path}")
