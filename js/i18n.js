/**
 * EthioDirect i18n System v3.0
 * Simple, reliable language switching for UA/RU/EN
 * Works with flat keys in JSON files
 */
(function () {
    'use strict';

    // ===== CONFIGURATION =====
    const CONFIG = {
        defaultLang: 'uk',
        supportedLangs: ['uk', 'ru', 'en'],
        storageKey: 'ed_language',
        localesPath: null  // Auto-detected
    };

    // Cache for loaded translations
    let translations = {};
    let currentLang = CONFIG.defaultLang;

    // ===== PATH DETECTION =====
    function getLocalesPath() {
        if (CONFIG.localesPath) return CONFIG.localesPath;

        const hostname = window.location.hostname;
        const pathname = window.location.pathname;

        // GitHub Pages detection
        if (hostname.includes('github.io')) {
            const match = pathname.match(/^\/([^\/]+)\//);
            if (match) {
                CONFIG.localesPath = '/' + match[1] + '/locales/';
                return CONFIG.localesPath;
            }
        }

        // Local development - detect depth
        const depth = (pathname.match(/\//g) || []).length - 1;
        if (depth > 0 && (pathname.includes('/articles/') || pathname.includes('/blog/'))) {
            CONFIG.localesPath = '../locales/';
        } else {
            CONFIG.localesPath = 'locales/';
        }
        return CONFIG.localesPath;
    }

    // ===== TRANSLATION LOADING =====
    async function loadTranslations(lang) {
        if (translations[lang]) {
            return translations[lang];
        }

        const path = getLocalesPath() + lang + '.json';
        try {
            const response = await fetch(path);
            if (!response.ok) throw new Error('HTTP ' + response.status);
            const data = await response.json();
            translations[lang] = flattenObject(data);
            console.log('[i18n] Loaded ' + lang + '.json (' + Object.keys(translations[lang]).length + ' keys)');
            return translations[lang];
        } catch (err) {
            console.error('[i18n] Failed to load ' + path + ':', err.message);
            return {};
        }
    }

    // Flatten nested JSON to dot notation
    function flattenObject(obj, prefix = '') {
        const result = {};
        for (const key in obj) {
            const fullKey = prefix ? prefix + '.' + key : key;
            if (typeof obj[key] === 'object' && obj[key] !== null && !Array.isArray(obj[key])) {
                Object.assign(result, flattenObject(obj[key], fullKey));
            } else {
                result[fullKey] = obj[key];
            }
        }
        return result;
    }

    // ===== TRANSLATION FUNCTION =====
    function t(key, params) {
        const dict = translations[currentLang] || {};
        let text = dict[key];

        if (text === undefined) {
            // Fallback to English, then Ukrainian
            text = (translations['en'] || {})[key] || (translations['uk'] || {})[key] || key;
        }

        // Interpolation: replace {{param}} with values
        if (params && typeof text === 'string') {
            for (const p in params) {
                text = text.replace(new RegExp('\\{\\{' + p + '\\}\\}', 'g'), params[p]);
            }
        }
        return text;
    }

    // ===== DOM TRANSLATION =====
    function translatePage() {
        // Text content
        document.querySelectorAll('[data-i18n]').forEach(function (el) {
            const key = el.getAttribute('data-i18n');
            if (key) {
                const text = t(key);
                if (text !== key) {
                    el.textContent = text;
                }
            }
        });

        // Placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(function (el) {
            const key = el.getAttribute('data-i18n-placeholder');
            if (key) {
                const text = t(key);
                if (text !== key) {
                    el.placeholder = text;
                }
            }
        });

        // Titles (tooltips)
        document.querySelectorAll('[data-i18n-title]').forEach(function (el) {
            const key = el.getAttribute('data-i18n-title');
            if (key) {
                const text = t(key);
                if (text !== key) {
                    el.title = text;
                }
            }
        });

        // Aria-labels
        document.querySelectorAll('[data-i18n-aria]').forEach(function (el) {
            const key = el.getAttribute('data-i18n-aria');
            if (key) {
                const text = t(key);
                if (text !== key) {
                    el.setAttribute('aria-label', text);
                }
            }
        });

        // Update HTML lang attribute
        document.documentElement.lang = currentLang;

        // Dispatch event for dynamic content (on both window and document for compatibility)
        const event = new CustomEvent('languageChanged', { detail: { lang: currentLang } });
        window.dispatchEvent(event);
        document.dispatchEvent(event);
    }

    // ===== BUTTON STATE =====
    function updateButtons() {
        document.querySelectorAll('.lang-btn, .top-bar-right a[onclick*="setLanguage"]').forEach(function (btn) {
            btn.classList.remove('active');
            const text = btn.textContent.trim().toUpperCase();

            if ((currentLang === 'uk' && text === 'UA') ||
                (currentLang === 'ru' && text === 'RU') ||
                (currentLang === 'en' && text === 'EN')) {
                btn.classList.add('active');
            }
        });
    }

    // ===== PUBLIC API =====
    async function setLanguage(lang) {
        if (!CONFIG.supportedLangs.includes(lang)) {
            console.warn('[i18n] Unsupported language:', lang);
            return;
        }

        currentLang = lang;
        localStorage.setItem(CONFIG.storageKey, lang);

        // Load translations if needed
        await loadTranslations(lang);

        // Apply to page
        translatePage();
        updateButtons();

        console.log('[i18n] Language set to:', lang);
    }

    function getCurrentLanguage() {
        return currentLang;
    }

    // ===== CSS FOR BUTTONS =====
    function injectStyles() {
        if (document.getElementById('i18n-styles')) return;

        const style = document.createElement('style');
        style.id = 'i18n-styles';
        style.textContent = `
            .top-bar-right a, .lang-btn {
                color: rgba(255,255,255,0.7);
                text-decoration: none;
                padding: 4px 12px;
                font-weight: 600;
                font-size: 0.85rem;
                border-radius: 4px;
                margin: 0 2px;
                transition: all 0.2s ease;
                cursor: pointer;
            }
            .top-bar-right a:hover, .lang-btn:hover {
                color: white;
                background: rgba(255,255,255,0.15);
            }
            .top-bar-right a.active, .lang-btn.active {
                color: white;
                background: var(--primary, #5D4037);
            }
        `;
        document.head.appendChild(style);
    }

    // ===== INITIALIZATION =====
    async function init() {
        injectStyles();

        // Get saved or default language
        const saved = localStorage.getItem(CONFIG.storageKey);
        currentLang = saved && CONFIG.supportedLangs.includes(saved) ? saved : CONFIG.defaultLang;

        // Preload all languages for fast switching
        await Promise.all([
            loadTranslations('uk'),
            loadTranslations('ru'),
            loadTranslations('en')
        ]);

        // Apply translations
        translatePage();
        updateButtons();

        console.log('[i18n] Initialized with language:', currentLang);
    }

    // Export to window
    window.setLanguage = setLanguage;
    window.getCurrentLanguage = getCurrentLanguage;
    window.t = t;

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
