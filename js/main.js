/* ===== ETHIODIRECT CORE ENGINE v4.0 ===== */

/* --- DATA --- */
const PRODUCTS = [
    {
        id: 1, name: 'Сидамо', region: 'Sidamo',
        desc: 'Класичний ефіопський. Шоколад, горіхи, м\'яка кислинка.',
        prices: { 250: 240, 500: 430, 1000: 820 },
        oldPrices: { 250: 280, 500: 510, 1000: 980 },
        weight: 250, roast: 'medium', taste: ['🍫', '🥜'],
        method: ['espresso', 'turka'],
        acidity: 2, body: 4, sweetness: 3,
        soldCount: 1247, rating: 4.8,
        image: 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
    },
    {
        id: 2, name: 'Йіргачеффе', region: 'Yirgacheffe',
        desc: 'Квітковий, цитрусовий. Ідеальний для фільтра.',
        prices: { 250: 280, 500: 520, 1000: 980 },
        oldPrices: { 250: 320, 500: 600, 1000: 1150 },
        weight: 250, roast: 'light', taste: ['🌸', '🍋'],
        method: ['filter'],
        acidity: 4, body: 2, sweetness: 4,
        soldCount: 892, rating: 4.9,
        image: 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
    },
    {
        id: 3, name: 'Гуджі Натурал', region: 'Guji',
        desc: 'Ягідний вибух. Полуниця, манго, мед.',
        prices: { 250: 320, 500: 590, 1000: 1120 },
        oldPrices: { 250: 380, 500: 720, 1000: 1400 },
        weight: 250, roast: 'light', taste: ['🍓', '🥭'],
        method: ['filter'],
        acidity: 3, body: 3, sweetness: 5,
        soldCount: 634, rating: 4.9,
        image: 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
    },
    {
        id: 4, name: 'Еспресо Бленд', region: 'Blend',
        desc: 'Стабільний смак для еспресо. Шоколад, карамель.',
        prices: { 250: 220, 500: 400, 1000: 760 },
        oldPrices: { 250: 260, 500: 480, 1000: 920 },
        weight: 250, roast: 'dark', taste: ['🍫', '🍬'],
        method: ['espresso'],
        acidity: 1, body: 5, sweetness: 3,
        soldCount: 2156, rating: 4.7,
        image: 'https://images.unsplash.com/photo-1550950158-d0d960dff51b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
    },
    {
        id: 5, name: 'Лімму', region: 'Limmu',
        desc: 'Збалансований. Зелене яблуко, карамель.',
        prices: { 250: 260, 500: 480, 1000: 920 },
        oldPrices: { 250: 300, 500: 560, 1000: 1080 },
        weight: 250, roast: 'medium', taste: ['🍏', '🍬'],
        method: ['espresso', 'filter'],
        acidity: 3, body: 3, sweetness: 4,
        soldCount: 421, rating: 4.6,
        image: 'https://images.unsplash.com/photo-1519681393784-d120267933ba?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
    },
    {
        id: 6, name: 'Харар', region: 'Harrar',
        desc: 'Дикий. Чорниця, вино, спеції.',
        prices: { 250: 340, 500: 640, 1000: 1220 },
        oldPrices: { 250: 420, 500: 800, 1000: 1540 },
        weight: 250, roast: 'light', taste: ['🫐', '🍷'],
        method: ['filter'],
        acidity: 4, body: 2, sweetness: 3,
        soldCount: 287, rating: 4.8,
        image: 'https://images.unsplash.com/photo-1610632380989-680fe40816c6?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
    }
];

// State for product selections (weight, qty per product)
const productSelections = {};

const SUBSCRIPTION_PLANS = [
    { id: 'espresso', name: 'Домашній еспресо', desc: 'Темна обжарка, 500г/міс', price: 450, roast: 'dark', weight: 500 },
    { id: 'filter', name: 'Фільтр і фрукти', desc: 'Світла обжарка, 300г/міс', price: 380, roast: 'light', weight: 300 },
    { id: 'discovery', name: 'Знайомство з Ефіопією', desc: 'Ротація сортів, 3×100г/міс', price: 420, roast: 'mixed', weight: 300 },
    { id: 'cafe', name: 'Кав\'ярня вдома', desc: '1кг/міс + безкоштовна доставка', price: 780, roast: 'medium', weight: 1000 }
];

const QUIZ_QUESTIONS = [
    {
        id: 1, text: 'Як ви готуєте каву?', options: [
            { text: 'Еспресо-машина', value: 'espresso', icon: 'fa-mug-hot' },
            { text: 'Фільтр / Воронка', value: 'filter', icon: 'fa-filter' },
            { text: 'Турка', value: 'turka', icon: 'fa-fire' },
            { text: 'Френч-прес', value: 'french', icon: 'fa-glass-water' }
        ]
    },
    {
        id: 2, text: 'Який смак вам ближче?', options: [
            { text: 'Шоколад і горіхи', value: 'chocolate', icon: 'fa-cookie' },
            { text: 'Ягоди і фрукти', value: 'fruity', icon: 'fa-lemon' },
            { text: 'Квіткові ноти', value: 'floral', icon: 'fa-spa' },
            { text: 'Пряний, насичений', value: 'spicy', icon: 'fa-pepper-hot' }
        ]
    },
    {
        id: 3, text: 'Яку міцність обираєте?', options: [
            { text: 'Легка (чайна)', value: 'light', icon: 'fa-feather' },
            { text: 'Середня (баланс)', value: 'medium', icon: 'fa-balance-scale' },
            { text: 'Міцна (насичена)', value: 'strong', icon: 'fa-bolt' }
        ]
    },
    {
        id: 4, text: 'Як часто п\'єте каву?', options: [
            { text: 'Рідко (1-2 рази/тиждень)', value: 'rare', icon: 'fa-clock' },
            { text: 'Іноді (3-4 рази/тиждень)', value: 'sometimes', icon: 'fa-calendar' },
            { text: 'Часто (щодня)', value: 'daily', icon: 'fa-coffee' },
            { text: 'Кавоман (2+ чашки/день)', value: 'addict', icon: 'fa-heart' }
        ]
    },
    {
        id: 5, text: 'Що для вас найважливіше?', options: [
            { text: 'Смак і аромат', value: 'taste', icon: 'fa-star' },
            { text: 'Енергія і бадьорість', value: 'energy', icon: 'fa-bolt' },
            { text: 'Ритуал приготування', value: 'ritual', icon: 'fa-magic' },
            { text: 'Користь для здоров\'я', value: 'health', icon: 'fa-leaf' }
        ]
    }
];

/* --- STATE --- */
const store = {
    cart: JSON.parse(localStorage.getItem('ed_cart')) || [],
    user: JSON.parse(localStorage.getItem('ed_user')) || { name: 'Guest', subscription: null },
    quizAnswers: {},
    currency: '₴'
};

/* --- SUBSCRIPTION CLASS --- */
class Subscription {
    constructor(config) {
        this.id = 'sub_' + Date.now();
        this.plan = config.plan;
        this.coffee = config.coffee;
        this.format = config.format;
        this.grind = config.grind || null;
        this.frequency = config.frequency;
        this.quantity = config.quantity;
        this.price = this.calculatePrice();
        this.status = 'active';
        this.nextDelivery = this.calculateNextDelivery();
        this.createdAt = new Date().toISOString();
    }

    calculatePrice() {
        let base = 380;
        if (this.quantity === 500) base *= 1.8;
        if (this.quantity === 1000) base *= 3.2;
        if (this.frequency === '2weeks') base *= 2;
        if (this.frequency === '2months') base *= 0.5;
        return Math.round(base * 0.9);
    }

    calculateNextDelivery() {
        const now = new Date();
        switch (this.frequency) {
            case '2weeks': now.setDate(now.getDate() + 14); break;
            case 'month': now.setMonth(now.getMonth() + 1); break;
            case '2months': now.setMonth(now.getMonth() + 2); break;
        }
        return now.toISOString();
    }

    pause() { this.status = 'paused'; this.save(); }
    resume() { this.status = 'active'; this.save(); }
    cancel() { this.status = 'cancelled'; this.save(); }

    save() {
        store.user.subscription = this;
        localStorage.setItem('ed_user', JSON.stringify(store.user));
    }
}

/* --- INIT --- */
document.addEventListener('DOMContentLoaded', () => {
    initABTest();
    initUI();
    initPageLogic();
    renderCart();

    window.addEventListener('beforeunload', () => {
        localStorage.setItem('ed_cart', JSON.stringify(store.cart));
        localStorage.setItem('ed_user', JSON.stringify(store.user));
    });

    // Re-render products when language changes
    document.addEventListener('languageChanged', () => {
        const path = window.location.pathname;
        if (path.endsWith('index.html') || path.endsWith('/') || path === '' || path.endsWith('/Ant/')) {
            renderFeatured();
            // Re-apply A/B test variant with new translations
            const variant = localStorage.getItem('ab_hero_cta');
            if (variant && typeof applyABTestVariant === 'function') {
                applyABTestVariant(variant);
            }
        }
        if (path.includes('shop.html')) {
            renderShop();
        }
        renderCart();
        renderMiniCart();
    });

    // Re-render products when i18n is fully initialized (translations loaded)
    document.addEventListener('i18nReady', () => {
        const path = window.location.pathname;
        if (path.endsWith('index.html') || path.endsWith('/') || path === '' || path.endsWith('/Ant/')) {
            renderFeatured();
        }
        if (path.includes('shop.html')) {
            renderShop();
        }
        renderCart();
        renderMiniCart();
    });
});

/* --- A/B TEST FRAMEWORK --- */
const AB_TESTS = {
    hero_cta: {
        variants: [
            { id: 'control', textKey: 'hero.hero_cta_control', icon: 'fa-fire' },
            { id: 'variant_a', textKey: 'hero.hero_cta_variant_a', icon: 'fa-coffee' },
            { id: 'variant_b', textKey: 'hero.hero_cta_variant_b', icon: 'fa-shopping-cart' }
        ],
        selector: '.btn-hero',
        active: true
    }
};

function initABTest() {
    // Get or assign variant
    let variant = localStorage.getItem('ab_hero_cta');

    if (!variant && AB_TESTS.hero_cta.active) {
        // Assign random variant
        const variants = AB_TESTS.hero_cta.variants;
        variant = variants[Math.floor(Math.random() * variants.length)].id;
        localStorage.setItem('ab_hero_cta', variant);
    }

    // Apply variant
    if (variant && AB_TESTS.hero_cta.active) {
        applyABTestVariant(variant);
        // Track impression
        trackABEvent('hero_cta', variant, 'impression');
    }
}

function applyABTestVariant(variant) {
    const test = AB_TESTS.hero_cta;
    const selectedVariant = test.variants.find(v => v.id === variant);
    if (selectedVariant) {
        const btn = document.querySelector(test.selector);
        if (btn) {
            // Use translation if t() function available
            const text = typeof t === 'function' ? t(selectedVariant.textKey) : selectedVariant.textKey;
            btn.innerHTML = `<i class="fas ${selectedVariant.icon}"></i> <span data-i18n="${selectedVariant.textKey}">${text}</span>`;
        }
    }
}

function trackABEvent(testName, variant, action) {
    // Store event locally for analysis
    const events = JSON.parse(localStorage.getItem('ab_events') || '[]');
    events.push({
        test: testName,
        variant: variant,
        action: action,
        timestamp: new Date().toISOString()
    });
    localStorage.setItem('ab_events', JSON.stringify(events));

    // Console log for dev
    console.log(`[A/B] ${testName}: ${variant} - ${action}`);
}

// Track CTA clicks
document.addEventListener('click', (e) => {
    const heroBtn = e.target.closest('.btn-hero');
    if (heroBtn) {
        const variant = localStorage.getItem('ab_hero_cta') || 'control';
        trackABEvent('hero_cta', variant, 'click');
    }
});

window.trackABEvent = trackABEvent;

function initUI() {
    setupDrawer();
    const header = document.querySelector('.header');
    if (header) {
        window.addEventListener('scroll', () => {
            header.style.boxShadow = window.scrollY > 20 ? '0 4px 20px rgba(0,0,0,0.1)' : 'none';
        });
    }
}

// Mobile Menu Toggle
function toggleMobileMenu() {
    const nav = document.getElementById('nav-mobile');
    const toggle = document.querySelector('.menu-toggle i');
    const body = document.body;

    if (!nav) return;

    const isOpen = nav.classList.contains('open');

    if (isOpen) {
        // Close menu
        closeMobileMenu();
    } else {
        // Open menu
        nav.classList.add('open');
        body.style.overflow = 'hidden'; // Prevent body scroll

        // Create and show overlay
        let overlay = document.querySelector('.nav-mobile-overlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'nav-mobile-overlay';
            document.body.appendChild(overlay);

            // Close on overlay click
            overlay.addEventListener('click', closeMobileMenu);
        }
        overlay.style.display = 'block';
        setTimeout(() => overlay.classList.add('active'), 10);

        // Update toggle icon
        if (toggle) {
            toggle.classList.remove('fa-bars');
            toggle.classList.add('fa-times');
        }
    }
}

function closeMobileMenu() {
    const nav = document.getElementById('nav-mobile');
    const toggle = document.querySelector('.menu-toggle i');
    const overlay = document.querySelector('.nav-mobile-overlay');
    const body = document.body;

    if (nav) {
        nav.classList.remove('open');
        body.style.overflow = ''; // Restore body scroll
    }

    if (overlay) {
        overlay.classList.remove('active');
        setTimeout(() => overlay.style.display = 'none', 300);
    }

    if (toggle) {
        toggle.classList.remove('fa-times');
        toggle.classList.add('fa-bars');
    }
}

// Close mobile menu when clicking a link inside it
document.addEventListener('DOMContentLoaded', () => {
    const navMobile = document.getElementById('nav-mobile');
    if (navMobile) {
        navMobile.querySelectorAll('a:not(.nav-mobile-footer a)').forEach(link => {
            link.addEventListener('click', closeMobileMenu);
        });
    }
});

window.toggleMobileMenu = toggleMobileMenu;
window.closeMobileMenu = closeMobileMenu;

function initPageLogic() {
    const path = window.location.pathname;
    if (path.endsWith('index.html') || path.endsWith('/') || path === '') renderFeatured();
    if (path.includes('shop.html')) { renderShop(); initFilters(); }
    if (path.includes('product.html')) initProductPage();
    if (path.includes('quiz.html')) initQuiz();
    if (path.includes('subscription.html')) initWizard();
    if (path.includes('account.html')) initDashboard();
}

/* --- SHOP --- */
function renderFeatured() {
    const grid = document.getElementById('featured-grid');
    if (!grid) return;
    grid.innerHTML = '';
    PRODUCTS.slice(0, 3).forEach(p => grid.innerHTML += createProductCard(p));
}

function renderShop(filter = 'all') { // filter arg kept for compatibility but we rely on DOM
    const grid = document.getElementById('products-grid');
    const countEl = document.getElementById('products-count');
    const noResults = document.getElementById('no-results');
    const resultsText = document.getElementById('results-text');

    if (!grid) return;

    // Safety check if PRODUCTS is undefined
    if (typeof PRODUCTS === 'undefined') return;

    let filtered = PRODUCTS;

    // 1. Roast (Checkboxes)
    const roastLight = document.getElementById('filter-light') && document.getElementById('filter-light').checked;
    const roastMedium = document.getElementById('filter-medium') && document.getElementById('filter-medium').checked;
    const roastDark = document.getElementById('filter-dark') && document.getElementById('filter-dark').checked;

    if (roastLight || roastMedium || roastDark) {
        filtered = filtered.filter(p => {
            if (roastLight && p.roast === 'light') return true;
            if (roastMedium && p.roast === 'medium') return true;
            if (roastDark && p.roast === 'dark') return true;
            return false;
        });
    }

    // 2. Taste (Checkboxes)
    const tasteFruity = document.getElementById('filter-fruity') && document.getElementById('filter-fruity').checked;
    const tasteChoco = document.getElementById('filter-chocolate') && document.getElementById('filter-chocolate').checked;
    const tasteFloral = document.getElementById('filter-floral') && document.getElementById('filter-floral').checked;

    if (tasteFruity || tasteChoco || tasteFloral) {
        const tasteMap = {
            fruity: ['🍓', '🥭', '🍋', '🍏', '🫐'],
            chocolate: ['🍫', '🥜', '🍬'],
            floral: ['🌸']
        };

        filtered = filtered.filter(p => {
            let match = false;
            // Check if product taste includes any of the selected category icons
            if (tasteFruity && p.taste.some(t => tasteMap.fruity.includes(t))) match = true;
            if (tasteChoco && p.taste.some(t => tasteMap.chocolate.includes(t))) match = true;
            if (tasteFloral && p.taste.some(t => tasteMap.floral.includes(t))) match = true;
            return match;
        });
    }

    // 3. Price (Inputs)
    const minPrice = document.getElementById('price-min') ? (parseInt(document.getElementById('price-min').value) || 0) : 0;
    const maxPrice = document.getElementById('price-max') ? (parseInt(document.getElementById('price-max').value) || 10000) : 10000;

    filtered = filtered.filter(p => {
        const price = p.prices[250]; // Base price
        return price >= minPrice && price <= maxPrice;
    });

    // 4. Sort (Select)
    const sortSelect = document.getElementById('sort-select');
    const sortMode = sortSelect ? sortSelect.value : 'popular';

    filtered.sort((a, b) => {
        const priceA = a.prices[250];
        const priceB = b.prices[250];

        switch (sortMode) {
            case 'price-asc': return priceA - priceB;
            case 'price-desc': return priceB - priceA;
            case 'rating': return b.rating - a.rating;
            case 'popular': default: return b.soldCount - a.soldCount;
        }
    });

    // Render
    grid.innerHTML = '';

    if (filtered.length === 0) {
        if (resultsText) resultsText.style.display = 'none';
        if (noResults) noResults.style.display = 'block';
    } else {
        if (noResults) noResults.style.display = 'none';
        if (resultsText) resultsText.style.display = 'block';
        grid.innerHTML = filtered.map(p => createProductCard(p)).join('');
    }

    // Update count
    if (countEl) countEl.textContent = filtered.length;
}

function applyFilters() { // Alias for main.js usage compatibility if any
    renderShop();
}

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav-desktop');
    if (toggle && nav) {
        toggle.addEventListener('click', () => {
            nav.classList.toggle('active');
            // Change icon
            const icon = toggle.querySelector('i');
            if (nav.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }
});


/* --- UTILS --- */
function createProductCard(p) {
    // Initialize selection state for this product
    if (!productSelections[p.id]) {
        productSelections[p.id] = { weight: 250, qty: 1, grind: 'beans' };
    }
    const sel = productSelections[p.id];
    const currentPrice = p.prices[sel.weight];
    const oldPrice = p.oldPrices[sel.weight];
    const discount = Math.round((1 - currentPrice / oldPrice) * 100);

    // Get product name and description from i18n
    const productKeys = {
        1: 'sidamo', 2: 'yirgacheffe', 3: 'guji',
        4: 'espresso_blend', 5: 'limmu', 6: 'harrar'
    };
    const productKey = productKeys[p.id] || 'sidamo';
    const productName = typeof t === 'function' ? t(`product.${productKey}`) : p.name;
    const productDesc = typeof t === 'function' ? t(`product.${productKey}_desc`) : p.desc;

    // Enhanced badges - competitor style
    const badges = [];
    if (discount >= 15) badges.push(`<div class="p-badge p-badge-sale">-${discount}%</div>`);
    if (p.soldCount > 1500) badges.push(`<div class="p-badge p-badge-hit"><i class="fas fa-fire"></i> ХІТ</div>`);
    if (p.id === 3 || p.id === 6) badges.push(`<div class="p-badge p-badge-new"><i class="fas fa-star"></i> NEW</div>`);

    // Simulated stock and review counts
    const stockLevels = { 1: 12, 2: 5, 3: 3, 4: 18, 5: 8, 6: 2 };
    const stock = stockLevels[p.id] || 10;
    const stockClass = stock <= 5 ? 'low-stock' : '';
    const reviewCount = Math.floor(p.soldCount * 0.12); // ~12% leave reviews

    // Roast labels with i18n
    const roastLabels = {
        light: typeof t === 'function' ? t('product.roast_light') : 'Світла',
        medium: typeof t === 'function' ? t('product.roast_medium') : 'Середня',
        dark: typeof t === 'function' ? t('product.roast_dark') : 'Темна'
    };

    // Taste profile labels with i18n
    const acidityLabel = typeof t === 'function' ? t('product.acidity') : 'Кислотність';
    const bodyLabel = typeof t === 'function' ? t('product.body') : 'Тіло';
    const sweetnessLabel = typeof t === 'function' ? t('product.sweetness') : 'Солодкість';

    // Grind labels with i18n
    const grindLabels = {
        beans: typeof t === 'function' ? t('product.whole_beans') : 'Зерно',
        espresso: typeof t === 'function' ? t('product.espresso') : 'Еспресо',
        filter: typeof t === 'function' ? t('product.filter') : 'Фільтр',
        turka: typeof t === 'function' ? t('product.turka') : 'Турка'
    };

    // Labels
    const addButtonText = typeof t === 'function' ? t('product.add') : 'В кошик';
    const purchasedText = typeof t === 'function' ? t('product.purchased') : 'Куплено';
    const reviewsText = typeof t === 'function' ? t('product.reviews') : 'відгуків';
    const stockLeftText = typeof t === 'function' ? t('product.stock_left') : 'Залишилось';
    const pcsText = typeof t === 'function' ? t('product.pcs') : 'шт';

    // Taste bar renderer (visual bars instead of dots)
    const renderTasteBar = (value, max = 5) => {
        return `<div class="taste-bar"><div class="taste-bar-fill" style="width: ${(value / max) * 100}%"></div></div>`;
    };

    // Rating with review count
    const renderRating = () => {
        return `
            <div class="p-rating-full">
                <div class="p-stars">
                    <i class="fas fa-star"></i>
                    <span class="p-rating-num">${p.rating}</span>
                </div>
                <span class="p-review-count">(${reviewCount} ${reviewsText})</span>
            </div>
        `;
    };

    return `
    <div class="product-card ${stockClass}" data-product-id="${p.id}">
        <!-- Badges -->
        <div class="p-badges">${badges.join('')}</div>
        
        <!-- Wishlist Button -->
        <button class="p-wishlist" onclick="toggleWishlist(${p.id})" title="В обране">
            <i class="far fa-heart"></i>
        </button>
        
        <!-- Image -->
        <div class="p-img-box">
            <a href="product.html?id=${p.id}">
                <img src="${p.image}" alt="${productName}" loading="lazy">
            </a>
            ${stock <= 5 ? `<div class="p-stock-warning"><i class="fas fa-clock"></i> ${stockLeftText} ${stock} ${pcsText}!</div>` : ''}
        </div>
        
        <div class="p-content">
            <!-- Header with Rating -->
            <div class="p-header">
                <h3 class="p-title"><a href="product.html?id=${p.id}">${productName}</a></h3>
                ${renderRating()}
            </div>
            
            <!-- Region & Roast -->
            <div class="p-meta">
                <span class="p-region"><i class="fas fa-map-marker-alt"></i> ${p.region}</span>
                <span class="p-roast"><i class="fas fa-fire-alt"></i> ${roastLabels[p.roast]}</span>
            </div>
            
            <!-- Description -->
            <p class="p-desc">${productDesc}</p>
            
            <!-- VISUAL Taste Profile -->
            <div class="taste-profile-visual">
                <div class="taste-item">
                    <span class="taste-label">${acidityLabel}</span>
                    ${renderTasteBar(p.acidity)}
                </div>
                <div class="taste-item">
                    <span class="taste-label">${bodyLabel}</span>
                    ${renderTasteBar(p.body)}
                </div>
                <div class="taste-item">
                    <span class="taste-label">${sweetnessLabel}</span>
                    ${renderTasteBar(p.sweetness)}
                </div>
            </div>
            
            <!-- Weight Selector -->
            <div class="weight-selector" data-product-id="${p.id}">
                <button class="weight-btn ${sel.weight === 250 ? 'active' : ''}" onclick="selectWeight(${p.id}, 250)">250g</button>
                <button class="weight-btn ${sel.weight === 500 ? 'active' : ''}" onclick="selectWeight(${p.id}, 500)">500g</button>
                <button class="weight-btn ${sel.weight === 1000 ? 'active' : ''}" onclick="selectWeight(${p.id}, 1000)">1 kg</button>
            </div>
            
            <!-- Grind Selector -->
            <div class="grind-selector" data-product-id="${p.id}">
                <button class="grind-btn ${sel.grind === 'beans' || !sel.grind ? 'active' : ''}" onclick="selectGrind(${p.id}, 'beans')">
                    <i class="fas fa-seedling"></i> ${grindLabels.beans}
                </button>
                <button class="grind-btn ${sel.grind === 'espresso' ? 'active' : ''}" onclick="selectGrind(${p.id}, 'espresso')">
                    <i class="fas fa-coffee"></i> ${grindLabels.espresso}
                </button>
                <button class="grind-btn ${sel.grind === 'filter' ? 'active' : ''}" onclick="selectGrind(${p.id}, 'filter')">
                    <i class="fas fa-mug-hot"></i> ${grindLabels.filter}
                </button>
                <button class="grind-btn ${sel.grind === 'turka' ? 'active' : ''}" onclick="selectGrind(${p.id}, 'turka')">
                    <i class="fas fa-fire-alt"></i> ${grindLabels.turka}
                </button>
            </div>

            <!-- Price Block - ENHANCED -->
            <div class="p-price-block">
                <div class="p-price-main">
                    <span class="p-price-old">${oldPrice} ₴</span>
                    <span class="p-price-current" id="price-${p.id}">${currentPrice} ₴</span>
                    ${discount >= 15 ? `<span class="p-discount-badge">-${discount}%</span>` : ''}
                </div>
            </div>

            <!-- Actions -->
            <div class="p-actions">
                <div class="qty-controls">
                    <button class="qty-btn" onclick="changeQty(${p.id}, -1)">−</button>
                    <span class="qty-value" id="qty-${p.id}">${sel.qty}</span>
                    <button class="qty-btn" onclick="changeQty(${p.id}, 1)">+</button>
                </div>
                <button class="p-btn-add" onclick="addToCartWithOptions(${p.id})">
                    <i class="fas fa-shopping-cart"></i> ${addButtonText}
                </button>
            </div>
            
            <!-- Social Proof - ENHANCED -->
            <div class="p-social-proof">
                <span class="p-purchased"><i class="fas fa-check-circle"></i> ${purchasedText}: <strong>${p.soldCount.toLocaleString()}</strong> ${pcsText}</span>
            </div>
        </div>
    </div>
    `;
}

// Wishlist toggle function
function toggleWishlist(productId) {
    const btn = document.querySelector(`.product-card[data-product-id="${productId}"] .p-wishlist i`);
    if (btn) {
        btn.classList.toggle('far');
        btn.classList.toggle('fas');
        btn.classList.toggle('active');
    }
}

// Weight selector handler
function selectWeight(productId, weight) {
    productSelections[productId] = productSelections[productId] || { weight: 250, qty: 1 };
    productSelections[productId].weight = weight;

    const p = PRODUCTS.find(x => x.id === productId);
    const currentPrice = p.prices[weight];
    const oldPrice = p.oldPrices[weight];

    // Update price display
    const priceEl = document.getElementById(`price-${productId}`);
    if (priceEl) priceEl.textContent = currentPrice + ' ₴';

    // Update old price
    const card = document.querySelector(`[data-product-id="${productId}"]`);
    if (card) {
        const oldPriceEl = card.querySelector('.p-price-old');
        const economyEl = card.querySelector('.p-economy strong');
        if (oldPriceEl) oldPriceEl.textContent = oldPrice + ' ₴';
        if (economyEl) economyEl.textContent = (oldPrice - currentPrice) + ' ₴';
    }

    // Update active button
    const selector = document.querySelector(`.weight-selector[data-product-id="${productId}"]`);
    if (selector) {
        selector.querySelectorAll('.weight-btn').forEach(btn => btn.classList.remove('active'));
        selector.querySelector(`.weight-btn:nth-child(${weight === 250 ? 1 : weight === 500 ? 2 : 3})`).classList.add('active');
    }
}

// Quantity control handler
function changeQty(productId, delta) {
    productSelections[productId] = productSelections[productId] || { weight: 250, qty: 1, grind: 'beans' };
    let newQty = productSelections[productId].qty + delta;
    if (newQty < 1) newQty = 1;
    if (newQty > 10) newQty = 10;
    productSelections[productId].qty = newQty;

    const qtyEl = document.getElementById(`qty-${productId}`);
    if (qtyEl) qtyEl.textContent = newQty;
}

// Grind selector handler
function selectGrind(productId, grind) {
    productSelections[productId] = productSelections[productId] || { weight: 250, qty: 1, grind: 'beans' };
    productSelections[productId].grind = grind;

    // Update active button
    const selector = document.querySelector(`.grind-selector[data-product-id="${productId}"]`);
    if (selector) {
        selector.querySelectorAll('.grind-btn').forEach(btn => btn.classList.remove('active'));
        const activeBtn = selector.querySelector(`.grind-btn:nth-child(${grind === 'beans' ? 1 : grind === 'espresso' ? 2 : grind === 'filter' ? 3 : 4})`);
        if (activeBtn) activeBtn.classList.add('active');
    }
}

// Add to cart with selected weight, quantity and grind
function addToCartWithOptions(productId) {
    const p = PRODUCTS.find(x => x.id === productId);
    if (!p) return;

    const sel = productSelections[productId] || { weight: 250, qty: 1, grind: 'beans' };
    const price = p.prices[sel.weight];
    const grindLabel = getGrindLabel(sel.grind);

    // Check if item already exists in cart with same options
    const existingItem = store.cart.find(item =>
        item.id === p.id &&
        item.selectedWeight === sel.weight &&
        item.selectedGrind === sel.grind
    );

    if (existingItem) {
        existingItem.qty += sel.qty;
    } else {
        store.cart.push({
            ...p,
            cartId: Date.now(),
            qty: sel.qty,
            selectedWeight: sel.weight,
            selectedGrind: sel.grind,
            price: price
        });
    }

    renderCart();

    const addedText = typeof t === 'function' ? t('product.added_to_cart') : 'Додано!';
    showToast(`${p.name} (${sel.weight}г, ${grindLabel}) ${addedText}`);
    openMiniCart();

    // Reset quantity after adding
    productSelections[productId].qty = 1;
    const qtyEl = document.getElementById(`qty-${productId}`);
    if (qtyEl) qtyEl.textContent = '1';
}

// Make selectGrind globally available
window.selectGrind = selectGrind;

// Toast notification
function showToast(message) {
    const toast = document.getElementById('toast');
    const msgEl = document.getElementById('toast-msg');
    if (toast && msgEl) {
        msgEl.textContent = message;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3000);
    }
}

/* ========================================
   SEARCH FUNCTIONALITY
   ======================================== */
function handleSearch(query) {
    const resultsContainer = document.getElementById('search-results');
    if (!resultsContainer) return;

    if (query.length < 2) {
        resultsContainer.classList.remove('active');
        return;
    }

    const q = query.toLowerCase();
    const results = PRODUCTS.filter(p =>
        p.name.toLowerCase().includes(q) ||
        p.region.toLowerCase().includes(q) ||
        p.desc.toLowerCase().includes(q)
    );

    if (results.length === 0) {
        resultsContainer.innerHTML = `
            <div style="padding: 20px; text-align: center; color: var(--text-muted);">
                <i class="fas fa-search" style="font-size: 2rem; margin-bottom: 10px; color: #ddd;"></i>
                <p>Нічого не знайдено для "${query}"</p>
            </div>
        `;
    } else {
        resultsContainer.innerHTML = results.map(p => `
            <a href="product.html?id=${p.id}" class="search-result-item">
                <img src="${p.image}" alt="${p.name}">
                <div class="search-result-info">
                    <div class="search-result-name">${p.name}</div>
                    <div class="search-result-price">від ${p.prices[250]} ₴</div>
                </div>
            </a>
        `).join('');
    }

    resultsContainer.classList.add('active');
}

// Close search results when clicking outside
document.addEventListener('click', (e) => {
    const searchWrapper = document.querySelector('.search-wrapper');
    const resultsContainer = document.getElementById('search-results');
    if (searchWrapper && resultsContainer && !searchWrapper.contains(e.target)) {
        resultsContainer.classList.remove('active');
    }
});

/* ========================================
   MINI-CART FUNCTIONALITY
   ======================================== */
function renderMiniCart() {
    const itemsContainer = document.getElementById('mini-cart-items');
    const countEl = document.getElementById('mini-cart-count');
    const totalEl = document.getElementById('mini-cart-total');
    const shippingEl = document.getElementById('mini-cart-shipping');
    const footerEl = document.getElementById('mini-cart-footer');

    if (!itemsContainer) return;

    const count = store.cart.length;
    if (countEl) {
        const word = count === 1 ? t('cart.items_single') : (count < 5 ? t('cart.items_few') : t('cart.items'));
        countEl.textContent = `${count} ${word}`;
    }

    if (count === 0) {
        itemsContainer.innerHTML = `
            <div class="mini-cart-empty">
                <i class="fas fa-mug-hot"></i>
                <p>${t('cart.empty')}</p>
                <a href="shop.html" style="color: var(--primary); font-weight: 600;">${t('cart.to_catalog')}</a>
            </div>
        `;
        if (footerEl) footerEl.style.display = 'none';
        return;
    }

    if (footerEl) footerEl.style.display = 'block';

    // Show last 3 items
    const displayItems = store.cart.slice(-3).reverse();
    let sum = 0;
    store.cart.forEach(item => sum += item.price * item.qty);

    itemsContainer.innerHTML = displayItems.map(item => `
        <div class="mini-cart-item">
            <img src="${item.image}" alt="${item.name}">
            <div class="mini-cart-item-info">
                <div class="mini-cart-item-name">${item.name}</div>
                <div class="mini-cart-item-meta">
                    ${item.selectedWeight || 250}${t('product.unit_g')} 
                    ${item.qty > 1 ? `<span style="color:var(--primary); font-weight:bold; margin-left:4px;">x${item.qty}</span>` : ''}
                </div>
            </div>
            <div class="mini-cart-item-price">${item.price} ₴</div>
            <button class="mini-cart-item-remove" onclick="removeFromCart(${item.cartId}); event.stopPropagation();" style="margin-left: auto;">&times;</button>
        </div>
    `).join('');

    if (store.cart.length > 3) {
        const moreItems = store.cart.length - 3;
        const moreText = t('cart.more_items') || `+ ${moreItems} more`;
        itemsContainer.innerHTML += `
            <div style="text-align: center; padding: 10px; color: var(--text-muted); font-size: 0.85rem;">
                ${moreText.replace('{count}', moreItems)}
            </div>
        `;
    }

    // Calculate total quantity for badges
    const totalQty = store.cart.reduce((total, item) => total + item.qty, 0);

    // Update all badge counters
    document.querySelectorAll('.cart-count').forEach(el => {
        el.textContent = totalQty;
        el.style.display = totalQty > 0 ? 'flex' : 'none'; // Optional: hide if 0? User wants to see 0 maybe.
        el.style.display = ''; // Reset display
    });

    if (totalEl) totalEl.textContent = sum + ' ₴';

    // Update shipping message
    if (shippingEl) {
        if (sum >= 500) {
            shippingEl.innerHTML = `<i class="fas fa-check-circle"></i> ${t('cart.free_shipping_done')}`;
            shippingEl.style.color = 'var(--success)';
        } else {
            const remaining = 500 - sum;
            shippingEl.innerHTML = `<i class="fas fa-truck"></i> ${t('cart.free_shipping_progress')} <strong>${remaining} ₴</strong>`;
            shippingEl.style.color = '';
        }
    }
}

function openMiniCart() {
    const miniCart = document.getElementById('mini-cart');
    if (miniCart) {
        miniCart.classList.add('active');
        renderMiniCart();

        // Auto-hide after 3 seconds
        setTimeout(() => {
            miniCart.classList.remove('active');
        }, 3000);
    }
}

// Make functions globally available
window.handleSearch = handleSearch;
window.selectWeight = selectWeight;
window.changeQty = changeQty;
window.addToCartWithOptions = addToCartWithOptions;
window.openMiniCart = openMiniCart;
window.applyFilters = renderShop; // Map applyFilters to renderShop
window.clearAllFilters = clearAllFilters;

function clearAllFilters() {
    document.querySelectorAll('input[type="checkbox"]').forEach(cb => cb.checked = false);
    const minP = document.getElementById('price-min'); if (minP) minP.value = '';
    const maxP = document.getElementById('price-max'); if (maxP) maxP.value = '';
    const sortS = document.getElementById('sort-select'); if (sortS) sortS.value = 'popular';
    renderShop();
}

function initFilters() {
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderShop(btn.dataset.filter || 'all');
        });
    });
}

/* --- PRODUCT PAGE --- */
function initProductPage() {
    const id = parseInt(new URLSearchParams(window.location.search).get('id'));
    const p = PRODUCTS.find(x => x.id === id);
    if (!p) return;

    document.getElementById('p-title').innerText = p.name;
    document.getElementById('p-price').innerText = p.price + ' ' + store.currency;
    document.getElementById('p-desc').innerText = p.desc;
    document.getElementById('p-main-img').src = p.image;
    document.title = p.name + ' — EthioDirect';

    document.getElementById('add-to-cart-btn').onclick = () => addToCart(p.id);
}

/* --- CART --- */
function addToCart(id) {
    const p = PRODUCTS.find(x => x.id === id);
    if (!p) return;
    const price = p.prices ? p.prices[250] : p.price;

    // Check for existing item (default: 250g, beans)
    const existingItem = store.cart.find(item =>
        item.id === p.id &&
        item.selectedWeight === 250 &&
        item.selectedGrind === 'beans'
    );

    if (existingItem) {
        existingItem.qty += 1;
    } else {
        store.cart.push({
            ...p,
            cartId: Date.now(),
            qty: 1,
            selectedWeight: 250,
            selectedGrind: 'beans',
            price: price
        });
    }

    renderCart();
    showToast(`${p.name} додано в кошик!`);
    openMiniCart();
}

function removeFromCart(cartId) {
    store.cart = store.cart.filter(i => i.cartId !== cartId);
    renderCart();
}

function renderCart() {
    const list = document.getElementById('cart-list');
    const total = document.getElementById('cart-total');
    const count = document.querySelector('.cart-count');

    // Calculate total quantity including groups
    const totalQty = store.cart.reduce((total, item) => total + item.qty, 0);

    // Update all counts
    document.querySelectorAll('.cart-count').forEach(el => el.innerText = totalQty);

    if (count) count.innerText = totalQty; // Fallback for specific element
    if (!list) return;

    if (store.cart.length === 0) {
        list.innerHTML = `
            <div style="text-align:center; padding:40px 20px;">
                <i class="fas fa-mug-hot" style="font-size:3rem; color:#eee; margin-bottom:20px; display:block;"></i>
                <p style="color:var(--text-muted); margin-bottom:20px;">${t('cart.empty')}</p>
                <a href="shop.html" class="btn btn-primary btn-sm" onclick="closeDrawer();">${t('cart.to_catalog')}</a>
            </div>
        `;
        if (total) total.innerText = '0 ' + store.currency;
        updateShippingProgress(0);
        renderMiniCart(); // Fix: Update mini-cart when empty
        return;
    }

    let sum = 0;
    list.innerHTML = '';
    store.cart.forEach(item => {
        sum += item.price * item.qty;
        const grindLabel = item.selectedGrind ? getGrindLabel(item.selectedGrind) : t('product.whole_beans');
        list.innerHTML += `
        <div class="cart-item">
            <img src="${item.image}" alt="${item.name}">
            <div style="flex:1;">
                <h4 style="font-size:0.95rem; margin-bottom:4px; font-weight:600;">${item.name}</h4>
                <p style="margin:0; font-size:0.8rem; color:var(--text-muted);">
                    ${item.selectedWeight || 250}${t('product.unit_g')} • ${grindLabel}
                    ${item.qty > 1 ? `<span style="color:var(--primary); font-weight:bold; margin-left:5px;">x${item.qty}</span>` : ''}
                </p>
                <p style="margin:5px 0 0; font-size:0.95rem; color:var(--primary); font-weight:700;">
                    ${item.price * item.qty} ${store.currency}
                    ${item.qty > 1 ? `<span style="font-size:0.8em; color:var(--text-muted); font-weight:normal;">(${item.price} ${store.currency}/${t('product.pcs')})</span>` : ''}
                </p>
            </div>
                </p>
            </div>
            <button onclick="removeFromCart(${item.cartId}); event.stopPropagation();" style="background:none; border:none; color:#999; cursor:pointer; font-size:1.3rem; padding:5px; margin-left: auto; align-self: flex-start;" title="${t('cart.remove') || 'Remove'}">&times;</button>
        </div>`;
    });
    if (total) total.innerText = sum + ' ' + store.currency;

    // Update shipping progress bar
    updateShippingProgress(sum);

    // Also update mini-cart
    renderMiniCart();
}

/* --- SHIPPING PROGRESS BAR --- */
const FREE_SHIPPING_THRESHOLD = 500;

function updateShippingProgress(currentTotal) {
    const progressFill = document.getElementById('drawer-progress-fill');
    const progressText = document.getElementById('drawer-progress-text');

    if (!progressFill || !progressText) return;

    const percentage = Math.min((currentTotal / FREE_SHIPPING_THRESHOLD) * 100, 100);
    progressFill.style.width = percentage + '%';

    if (currentTotal >= FREE_SHIPPING_THRESHOLD) {
        progressText.innerHTML = `<i class="fas fa-check-circle"></i> <strong>${t('cart.free_shipping_done')}</strong>`;
        progressText.classList.add('progress-complete');
        progressFill.style.background = 'linear-gradient(90deg, #3D5A40, #4CAF50)';
    } else {
        const remaining = FREE_SHIPPING_THRESHOLD - currentTotal;
        progressText.innerHTML = `<i class="fas fa-truck"></i> ${t('cart.free_shipping_progress')} <strong>${remaining} ₴</strong>`;
        progressText.classList.remove('progress-complete');
        progressFill.style.background = 'linear-gradient(90deg, var(--success), #4CAF50)';
    }
}

/* --- GRIND OPTIONS --- */
const GRIND_OPTIONS = [
    { id: 'beans', label: 'Зерно', icon: '🫘' },
    { id: 'espresso', label: 'Еспресо', icon: '☕' },
    { id: 'filter', label: 'Фільтр', icon: '🫖' },
    { id: 'turka', label: 'Турка', icon: '🏺' }
];

function getGrindLabel(grindId) {
    if (!grindId) return t('product.whole_beans');
    return t('product.' + grindId);
}

/* --- DRAWER --- */
function setupDrawer() {
    const overlay = document.querySelector('.overlay');
    if (overlay) {
        overlay.addEventListener('click', closeDrawer);
    }
}

function openDrawer() {
    document.querySelector('.drawer')?.classList.add('open');
    document.querySelector('.overlay')?.classList.add('open');
    document.body.style.overflow = 'hidden'; // Lock scroll
}

function closeDrawer() {
    document.querySelector('.drawer')?.classList.remove('open');
    document.querySelector('.overlay')?.classList.remove('open');
    document.body.style.overflow = ''; // Unlock scroll
}

/* --- QUIZ --- */
let quizStep = 0;
function initQuiz() {
    quizStep = 0;
    store.quizAnswers = {};
    renderQuizStep();
}

function renderQuizStep() {
    if (quizStep >= QUIZ_QUESTIONS.length) { showQuizResult(); return; }

    const q = QUIZ_QUESTIONS[quizStep];
    const container = document.getElementById('quiz-content');
    if (!container) return;

    document.querySelector('.quiz-progress-bar').style.width = ((quizStep + 1) / QUIZ_QUESTIONS.length * 100) + '%';

    container.innerHTML = `
        <div class="quiz-question">
            <h3 style="margin-bottom:10px;">Питання ${quizStep + 1} / ${QUIZ_QUESTIONS.length}</h3>
            <h2>${q.text}</h2>
            <div class="quiz-options">
                ${q.options.map(o => `
                    <div class="quiz-option" onclick="selectQuizOption('${o.value}')">
                        <i class="fas ${o.icon}" style="margin-right:12px; color:var(--primary);"></i>
                        ${o.text}
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

function selectQuizOption(value) {
    store.quizAnswers[QUIZ_QUESTIONS[quizStep].id] = value;
    quizStep++;
    renderQuizStep();
}

function showQuizResult() {
    // Personalization scoring algorithm
    const answers = store.quizAnswers;
    const scores = {};

    // Initialize scores for each product
    PRODUCTS.forEach(p => scores[p.id] = { score: 0, reasons: [] });

    // Question 1: Brewing method
    const method = answers[1];
    PRODUCTS.forEach(p => {
        if (p.method.includes(method)) {
            scores[p.id].score += 30;
            const methodNames = { espresso: 'еспресо', filter: 'фільтру', turka: 'турки', french: 'френч-преса' };
            scores[p.id].reasons.push(`Ідеально для ${methodNames[method] || method}`);
        }
    });

    // Question 2: Taste preference
    const taste = answers[2];
    PRODUCTS.forEach(p => {
        const tasteMap = {
            'chocolate': ['🍫', '🥜', '🍬'],
            'fruity': ['🍓', '🥭', '🍋', '🍏', '🫐'],
            'floral': ['🌸'],
            'spicy': ['🍷', '🌶️']
        };
        const matches = p.taste.filter(t => (tasteMap[taste] || []).includes(t));
        if (matches.length > 0) {
            scores[p.id].score += 25 * matches.length;
            const tasteNames = { chocolate: 'шоколадний', fruity: 'фруктовий', floral: 'квітковий', spicy: 'пряний' };
            scores[p.id].reasons.push(`${tasteNames[taste]} профіль смаку`);
        }
    });

    // Question 3: Strength preference
    const strength = answers[3];
    const roastMap = { light: 'light', medium: 'medium', strong: 'dark' };
    PRODUCTS.forEach(p => {
        if (p.roast === roastMap[strength]) {
            scores[p.id].score += 20;
            const strengthNames = { light: 'легка', medium: 'збалансована', strong: 'насичена' };
            scores[p.id].reasons.push(`${strengthNames[strength]} обсмажка`);
        }
    });

    // Question 4: Frequency (affects recommendation emphasis)
    const freq = answers[4];
    if (freq === 'daily' || freq === 'addict') {
        // Recommend subscription-friendly products
        PRODUCTS.forEach(p => {
            if (p.price <= 280) {
                scores[p.id].score += 10;
            }
        });
    }

    // Question 5: Priority (taste, energy, ritual, health)
    const priority = answers[5];
    if (priority === 'taste') {
        // Boost specialty high-score products
        PRODUCTS.filter(p => p.price >= 300).forEach(p => scores[p.id].score += 15);
    }

    // Find top recommendation
    const sorted = Object.entries(scores).sort((a, b) => b[1].score - a[1].score);
    const topId = parseInt(sorted[0][0]);
    const recommended = PRODUCTS.find(p => p.id === topId);
    const reasons = scores[topId].reasons.slice(0, 3).join(' • ');

    const container = document.getElementById('quiz-content');
    container.innerHTML = `
        <div class="text-center" style="background:white; padding:50px; border-radius:var(--radius);">
            <i class="fas fa-check-circle" style="font-size:4rem; color:var(--success); margin-bottom:20px;"></i>
            <h2>Ваша ідеальна кава:</h2>
            <h1 style="color:var(--primary); margin:20px 0;">${recommended.name}</h1>
            <p style="margin-bottom:15px;">${recommended.desc}</p>
            <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:25px;">
                <strong>Чому саме ця:</strong> ${reasons || 'Збалансований вибір для вас'}
            </p>
            <div style="margin-top:30px; display:flex; gap:15px; justify-content:center; flex-wrap:wrap;">
                <button class="btn btn-primary" onclick="addToCart(${recommended.id}); closeQuiz();">Додати в кошик — ${recommended.price}₴</button>
                <a href="subscription.html?product=${recommended.id}" class="btn btn-secondary">Оформити підписку -10%</a>
            </div>
        </div>
    `;
}

/* --- WIZARD --- */
let wizardStep = 1;
let wizardData = { coffee: 'auto', format: 'grain', grind: null, frequency: 'month' };

function initWizard() {
    wizardStep = 1;
    renderWizardStep();
}

function renderWizardStep() {
    updateWizardIndicator();
    const container = document.getElementById('wizard-content');
    if (!container) return;

    let html = '';
    switch (wizardStep) {
        case 1:
            html = `<h2>Крок 1: Оберіть каву</h2>
            <div class="wizard-options">
                <div class="option-card ${wizardData.coffee === 'auto' ? 'selected' : ''}" onclick="setWizard('coffee','auto')">
                    <i class="fas fa-magic"></i><div><h4>Автоматичний вибір</h4><p style="margin:0;font-size:0.9rem;">Обжарщик обирає найкраще</p></div>
                </div>
                ${PRODUCTS.slice(0, 4).map(p => `
                    <div class="option-card ${wizardData.coffee === p.id ? 'selected' : ''}" onclick="setWizard('coffee',${p.id})">
                        <img src="${p.image}" style="width:50px;height:50px;border-radius:8px;">
                        <div><h4>${p.name}</h4><p style="margin:0;font-size:0.9rem;">${p.region}</p></div>
                    </div>
                `).join('')}
            </div>`;
            break;
        case 2:
            html = `<h2>Крок 2: Формат</h2>
            <div class="wizard-options">
                <div class="option-card ${wizardData.format === 'grain' ? 'selected' : ''}" onclick="setWizard('format','grain')">
                    <i class="fas fa-circle"></i><div><h4>Зерно</h4></div>
                </div>
                <div class="option-card ${wizardData.format === 'ground' ? 'selected' : ''}" onclick="setWizard('format','ground')">
                    <i class="fas fa-mortar-pestle"></i><div><h4>Молотий</h4></div>
                </div>
            </div>
            ${wizardData.format === 'ground' ? `
                <h3 style="margin-top:30px;">Помол під:</h3>
                <div class="wizard-options">
                    <div class="option-card ${wizardData.grind === 'espresso' ? 'selected' : ''}" onclick="setWizard('grind','espresso')"><i class="fas fa-mug-hot"></i><div>Еспресо</div></div>
                    <div class="option-card ${wizardData.grind === 'filter' ? 'selected' : ''}" onclick="setWizard('grind','filter')"><i class="fas fa-filter"></i><div>Фільтр</div></div>
                    <div class="option-card ${wizardData.grind === 'turka' ? 'selected' : ''}" onclick="setWizard('grind','turka')"><i class="fas fa-fire"></i><div>Турка</div></div>
                </div>
            ` : ''}`;
            break;
        case 3:
            html = `<h2>Крок 3: Частота доставки</h2>
            <div class="wizard-options">
                <div class="option-card ${wizardData.frequency === '2weeks' ? 'selected' : ''}" onclick="setWizard('frequency','2weeks')"><i class="fas fa-calendar-week"></i><div><h4>Раз на 2 тижні</h4></div></div>
                <div class="option-card ${wizardData.frequency === 'month' ? 'selected' : ''}" onclick="setWizard('frequency','month')"><i class="fas fa-calendar-alt"></i><div><h4>Раз на місяць</h4><span style="color:var(--secondary);font-size:0.8rem;">⭐ Найпопулярніше</span></div></div>
                <div class="option-card ${wizardData.frequency === '2months' ? 'selected' : ''}" onclick="setWizard('frequency','2months')"><i class="fas fa-calendar"></i><div><h4>Раз на 2 місяці</h4></div></div>
            </div>`;
            break;
        case 4:
            html = `<h2>Крок 4: Підтвердження</h2>
            <div style="background:#f9f9f9; padding:30px; border-radius:var(--radius); margin:20px 0;">
                <p><strong>Кава:</strong> ${wizardData.coffee === 'auto' ? 'Вибір обжарщика' : PRODUCTS.find(p => p.id === wizardData.coffee)?.name}</p>
                <p><strong>Формат:</strong> ${wizardData.format === 'grain' ? 'Зерно' : 'Молотий (' + wizardData.grind + ')'}</p>
                <p><strong>Частота:</strong> ${wizardData.frequency === '2weeks' ? 'Раз на 2 тижні' : wizardData.frequency === 'month' ? 'Раз на місяць' : 'Раз на 2 місяці'}</p>
                <p style="font-size:1.5rem; color:var(--primary); font-weight:bold; margin-top:20px;">~380 ₴ / місяць</p>
            </div>`;
            break;
    }

    html += `<div style="display:flex; gap:15px; margin-top:30px; justify-content:center;">
        ${wizardStep > 1 ? '<button class="btn btn-outline" onclick="prevWizardStep()">Назад</button>' : ''}
        ${wizardStep < 4 ? '<button class="btn btn-primary" onclick="nextWizardStep()">Далі</button>' : '<button class="btn btn-primary" onclick="finishWizard()">Оформити підписку</button>'}
    </div>`;

    container.innerHTML = html;
}

function setWizard(key, val) { wizardData[key] = val; renderWizardStep(); }
function nextWizardStep() { if (wizardStep < 4) { wizardStep++; renderWizardStep(); } }
function prevWizardStep() { if (wizardStep > 1) { wizardStep--; renderWizardStep(); } }
function updateWizardIndicator() {
    document.querySelectorAll('.wizard-step').forEach((el, i) => {
        el.classList.remove('active', 'done');
        if (i + 1 === wizardStep) el.classList.add('active');
        if (i + 1 < wizardStep) el.classList.add('done');
    });
}
function finishWizard() {
    const sub = new Subscription({ plan: 'custom', coffee: wizardData.coffee, format: wizardData.format, grind: wizardData.grind, frequency: wizardData.frequency, quantity: 250 });
    sub.save();
    alert('Підписку оформлено! Перша доставка: ' + new Date(sub.nextDelivery).toLocaleDateString('uk-UA'));
    location.href = 'account.html';
}

/* --- DASHBOARD --- */
function initDashboard() {
    const sub = store.user.subscription;
    const widget = document.getElementById('sub-widget');
    if (!widget) return;

    if (!sub) {
        widget.innerHTML = '<p>У вас ще немає активної підписки.</p><a href="subscription.html" class="btn btn-primary">Оформити підписку</a>';
        return;
    }

    widget.innerHTML = `
        <div style="display:flex; justify-content:space-between; align-items:start; margin-bottom:20px;">
            <div>
                <span class="status-badge ${sub.status === 'active' ? 'status-active' : 'status-paused'}">${sub.status === 'active' ? 'Активна' : 'На паузі'}</span>
                <h3 style="margin-top:10px;">Наступна доставка: ${new Date(sub.nextDelivery).toLocaleDateString('uk-UA')}</h3>
            </div>
        </div>
        <div style="display:flex; gap:10px; flex-wrap:wrap;">
            <button class="btn btn-outline btn-sm" onclick="pauseSub()">⏸️ Пауза</button>
            <button class="btn btn-outline btn-sm" onclick="skipDelivery()">⏭️ Пропустити</button>
            <button class="btn btn-outline btn-sm" style="color:var(--error);" onclick="cancelSub()">❌ Скасувати</button>
        </div>
    `;
}


/* --- DASHBOARD --- */
function initDashboard() {
    const sub = store.user.subscription;

    // Render subscription widgets (both overview and detail tabs)
    renderSubWidget('sub-widget-overview', true);
    renderSubWidget('sub-widget-detail', false);

    // Render orders
    renderOrders();

    // Render delivery history
    renderDeliveryHistory();

    // Tab switching
    document.querySelectorAll('.dash-link[data-tab]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const tab = link.getAttribute('data-tab');
            switchTab(tab);
        });
    });

    // Settings form
    const settingsForm = document.getElementById('settings-form');
    if (settingsForm) {
        settingsForm.addEventListener('submit', (e) => {
            e.preventDefault();
            saveSettings();
        });
    }

    // Load user data
    loadUserData();
}

function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.dash-tab-content').forEach(tab => {
        tab.style.display = 'none';
    });

    // Show selected tab
    document.getElementById(`tab-${tabName}`).style.display = 'block';

    // Update active link
    document.querySelectorAll('.dash-link').forEach(link => {
        link.classList.remove('active');
    });
    document.querySelector(`.dash-link[data-tab="${tabName}"]`).classList.add('active');
}

function renderSubWidget(widgetId, isCompact) {
    const widget = document.getElementById(widgetId);
    if (!widget) return;

    const sub = store.user.subscription;

    if (!sub) {
        widget.innerHTML = isCompact
            ? '<p>Немає активної підписки. <a href="subscription.html" style="color:var(--primary);">Оформити →</a></p>'
            : '<p>У вас ще немає активної підписки.</p><a href="subscription.html" class="btn btn-primary">Оформити підписку</a>';
        return;
    }

    const nextDate = new Date(sub.nextDelivery).toLocaleDateString('uk-UA');
    const statusClass = sub.status === 'active' ? 'status-active' : 'status-paused';
    const statusText = sub.status === 'active' ? 'Активна' : 'На паузі';

    if (isCompact) {
        widget.innerHTML = `
            <h3 style="margin-bottom:15px;">Моя підписка</h3>
            <span class="status-badge ${statusClass}">${statusText}</span>
            <p style="margin-top:10px;"><strong>Наступна доставка:</strong> ${nextDate}</p>
            <a href="#" onclick="switchTab('subscription'); return false;" style="color:var(--primary); font-weight:600; margin-top:10px; display:inline-block;">Управління →</a>
        `;
    } else {
        widget.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:start; margin-bottom:20px;">
                <div>
                    <span class="status-badge ${statusClass}">${statusText}</span>
                    <h3 style="margin-top:15px;">Наступна доставка: ${nextDate}</h3>
                    <p style="margin-top:10px; color:#666;">
                        <strong>Кава:</strong> ${sub.coffee === 'auto' ? 'Вибір обжарщика' : 'Конкретний сорт'}<br>
                        <strong>Формат:</strong> ${sub.format === 'grain' ? 'Зерно' : 'Молотий'}<br>
                        <strong>Частота:</strong> ${sub.frequency === 'month' ? 'Раз на місяць' : sub.frequency === '2weeks' ? 'Раз на 2 тижні' : 'Раз на 2 місяці'}<br>
                        <strong>Вартість:</strong> ${sub.price}₴
                    </p>
                </div>
            </div>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
                ${sub.status === 'active'
                ? '<button class="btn btn-outline btn-sm" onclick="pauseSub()">⏸️ Пауза</button>'
                : '<button class="btn btn-outline btn-sm" onclick="resumeSub()">▶️ Відновити</button>'}
                <button class="btn btn-outline btn-sm" onclick="skipDelivery()">⏭️ Пропустити доставку</button>
                <button class="btn btn-outline btn-sm" onclick="changeSub()">✏️ Змінити</button>
                <button class="btn btn-outline btn-sm" style="color:var(--error);" onclick="cancelSub()">❌ Скасувати</button>
            </div>
        `;
    }
}

function renderOrders() {
    const container = document.getElementById('recent-orders');
    if (!container) return;

    // Mock orders for demo
    const orders = store.user.orders || [];

    if (orders.length === 0) {
        container.innerHTML = '<p style="color:#999;">Ще немає замовлень. <a href="shop.html" style="color:var(--primary);">Перейти до магазину →</a></p>';
        return;
    }

    container.innerHTML = orders.slice(0, 3).map(order => `
        <div style="padding:15px; border:1px solid #eee; border-radius:4px; margin-bottom:10px;">
            <div style="display:flex; justify-content:space-between;">
                <strong>${order.date}</strong>
                <span style="color:var(--primary);">${order.total}₴</span>
            </div>
            <p style="margin:5px 0 0; color:#666;">${order.items}</p>
        </div>
    `).join('');
}

function renderDeliveryHistory() {
    const container = document.getElementById('delivery-history');
    if (!container) return;

    const history = [
        { date: '15 лютого 2024', product: 'Сидамо, 500г', status: 'Доставлено' },
        { date: '15 січня 2024', product: 'Йіргачеффе, 500г', status: 'Доставлено' },
        { date: '15 грудня 2023', product: 'Харрар, 500г', status: 'Доставлено' }
    ];

    container.innerHTML = `
        <ul style="list-style:none; padding:0;">
            ${history.map(h => `
                <li style="padding:12px 0; border-bottom:1px solid #f0f0f0;">
                    <strong>${h.date}</strong> — ${h.product} 
                    <span style="color:var(--success); margin-left:10px;">✓ ${h.status}</span>
                </li>
            `).join('')}
        </ul>
    `;
}

function loadUserData() {
    // Load from localStorage
    const userName = document.getElementById('userName');
    const userEmail = document.getElementById('userEmail');
    const settingsName = document.getElementById('settings-name');
    const settingsEmail = document.getElementById('settings-email');

    if (store.user.name && store.user.name !== 'Guest') {
        if (userName) userName.textContent = store.user.name;
        if (settingsName) settingsName.value = store.user.name;
    }

    if (store.user.email) {
        if (userEmail) userEmail.textContent = store.user.email;
        if (settingsEmail) settingsEmail.value = store.user.email;
    }
}

function saveSettings() {
    const name = document.getElementById('settings-name').value;
    const email = document.getElementById('settings-email').value;
    const phone = document.getElementById('settings-phone').value;

    store.user.name = name;
    store.user.email = email;
    store.user.phone = phone;

    localStorage.setItem('ed_user', JSON.stringify(store.user));

    alert('Налаштування збережено!');
    loadUserData();
}

function pauseSub() {
    if (!store.user.subscription) return;
    store.user.subscription.status = 'paused';
    localStorage.setItem('ed_user', JSON.stringify(store.user));
    renderSubWidget('sub-widget-overview', true);
    renderSubWidget('sub-widget-detail', false);
    alert('Підписку поставлено на паузу. Доставки зупинені.');
}

function resumeSub() {
    if (!store.user.subscription) return;
    store.user.subscription.status = 'active';
    localStorage.setItem('ed_user', JSON.stringify(store.user));
    renderSubWidget('sub-widget-overview', true);
    renderSubWidget('sub-widget-detail', false);
    alert('Підписку відновлено!');
}

function skipDelivery() {
    if (!store.user.subscription) return;
    // Move next delivery forward
    const current = new Date(store.user.subscription.nextDelivery);
    current.setMonth(current.getMonth() + 1);
    store.user.subscription.nextDelivery = current.toISOString();
    localStorage.setItem('ed_user', JSON.stringify(store.user));
    renderSubWidget('sub-widget-overview', true);
    renderSubWidget('sub-widget-detail', false);
    alert('Наступну доставку пропущено. Нова дата: ' + current.toLocaleDateString('uk-UA'));
}

function changeSub() {
    window.location.href = 'subscription.html';
}

function cancelSub() {
    if (confirm('Точно скасувати підписку? Це можна буде відмінити.')) {
        store.user.subscription = null;
        localStorage.setItem('ed_user', JSON.stringify(store.user));
        renderSubWidget('sub-widget-overview', true);
        renderSubWidget('sub-widget-detail', false);
        alert('Підписку скасовано. Сподіваємось побачити вас знову!');
    }
}

// Make functions global for inline onclick handlers
window.switchTab = switchTab;
window.pauseSub = pauseSub;
window.resumeSub = resumeSub;
window.skipDelivery = skipDelivery;
window.changeSub = changeSub;
window.cancelSub = cancelSub;

/* --- NEWSLETTER --- */
function subscribeNewsletter(event) {
    event.preventDefault();
    const form = event.target;
    const email = form.querySelector('input[type="email"]').value;

    // Simulate newsletter subscription
    alert(`Дякуємо! Email ${email} додано до розсилки. Скоро отримаєте першу порцію кавових новин!`);
    form.reset();
}

window.subscribeNewsletter = subscribeNewsletter;
/* --- QUIZ ENGINE (PHASE 3) --- */
let currentQuestionIndex = 0;
const userAnswers = {};

function openQuiz() {
    // Create Modal if not exists
    if (!document.getElementById('quiz-modal')) {
        const modalHTML = `
        <div id="quiz-modal" class="modal-overlay" style="display:flex;">
            <div class="quiz-card">
                <button class="quiz-close" onclick="closeQuiz()">&times;</button>
                <div id="quiz-content">
                    <!-- Dynamic Content -->
                </div>
            </div>
        </div>`;
        document.body.insertAdjacentHTML('beforeend', modalHTML);
    } else {
        document.getElementById('quiz-modal').style.display = 'flex';
    }
    currentQuestionIndex = 0;
    renderQuizStep();
}

function closeQuiz() {
    const m = document.getElementById('quiz-modal');
    if (m) m.style.display = 'none';
}

function renderQuizStep() {
    const container = document.getElementById('quiz-content');
    const q = QUIZ_QUESTIONS[currentQuestionIndex];

    if (!q) {
        showQuizResult();
        return;
    }

    let html = `
        <div class="quiz-step-indicator">Питання ${currentQuestionIndex + 1} з ${QUIZ_QUESTIONS.length}</div>
        <h3 class="quiz-question">${q.text}</h3>
        <div class="quiz-options">
    `;

    q.options.forEach(opt => {
        html += `
            <div class="quiz-option" onclick="handleQuizAnswer('${q.id}', '${opt.value}')">
                <i class="fas ${opt.icon}"></i>
                <span>${opt.text}</span>
            </div>
        `;
    });

    html += `</div>`;
    container.innerHTML = html;
}

function handleQuizAnswer(qId, value) {
    userAnswers[qId] = value;
    currentQuestionIndex++;
    // Add small delay for animation effect
    setTimeout(renderQuizStep, 300);
}

function showQuizResult() {
    const container = document.getElementById('quiz-content');

    // Simple Logic Recommendation (Mock)
    let recommendedProduct = PRODUCTS[0]; // Default Sidamo
    if (userAnswers[2] === 'fruity') recommendedProduct = PRODUCTS[2]; // Guji
    if (userAnswers[2] === 'floral') recommendedProduct = PRODUCTS[1]; // Yirga
    if (userAnswers[1] === 'espresso') recommendedProduct = PRODUCTS[3]; // Blend

    const html = `
        <div class="quiz-result">
            <div class="result-badge">98% Сумісність</div>
            <h2>Ми знайшли ваш ідеал!</h2>
            <img src="${recommendedProduct.image}" class="result-img" alt="${recommendedProduct.name}">
            <h3>${recommendedProduct.name}</h3>
            <p>${recommendedProduct.desc}</p>
            <div class="result-actions">
                <button class="btn btn-primary" onclick="addToCart(${recommendedProduct.id}); closeQuiz();">Спробувати зі знижкою 20%</button>
                <button class="btn btn-secondary" onclick="closeQuiz()">Зберегти в профіль</button>
            </div>
        </div>
    `;
    container.innerHTML = html;
}

/* --- TOAST NOTIFICATIONS --- */
function showToast(message) {
    // Remove existing
    const existing = document.querySelector('.toast-notification');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.className = 'toast-notification';
    toast.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
    document.body.appendChild(toast);

    // Animate in
    setTimeout(() => toast.classList.add('show'), 10);

    // Remove
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Override addToCart to use Toast
const originalAddToCart = addToCart;
addToCart = function (id) {
    const p = PRODUCTS.find(x => x.id === id);
    if (p) {
        store.cart.push({ ...p, cartId: Date.now(), qty: 1 });
        renderCart();
        showToast(`<b>${p.name}</b> додано до кошика!`);
        // Optional: openDrawer(); // Maybe don't open drawer, just show toast for better flow? 
        // User asked for "Notification", implies less intrusive than drawer opening.
    }
}

/* ========================================
   LANGUAGE SWITCHER - FULL SITE TRANSLATION
   ======================================== */
const TRANSLATIONS = {
    uk: {
        // Navigation
        catalog: 'Каталог',
        subscription: 'Підписка',
        certificates: 'Сертифікати',
        stories: 'Історії',
        about: 'Про нас',
        test: 'Тест',
        // Search
        search: 'Пошук кави...',
        // Cart
        cart: 'Ваш кошик',
        cartEmpty: 'Ваша чашка поки що порожня...',
        goToCatalog: 'Перейти до каталогу',
        total: 'Разом:',
        checkout: 'Оформити замовлення',
        freeShipping: 'До безкоштовної доставки:',
        freeShippingDone: 'Безкоштовна доставка!',
        addToCart: 'Додати',
        // Product
        weight: 'Вага',
        grind: 'Помол',
        beans: 'Зерно',
        espresso: 'Еспресо',
        filter: 'Фільтр',
        turka: 'Турка',
        // Top bar
        phone: '+380 (50) 123-45-67',
        workHours: 'Пн-Пт: 9:00-18:00',
        promoFreeShipping: 'безкоштовна доставка від 500₴',
        promoSubscription: 'Підписка: -10% на кожну доставку',
        promoFresh: 'Свіжа обсмажка до 3 днів',
        // Footer
        footerShop: 'Магазин',
        footerSupport: 'Підтримка',
        footerContacts: 'Контакти',
        footerNewsletter: 'Підписка на новини',
        footerNewsletterDesc: 'Отримуйте акції, новинки та поради щодо заварювання',
        footerSubscribe: 'Підписатись',
        fullCatalog: 'Весь каталог',
        coffeeSubscription: 'Підписка на каву',
        giftCertificates: 'Сертифікати',
        b2bSolutions: 'B2B рішення',
        personalAccount: 'Особистий кабінет',
        deliveryPayment: 'Доставка та оплата',
        returnExchange: 'Повернення та обмін',
        faq: 'Часті питання',
        contacts: 'Контакти',
        aboutUs: 'Про нас',
        city: 'Одеса, Україна',
        // Trust badges
        return14days: '14 днів',
        returnLabel: 'повернення',
        specialty100: '100% Specialty',
        qualityLabel: 'якість зерна',
        freeDelivery: 'Безкоштовна',
        freeDeliveryLabel: 'доставка від 500₴',
        freshRoast: 'Свіжа обсмажка',
        freshRoastLabel: 'до 3 днів',
        // Payment
        paymentMethods: 'Способи оплати:',
        // Footer bottom
        allRightsReserved: 'Всі права захищені.',
        privacyPolicy: 'Політика конфіденційності',
        returnTerms: 'Умови повернення',
        publicOffer: 'Публічна оферта',
        // Common
        orderNow: 'Замовити',
        learnMore: 'Детальніше',
        yourEmail: 'Ваш email'
    },
    ru: {
        // Navigation
        catalog: 'Каталог',
        subscription: 'Подписка',
        certificates: 'Сертификаты',
        stories: 'Истории',
        about: 'О нас',
        test: 'Тест',
        // Search
        search: 'Поиск кофе...',
        // Cart
        cart: 'Ваша корзина',
        cartEmpty: 'Ваша чашка пока пустая...',
        goToCatalog: 'Перейти в каталог',
        total: 'Итого:',
        checkout: 'Оформить заказ',
        freeShipping: 'До бесплатной доставки:',
        freeShippingDone: 'Бесплатная доставка!',
        addToCart: 'Добавить',
        // Product
        weight: 'Вес',
        grind: 'Помол',
        beans: 'Зерно',
        espresso: 'Эспрессо',
        filter: 'Фильтр',
        turka: 'Турка',
        // Top bar
        phone: '+380 (50) 123-45-67',
        workHours: 'Пн-Пт: 9:00-18:00',
        promoFreeShipping: 'бесплатная доставка от 500₴',
        promoSubscription: 'Подписка: -10% на каждую доставку',
        promoFresh: 'Свежая обжарка до 3 дней',
        // Footer
        footerShop: 'Магазин',
        footerSupport: 'Поддержка',
        footerContacts: 'Контакты',
        footerNewsletter: 'Подписка на новости',
        footerNewsletterDesc: 'Получайте акции, новинки и советы по завариванию',
        footerSubscribe: 'Подписаться',
        fullCatalog: 'Весь каталог',
        coffeeSubscription: 'Подписка на кофе',
        giftCertificates: 'Сертификаты',
        b2bSolutions: 'B2B решения',
        personalAccount: 'Личный кабинет',
        deliveryPayment: 'Доставка и оплата',
        returnExchange: 'Возврат и обмен',
        faq: 'Частые вопросы',
        contacts: 'Контакты',
        aboutUs: 'О нас',
        city: 'Одесса, Украина',
        // Trust badges
        return14days: '14 дней',
        returnLabel: 'возврат',
        specialty100: '100% Specialty',
        qualityLabel: 'качество зерна',
        freeDelivery: 'Бесплатная',
        freeDeliveryLabel: 'доставка от 500₴',
        freshRoast: 'Свежая обжарка',
        freshRoastLabel: 'до 3 дней',
        // Payment
        paymentMethods: 'Способы оплаты:',
        // Footer bottom
        allRightsReserved: 'Все права защищены.',
        privacyPolicy: 'Политика конфиденциальности',
        returnTerms: 'Условия возврата',
        publicOffer: 'Публичная оферта',
        // Common
        orderNow: 'Заказать',
        learnMore: 'Подробнее',
        yourEmail: 'Ваш email'
    },
    en: {
        // Navigation
        catalog: 'Catalog',
        subscription: 'Subscription',
        certificates: 'Gift Cards',
        stories: 'Stories',
        about: 'About Us',
        test: 'Quiz',
        // Search
        search: 'Search coffee...',
        // Cart
        cart: 'Your Cart',
        cartEmpty: 'Your cup is empty...',
        goToCatalog: 'Go to Catalog',
        total: 'Total:',
        checkout: 'Checkout',
        freeShipping: 'Until free shipping:',
        freeShippingDone: 'Free shipping!',
        addToCart: 'Add to Cart',
        // Product
        weight: 'Weight',
        grind: 'Grind',
        beans: 'Beans',
        espresso: 'Espresso',
        filter: 'Filter',
        turka: 'Turkish',
        // Top bar
        phone: '+380 (50) 123-45-67',
        workHours: 'Mon-Fri: 9:00-18:00',
        promoFreeShipping: 'free shipping from 500₴',
        promoSubscription: 'Subscription: -10% on each delivery',
        promoFresh: 'Fresh roast up to 3 days',
        // Footer
        footerShop: 'Shop',
        footerSupport: 'Support',
        footerContacts: 'Contacts',
        footerNewsletter: 'Newsletter',
        footerNewsletterDesc: 'Get deals, news and brewing tips',
        footerSubscribe: 'Subscribe',
        fullCatalog: 'Full Catalog',
        coffeeSubscription: 'Coffee Subscription',
        giftCertificates: 'Gift Cards',
        b2bSolutions: 'B2B Solutions',
        personalAccount: 'My Account',
        deliveryPayment: 'Delivery & Payment',
        returnExchange: 'Returns & Exchanges',
        faq: 'FAQ',
        contacts: 'Contacts',
        aboutUs: 'About Us',
        city: 'Odesa, Ukraine',
        // Trust badges
        return14days: '14 days',
        returnLabel: 'returns',
        specialty100: '100% Specialty',
        qualityLabel: 'bean quality',
        freeDelivery: 'Free',
        freeDeliveryLabel: 'shipping from 500₴',
        freshRoast: 'Fresh Roast',
        freshRoastLabel: 'up to 3 days',
        // Payment
        paymentMethods: 'Payment methods:',
        // Footer bottom
        allRightsReserved: 'All rights reserved.',
        privacyPolicy: 'Privacy Policy',
        returnTerms: 'Return Policy',
        publicOffer: 'Terms of Service',
        // Common
        orderNow: 'Order Now',
        learnMore: 'Learn More',
        yourEmail: 'Your email'
    }
};

function switchLang(lang) {
    // Prevent default action
    event && event.preventDefault();

    // Save to localStorage
    localStorage.setItem('ed_lang', lang);

    // Update active state on lang switches
    document.querySelectorAll('.lang-switch').forEach(el => {
        el.classList.remove('active');
        const txt = el.textContent.trim().toUpperCase();
        if ((lang === 'uk' && txt === 'UA') || (lang === 'ru' && txt === 'RU') || (lang === 'en' && txt === 'EN')) {
            el.classList.add('active');
        }
    });

    // Apply translations
    applyTranslations(lang);

    // Show toast
    const messages = {
        uk: 'Мова змінена на українську',
        ru: 'Язык изменён на русский',
        en: 'Language changed to English'
    };
    if (typeof showToast === 'function') {
        showToast(messages[lang] || messages.uk);
    }
}

function applyTranslations(lang) {
    const t = TRANSLATIONS[lang] || TRANSLATIONS.uk;

    // Update all elements with data-translate attribute
    document.querySelectorAll('[data-translate]').forEach(el => {
        const key = el.getAttribute('data-translate');
        if (t[key]) {
            el.textContent = t[key];
        }
    });

    // Update nav links by href
    document.querySelectorAll('.nav-desktop .nav-link').forEach(link => {
        const href = link.getAttribute('href');
        if (href && href.includes('shop.html')) link.textContent = t.catalog;
        if (href && href.includes('subscription.html')) link.textContent = t.subscription;
        if (href && href.includes('gift-certificates.html')) link.textContent = t.certificates;
        if (href && href.includes('blog.html')) link.textContent = t.stories;
        if (href && href.includes('about.html')) link.textContent = t.about;
        if (href && href.includes('quiz.html')) link.textContent = t.test;
    });

    // Update search placeholder 
    const searchInput = document.getElementById('search-input');
    if (searchInput) searchInput.placeholder = t.search;

    // Update drawer header
    // Update drawer header - REMOVED to allow i18n.js to handle it via data-i18n
    // const drawerHeader = document.querySelector('.drawer-header h3');
    // if (drawerHeader) {
    //    drawerHeader.innerHTML = `<i class="fas fa-shopping-bag" style="margin-right:10px; color:var(--primary);"></i> ${t.cart}`;
    // }

    // Update footer section titles
    document.querySelectorAll('.footer-col h4').forEach((h4, index) => {
        const text = h4.textContent.trim().toLowerCase();
        if (text.includes('магазин') || text.includes('shop')) h4.textContent = t.footerShop;
        if (text.includes('підтримка') || text.includes('поддержка') || text.includes('support')) h4.textContent = t.footerSupport;
        if (text.includes('контакт') || text.includes('contact')) h4.textContent = t.footerContacts;
        if (text.includes('підписка на новини') || text.includes('подписка на новости') || text.includes('newsletter')) h4.textContent = t.footerNewsletter;
    });

    // Update footer links
    document.querySelectorAll('.footer-links a').forEach(link => {
        const href = link.getAttribute('href');
        if (href) {
            if (href.includes('shop.html')) link.textContent = t.fullCatalog;
            if (href.includes('subscription.html')) link.textContent = t.coffeeSubscription;
            if (href.includes('gift-certificates.html')) link.textContent = t.giftCertificates;
            if (href.includes('b2b.html')) link.textContent = t.b2bSolutions;
            if (href.includes('account.html')) link.textContent = t.personalAccount;
            if (href.includes('delivery.html')) link.textContent = t.deliveryPayment;
            if (href.includes('return.html')) link.textContent = t.returnExchange;
            if (href.includes('faq.html')) link.textContent = t.faq;
            if (href.includes('contacts.html')) link.textContent = t.contacts;
            if (href.includes('about.html')) link.textContent = t.aboutUs;
        }
    });

    // Update trust badges
    document.querySelectorAll('.trust-badge').forEach(badge => {
        const icon = badge.querySelector('i');
        const strong = badge.querySelector('strong');
        const span = badge.querySelector('span');
        if (icon && strong && span) {
            const iconClass = icon.className;
            if (iconClass.includes('shield')) {
                strong.textContent = t.return14days;
                span.textContent = t.returnLabel;
            }
            if (iconClass.includes('coffee')) {
                strong.textContent = t.specialty100;
                span.textContent = t.qualityLabel;
            }
            if (iconClass.includes('shipping')) {
                strong.textContent = t.freeDelivery;
                span.textContent = t.freeDeliveryLabel;
            }
            if (iconClass.includes('fire')) {
                strong.textContent = t.freshRoast;
                span.textContent = t.freshRoastLabel;
            }
        }
    });

    // Update newsletter form
    document.querySelectorAll('.newsletter-form input[type="email"]').forEach(input => {
        input.placeholder = t.yourEmail;
    });
    document.querySelectorAll('.newsletter-form button, .btn-newsletter').forEach(btn => {
        btn.textContent = t.footerSubscribe;
    });

    // Update footer bottom links
    document.querySelectorAll('.footer-bottom-right a').forEach(link => {
        const href = link.getAttribute('href');
        if (href) {
            if (href.includes('privacy')) link.textContent = t.privacyPolicy;
            if (href.includes('return')) link.textContent = t.returnTerms;
            if (href === '#' || href.includes('offer')) link.textContent = t.publicOffer;
        }
    });
}

// Initialize language on page load
document.addEventListener('DOMContentLoaded', () => {
    const savedLang = localStorage.getItem('ed_lang') || 'uk';

    // Update active state on lang switches
    document.querySelectorAll('.lang-switch').forEach(el => {
        el.classList.remove('active');
        const langText = el.textContent.trim().toUpperCase();
        if ((savedLang === 'uk' && langText === 'UA') ||
            (savedLang === 'ru' && langText === 'RU') ||
            (savedLang === 'en' && langText === 'EN')) {
            el.classList.add('active');
        }
    });

    // Always apply translations on load
    applyTranslations(savedLang);
});

// Make switchLang globally available
window.switchLang = switchLang;

