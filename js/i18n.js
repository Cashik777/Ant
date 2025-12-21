/* ===== ETHIODIRECT - COMPLETE i18n SOLUTION ===== */
/* Uses Google Translate for full page translation */
/* Buttons: UA / RU / EN */

(function () {
    'use strict';

    const CONFIG = {
        defaultLang: 'uk',
        storageKey: 'ed_language',
        pageLanguage: 'uk'
    };

    // ===== GOOGLE TRANSLATE SETUP =====

    function createTranslateWidget() {
        // Create hidden container for Google Translate
        if (!document.getElementById('google_translate_element')) {
            const div = document.createElement('div');
            div.id = 'google_translate_element';
            div.style.cssText = 'display:none !important;';
            document.body.insertBefore(div, document.body.firstChild);
        }
    }

    function loadGoogleTranslateScript() {
        if (document.querySelector('script[src*="translate.google.com"]')) return;

        const script = document.createElement('script');
        script.src = 'https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
        script.async = true;
        script.onerror = function () {
            console.error('[i18n] Failed to load Google Translate. Falling back to page reload.');
        };
        document.head.appendChild(script);
        console.log('[i18n] Google Translate script loading...');
    }

    // Google Translate callback - must be global
    window.googleTranslateElementInit = function () {
        new google.translate.TranslateElement({
            pageLanguage: CONFIG.pageLanguage,
            includedLanguages: 'uk,ru,en',
            autoDisplay: false,
            multilanguagePage: false
        }, 'google_translate_element');

        // Apply saved language after widget loads
        setTimeout(function () {
            const saved = localStorage.getItem(CONFIG.storageKey);
            if (saved && saved !== CONFIG.pageLanguage) {
                translateTo(saved);
            }
            updateButtons(saved || CONFIG.pageLanguage);
        }, 1000);
    };

    // ===== TRANSLATION FUNCTIONS =====

    function translateTo(lang) {
        const select = document.querySelector('.goog-te-combo');

        if (!select) {
            // Widget not ready, retry
            setTimeout(function () { translateTo(lang); }, 500);
            return;
        }

        if (lang === 'uk' || lang === CONFIG.pageLanguage) {
            // Reset to original (Ukrainian)
            resetTranslation();
        } else {
            // Translate to selected language
            select.value = lang;
            select.dispatchEvent(new Event('change', { bubbles: true }));
        }
    }

    function resetTranslation() {
        // Try to use Google's restore function
        const iframe = document.querySelector('.goog-te-banner-frame');
        if (iframe && iframe.contentDocument) {
            const btn = iframe.contentDocument.querySelector('.goog-te-button button');
            if (btn) {
                btn.click();
                return;
            }
        }

        // Clear via combo
        const select = document.querySelector('.goog-te-combo');
        if (select) {
            select.value = '';
            select.dispatchEvent(new Event('change', { bubbles: true }));
        }

        // Clear cookies
        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=.' + window.location.hostname;

        // Reload if still translated
        setTimeout(function () {
            if (document.body.classList.contains('translated-ltr') ||
                document.body.classList.contains('translated-rtl')) {
                window.location.reload();
            }
        }, 300);
    }

    // ===== BUTTON STATE =====

    function updateButtons(lang) {
        const buttons = document.querySelectorAll('.lang-btn, .top-bar-right a[onclick*="setLanguage"]');

        buttons.forEach(function (btn) {
            btn.classList.remove('active');
            const text = btn.textContent.trim().toUpperCase();

            if ((lang === 'uk' && text === 'UA') ||
                (lang === 'ru' && text === 'RU') ||
                (lang === 'en' && text === 'EN')) {
                btn.classList.add('active');
            }
        });
    }

    // ===== PUBLIC API =====

    window.setLanguage = function (lang) {
        // Save preference
        localStorage.setItem(CONFIG.storageKey, lang);

        // Set cookies for cross-page persistence
        const domain = window.location.hostname;
        if (lang === 'uk') {
            document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
            document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=.' + domain;
        } else {
            const val = '/uk/' + lang;
            document.cookie = 'googtrans=' + val + '; path=/;';
            document.cookie = 'googtrans=' + val + '; path=/; domain=.' + domain;
        }

        // Update button states
        updateButtons(lang);

        // Do translation
        translateTo(lang);
    };

    // ===== CSS INJECTION =====

    function injectStyles() {
        if (document.getElementById('gt-custom-styles')) return;

        const style = document.createElement('style');
        style.id = 'gt-custom-styles';
        style.textContent = `
            /* Hide Google Translate UI */
            .goog-te-banner-frame { display: none !important; }
            .goog-te-menu-frame { display: none !important; }
            body { top: 0 !important; }
            .skiptranslate { display: none !important; height: 0 !important; }
            #google_translate_element { display: none !important; }
            .goog-te-gadget { display: none !important; }
            html.translated-ltr, html.translated-rtl { margin-top: 0 !important; }
            body.translated-ltr, body.translated-rtl { margin-top: 0 !important; top: 0 !important; }

            /* Keep buttons untranslated */
            .top-bar-right a, .lang-btn {
                font-style: normal !important;
            }

            /* Language button styles */
            .top-bar-right a, .lang-btn {
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

    // ===== INIT =====

    function init() {
        injectStyles();
        createTranslateWidget();
        loadGoogleTranslateScript();

        // Set initial button state
        const saved = localStorage.getItem(CONFIG.storageKey);
        updateButtons(saved || CONFIG.pageLanguage);
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
