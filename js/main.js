/* ===== MAIN LOGIC ===== */

document.addEventListener('DOMContentLoaded', () => {
    // Determine current page
    const path = window.location.pathname;

    if (path.includes('index.html') || path === '/' || path.endsWith('/')) {
        initHomePage();
    } else if (path.includes('shop.html')) {
        initShopPage();
    } else if (path.includes('subscription.html')) {
        initSubscriptionPage();
    }
});

/* --- HOME PAGE --- */
function initHomePage() {
    const container = document.getElementById('best-sellers-grid');
    if (!container) return;

    // Show top 3 products
    const topProducts = PRODUCTS.slice(0, 3);

    topProducts.forEach(product => {
        container.innerHTML += createProductCard(product);
    });
}

/* --- SHOP PAGE --- */
function initShopPage() {
    const container = document.getElementById('products-grid');
    if (!container) return;

    // Initial render
    renderShopProducts(PRODUCTS);

    // Filters logic
    const filterButtons = document.querySelectorAll('.filter-btn');
    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all
            filterButtons.forEach(b => b.classList.remove('active'));
            // Add to click
            btn.classList.add('active');

            const type = btn.dataset.type;

            if (type === 'all') {
                renderShopProducts(PRODUCTS);
            } else {
                const filtered = PRODUCTS.filter(p => p.type === type);
                renderShopProducts(filtered);
            }
        });
    });
}

function renderShopProducts(list) {
    const container = document.getElementById('products-grid');
    container.innerHTML = '';

    if (list.length === 0) {
        container.innerHTML = '<p class="text-center">Товары не найдены</p>';
        return;
    }

    list.forEach(product => {
        container.innerHTML += createProductCard(product);
    });
}

/* --- HELPERS --- */
function createProductCard(product) {
    return `
    <div class="card product-card">
        <div class="product-img-wrapper" style="position: relative; overflow: hidden; border-radius: 8px; margin-bottom: 20px;">
             <span class="badge" style="position: absolute; top: 10px; left: 10px; z-index: 2; padding: 5px 12px; border-radius: 20px; font-size: 0.8rem;">${product.roast} roast</span>
            <img src="${product.image}" alt="${product.name}" style="width: 100%; height: 250px; object-fit: cover; transition: transform 0.3s ease;">
        </div>
        
        <h3 style="font-size: 1.4rem; margin-bottom: 10px;">${product.name}</h3>
        
        <div class="tags" style="display: flex; gap: 10px; margin-bottom: 15px;">
            ${product.tags.map(t => `<span style="font-size: 0.8rem; background: #f4f4f4; padding: 4px 10px; border-radius: 12px;">${t}</span>`).join('')}
        </div>
        
        <p style="font-size: 0.95rem; line-height: 1.4; margin-bottom: 20px; height: 40px; overflow: hidden;">${product.desc}</p>
        
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-size: 1.5rem; font-weight: 700; color: var(--primary);">${product.price}₴</span>
            <button class="btn btn-outline" style="padding: 10px 20px; border-radius: 20px; font-size: 0.9rem;" onclick="addToCart(${product.id})">
                В корзину
            </button>
        </div>
    </div>
    `;
}

function initSubscriptionPage() {
    // Logic for subscription interactive elements
    console.log('Subscription page logic ready');
}

function addToCart(id) {
    alert('Товар добавлен в корзину (Демо)');
    // Тут будет логика сохранения в localStorage
}
