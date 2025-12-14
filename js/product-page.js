/* PRODUCT PAGE LOGIC */

// Get product ID from URL
const urlParams = new URLSearchParams(window.location.search);
const productId = urlParams.get('id') || 'yirgacheffe';

// Load product data
function loadProductData() {
    const product = PRODUCTS.find(p => p.id === productId);
    if (!product) {
        window.location.href = 'shop.html';
        return;
    }

    // Update page title
    document.title = `${product.name} — EthioDirect`;
    document.getElementById('product-title').textContent = `${product.name} — EthioDirect`;

    // Breadcrumb
    document.getElementById('breadcrumb-product').textContent = product.name;

    // Main info
    document.getElementById('product-name').textContent = product.name;
    document.getElementById('product-region').textContent = `Регіон: ${product.region}`;
    document.getElementById('product-price-display').innerHTML = `
        <span class="price-current">${product.price} ₴</span>
        <span class="price-per-kg">/ 250г</span>
    `;

    // Gallery
    document.getElementById('main-image').src = product.image;
    document.getElementById('modal-image').src = product.image;

    // Taste notes
    const tasteHtml = product.taste.split(',').map(t =>
        `<span class="taste-tag">${t.trim()}</span>`
    ).join('');
    document.querySelector('.taste-tags').innerHTML = tasteHtml;

    // Quick specs
    document.getElementById('spec-roast').textContent = getRoastName(product.roast);
    document.getElementById('spec-weight').textContent = '250г';
    document.getElementById('spec-method').textContent = getMethodName(product.method);

    // Description tab
    document.getElementById('product-description').textContent = `Ця кава з ${product.region} вирощена в екологічно чистих регіонах на висоті понад 1800 метрів. ${product.desc}`;

    // Specs tab
    document.getElementById('specs-region').textContent = product.region;
    document.getElementById('specs-roast').textContent = getRoastName(product.roast);

    // Load related products
    loadRelatedProducts(product.id);
}

function getRoastName(roast) {
    const names = { light: 'Світла', medium: 'Середня', dark: 'Темна' };
    return names[roast] || roast;
}

function getMethodName(methods) {
    if (methods.includes('espresso') && methods.includes('filter')) return 'Універсальна';
    if (methods.includes('espresso')) return 'Еспресо';
    if (methods.includes('filter')) return 'Фільтр';
    return 'Універсальна';
}

// Gallery functions
function changeMainImage(src) {
    document.getElementById('main-image').src = src;
    document.getElementById('modal-image').src = src;
}

function openImageModal() {
    document.getElementById('image-modal').classList.add('active');
}

function closeImageModal() {
    document.getElementById('image-modal').classList.remove('active');
}

// Tabs switching
function initTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.dataset.tab;

            // Remove active
            tabBtns.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));

            // Add active
            btn.classList.add('active');
            document.getElementById(`tab-${tabId}`).classList.add('active');
        });
    });
}

// Star rating input
function initStarRating() {
    const stars = document.querySelectorAll('.star-input i');
    let selectedRating = 0;

    stars.forEach((star, index) => {
        star.addEventListener('click', () => {
            selectedRating = index + 1;
            updateStars(selectedRating);
        });

        star.addEventListener('mouseenter', () => {
            updateStars(index + 1);
        });
    });

    document.querySelector('.star-input').addEventListener('mouseleave', () => {
        updateStars(selectedRating);
    });

    function updateStars(rating) {
        stars.forEach((star, index) => {
            if (index < rating) {
                star.classList.remove('far');
                star.classList.add('fas', 'active');
            } else {
                star.classList.remove('fas', 'active');
                star.classList.add('far');
            }
        });
    }
}

// Quantity selector
let quantity = 1;

function changeQuantity(delta) {
    const input = document.getElementById('quantity');
    quantity = Math.max(1, Math.min(10, quantity + delta));
    input.value = quantity;
}

// Add to cart from product page
function addToCartFromProduct() {
    const product = PRODUCTS.find(p => p.id === productId);
    if (!product) return;

    for (let i = 0; i < quantity; i++) {
        addToCart(product);
    }

    alert(`${product.name} (x${quantity}) додано до кошика!`);
}

// Submit review
function submitReview(event) {
    event.preventDefault();
    alert('Дякуємо за відгук! Він буде опублікований після модерації.');
    event.target.reset();

    // Reset stars
    document.querySelectorAll('.star-input i').forEach(star => {
        star.classList.remove('fas', 'active');
        star.classList.add('far');
    });
}

// Load related products
function loadRelatedProducts(currentProductId) {
    const related = PRODUCTS.filter(p => p.id !== currentProductId).slice(0, 3);
    const grid = document.getElementById('related-products');
    if (grid) {
        grid.innerHTML = related.map(p => createProductCard(p)).join('');
    }
}

// Make functions global
window.changeMainImage = changeMainImage;
window.openImageModal = openImageModal;
window.closeImageModal = closeImageModal;
window.changeQuantity = changeQuantity;
window.addToCartFromProduct = addToCartFromProduct;
window.submitReview = submitReview;

// Initialize on load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        loadProductData();
        initTabs();
        initStarRating();
    });
} else {
    loadProductData();
    initTabs();
    initStarRating();
}
