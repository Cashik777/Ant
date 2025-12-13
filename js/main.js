/* ===== ETHIODIRECT CORE ENGINE (v3.0) ===== */

/* --- STORE & STATE MANAGEMENT --- */
const store = {
    cart: JSON.parse(localStorage.getItem('ant_cart')) || [],
    user: JSON.parse(localStorage.getItem('ant_user')) || {
        name: 'Guest',
        subscription: null
    },
    currency: '₴'
};

/* --- EVENTS & INIT --- */
document.addEventListener('DOMContentLoaded', () => {
    initUI();
    initPageLogic();
    renderCart();

    window.addEventListener('beforeunload', () => {
        localStorage.setItem('ant_cart', JSON.stringify(store.cart));
        localStorage.setItem('ant_user', JSON.stringify(store.user));
    });
});

function initUI() {
    const header = document.querySelector('.header');
    if (header) {
        window.addEventListener('scroll', () => {
            header.classList.toggle('scrolled', window.scrollY > 20);
        });
    }
    setupDrawer();
}

function initPageLogic() {
    const path = window.location.pathname;

    if (path.endsWith('index.html') || path.endsWith('/') || path === '') {
        renderFeatured();
    }
    if (path.includes('shop.html')) {
        renderShop();
    }
    if (path.includes('product.html')) {
        initProductPage();
    }
}

/* --- SUBSCRIPTION ENGINE --- */
const SubEngine = {
    frequencies: { 'weekly': 7, 'biweekly': 14, 'monthly': 30 },

    create(productId, frequency, grind) {
        const today = new Date();
        const nextDate = new Date(today);
        nextDate.setDate(today.getDate() + this.frequencies[frequency]);

        store.user.subscription = {
            id: 'sub_' + Date.now(),
            productId, frequency, grind,
            startDate: today.toISOString(),
            nextDate: nextDate.toISOString(),
            status: 'active'
        };
        this.save();
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
            const next = new Date(store.user.subscription.nextDate);
            next.setDate(next.getDate() + this.frequencies[store.user.subscription.frequency]);
            store.user.subscription.nextDate = next.toISOString();
            this.save();
        }
    },

    save() {
        localStorage.setItem('ant_user', JSON.stringify(store.user));
    }
};

/* --- PAGE RENDERERS --- */
function renderFeatured() {
    const grid = document.getElementById('featured-grid');
    if (!grid || typeof PRODUCTS === 'undefined') return;

    grid.innerHTML = '';
    PRODUCTS.slice(0, 3).forEach(p => {
        grid.innerHTML += createProductCard(p);
    });
}

function renderShop() {
    const grid = document.getElementById('products-grid');
    if (!grid || typeof PRODUCTS === 'undefined') return;

    grid.innerHTML = '';
    PRODUCTS.forEach(p => {
        grid.innerHTML += createProductCard(p);
    });

    // Filter buttons
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            // Filter logic placeholder
        });
    });
}

function createProductCard(p) {
    return `
    <div class="product-card">
        <div class="p-img-wrap">
            <a href="product.html?id=${p.id}">
                <img src="${p.image}" alt="${p.name}">
            </a>
        </div>
        <div class="p-info">
            <div class="p-meta">${p.tags.join(' • ')}</div>
            <h3><a href="product.html?id=${p.id}">${p.name}</a></h3>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:15px;">
                <span class="p-price">${p.price} ${store.currency}</span>
                <button class="btn btn-primary" style="padding:10px 18px; font-size:0.85rem;" onclick="quickAdd(${p.id})">
                    <i class="fas fa-plus"></i>
                </button>
            </div>
        </div>
    </div>
    `;
}

function initProductPage() {
    const params = new URLSearchParams(window.location.search);
    const id = parseInt(params.get('id'));
    if (!id || typeof PRODUCTS === 'undefined') return;

    const product = PRODUCTS.find(p => p.id === id);
    if (!product) return;

    document.getElementById('p-title').innerText = product.name;
    document.getElementById('p-price').innerText = product.price + ' ' + store.currency;
    document.getElementById('p-desc').innerText = product.desc;
    document.getElementById('p-main-img').src = product.image;
    document.title = product.name + ' — EthioDirect';

    document.getElementById('add-to-cart-btn').onclick = () => {
        addToCart(product);
    };
}

function quickAdd(id) {
    if (typeof PRODUCTS === 'undefined') return;
    const product = PRODUCTS.find(p => p.id === id);
    if (product) addToCart(product);
}

/* --- CART FUNCTIONS --- */
function addToCart(product, isSub = false) {
    store.cart.push({
        ...product,
        type: isSub ? 'subscription' : 'one-time',
        cartId: Date.now()
    });
    renderCart();
    openDrawer();
}

function removeFromCart(cartId) {
    store.cart = store.cart.filter(i => i.cartId !== cartId);
    renderCart();
}

function renderCart() {
    const list = document.getElementById('cart-list');
    const totalEl = document.getElementById('cart-total');
    const countEl = document.querySelector('.cart-count');

    if (countEl) countEl.innerText = store.cart.length;

    if (list) {
        if (store.cart.length === 0) {
            list.innerHTML = '<p class="text-muted text-center">Корзина пуста</p>';
        } else {
            list.innerHTML = '';
            let total = 0;

            store.cart.forEach(item => {
                total += item.price;
                list.innerHTML += `
                    <div class="cart-item" style="display:flex; gap:15px; margin-bottom:20px; align-items:center;">
                        <img src="${item.image}" style="width:60px; height:60px; object-fit:cover; border-radius:8px;">
                        <div style="flex:1;">
                            <h4 style="font-size:0.95rem; margin-bottom:4px;">${item.name}</h4>
                            <p style="margin:0; font-size:0.9rem;">${item.price} ${store.currency}</p>
                        </div>
                        <button onclick="removeFromCart(${item.cartId})" style="background:none; border:none; color:#999; cursor:pointer; font-size:1.2rem;">&times;</button>
                    </div>
                `;
            });

            if (totalEl) totalEl.innerText = total + ' ' + store.currency;
        }
    }
}

/* --- DRAWER UI --- */
function setupDrawer() {
    const triggers = document.querySelectorAll('.cart-trigger');
    const closers = document.querySelectorAll('.cart-close, .overlay');

    triggers.forEach(t => t.addEventListener('click', openDrawer));
    closers.forEach(c => c.addEventListener('click', closeDrawer));
}

function openDrawer() {
    document.querySelector('.drawer')?.classList.add('open');
    document.querySelector('.overlay')?.classList.add('open');
}

function closeDrawer() {
    document.querySelector('.drawer')?.classList.remove('open');
    document.querySelector('.overlay')?.classList.remove('open');
}

