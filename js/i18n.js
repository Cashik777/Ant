/**
 * EthioDirect Production i18n System
 * ====================================
 * Async JSON-based internationalization without DOM auto-translation
 * Supports: UK (default), RU, EN
 * 
 * @version 2.0.0
 * @author EthioDirect
 */

(function (global) {
    'use strict';

    /**
     * I18n Class - Production-grade internationalization
     */
    class I18n {
        constructor(options = {}) {
            this.defaultLocale = options.defaultLocale || 'uk';
            this.supportedLocales = options.supportedLocales || ['uk', 'ru', 'en'];

            // Detect base path from script location or current URL
            this.basePath = this._detectBasePath();
            this.localesPath = options.localesPath || (this.basePath + 'locales');

            this.storageKey = options.storageKey || 'ethiodirect_locale';

            this.translations = {};
            this.loadedNamespaces = {};
            this.currentLocale = null;
            this.isInitialized = false;

            // Callbacks
            this.onLocaleChange = options.onLocaleChange || null;
        }

        /**
         * Detect base path for loading resources
         * Works for both root pages and subdirectory pages (articles/, blog/)
         * @returns {string}
         */
        _detectBasePath() {
            // Try to get path from script src
            const scripts = document.getElementsByTagName('script');
            for (let script of scripts) {
                const src = script.src || '';
                if (src.includes('i18n.js')) {
                    // Extract base path (everything before 'js/i18n.js')
                    const idx = src.indexOf('js/i18n.js');
                    if (idx !== -1) {
                        return src.substring(0, idx);
                    }
                }
            }

            // Fallback: detect from current path
            const path = window.location.pathname;
            if (path.includes('/articles/') || path.includes('/blog/')) {
                return '../';
            }
            return '';
        }

        /**
         * Get stored locale from localStorage
         * @returns {string|null}
         */
        getStoredLocale() {
            try {
                const stored = localStorage.getItem(this.storageKey);
                return this.supportedLocales.includes(stored) ? stored : null;
            } catch (e) {
                console.warn('localStorage not available:', e);
                return null;
            }
        }

        /**
         * Save locale to localStorage
         * @param {string} locale
         */
        setStoredLocale(locale) {
            try {
                localStorage.setItem(this.storageKey, locale);
            } catch (e) {
                console.warn('Failed to save locale:', e);
            }
        }

        /**
         * Detect browser locale
         * @returns {string}
         */
        detectBrowserLocale() {
            const browserLang = navigator.language || navigator.userLanguage || '';
            const shortLang = browserLang.split('-')[0].toLowerCase();

            // Map browser locale to supported locale
            const localeMap = {
                'uk': 'uk',
                'ua': 'uk',
                'ru': 'ru',
                'en': 'en'
            };

            return localeMap[shortLang] || this.defaultLocale;
        }

        /**
         * Get initial locale (priority: stored > browser > default)
         * @returns {string}
         */
        getInitialLocale() {
            return this.getStoredLocale() || this.defaultLocale;
        }

        /**
         * Load a translation namespace for a locale
         * @param {string} locale
         * @param {string} namespace
         * @returns {Promise<object>}
         */
        async loadNamespace(locale, namespace) {
            const cacheKey = `${locale}:${namespace}`;

            // Return cached if already loaded
            if (this.loadedNamespaces[cacheKey]) {
                return this.translations[locale]?.[namespace] || {};
            }

            // PRIORITY 1: Try to use inline translations if available
            if (window.ETHIO_TRANSLATIONS &&
                window.ETHIO_TRANSLATIONS[locale] &&
                window.ETHIO_TRANSLATIONS[locale][namespace]) {

                // Initialize locale object if needed
                if (!this.translations[locale]) {
                    this.translations[locale] = {};
                }

                this.translations[locale][namespace] = window.ETHIO_TRANSLATIONS[locale][namespace];
                this.loadedNamespaces[cacheKey] = true;
                console.log(`[i18n] Loaded from inline: ${locale}/${namespace}`);
                return this.translations[locale][namespace];
            }

            // PRIORITY 2: Try to fetch from server (for production)
            try {
                const url = `${this.localesPath}/${locale}/${namespace}.json?v=${Date.now()}`;
                const response = await fetch(url);

                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${url}`);
                }

                const data = await response.json();

                // Initialize locale object if needed
                if (!this.translations[locale]) {
                    this.translations[locale] = {};
                }

                this.translations[locale][namespace] = data;
                this.loadedNamespaces[cacheKey] = true;
                console.log(`[i18n] Loaded from server: ${locale}/${namespace}`);

                return data;
            } catch (error) {
                console.error(`[i18n] Failed to load translations: ${locale}/${namespace}`, error);
                return {};
            }
        }

        /**
         * Load multiple namespaces for a locale
         * @param {string} locale
         * @param {string[]} namespaces
         * @returns {Promise<void>}
         */
        async loadNamespaces(locale, namespaces) {
            const promises = namespaces.map(ns => this.loadNamespace(locale, ns));
            await Promise.all(promises);
        }

        /**
         * Get namespaces needed for current page
         * @returns {string[]}
         */
        getPageNamespaces() {
            const namespaces = ['common'];

            // Check if we're in the /articles/ subdirectory
            const pathname = window.location.pathname;
            if (pathname.includes('/articles/')) {
                // Article pages need the blog namespace
                namespaces.push('blog');
                return namespaces;
            }

            // Determine page from URL
            let page = pathname
                .split('/')
                .pop()
                .replace('.html', '')
                .replace('.htm', '') || 'index';

            // Map pages to namespaces
            const pageNamespaceMap = {
                'index': 'home',
                'home': 'home',
                'shop': 'shop',
                'blog': 'blog',
                'about': 'about',
                'contacts': 'contacts',
                'quiz': 'quiz',
                'subscription': 'subscription',
                'delivery': 'delivery',
                'faq': 'faq',
                'gift-certificates': 'gift',
                'account': 'account',
                'b2b': 'b2b',
                'return': 'delivery',
                'product': 'shop',
                'privacy': 'common'
            };

            const pageNs = pageNamespaceMap[page];
            if (pageNs && !namespaces.includes(pageNs)) {
                namespaces.push(pageNs);
            }

            return namespaces;
        }

        /**
         * Get nested value from object using dot notation
         * @param {object} obj
         * @param {string} path
         * @returns {*}
         */
        getNestedValue(obj, path) {
            return path.split('.').reduce((current, key) => {
                return current && current[key] !== undefined ? current[key] : undefined;
            }, obj);
        }

        /**
         * Get translation by key
         * @param {string} key - Dot notation key (e.g., "nav.catalog" or "home.hero.title")
         * @param {object} params - Interpolation parameters
         * @returns {string}
         */
        t(key, params = {}) {
            const locale = this.currentLocale || this.defaultLocale;
            const keys = key.split('.');

            let value;  // undefined by default, allows fallback strategies to work

            // Strategy 1: First part is namespace (e.g., "home.hero.title")
            if (keys.length >= 2) {
                const namespace = keys[0];
                const path = keys.slice(1).join('.');

                if (this.translations[locale]?.[namespace]) {
                    value = this.getNestedValue(this.translations[locale][namespace], path);
                }
            }

            // Strategy 2: Key is in common namespace (e.g., "nav.catalog")
            if (value === undefined) {
                value = this.getNestedValue(this.translations[locale]?.common, key);
            }

            // Strategy 2.5: Key is in page-specific namespace (e.g., "hero.title" in home.json)
            if (value === undefined) {
                const pageNs = this.getPageNamespaces().find(ns => ns !== 'common');
                if (pageNs && this.translations[locale]?.[pageNs]) {
                    value = this.getNestedValue(this.translations[locale][pageNs], key);
                }
            }

            // Strategy 3: Fallback to default locale
            if (value === undefined && locale !== this.defaultLocale) {
                // Try namespace approach
                if (keys.length >= 2) {
                    const namespace = keys[0];
                    const path = keys.slice(1).join('.');
                    if (this.translations[this.defaultLocale]?.[namespace]) {
                        value = this.getNestedValue(this.translations[this.defaultLocale][namespace], path);
                    }
                }
                // Try common namespace
                if (value === undefined) {
                    value = this.getNestedValue(this.translations[this.defaultLocale]?.common, key);
                }
                // Try page-specific namespace
                if (value === undefined) {
                    const pageNs = this.getPageNamespaces().find(ns => ns !== 'common');
                    if (pageNs && this.translations[this.defaultLocale]?.[pageNs]) {
                        value = this.getNestedValue(this.translations[this.defaultLocale][pageNs], key);
                    }
                }
            }

            // Return key if not found
            if (value === undefined) {
                console.warn(`[i18n] Translation not found: "${key}"`);
                return key;
            }

            // Interpolate parameters {{param}}
            if (typeof value === 'string' && Object.keys(params).length > 0) {
                return value.replace(/\{\{(\w+)\}\}/g, (match, param) => {
                    return params[param] !== undefined ? params[param] : match;
                });
            }

            return value;
        }

        /**
         * Update all DOM elements with data-i18n attributes
         */
        updateDOM() {
            // Text content
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (key) {
                    el.textContent = this.t(key);
                }
            });

            // Placeholders
            document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
                const key = el.getAttribute('data-i18n-placeholder');
                if (key) {
                    el.placeholder = this.t(key);
                }
            });

            // Title attributes
            document.querySelectorAll('[data-i18n-title]').forEach(el => {
                const key = el.getAttribute('data-i18n-title');
                if (key) {
                    el.title = this.t(key);
                }
            });

            // Aria labels
            document.querySelectorAll('[data-i18n-aria]').forEach(el => {
                const key = el.getAttribute('data-i18n-aria');
                if (key) {
                    el.setAttribute('aria-label', this.t(key));
                }
            });

            // HTML content (use with caution)
            document.querySelectorAll('[data-i18n-html]').forEach(el => {
                const key = el.getAttribute('data-i18n-html');
                if (key) {
                    el.innerHTML = this.t(key);
                }
            });
        }

        /**
         * Update HTML lang attribute
         */
        updateHTMLLang() {
            document.documentElement.lang = this.currentLocale;
        }

        /**
         * Update document title
         */
        updatePageTitle() {
            const namespaces = this.getPageNamespaces();
            const pageNs = namespaces.find(ns => ns !== 'common');

            if (pageNs && this.translations[this.currentLocale]?.[pageNs]?.meta?.title) {
                document.title = this.translations[this.currentLocale][pageNs].meta.title;
            }
        }

        /**
         * Update language switcher buttons UI
         */
        updateLanguageButtons() {
            const currentLang = this.currentLocale;

            // Handle elements with data-lang attribute
            document.querySelectorAll('[data-lang]').forEach(btn => {
                const btnLang = btn.getAttribute('data-lang');
                btn.classList.toggle('active', btnLang === currentLang);
            });

            // Handle anchor/button elements with onclick setLanguage (for pages using older pattern)
            document.querySelectorAll('.top-bar-right a, .top-bar-right button, .language-switcher a, .language-switcher button').forEach(btn => {
                const onclickAttr = btn.getAttribute('onclick') || '';
                const match = onclickAttr.match(/setLanguage\(['"](\w+)['"]\)/);
                if (match) {
                    const btnLang = match[1];
                    btn.classList.toggle('active', btnLang === currentLang);
                }
            });
        }

        /**
         * Switch to a different locale
         * @param {string} locale
         * @returns {Promise<void>}
         */
        async setLocale(locale) {
            if (!this.supportedLocales.includes(locale)) {
                console.error(`[i18n] Unsupported locale: ${locale}`);
                return;
            }

            if (locale === this.currentLocale && this.isInitialized) {
                return;
            }

            this.currentLocale = locale;
            this.setStoredLocale(locale);

            // Load required namespaces
            const namespaces = this.getPageNamespaces();
            await this.loadNamespaces(locale, namespaces);

            // Update everything
            this.updateDOM();
            this.updateHTMLLang();
            this.updatePageTitle();
            this.updateLanguageButtons();

            // Callback
            if (typeof this.onLocaleChange === 'function') {
                this.onLocaleChange(locale);
            }

            console.log(`[i18n] Locale switched to: ${locale}`);
        }

        /**
         * Initialize the i18n system
         * @returns {Promise<void>}
         */
        async init() {
            if (this.isInitialized) return;

            const initialLocale = this.getInitialLocale();
            const namespaces = this.getPageNamespaces();

            // Always load default locale first (for fallback)
            await this.loadNamespaces(this.defaultLocale, namespaces);

            // Set and load current locale
            this.currentLocale = initialLocale;

            if (initialLocale !== this.defaultLocale) {
                await this.loadNamespaces(initialLocale, namespaces);
            }

            // Update DOM
            this.updateDOM();
            this.updateHTMLLang();
            this.updatePageTitle();
            this.updateLanguageButtons();

            this.isInitialized = true;
            console.log(`[i18n] Initialized with locale: ${initialLocale}`);

            // Dispatch event to notify other scripts that i18n is ready
            document.dispatchEvent(new CustomEvent('i18nReady', { detail: { locale: initialLocale } }));
        }

        /**
         * Get current locale
         * @returns {string}
         */
        getLocale() {
            return this.currentLocale || this.defaultLocale;
        }

        /**
         * Check if a locale is supported
         * @param {string} locale
         * @returns {boolean}
         */
        isSupported(locale) {
            return this.supportedLocales.includes(locale);
        }
    }

    // ====================================
    // GLOBAL INSTANCE & HELPER FUNCTIONS
    // ====================================

    // Create global instance
    const i18n = new I18n({
        defaultLocale: 'uk',
        supportedLocales: ['uk', 'ru', 'en'],
        // localesPath is auto-detected from script location
        onLocaleChange: function (locale) {
            // Custom callback when locale changes
            // Can be used to re-render dynamic content
            if (typeof window.onLanguageChange === 'function') {
                window.onLanguageChange(locale);
            }
        }
    });

    /**
     * Global translation function
     * @param {string} key
     * @param {object} params
     * @returns {string}
     */
    function t(key, params = {}) {
        return i18n.t(key, params);
    }

    /**
     * Global language setter
     * @param {string} locale
     * @returns {Promise<void>}
     */
    async function setLanguage(locale) {
        await i18n.setLocale(locale);
    }

    /**
     * Get current language
     * @returns {string}
     */
    function getLanguage() {
        return i18n.getLocale();
    }

    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => i18n.init());
    } else {
        i18n.init();
    }

    // Export to global scope
    global.I18n = I18n;
    global.i18n = i18n;
    global.t = t;
    global.setLanguage = setLanguage;
    global.getLanguage = getLanguage;

})(typeof window !== 'undefined' ? window : this);
