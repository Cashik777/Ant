/* CONVERSION WIDGETS JAVASCRIPT */

// Promo Bar
function initPromoBar() {
    const promoBar = document.getElementById('promo-bar');
    const closeBtn = document.getElementById('promo-bar-close');

    // Check if user has closed it before
    if (localStorage.getItem('promoBarClosed') === 'true') {
        if (promoBar) promoBar.style.display = 'none';
        return;
    }

    // Show promo bar
    if (promoBar) {
        promoBar.classList.remove('hidden');

        // Adjust header position
        const header = document.querySelector('.header');
        if (header) {
            header.style.top = promoBar.offsetHeight + 'px';
        }
    }

    // Close button
    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            promoBar.classList.add('hidden');
            localStorage.setItem('promoBarClosed', 'true');

            // Reset header
            setTimeout(() => {
                const header = document.querySelector('.header');
                if (header) header.style.top = '0';
            }, 300);
        });
    }
}

// Floating Chat
function initFloatingChat() {
    const chatButton = document.getElementById('chat-button');
    const chatBubble = document.getElementById('chat-bubble');
    let bubbleTimeout;

    if (!chatButton) return;

    // Show bubble after 3 seconds
    setTimeout(() => {
        if (chatBubble) chatBubble.style.display = 'block';

        // Hide after 5 seconds
        bubbleTimeout = setTimeout(() => {
            if (chatBubble) chatBubble.style.display = 'none';
        }, 5000);
    }, 3000);

    // Click handler
    chatButton.addEventListener('click', () => {
        // Open Telegram/WhatsApp
        window.open('https://t.me/ethiodirect', '_blank');
    });
}

// Exit Intent Popup
let exitPopupShown = false;

function initExitIntent() {
    const popup = document.getElementById('exit-popup');
    const closeBtn = document.getElementById('exit-popup-close');
    const form = document.getElementById('exit-popup-form');

    if (!popup) return;

    // Check if already shown
    if (sessionStorage.getItem('exitPopupShown') === 'true') {
        return;
    }

    // Detect mouse leaving viewport
    document.addEventListener('mouseleave', (e) => {
        if (e.clientY <= 0 && !exitPopupShown) {
            showExitPopup();
        }
    });

    // Close button
    if (closeBtn) {
        closeBtn.addEventListener('click', hideExitPopup);
    }

    // Click outside to close
    popup.addEventListener('click', (e) => {
        if (e.target === popup) {
            hideExitPopup();
        }
    });

    // Form submit
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = form.querySelector('input[type="email"]').value;

            // Save to localStorage
            let subscribers = JSON.parse(localStorage.getItem('newsletterSubscribers') || '[]');
            if (!subscribers.includes(email)) {
                subscribers.push(email);
                localStorage.setItem('newsletterSubscribers', JSON.stringify(subscribers));
            }

            // Show success
            alert('Дякуємо! Перевірте email - ваш промокод на -10% вже чекає!');
            hideExitPopup();
        });
    }
}

function showExitPopup() {
    const popup = document.getElementById('exit-popup');
    if (popup && !exitPopupShown) {
        popup.classList.add('active');
        exitPopupShown = true;
        sessionStorage.setItem('exitPopupShown', 'true');
    }
}

function hideExitPopup() {
    const popup = document.getElementById('exit-popup');
    if (popup) {
        popup.classList.remove('active');
    }
}

// Back to Top Button
function initBackToTop() {
    const btn = document.getElementById('back-to-top');

    if (!btn) return;

    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            btn.classList.add('visible');
        } else {
            btn.classList.remove('visible');
        }
    });

    btn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Initialize all widgets
function initConversionWidgets() {
    initPromoBar();
    initFloatingChat();
    initExitIntent();
    initBackToTop();
}

// Auto-init on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initConversionWidgets);
} else {
    initConversionWidgets();
}

// Make functions global if needed
window.initConversionWidgets = initConversionWidgets;
