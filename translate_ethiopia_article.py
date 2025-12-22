#!/usr/bin/env python3
"""
Complete translations for ethiopia-coffee-origin.html
"""
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

ARTICLE = {
    "ethiopia_origin": {
        "uk": {
            "title": "Ефіопія — батьківщина кави: легенда про пастуха Калді",
            "subtitle": "Історія про те, як козопас випадково відкрив магію кавових ягід понад 1000 років тому.",
            "category": "Про каву",
            "reading_time": "4 хвилини читання",
            "intro": "Кожна чашка кави починається з Ефіопії. Це не просто красива фраза — це історичний факт. Саме тут, у горах східної Африки, понад тисячу років тому людство вперше відкрило для себе бадьору дію кавових ягід.",
            "h2_legend": "Легенда про пастуха Калді",
            "p_legend1": "Найвідоміша легенда про походження кави розповідає про ефіопського пастуха на ім'я Калді, який жив приблизно у 9 столітті нашої ери.",
            "p_legend2": "Одного дня Калді помітив, що його кози стали надзвичайно енергійними та активними після того, як поїли червоних ягід з невідомого куща. Вони стрибали, бігали і не могли заспокоїтись до пізньої ночі.",
            "p_legend3": "Зацікавлений пастух вирішив спробувати ягоди сам. Відчувши прилив бадьорості, він відніс знахідку до місцевого монастиря.",
            "h2_monastery": "Монахи та перша \"кава\"",
            "p_monastery1": "Монахи спочатку скептично поставились до знахідки. За однією версією, настоятель навіть кинув ягоди у вогонь, назвавши їх \"дияволовою роботою\".",
            "p_monastery2": "Але коли ягоди почали обсмажуватись, приміщення наповнив неймовірний аромат. Монахи дістали обсмажене зерно, подрібнили його та залили гарячою водою — так народився перший кавовий напій.",
            "p_monastery3": "Монахи швидко оцінили практичну користь: напій допомагав їм не засинати під час довгих нічних молитов.",
            "h2_spread": "Поширення по світу",
            "p_spread1": "Протягом наступних століть кава поширилась спочатку на Аравійський півострів, потім до Туреччини, Венеції та решти Європи.",
            "p_spread2": "Але Ефіопія залишається унікальною — це єдина країна у світі, де кава росте в дикій природі. Тут можна знайти тисячі різновидів, яких немає більше ніде.",
            "h2_today": "Ефіопська кава сьогодні",
            "p_today1": "Ефіопія — п'ятий найбільший виробник кави у світі та перший в Африці. Кава забезпечує близько 60% експортних надходжень країни.",
            "p_today2": "Найвідоміші регіони виробництва: Yirgacheffe, Sidamo, Guji, Harrar, Limu. Кожен з них має унікальний терруар та смаковий профіль.",
            "h2_ceremony": "Кавова церемонія",
            "p_ceremony": "В Ефіопії кава — це більше ніж напій. Традиційна кавова церемонія (\"Buna\") може тривати годинами і є важливою частиною соціального життя. Зерна обсмажують, мелють та заварюють прямо перед гостями.",
            "cta_title": "Спробуйте смак батьківщини кави",
            "cta_text": "Замовте справжню ефіопську каву з регіонів Yirgacheffe та Sidamo",
            "cta_button": "До каталогу"
        },
        "ru": {
            "title": "Эфиопия — родина кофе: легенда о пастухе Калди",
            "subtitle": "История о том, как козопас случайно открыл магию кофейных ягод более 1000 лет назад.",
            "category": "О кофе",
            "reading_time": "4 минуты чтения",
            "intro": "Каждая чашка кофе начинается с Эфиопии. Это не просто красивая фраза — это исторический факт. Именно здесь, в горах восточной Африки, более тысячи лет назад человечество впервые открыло для себя бодрящее действие кофейных ягод.",
            "h2_legend": "Легенда о пастухе Калди",
            "p_legend1": "Самая известная легенда о происхождении кофе рассказывает об эфиопском пастухе по имени Калди, жившем примерно в 9 веке нашей эры.",
            "p_legend2": "Однажды Калди заметил, что его козы стали необычайно энергичными и активными после того, как поели красных ягод с неизвестного куста. Они прыгали, бегали и не могли успокоиться до поздней ночи.",
            "p_legend3": "Заинтересованный пастух решил попробовать ягоды сам. Ощутив прилив бодрости, он отнёс находку в местный монастырь.",
            "h2_monastery": "Монахи и первый \"кофе\"",
            "p_monastery1": "Монахи сначала скептически отнеслись к находке. По одной версии, настоятель даже бросил ягоды в огонь, назвав их \"дьявольской работой\".",
            "p_monastery2": "Но когда ягоды начали обжариваться, помещение наполнил невероятный аромат. Монахи достали обжаренное зерно, измельчили его и залили горячей водой — так родился первый кофейный напиток.",
            "p_monastery3": "Монахи быстро оценили практическую пользу: напиток помогал им не засыпать во время долгих ночных молитв.",
            "h2_spread": "Распространение по миру",
            "p_spread1": "В течение следующих столетий кофе распространился сначала на Аравийский полуостров, затем в Турцию, Венецию и остальную Европу.",
            "p_spread2": "Но Эфиопия остаётся уникальной — это единственная страна в мире, где кофе растёт в дикой природе. Здесь можно найти тысячи разновидностей, которых нет больше нигде.",
            "h2_today": "Эфиопский кофе сегодня",
            "p_today1": "Эфиопия — пятый крупнейший производитель кофе в мире и первый в Африке. Кофе обеспечивает около 60% экспортных поступлений страны.",
            "p_today2": "Самые известные регионы производства: Yirgacheffe, Sidamo, Guji, Harrar, Limu. Каждый из них имеет уникальный терруар и вкусовой профиль.",
            "h2_ceremony": "Кофейная церемония",
            "p_ceremony": "В Эфиопии кофе — это больше, чем напиток. Традиционная кофейная церемония (\"Buna\") может длиться часами и является важной частью социальной жизни. Зёрна обжаривают, мелют и заваривают прямо перед гостями.",
            "cta_title": "Попробуйте вкус родины кофе",
            "cta_text": "Закажите настоящий эфиопский кофе из регионов Yirgacheffe и Sidamo",
            "cta_button": "В каталог"
        },
        "en": {
            "title": "Ethiopia — The Birthplace of Coffee: The Legend of Kaldi",
            "subtitle": "The story of how a goatherd accidentally discovered the magic of coffee berries over 1000 years ago.",
            "category": "About Coffee",
            "reading_time": "4 min read",
            "intro": "Every cup of coffee begins in Ethiopia. This isn't just a nice phrase — it's a historical fact. Right here, in the mountains of East Africa, more than a thousand years ago, humanity first discovered the invigorating effects of coffee berries.",
            "h2_legend": "The Legend of Kaldi the Goatherd",
            "p_legend1": "The most famous legend about coffee's origin tells of an Ethiopian goatherd named Kaldi, who lived around the 9th century AD.",
            "p_legend2": "One day, Kaldi noticed that his goats became extraordinarily energetic and active after eating red berries from an unknown bush. They jumped, ran, and couldn't calm down until late at night.",
            "p_legend3": "The curious shepherd decided to try the berries himself. Feeling a surge of energy, he brought his discovery to the local monastery.",
            "h2_monastery": "The Monks and the First \"Coffee\"",
            "p_monastery1": "The monks were initially skeptical of the discovery. According to one version, the abbot even threw the berries into the fire, calling them \"the devil's work.\"",
            "p_monastery2": "But when the berries began to roast, the room filled with an incredible aroma. The monks retrieved the roasted beans, ground them, and poured hot water over them — thus was born the first coffee drink.",
            "p_monastery3": "The monks quickly appreciated the practical benefit: the drink helped them stay awake during long night prayers.",
            "h2_spread": "Spreading Across the World",
            "p_spread1": "Over the following centuries, coffee spread first to the Arabian Peninsula, then to Turkey, Venice, and the rest of Europe.",
            "p_spread2": "But Ethiopia remains unique — it's the only country in the world where coffee grows wild. Here you can find thousands of varieties that exist nowhere else.",
            "h2_today": "Ethiopian Coffee Today",
            "p_today1": "Ethiopia is the fifth-largest coffee producer in the world and first in Africa. Coffee provides about 60% of the country's export revenue.",
            "p_today2": "The most famous production regions: Yirgacheffe, Sidamo, Guji, Harrar, Limu. Each has a unique terroir and flavor profile.",
            "h2_ceremony": "The Coffee Ceremony",
            "p_ceremony": "In Ethiopia, coffee is more than a drink. The traditional coffee ceremony (\"Buna\") can last for hours and is an important part of social life. Beans are roasted, ground, and brewed right before guests.",
            "cta_title": "Taste the Birthplace of Coffee",
            "cta_text": "Order authentic Ethiopian coffee from Yirgacheffe and Sidamo regions",
            "cta_button": "To Catalog"
        }
    }
}

def update_locales():
    for lang in ["uk", "ru", "en"]:
        path = BASE_DIR / "locales" / f"{lang}.json"
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if "articles" not in data:
            data["articles"] = {}
        
        for key, translations in ARTICLE.items():
            if key not in data["articles"]:
                data["articles"][key] = {}
            data["articles"][key].update(translations[lang])
        
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        print(f"Updated {path}")

if __name__ == "__main__":
    update_locales()
    print("Done!")
