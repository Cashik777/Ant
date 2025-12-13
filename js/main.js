/* ===== MAIN LOGIC v2.0 ===== */

// State
const state = {
    cart: JSON.parse(localStorage.getItem('cart')) || [],
    currency: '₴'
};

document.addEventListener('DOMContentLoaded', () => {
    initComponents();
    initPageLogic();
    updateCartUI();
    initScrollAnimations();
});

/* --- INITIALIZATION --- */
function initComponents() {
    // Header Scroll Effect
    const header = document.querySelector('.header');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;

        if (currentScroll > 50) {
            header.style.background = 'rgba(255,255,255,0.95)';
            header.style.boxShadow = '0 5px 20px rgba(0,0,0,0.05)';
        } else {
            header.style.background = 'rgba(253, 251, 247, 0.9)'; // Default
            header.style.boxShadow = 'none';
        }

        lastScroll = currentScroll;
    });

    // Mobile Menu
    const toggle = document.querySelector('.mobile-toggle');
    const nav = document.querySelector('.nav-desktop'); // In mobile this should be styled differently
    if (toggle && nav) {
        toggle.addEventListener('click', () => {
            nav.classList.toggle('active');
        });
    }

    // Cart Drawer
    document.querySelector('.cart-trigger')?.addEventListener('click', openCart);
    document.querySelector('.cart-close')?.addEventListener('click', closeCart);
    document.querySelector('.cart-overlay')?.addEventListener('click', closeCart);
}

function initPageLogic() {
    const path = window.location.pathname;

    // Home Page
    if (path.includes('index') || path === '/' || path === '') {
        renderBestSellers();
    }

    // Product Page
    if (path.includes('product.html')) {
        initProductPage();
    }

    // Shop Page
    if (path.includes('shop.html')) {
        renderShop();
    }
}

/* --- ANIMATIONS --- */
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

/* --- CART DRAWER LOGIC --- */
function openCart() {
    document.querySelector('.cart-drawer').classList.add('open');
    document.querySelector('.cart-overlay').classList.add('open');
}

function closeCart() {
    document.querySelector('.cart-drawer').classList.remove('open');
    document.querySelector('.cart-overlay').classList.remove('open');
}

function addToCart(id, qty = 1) {
    const product = PRODUCTS.find(p => p.id === id);
    if (!product) return;

    const existing = state.cart.find(i => i.id === id);
    if (existing) {
        existing.qty += qty;
    } else {
        state.cart.push({ ...product, qty });
    }

    saveCart();
    updateCartUI();
    openCart(); // Auto open to show success
}

function removeFromCart(id) {
    state.cart = state.cart.filter(i => i.id !== id);
    saveCart();
    updateCartUI();
}

function updateQty(id, delta) {
    const item = state.cart.find(i => i.id === id);
    if (item) {
        item.qty += delta;
        if (item.qty <= 0) removeFromCart(id);
        else saveCart();
        updateCartUI();
    }
}

function saveCart() {
    localStorage.setItem('cart', JSON.stringify(state.cart));
}

function updateCartUI() {
    const container = document.getElementById('cart-items');
    const countBadge = document.querySelector('.cart-count');
    const totalEl = document.getElementById('cart-total');

    if (countBadge) countBadge.innerText = state.cart.reduce((a, b) => a + b.qty, 0);

    if (container) {
        container.innerHTML = '';
        let total = 0;

        state.cart.forEach(item => {
            total += item.price * item.qty;
            container.innerHTML += `
                <div class="cart-item">
                    <img src="${item.image}" alt="${item.name}">
                    <div style="flex:1;">
                        <h4 style="font-size: 0.95rem; margin-bottom: 5px;">${item.name}</h4>
                        <p style="color: #666; font-size: 0.85rem;">${item.price}₴</p>
                        <div style="display: flex; align-items: center; gap: 10px; margin-top: 10px;">
                            <button class="btn-qty" onclick="updateQty(${item.id}, -1)">-</button>
                            <span>${item.qty}</span>
                            <button class="btn-qty" onclick="updateQty(${item.id}, 1)">+</button>
                        </div>
                    </div>
                    <button onclick="removeFromCart(${item.id})" style="color: red; background: none; border: none; cursor: pointer;">&times;</button>
                </div>
            `;
        });

        if (state.cart.length === 0) container.innerHTML = '<p class="text-center text-muted">Корзина пуста</p>';
        if (totalEl) totalEl.innerText = total + ' ' + state.currency;
    }
}

/* --- PAGE RENDERERS --- */
function renderBestSellers() {
    const grid = document.getElementById('best-sellers-grid');
    if (!grid) return;

    PRODUCTS.slice(0, 3).forEach(p => {
        grid.innerHTML += createProductCard(p);
    });
}

function renderShop() {
    const grid = document.getElementById('products-grid');
    if (!grid) return;
    grid.innerHTML = '';
    PRODUCTS.forEach(p => grid.innerHTML += createProductCard(p));
}

function createProductCard(p) {
    return `
    <div class="product-card reveal">
        <div class="p-image-wrap">
            <span class="p-badge">${p.roast} roast</span>
            <a href="product.html?id=${p.id}"><img src="${p.image}" alt="${p.name}"></a>
        </div>
        <div class="p-info">
            <div class="p-meta">${p.type} • ${p.weight}g</div>
            <h3><a href="product.html?id=${p.id}">${p.name}</a></h3>
            <div class="p-footer">
                <span class="p-price">${p.price} ${state.currency}</span>
                <button class="btn-add" onclick="addToCart(${p.id})"><i class="fas fa-plus"></i></button>
            </div>
        </div>
    </div>
    `;
}

function initProductPage() {
    const params = new URLSearchParams(window.location.search);
    const id = parseInt(params.get('id'));
    const product = PRODUCTS.find(p => p.id === id);

    if (!product) return; // Handle 404

    document.getElementById('p-title').innerText = product.name;
    document.getElementById('p-price').innerText = product.price + ' ' + state.currency;
    document.getElementById('p-desc').innerText = product.desc;
    document.getElementById('p-main-img').src = product.image;

    // Setup add button
    document.getElementById('add-to-cart-btn').onclick = () => addToCart(product.id, 1);
}
