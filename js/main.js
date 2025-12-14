/* ===== ETHIODIRECT CORE ENGINE v4.0 ===== */

/* --- DATA --- */
const PRODUCTS = [
    { id: 1, name: 'Сидамо', region: 'Sidamo', desc: 'Классический эфиопский. Шоколад, орехи, мягкая кислинка.', price: 240, weight: 250, roast: 'medium', taste: ['🍫', '🥜'], method: ['espresso', 'turka'], image: 'https://images.unsplash.com/photo-1587734195507-6b7c8b6a3e5a?auto=format&fit=crop&w=600&q=80' },
    { id: 2, name: 'Йіргачеффе', region: 'Yirgacheffe', desc: 'Цветочный, цитрусовый. Идеален для фильтра.', price: 280, weight: 250, roast: 'light', taste: ['🌸', '🍋'], method: ['filter'], image: 'https://images.unsplash.com/photo-1510707577719-ae7c9b788690?auto=format&fit=crop&w=600&q=80' },
    { id: 3, name: 'Гуджі Натурал', region: 'Guji', desc: 'Ягодний вибух. Полуниця, манго, мед.', price: 320, weight: 250, roast: 'light', taste: ['🍓', '🥭'], method: ['filter'], image: 'https://images.unsplash.com/photo-1621262974917-76b4a39f60af?auto=format&fit=crop&w=600&q=80' },
    { id: 4, name: 'Еспресо Бленд', region: 'Blend', desc: 'Стабільний смак для еспресо. Шоколад, карамель.', price: 220, weight: 250, roast: 'dark', taste: ['🍫', '🍬'], method: ['espresso'], image: 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=600&q=80' },
    { id: 5, name: 'Лімму', region: 'Limmu', desc: 'Збалансований. Зелене яблуко, карамель.', price: 260, weight: 250, roast: 'medium', taste: ['🍏', '🍬'], method: ['espresso', 'filter'], image: 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=600&q=80' },
    { id: 6, name: 'Харар', region: 'Harrar', desc: 'Дикий. Чорниця, вино, спеції.', price: 340, weight: 250, roast: 'light', taste: ['🫐', '🍷'], method: ['filter'], image: 'https://images.unsplash.com/photo-1442512595331-e89e7385a861?auto=format&fit=crop&w=600&q=80' }
];

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
    initUI();
    initPageLogic();
    renderCart();

    window.addEventListener('beforeunload', () => {
        localStorage.setItem('ed_cart', JSON.stringify(store.cart));
        localStorage.setItem('ed_user', JSON.stringify(store.user));
    });
});

function initUI() {
    setupDrawer();
    const header = document.querySelector('.header');
    if (header) {
        window.addEventListener('scroll', () => {
            header.style.boxShadow = window.scrollY > 20 ? '0 4px 20px rgba(0,0,0,0.1)' : 'none';
        });
    }
}

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

function renderShop(filter = 'all') {
    const grid = document.getElementById('products-grid');
    if (!grid) return;
    grid.innerHTML = '';
    let filtered = PRODUCTS;
    if (filter !== 'all') {
        filtered = PRODUCTS.filter(p => p.roast === filter || p.method.includes(filter));
    }
    filtered.forEach(p => grid.innerHTML += createProductCard(p));
}

function createProductCard(p) {
    return `
    <div class="product-card">
        <a href="product.html?id=${p.id}"><img src="${p.image}" alt="${p.name}"></a>
        <div class="p-body">
            <div class="p-region">${p.region}</div>
            <h3><a href="product.html?id=${p.id}">${p.name}</a></h3>
            <div class="p-taste">${p.taste.join(' ')}</div>
            <div class="p-price">${p.price} ${store.currency} / ${p.weight}г</div>
            <div class="p-actions">
                <button class="btn btn-primary btn-sm" onclick="addToCart(${p.id})">Купити</button>
                <button class="btn btn-outline btn-sm" onclick="location.href='subscription.html?product=${p.id}'">Підписка -10%</button>
            </div>
        </div>
    </div>`;
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
    store.cart.push({ ...p, cartId: Date.now(), qty: 1 });
    renderCart();
    openDrawer();
}

function removeFromCart(cartId) {
    store.cart = store.cart.filter(i => i.cartId !== cartId);
    renderCart();
}

function renderCart() {
    const list = document.getElementById('cart-list');
    const total = document.getElementById('cart-total');
    const count = document.querySelector('.cart-count');

    if (count) count.innerText = store.cart.length;
    if (!list) return;

    if (store.cart.length === 0) {
        list.innerHTML = '<p class="text-center" style="color:#999;">Кошик порожній</p>';
        if (total) total.innerText = '0 ' + store.currency;
        return;
    }

    let sum = 0;
    list.innerHTML = '';
    store.cart.forEach(item => {
        sum += item.price;
        list.innerHTML += `
        <div class="cart-item">
            <img src="${item.image}" alt="${item.name}">
            <div style="flex:1;">
                <h4 style="font-size:0.95rem; margin-bottom:4px;">${item.name}</h4>
                <p style="margin:0; font-size:0.9rem; color:var(--primary);">${item.price} ${store.currency}</p>
            </div>
            <button onclick="removeFromCart(${item.cartId})" style="background:none; border:none; color:#999; cursor:pointer; font-size:1.3rem;">&times;</button>
        </div>`;
    });
    if (total) total.innerText = sum + ' ' + store.currency;
}

/* --- DRAWER --- */
function setupDrawer() {
    document.querySelectorAll('.cart-trigger').forEach(t => t.addEventListener('click', openDrawer));
    document.querySelectorAll('.cart-close, .overlay').forEach(c => c.addEventListener('click', closeDrawer));
}
function openDrawer() {
    document.querySelector('.drawer')?.classList.add('open');
    document.querySelector('.overlay')?.classList.add('open');
}
function closeDrawer() {
    document.querySelector('.drawer')?.classList.remove('open');
    document.querySelector('.overlay')?.classList.remove('open');
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
    const recommended = PRODUCTS[Math.floor(Math.random() * PRODUCTS.length)];
    const container = document.getElementById('quiz-content');
    container.innerHTML = `
        <div class="text-center" style="background:white; padding:50px; border-radius:var(--radius);">
            <i class="fas fa-check-circle" style="font-size:4rem; color:var(--success); margin-bottom:20px;"></i>
            <h2>Ваша ідеальна кава:</h2>
            <h1 style="color:var(--primary); margin:20px 0;">${recommended.name}</h1>
            <p>${recommended.desc}</p>
            <div style="margin-top:30px; display:flex; gap:15px; justify-content:center;">
                <button class="btn btn-primary" onclick="addToCart(${recommended.id})">Додати в кошик</button>
                <a href="subscription.html?product=${recommended.id}" class="btn btn-outline">Оформити підписку</a>
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
