import json
import os

def update_translations():
    files = [
        ('locales/en/product.json', {'strength': 'Strength', 'wishlist': 'Add to Wishlist'}),
        ('locales/uk/product.json', {'strength': 'Крепкість', 'wishlist': 'В обране'}),
        ('locales/ru/product.json', {'strength': 'Крепость', 'wishlist': 'В избранное'})
    ]

    for file_path, new_keys in files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            updated = False
            for k, v in new_keys.items():
                if k not in data:
                    data[k] = v
                    updated = True
            
            if updated:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                print(f'Updated {file_path}')
        else:
            print(f'File not found: {file_path}')

if __name__ == '__main__':
    update_translations()
