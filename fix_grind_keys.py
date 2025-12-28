import json
import os

def update_grind_keys():
    files = [
        ('locales/en/shop.json', {
            'product.grind_beans': 'Whole Beans',
            'product.grind_espresso': 'Espresso',
            'product.grind_filter': 'Filter',
            'product.grind_turka': 'Turkish'
        }),
        ('locales/uk/shop.json', {
            'product.grind_beans': 'Зерно',
            'product.grind_espresso': 'Еспресо',
            'product.grind_filter': 'Фільтр',
            'product.grind_turka': 'Турка'
        }),
        ('locales/ru/shop.json', {
            'product.grind_beans': 'Зерно',
            'product.grind_espresso': 'Эспрессо',
            'product.grind_filter': 'Фильтр',
            'product.grind_turka': 'Турка'
        })
    ]

    for file_path, new_keys in files:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                updated = False
                
                if 'product' not in data:
                    data['product'] = {}
                    updated = True
                
                for k, v in new_keys.items():
                    key_part = k.split('.')[1]
                    if key_part not in data['product']:
                        data['product'][key_part] = v
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
    update_grind_keys()
