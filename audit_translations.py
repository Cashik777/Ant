import os
import re
import json
from collections import defaultdict

root_dir = r"c:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect"
locales_dir = os.path.join(root_dir, "locales")
langs = ["uk", "ru", "en"]

# 1. Load all translations
translations = {lang: {} for lang in langs}

for lang in langs:
    lang_dir = os.path.join(locales_dir, lang)
    if os.path.exists(lang_dir):
        for file in os.listdir(lang_dir):
            if file.endswith(".json"):
                ns = file.replace(".json", "")
                try:
                    with open(os.path.join(lang_dir, file), 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        translations[lang][ns] = data
                except Exception as e:
                    print(f"[ERROR] Failed to load {lang}/{file}: {e}")

def get_translation(lang, key):
    parts = key.split('.')
    if len(parts) < 2:
        # Check common
        val = translations[lang].get('common', {}).get(key)
        return val
    
    ns = parts[0]
    rest = parts[1:]
    
    val = translations[lang].get(ns, {})
    for p in rest:
        if isinstance(val, dict):
            val = val.get(p)
        else:
            val = None
            break
    
    if val is None:
        # Fallback: check "common"
        common_val = translations[lang].get('common', {})
        for p in parts:
            if isinstance(common_val, dict):
                common_val = common_val.get(p)
            else:
                common_val = None
                break
        if common_val is not None:
             return common_val

    return val

# 2. Audit HTML files
missing_keys = defaultdict(list)
hardcoded_candidates = defaultdict(list)

# Regex for data-i18n
i18n_pattern = re.compile(r'data-i18n=["\']([^"\']+)["\']')

def check_file(filepath):
    rel_path = os.path.relpath(filepath, root_dir)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return # Skip binary or weird files
    
    # Check data-i18n keys
    keys = i18n_pattern.findall(content)
    for key in keys:
        if "{" in key: continue # Dynamics
        for lang in langs:
            val = get_translation(lang, key)
            if val is None:
                     missing_keys[key].append(f"{lang} ({rel_path})")

    # Hardcoded check
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'data-i18n' in line: continue
        if '<!--' in line: continue
        
        # Check if line has Cyrillic
        if re.search(r'[а-яА-ЯіїєґІЇЄҐ]', line):
             stripped = line.strip()
             if stripped and not stripped.startswith('<script') and not stripped.startswith('<style') and not stripped.startswith('<meta') and not stripped.startswith('<html'):
                  hardcoded_candidates[rel_path].append(f"L{i+1}: {stripped[:50]}...")

# Scan
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            check_file(os.path.join(subdir, file))

# Report
print("=== MISSING KEYS ===")
sorted_missing = sorted(missing_keys.items(), key=lambda x: x[0])
for key, locs in sorted_missing:
    # Deduplicate locations
    unique_locs = sorted(list(set(locs)))
    print(f"Key: {key}")
    print(f"  Missing in: {', '.join(unique_locs[:3])}...")

print("\n=== POTENTIAL HARDCODED TEXT (Sample) ===")
sorted_hardcoded = sorted(hardcoded_candidates.items(), key=lambda x: x[0])
for file, lines in sorted_hardcoded[:10]: # Limit output
    print(f"File: {file}")
    for l in lines[:3]:
        try:
            print(f"  {l}".encode('utf-8', errors='replace').decode('utf-8', errors='replace'))
        except:
            print(f"  {repr(l)}")
