import json
import os

def update_shop_keys():
    files = [
        ('locales/en/shop.json', {'product.strength': 'Strength', 'product.wishlist': 'Add to Wishlist'}),
        ('locales/uk/shop.json', {'product.strength': 'Крепкість', 'product.wishlist': 'В обране'}),
        ('locales/ru/shop.json', {'product.strength': 'Крепость', 'product.wishlist': 'В избранное'})
    ]

    for file_path, new_keys in files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                updated = False
                
                # Check for 'product' key, create if missing
                if 'product' not in data:
                    data['product'] = {}
                    updated = True
                
                # Add keys if missing
                if 'strength' not in data['product']:
                    data['product']['strength'] = new_keys['product.strength']
                    updated = True
                if 'wishlist' not in data['product']:
                    data['product']['wishlist'] = new_keys['product.wishlist']
                    updated = True
                
                if updated:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    print(f'Updated {file_path}')
                else:
                    print(f'No updates needed for {file_path}')
            except Exception as e:
                print(f'Error processing {file_path}: {e}')
        else:
            print(f'File not found: {file_path}')

if __name__ == '__main__':
    update_shop_keys()
