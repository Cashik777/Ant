import json
import os

root = r"c:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect\locales"
langs = ["uk", "ru", "en"]
keys_to_move = ["timer", "trust"]

for lang in langs:
    home_path = os.path.join(root, lang, "home.json")
    common_path = os.path.join(root, lang, "common.json")
    
    if os.path.exists(home_path) and os.path.exists(common_path):
        with open(home_path, 'r', encoding='utf-8-sig') as f:
            home_data = json.load(f)
        with open(common_path, 'r', encoding='utf-8-sig') as f:
            common_data = json.load(f)
        
        modified = False
        for key in keys_to_move:
            if key in home_data:
                common_data[key] = home_data[key]
                del home_data[key]
                modified = True
                print(f"Moved {key} in {lang}")
        
        if modified:
            with open(home_path, 'w', encoding='utf-8') as f:
                json.dump(home_data, f, indent=4, ensure_ascii=False)
            with open(common_path, 'w', encoding='utf-8') as f:
                json.dump(common_data, f, indent=4, ensure_ascii=False)
