/* ===== ETHIODIRECT CORE ENGINE (v3.0) ===== */

/* --- STORE & STATE MANAGEMENT --- */
const store = {
    cart: JSON.parse(localStorage.getItem('ant_cart')) || [],
    user: JSON.parse(localStorage.getItem('ant_user')) || {
        name: 'Guest',
        subscription: null // { productId, frequency, nextDate, status }
    },
    currency: '₴'
};

/* --- EVENTS & INIT --- */
document.addEventListener('DOMContentLoaded', () => {
    initUI();
    initLogic();
    renderCart();

    // Auto-save logic
    window.addEventListener('beforeunload', () => {
        localStorage.setItem('ant_cart', JSON.stringify(store.cart));
        localStorage.setItem('ant_user', JSON.stringify(store.user));
    });
});

function initUI() {
    // Scroll header effect
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        header.classList.toggle('scrolled', window.scrollY > 20);
    });

    // Mobile nav
    // ... (Standard mobile nav logic)

    // Components
    setupDrawer();
}

function initLogic() {
    // Route matching
    const path = window.location.pathname;

    if (path.includes('quiz')) initQuiz();
    if (path.includes('subscription')) initSubWizard();
    if (path.includes('account')) initDashboard();
}

/* --- SUBSCRIPTION ENGINE --- */
const SubEngine = {
    frequencies: {
        'weekly': 7,
        'biweekly': 14,
        'monthly': 30
    },

    create(productId, frequency, grind) {
        const today = new Date();
        const nextDate = new Date(today);
        nextDate.setDate(today.getDate() + this.frequencies[frequency]);

        const sub = {
            id: 'sub_' + Date.now(),
            productId,
            frequency,
            grind,
            startDate: today.toISOString(),
            nextDate: nextDate.toISOString(),
            status: 'active'
        };

        store.user.subscription = sub;
        this.save();
        return sub;
    },

    pause() {
        if (store.user.subscription) {
            store.user.subscription.status = 'paused';
            this.save();
        }
    },

    resume() {
        if (store.user.subscription) {
            store.user.subscription.status = 'active';
            this.save();
        }
    },

    skip() {
        if (store.user.subscription) {
            const currentNext = new Date(store.user.subscription.nextDate);
            currentNext.setDate(currentNext.getDate() + this.frequencies[store.user.subscription.frequency]);
            store.user.subscription.nextDate = currentNext.toISOString();
            this.save();
        }
    },

    save() {
        localStorage.setItem('ant_user', JSON.stringify(store.user));
        // In real app: API call sync
    }
};

/* --- QUIZ MODULE (COFFEE MATCHER) --- */
function initQuiz() {
    const questions = [
        {
            id: q1,
            text: "Как вы готовите кофе?",
            options: [
                { text: "Эспрессо машина", points: { espresso: 5, filter: 0 } },
                { text: "Фильтр / Воронка", points: { espresso: 0, filter: 5 } },
                { text: "Турка / Гейзер", points: { espresso: 3, filter: 2 } }
            ]
        },
        {
            id: q2,
            text: "Что важнее во вкусе?",
            options: [
                { text: "Кислинка и фрукты", points: { acidic: 5, bitter: 0 } },
                { text: "Шоколад и орехи", points: { acidic: 0, bitter: 5 } },
                { text: "Баланс", points: { acidic: 2, bitter: 2 } }
            ]
        }
    ];
    // Simple logic placeholder
    console.log('Quiz initialized');
}

/* --- CART FUNCTIONS --- */
function addToCart(product, isSub = false) {
    store.cart.push({
        ...product,
        type: isSub ? 'subscription' : 'one-time',
        id: Date.now() // Unique item ID
    });
    renderCart();
    openDrawer();
}

function removeFromCart(id) {
    store.cart = store.cart.filter(i => i.id !== id);
    renderCart();
}

function renderCart() {
    const list = document.getElementById('cart-list');
    const totalEl = document.getElementById('cart-total');
    const countEl = document.querySelector('.cart-count');

    if (countEl) countEl.innerText = store.cart.length;

    if (list) {
        list.innerHTML = '';
        let total = 0;

        store.cart.forEach(item => {
            total += item.price;
            list.innerHTML += `
                <div class="cart-item" style="display:flex; gap:15px; margin-bottom:20px;">
                    <img src="${item.image}" style="width:60px; height:60px; object-fit:cover; border-radius:4px;">
                    <div>
                        <h4>${item.name}</h4>
                        <p>${item.price} ${store.currency}</p>
                        ${item.type === 'subscription' ? '<span style="font-size:0.8rem; color:var(--accent);">Подписка (-10%)</span>' : ''}
                    </div>
                </div>
            `;
        });

        if (totalEl) totalEl.innerText = total + ' ' + store.currency;
    }
}

/* --- DRAWER UI --- */
function setupDrawer() {
    const drawer = document.querySelector('.drawer');
    const overlay = document.querySelector('.overlay');
    const triggers = document.querySelectorAll('.cart-trigger');
    const closers = document.querySelectorAll('.cart-close, .overlay');

    triggers.forEach(t => t.addEventListener('click', openDrawer));
    closers.forEach(c => c.addEventListener('click', closeDrawer));
}

function openDrawer() {
    document.querySelector('.drawer').classList.add('open');
    document.querySelector('.overlay').classList.add('open');
}

function closeDrawer() {
    document.querySelector('.drawer').classList.remove('open');
    document.querySelector('.overlay').classList.remove('open');
}
