import json
from pathlib import Path

# Translations to add for all languages
TRANSLATIONS = {
    "uk": {
        "related_articles": "Читайте також",
        "all_articles": "Усі статті"
    },
    "ru": {
        "related_articles": "Читайте также",
        "all_articles": "Все статьи"
    },
    "en": {
        "related_articles": "Related Articles",
        "all_articles": "All Articles"
    }
}

# Article titles for all languages
ARTICLE_TITLES = {
    "ethiopia_origin": {"uk": "Ефіопія — батьківщина кави", "ru": "Эфиопия — родина кофе", "en": "Ethiopia — Birthplace of Coffee"},
    "yirgacheffe": {"uk": "Yirgacheffe: регіон легенд", "ru": "Yirgacheffe: регион легенд", "en": "Yirgacheffe: Region of Legends"},
    "sidamo": {"uk": "Sidamo: повний гід", "ru": "Sidamo: полный гид", "en": "Sidamo: Complete Guide"},
    "specialty": {"uk": "Що таке specialty кава?", "ru": "Что такое specialty кофе?", "en": "What is Specialty Coffee?"},
    "processing": {"uk": "Натуральна vs мита обробка", "ru": "Натуральная vs мытая обработка", "en": "Natural vs Washed Processing"},
    "roast": {"uk": "Світле vs темне обсмаження", "ru": "Светлая vs темная обжарка", "en": "Light vs Dark Roast"},
    "v60": {"uk": "Як заварювати V60", "ru": "Как заваривать V60", "en": "How to Brew V60"},
    "aeropress": {"uk": "Рецепти для AeroPress", "ru": "Рецепты для AeroPress", "en": "AeroPress Recipes"},
    "coldbrew": {"uk": "Cold Brew: повний гід", "ru": "Cold Brew: полный гид", "en": "Cold Brew: Complete Guide"},
    "turka": {"uk": "Кава в турці", "ru": "Кофе в турке", "en": "Turkish Coffee"},
    "espresso": {"uk": "Помилки при еспресо", "ru": "Ошибки при эспрессо", "en": "Espresso Mistakes"},
    "grinder": {"uk": "Як обрати кавомолку", "ru": "Как выбрать кофемолку", "en": "How to Choose a Grinder"},
    "water": {"uk": "Вода для кави", "ru": "Вода для кофе", "en": "Water for Coffee"},
    "storage": {"uk": "Як зберігати каву", "ru": "Как хранить кофе", "en": "How to Store Coffee"},
    "caffeine": {"uk": "Міфи про кофеїн", "ru": "Мифы о кофеине", "en": "Caffeine Myths"},
}

for lang in ["uk", "ru", "en"]:
    blog_path = Path(f"locales/{lang}/blog.json")
    
    try:
        with open(blog_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        print(f"ERROR reading {blog_path}")
        continue
    
    # Add related articles translations
    data["related_articles"] = TRANSLATIONS[lang]["related_articles"]
    data["all_articles"] = TRANSLATIONS[lang]["all_articles"]
    
    # Add articles section if not exists
    if "articles" not in data:
        data["articles"] = {}
    
    # Add article titles
    for key, titles in ARTICLE_TITLES.items():
        if key not in data["articles"]:
            data["articles"][key] = {}
        data["articles"][key]["title"] = titles[lang]
    
    with open(blog_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print(f"OK: {blog_path}")

print("\nTranslations added!")
