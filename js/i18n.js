/* ===== ETHIODIRECT - PRODUCTION-READY i18n ENGINE ===== */
/* Custom implementation without external dependencies */
/* Version: 2.0.0 */

(function () {
    'use strict';

    // ========================================
    // CONFIGURATION
    // ========================================

    const CONFIG = {
        defaultLang: 'uk',           // Default language (Ukrainian)
        fallbackLang: 'en',          // Fallback if key not found
        storageKey: 'ed_language',   // localStorage key
        supportedLangs: ['uk', 'ru', 'en'],

        // Dev mode: set to true to log missing translations
        devMode: true,

        // Track missing keys to avoid duplicate warnings
        _missingKeys: new Set(),

        // Attribute mapping for different translation types
        attrMap: {
            'data-i18n': 'textContent',
            'data-i18n-placeholder': 'placeholder',
            'data-i18n-title': 'title',
            'data-i18n-alt': 'alt',
            'data-i18n-aria': 'aria-label'
        }
    };

    // ========================================
    // I18N CLASS
    // ========================================

    class I18n {
        constructor() {
            this.currentLang = null;
            this.translations = {};
            this.isInitialized = false;
            this.pendingCallbacks = [];
        }

        // ----------------------------------------
        // PUBLIC API
        // ----------------------------------------

        /**
         * Initialize the i18n system
         * @returns {Promise<void>}
         */
        async init() {
            if (this.isInitialized) return;

            try {
                // Determine initial language
                this.currentLang = this._getInitialLanguage();

                // Load translations for all languages (enables instant switching)
                await this._loadAllTranslations();

                // Apply translations to DOM
                this.applyTranslations();

                // Update UI states
                this._updateHtmlLang();
                this._updateButtonStates();

                // Mark as initialized
                this.isInitialized = true;

                // Execute pending callbacks
                this.pendingCallbacks.forEach(cb => cb());
                this.pendingCallbacks = [];

                console.log(`[i18n] Initialized with language: ${this.currentLang}`);

            } catch (error) {
                console.error('[i18n] Initialization failed:', error);
            }
        }

        /**
         * Translate a key with optional interpolation
         * @param {string} key - Dot-notation key (e.g., 'nav.catalog')
         * @param {Object} params - Interpolation parameters
         * @returns {string} - Translated string
         */
        t(key, params = {}) {
            if (!key) return '';

            // Get translation from current language
            let translation = this._getNestedValue(
                this.translations[this.currentLang],
                key
            );

            // Fallback to fallback language
            if (translation === undefined || translation === key) {
                translation = this._getNestedValue(
                    this.translations[CONFIG.fallbackLang],
                    key
                );
            }

            // Fallback to default language
            if (translation === undefined || translation === key) {
                translation = this._getNestedValue(
                    this.translations[CONFIG.defaultLang],
                    key
                );
            }

            // Return key if no translation found
            if (translation === undefined) {
                // Log missing key in dev mode (once per key)
                if (CONFIG.devMode && !CONFIG._missingKeys.has(key)) {
                    CONFIG._missingKeys.add(key);
                    console.warn(`[i18n] Missing translation key: "${key}" for language: "${this.currentLang}"`);
                }
                return key;
            }

            // Apply interpolation
            return this._interpolate(translation, params);
        }

        /**
         * Set current language
         * @param {string} lang - Language code (uk, ru, en)
         */
        setLanguage(lang) {
            if (!CONFIG.supportedLangs.includes(lang)) {
                console.warn(`[i18n] Unsupported language: ${lang}`);
                return;
            }

            if (lang === this.currentLang) return;

            // Update current language
            this.currentLang = lang;

            // Save to localStorage
            localStorage.setItem(CONFIG.storageKey, lang);

            // Apply translations
            this.applyTranslations();

            // Update UI
            this._updateHtmlLang();
            this._updateButtonStates();

            // Dispatch event for components that need to react
            document.dispatchEvent(new CustomEvent('languageChanged', {
                detail: { language: lang }
            }));

            console.log(`[i18n] Language changed to: ${lang}`);
        }

        /**
         * Get current language
         * @returns {string}
         */
        getCurrentLanguage() {
            return this.currentLang || CONFIG.defaultLang;
        }

        /**
         * Get supported languages
         * @returns {string[]}
         */
        getSupportedLanguages() {
            return [...CONFIG.supportedLangs];
        }

        /**
         * Apply translations to all DOM elements with data-i18n attributes
         */
        applyTranslations() {
            // Translate elements with data-i18n (textContent)
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (!key) return;

                // Check for attribute-specific translations
                if (el.hasAttribute('data-i18n-placeholder')) {
                    el.placeholder = this.t(key);
                } else if (el.hasAttribute('data-i18n-title')) {
                    el.title = this.t(key);
                } else if (el.hasAttribute('data-i18n-alt')) {
                    el.alt = this.t(key);
                } else if (el.hasAttribute('data-i18n-aria')) {
                    el.setAttribute('aria-label', this.t(key));
                } else {
                    // Default: update textContent
                    el.textContent = this.t(key);
                }
            });

            // Handle elements with only attribute-specific i18n (without data-i18n)
            this._translateAttribute('data-i18n-placeholder', 'placeholder');
            this._translateAttribute('data-i18n-title', 'title');
            this._translateAttribute('data-i18n-alt', 'alt');
            this._translateAttribute('data-i18n-aria', 'aria-label');
        }

        /**
         * Register callback for when i18n is ready
         * @param {Function} callback
         */
        onReady(callback) {
            if (this.isInitialized) {
                callback();
            } else {
                this.pendingCallbacks.push(callback);
            }
        }

        // ----------------------------------------
        // PRIVATE METHODS
        // ----------------------------------------

        /**
         * Determine initial language from localStorage or browser
         * @returns {string}
         * @private
         */
        _getInitialLanguage() {
            // 1. Check localStorage
            const saved = localStorage.getItem(CONFIG.storageKey);
            if (saved && CONFIG.supportedLangs.includes(saved)) {
                return saved;
            }

            // 2. Detect browser language
            const browserLang = this._detectBrowserLanguage();
            if (browserLang) {
                return browserLang;
            }

            // 3. Default
            return CONFIG.defaultLang;
        }

        /**
         * Detect browser language
         * @returns {string|null}
         * @private
         */
        _detectBrowserLanguage() {
            // Get browser language(s)
            const languages = navigator.languages || [navigator.language];

            for (const lang of languages) {
                // Extract language code (e.g., 'en-US' → 'en')
                const code = lang.split('-')[0].toLowerCase();

                // Check if supported
                if (CONFIG.supportedLangs.includes(code)) {
                    return code;
                }

                // Special handling for Ukrainian (uk/ua)
                if (code === 'ua') {
                    return 'uk';
                }
            }

            return null;
        }

        /**
         * Load all translation files
         * @returns {Promise<void>}
         * @private
         */
        async _loadAllTranslations() {
            const basePath = this._getLocalesPath();

            const loadPromises = CONFIG.supportedLangs.map(async (lang) => {
                try {
                    const response = await fetch(`${basePath}${lang}.json`);
                    if (response.ok) {
                        this.translations[lang] = await response.json();
                    } else {
                        console.warn(`[i18n] Failed to load ${lang}.json`);
                        this.translations[lang] = {};
                    }
                } catch (error) {
                    console.error(`[i18n] Error loading ${lang}.json:`, error);
                    this.translations[lang] = {};
                }
            });

            await Promise.all(loadPromises);
        }

        /**
         * Get locales path based on current page location
         * @returns {string}
         * @private
         */
        _getLocalesPath() {
            const path = window.location.pathname;
            // Handle subdirectories (blog, articles)
            if (path.includes('/blog/') || path.includes('/articles/')) {
                return '../locales/';
            }
            return 'locales/';
        }

        /**
         * Get nested value from object using dot notation
         * @param {Object} obj
         * @param {string} key - Dot-notation key
         * @returns {*}
         * @private
         */
        _getNestedValue(obj, key) {
            if (!obj || !key) return undefined;

            return key.split('.').reduce((current, part) => {
                return current && current[part] !== undefined
                    ? current[part]
                    : undefined;
            }, obj);
        }

        /**
         * Interpolate parameters into string
         * @param {string} str
         * @param {Object} params
         * @returns {string}
         * @private
         */
        _interpolate(str, params) {
            if (!params || Object.keys(params).length === 0) {
                return str;
            }

            return str.replace(/\{\{(\w+)\}\}/g, (match, key) => {
                return params.hasOwnProperty(key) ? params[key] : match;
            });
        }

        /**
         * Translate elements with attribute-specific i18n
         * @param {string} dataAttr - Data attribute name
         * @param {string} targetAttr - Target attribute to set
         * @private
         */
        _translateAttribute(dataAttr, targetAttr) {
            document.querySelectorAll(`[${dataAttr}]:not([data-i18n])`).forEach(el => {
                const key = el.getAttribute(dataAttr);
                if (key) {
                    if (targetAttr === 'aria-label') {
                        el.setAttribute('aria-label', this.t(key));
                    } else {
                        el[targetAttr] = this.t(key);
                    }
                }
            });
        }

        /**
         * Update <html lang=""> attribute
         * @private
         */
        _updateHtmlLang() {
            document.documentElement.lang = this.currentLang;
        }

        /**
         * Update language switcher button states
         * @private
         */
        _updateButtonStates() {
            const buttons = document.querySelectorAll('[data-lang-switch]');

            buttons.forEach(btn => {
                const btnLang = btn.getAttribute('data-lang-switch');
                btn.classList.toggle('active', btnLang === this.currentLang);
            });

            // Legacy support for onclick buttons
            document.querySelectorAll('.top-bar-right a[onclick*="setLanguage"]').forEach(btn => {
                btn.classList.remove('active');
                const text = btn.textContent.trim().toUpperCase();

                if ((this.currentLang === 'uk' && text === 'UA') ||
                    (this.currentLang === 'ru' && text === 'RU') ||
                    (this.currentLang === 'en' && text === 'EN')) {
                    btn.classList.add('active');
                }
            });
        }
    }

    // ========================================
    // SINGLETON INSTANCE
    // ========================================

    const i18n = new I18n();

    // ========================================
    // GLOBAL API
    // ========================================

    /**
     * Global translation function
     * @param {string} key
     * @param {Object} params
     * @returns {string}
     */
    window.t = function (key, params) {
        return i18n.t(key, params);
    };

    /**
     * Set language (for button onclick handlers)
     * @param {string} lang
     */
    window.setLanguage = function (lang) {
        i18n.setLanguage(lang);
    };

    /**
     * Get current language
     * @returns {string}
     */
    window.getCurrentLanguage = function () {
        return i18n.getCurrentLanguage();
    };

    /**
     * Access to i18n instance
     */
    window.i18n = i18n;

    // ========================================
    // STYLES INJECTION
    // ========================================

    function injectStyles() {
        if (document.getElementById('i18n-styles')) return;

        const style = document.createElement('style');
        style.id = 'i18n-styles';
        style.textContent = `
            /* Language Switcher Styles */
            .top-bar-right a,
            [data-lang-switch] {
                color: rgba(255,255,255,0.7);
                text-decoration: none;
                padding: 4px 12px;
                font-weight: 600;
                font-size: 0.85rem;
                border-radius: 4px;
                margin: 0 2px;
                transition: all 0.2s ease;
                display: inline-block;
                cursor: pointer;
                border: none;
                background: transparent;
            }
            
            .top-bar-right a:hover,
            [data-lang-switch]:hover {
                color: white;
                background: rgba(255,255,255,0.15);
            }
            
            .top-bar-right a.active,
            [data-lang-switch].active {
                color: white;
                background: var(--primary, #5D4037);
            }
        `;
        document.head.appendChild(style);
    }

    // ========================================
    // INITIALIZATION
    // ========================================

    function bootstrap() {
        injectStyles();
        i18n.init();
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', bootstrap);
    } else {
        bootstrap();
    }

})();
