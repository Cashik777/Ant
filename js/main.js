/* ===== MAIN LOGIC v2.5 ===== */

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
    if (header) {
        window.addEventListener('scroll', () => {
            const currentScroll = window.scrollY;
            if (currentScroll > 50) {
                header.style.background = 'rgba(255,255,255,0.98)';
                header.style.boxShadow = '0 5px 20px rgba(0,0,0,0.05)';
            } else {
                header.style.background = 'rgba(253, 251, 247, 0.9)';
                header.style.boxShadow = 'none';
            }
        });
    }

    // Mobile Menu
    const toggle = document.querySelector('.mobile-toggle');
    const nav = document.querySelector('.nav-desktop');
    if (toggle && nav) {
        toggle.addEventListener('click', () => {
            nav.classList.toggle('active');
        });
    }

    // Cart Drawer logic
    const cartTrigger = document.querySelector('.cart-trigger');
    if (cartTrigger) cartTrigger.addEventListener('click', openCart);

    document.querySelector('.cart-close')?.addEventListener('click', closeCart);
    document.querySelector('.cart-overlay')?.addEventListener('click', closeCart);
}

function initPageLogic() {
    const path = window.location.pathname;

    // Home Page
    if (path.includes('index') || path === '/' || path === '' || path.endsWith('/')) {
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
    const drawer = document.querySelector('.cart-drawer');
    const overlay = document.querySelector('.cart-overlay');
    if (drawer) drawer.classList.add('open');
    if (overlay) overlay.classList.add('open');
}

function closeCart() {
    const drawer = document.querySelector('.cart-drawer');
    const overlay = document.querySelector('.cart-overlay');
    if (drawer) drawer.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
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
    openCart();
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
    // Calculate subscription price (15% off)
    const subPrice = Math.floor(p.price * 0.85);

    return `
    <div class="product-card reveal">
        <div class="p-image-wrap">
            <span class="p-badge">${p.roast} roast</span>
            <a href="product.html?id=${p.id}"><img src="${p.image}" alt="${p.name}"></a>
        </div>
        <div class="p-info">
            <div class="p-meta" style="font-size: 0.8rem; text-transform:uppercase; color: #999; margin-bottom:5px;">
                ${p.tags.join(' • ')}
            </div>
            <h3 style="margin-top:0;"><a href="product.html?id=${p.id}">${p.name}</a></h3>
             <div style="display:flex; gap:10px; margin-bottom:15px; font-size:0.9rem; color:#666;">
                <span><i class="fas fa-mountain"></i> Ethiopia</span>
                <span><i class="fas fa-weight"></i> ${p.weight}g</span>
            </div>
            
            <div style="border-top:1px solid #eee; padding-top:15px;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                    <span style="font-weight:700; font-size:1.2rem;">${p.price} ₴</span>
                    <button class="btn btn-primary" style="padding: 8px 16px; font-size:0.8rem;" onclick="addToCart(${p.id})">Купить</button>
                </div>
                
                 <div style="display:flex; justify-content:space-between; align-items:center; background:#f9f9f9; padding:8px; border-radius:4px;">
                    <span style="font-size:0.9rem; color:var(--primary); font-weight:600;">${subPrice} ₴ <small style="color:#666; font-weight:400;">по подписке</small></span>
                    <a href="subscription.html?product=${p.id}" style="font-size:0.8rem; text-decoration:underline; cursor:pointer; color:var(--text-main);">Подписаться</a>
                </div>
            </div>
        </div>
    </div>
    `;
}

function initProductPage() {
    const params = new URLSearchParams(window.location.search);
    const id = parseInt(params.get('id'));
    const product = PRODUCTS.find(p => p.id === id);

    if (!product) return;

    document.getElementById('p-title').innerText = product.name;
    document.getElementById('p-price').innerText = product.price + ' ' + state.currency;
    document.getElementById('p-desc').innerText = product.desc;
    document.getElementById('p-main-img').src = product.image;

    document.getElementById('add-to-cart-btn').onclick = () => addToCart(product.id, 1);
}
