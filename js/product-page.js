/* PRODUCT PAGE LOGIC */

// Get product ID from URL
const urlParams = new URLSearchParams(window.location.search);
const productId = urlParams.get('id') || 'yirgacheffe';

// Load product data
// Load product data
function loadProductData() {
    // PRODUCTS uses number IDs, productId from URL is string
    const product = PRODUCTS.find(p => p.id == productId);
    if (!product) {
        // Only redirect if truly not found
        console.warn('Product not found for ID:', productId);
        window.location.href = 'shop.html';
        return;
    }

    // Get product key for translation
    const productKeys = {
        1: 'sidamo', 2: 'yirgacheffe', 3: 'guji',
        4: 'espresso_blend', 5: 'limmu', 6: 'harrar'
    };
    const pKey = productKeys[product.id] || 'sidamo';

    // Helper for safe translation
    const tr = (key, defaultText) => (typeof t === 'function' ? t(key) : defaultText);

    const name = tr(`product.${pKey}`, product.name);
    const desc = tr(`product.${pKey}_desc`, product.desc);

    // Update page title
    document.title = `${name} — EthioDirect`;
    const titleEl = document.getElementById('product-title');
    if (titleEl) titleEl.textContent = `${name} — EthioDirect`;

    // Breadcrumb
    const breadcrumb = document.getElementById('breadcrumb-product');
    if (breadcrumb) breadcrumb.textContent = name;

    // Main info
    document.getElementById('product-name').textContent = name;

    // Region
    const regionLabel = tr('product.spec_region', 'Регіон'); // Ensure this key exists or use fallback
    // For region value, we might want to keep it as is or translate if we had keys. Keeping as is for now.
    document.getElementById('product-region').textContent = `${regionLabel}: ${product.region}`;

    // Price
    const pricePer250 = tr('product.spec_weight_250', '/ 250г'); // "/ 250g"
    document.getElementById('product-price-display').innerHTML = `
        <span class="price-current">${product.price} ₴</span>
        <span class="price-per-kg">${pricePer250}</span>
    `;

    // Gallery
    const mainImg = document.getElementById('main-image');
    if (mainImg && mainImg.getAttribute('src') !== product.image) {
        mainImg.src = product.image;
    }
    const modalImg = document.getElementById('modal-image');
    if (modalImg && modalImg.getAttribute('src') !== product.image) {
        modalImg.src = product.image;
    }

    // Taste notes - mapping to keys if possible, or using mapped values
    // Assuming taste notes in product.taste are e.g. "Chocolate", "Nut" etc.
    // We can try to translate them if we have keys, otherwise leave as is.
    // For now, let's just use the raw string or simple mapping if feasible. 
    // Given current state, we'll leave taste tags as is or try to translate common ones.
    const tasteHtml = product.taste.split(',').map(tag => {
        const cleanTag = tag.trim();
        // Try to find a translation for taste profile? 
        // We lack specific keys for every taste note. We will leave them for now or assume they are covered elsewhere.
        // Actually, let's mostly rely on the existing text but if we want perfection we need keys.
        return `<span class="taste-tag">${cleanTag}</span>`;
    }).join('');
    document.querySelector('.taste-tags').innerHTML = tasteHtml;

    // Quick specs
    document.getElementById('spec-roast').textContent = getRoastName(product.roast);
    const weightLabel = typeof t === 'function' ? '250' + tr('product.unit_g', 'г') : '250г';
    document.getElementById('spec-weight').textContent = weightLabel;
    document.getElementById('spec-method').textContent = getMethodName(product.method);

    // Description tab
    // We construct the description dynamically
    const introTemplate = tr('product_page.desc_intro', 'Ця кава з {region} вирощена в екологічно чистих регіонах на висоті понад 1800 метрів.');
    const fullDesc = `${introTemplate.replace('{region}', product.region)} ${desc}`;
    document.getElementById('product-description').textContent = fullDesc;

    // Specs tab
    document.getElementById('specs-region').textContent = product.region;
    document.getElementById('specs-roast').textContent = getRoastName(product.roast);

    // Re-render related products
    loadRelatedProducts(product.id);
}

function getRoastName(roast) {
    if (typeof t !== 'function') return roast;
    const keys = { light: 'product.roast_light', medium: 'product.roast_medium', dark: 'product.roast_dark' };
    return t(keys[roast]) || roast;
}

function getMethodName(methods) {
    const tr = (key, def) => (typeof t === 'function' ? t(key) : def);
    if (methods.includes('espresso') && methods.includes('filter')) return tr('product.method_universal', 'Універсальна');
    if (methods.includes('espresso')) return tr('product.espresso', 'Еспресо');
    if (methods.includes('filter')) return tr('product.filter', 'Фільтр');
    return tr('product.method_universal', 'Універсальна');
}

// Hook into i18n events
document.addEventListener('i18nReady', () => {
    loadProductData();
});

window.onLanguageChange = function (lang) {
    console.log('[product-page] Language changed to:', lang);
    loadProductData();
};

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
        // createProductCard now handles translations internally if t() is available
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
