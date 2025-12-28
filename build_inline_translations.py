#!/usr/bin/env python3
"""
Build inline translations for local development
This script consolidates all JSON translation files into a single JavaScript file
to avoid CORS issues when running via file:// protocol
"""
import json
import os
from pathlib import Path

def main():
    # Paths
    locales_dir = Path("locales")
    output_file = Path("js/i18n-inline.js")
    
    # Supported languages
    languages = ["uk", "ru", "en"]
    
    # Load all translations
    translations = {}
    
    for lang in languages:
        translations[lang] = {}
        lang_dir = locales_dir / lang
        
        if not lang_dir.exists():
            print(f"Warning: {lang_dir} does not exist")
            continue
        
        # Load all JSON files in this language directory
        for json_file in lang_dir.glob("*.json"):
            namespace = json_file.stem
            # Try utf-8-sig first to handle BOM, then fall back to utf-8
            for encoding in ['utf-8-sig', 'utf-8']:
                try:
                    with open(json_file, 'r', encoding=encoding) as f:
                        data = json.load(f)
                        translations[lang][namespace] = data
                        print(f"Loaded: {lang}/{namespace}.json")
                        break
                except (json.JSONDecodeError, UnicodeDecodeError) as e:
                    if encoding == 'utf-8':  # Last attempt failed
                        print(f"Error loading {json_file}: {e}")
    
    # Generate JavaScript file
    js_content = """/**
 * EthioDirect Inline Translations
 * Auto-generated from JSON files - DO NOT EDIT MANUALLY
 * Generated: {timestamp}
 */

// Store translations globally
window.ETHIO_TRANSLATIONS = {json_data};

console.log('[i18n-inline] Loaded inline translations for:', Object.keys(window.ETHIO_TRANSLATIONS));
""".format(
        timestamp=Path(__file__).stat().st_mtime if os.path.exists(__file__) else "unknown",
        json_data=json.dumps(translations, ensure_ascii=False, indent=2)
    )
    
    # Write to file
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print(f"\n[OK] Successfully created {output_file}")
    print(f"     Total size: {len(js_content):,} bytes")
    print(f"     Languages: {', '.join(languages)}")
    print(f"     Namespaces per language: {list(translations['uk'].keys())}")

if __name__ == "__main__":
    main()
