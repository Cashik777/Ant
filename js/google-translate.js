/* ===== ETHIODIRECT - GOOGLE TRANSLATE INTEGRATION ===== */
/* 3 buttons: UA / RU / EN - stable translation across all pages */

(function () {
    'use strict';

    // Configuration
    const STORAGE_KEY = 'ed_language';
    const DEFAULT_LANG = 'uk';
    const PAGE_LANG = 'uk'; // Original page language

    // ===== INITIALIZATION =====

    // Add Google Translate hidden container
    function initGoogleTranslate() {
        // Create hidden container for Google Translate widget
        if (!document.getElementById('google_translate_element')) {
            var gtDiv = document.createElement('div');
            gtDiv.id = 'google_translate_element';
            gtDiv.style.cssText = 'display:none !important; visibility:hidden !important; height:0 !important; overflow:hidden !important;';
            document.body.insertBefore(gtDiv, document.body.firstChild);
        }

        // Load Google Translate script
        if (!document.querySelector('script[src*="translate.google.com"]')) {
            var script = document.createElement('script');
            script.src = '//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit';
            script.async = true;
            document.head.appendChild(script);
        }
    }

    // Google Translate initialization callback (must be global)
    window.googleTranslateElementInit = function () {
        new google.translate.TranslateElement({
            pageLanguage: PAGE_LANG,
            includedLanguages: 'uk,ru,en',
            autoDisplay: false,
            multilanguagePage: false
        }, 'google_translate_element');

        // Apply saved language after a short delay
        setTimeout(function () {
            var savedLang = localStorage.getItem(STORAGE_KEY);
            if (savedLang && savedLang !== PAGE_LANG) {
                doTranslate(savedLang);
            }
            updateButtonStates(savedLang || PAGE_LANG);
        }, 1000);
    };

    // ===== TRANSLATION FUNCTIONS =====

    // Perform translation via Google Translate
    function doTranslate(lang) {
        var combo = document.querySelector('.goog-te-combo');

        if (!combo) {
            // Widget not ready yet, retry
            setTimeout(function () { doTranslate(lang); }, 500);
            return;
        }

        if (lang === PAGE_LANG || lang === 'uk') {
            // Reset to original language
            resetToOriginal();
        } else {
            // Translate to selected language
            combo.value = lang;
            combo.dispatchEvent(new Event('change', { bubbles: true }));
        }
    }

    // Reset to original language (Ukrainian)
    function resetToOriginal() {
        // Method 1: Try the Google Translate restore button
        var iframe = document.querySelector('.goog-te-banner-frame');
        if (iframe && iframe.contentDocument) {
            var restoreBtn = iframe.contentDocument.querySelector('.goog-te-button button');
            if (restoreBtn) {
                restoreBtn.click();
                return;
            }
        }

        // Method 2: Clear the combo and cookies
        var combo = document.querySelector('.goog-te-combo');
        if (combo) {
            combo.value = '';
            combo.dispatchEvent(new Event('change', { bubbles: true }));
        }

        // Method 3: Clear translation cookie and reload if needed
        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
        document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=.' + window.location.hostname;

        // Force reload the page for clean reset if still translated
        setTimeout(function () {
            var body = document.body;
            if (body.classList.contains('translated-ltr') || body.classList.contains('translated-rtl')) {
                window.location.reload();
            }
        }, 300);
    }

    // ===== BUTTON STATE MANAGEMENT =====

    // Update active state on language buttons
    function updateButtonStates(lang) {
        var langCode = lang || PAGE_LANG;
        var buttons = document.querySelectorAll('.top-bar-right a[onclick*="setLanguage"]');

        buttons.forEach(function (btn) {
            btn.classList.remove('active');
            var btnText = btn.textContent.trim().toUpperCase();

            if ((langCode === 'uk' && btnText === 'UA') ||
                (langCode === 'ru' && btnText === 'RU') ||
                (langCode === 'en' && btnText === 'EN')) {
                btn.classList.add('active');
            }
        });
    }

    // ===== PUBLIC API =====

    // Main function called by buttons
    window.setLanguage = function (lang) {
        // Save preference
        localStorage.setItem(STORAGE_KEY, lang);

        // Set Google Translate cookie for persistence across pages
        var domain = window.location.hostname;
        if (lang === 'uk' || lang === PAGE_LANG) {
            // Clear translation
            document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
            document.cookie = 'googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; domain=.' + domain;
        } else {
            // Set translation cookie
            var cookieVal = '/uk/' + lang;
            document.cookie = 'googtrans=' + cookieVal + '; path=/;';
            document.cookie = 'googtrans=' + cookieVal + '; path=/; domain=.' + domain;
        }

        // Update button states immediately
        updateButtonStates(lang);

        // Perform translation
        doTranslate(lang);
    };

    // ===== CSS STYLES =====

    // Inject styles to hide Google Translate UI and style buttons
    function injectStyles() {
        var style = document.createElement('style');
        style.id = 'google-translate-styles';
        style.textContent = [
            '/* Hide Google Translate UI elements */',
            '.goog-te-banner-frame { display: none !important; }',
            '.goog-te-menu-frame { display: none !important; }',
            'body { top: 0 !important; position: relative !important; }',
            '.skiptranslate { display: none !important; height: 0 !important; }',
            '#google_translate_element { display: none !important; }',
            '.goog-te-gadget { display: none !important; }',
            '',
            '/* Prevent layout shift from translation */',
            'html.translated-ltr, html.translated-rtl { margin-top: 0 !important; }',
            'body.translated-ltr, body.translated-rtl { margin-top: 0 !important; top: 0 !important; }',
            '',
            '/* Language button styles */',
            '.top-bar-right a {',
            '    color: rgba(255,255,255,0.7);',
            '    text-decoration: none;',
            '    padding: 4px 12px;',
            '    font-weight: 600;',
            '    font-size: 0.85rem;',
            '    border-radius: 4px;',
            '    margin: 0 2px;',
            '    transition: all 0.2s ease;',
            '    display: inline-block;',
            '}',
            '.top-bar-right a:hover {',
            '    color: white;',
            '    background: rgba(255,255,255,0.15);',
            '}',
            '.top-bar-right a.active {',
            '    color: white;',
            '    background: var(--primary, #5D4037);',
            '}',
            '',
            '/* Ensure notranslate elements stay untranslated */',
            '[translate="no"], .notranslate {',
            '    font-style: inherit !important;',
            '}'
        ].join('\n');

        if (!document.getElementById('google-translate-styles')) {
            document.head.appendChild(style);
        }
    }

    // ===== INITIALIZATION ON PAGE LOAD =====

    function init() {
        injectStyles();
        initGoogleTranslate();

        // Update button states based on saved preference
        var savedLang = localStorage.getItem(STORAGE_KEY);
        updateButtonStates(savedLang || PAGE_LANG);
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

})();
