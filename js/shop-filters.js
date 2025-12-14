/* --- SHOP FILTERS LOGIC --- */
let activeFilters = { price: [0, 500], roast: [], taste: [], method: [] };

function initShopFilters() {
    // Price sliders
    const priceMin = document.getElementById('price-min');
    const priceMax = document.getElementById('price-max');
    if (priceMin && priceMax) {
        priceMin.addEventListener('input', updatePriceFilter);
        priceMax.addEventListener('input', updatePriceFilter);
    }

    // Checkboxes
    document.querySelectorAll('.filter-checkbox input').forEach(checkbox => {
        checkbox.addEventListener('change', applyFilters);
    });

    // View switcher
    document.querySelectorAll('.view-btn').forEach(btn => {
        btn.addEventListener('click', switchView);
    });

    // Initial render
    if (document.getElementById('products-grid')) {
        applyFilters();
    }
}

function updatePriceFilter() {
    let min = parseInt(document.getElementById('price-min').value);
    let max = parseInt(document.getElementById('price-max').value);

    if (min > max) {
        const temp = min;
        min = max;
        max = temp;
    }

    document.getElementById('price-min-display').textContent = min;
    document.getElementById('price-max-display').textContent = max;
    activeFilters.price = [min, max];
    applyFilters();
}

function applyFilters() {
    // Collect active filters
    activeFilters.roast = Array.from(document.querySelectorAll('input[data-filter="roast"]:checked')).map(el => el.value);
    activeFilters.taste = Array.from(document.querySelectorAll('input[data-filter="taste"]:checked')).map(el => el.value);
    activeFilters.method = Array.from(document.querySelectorAll('input[data-filter="method"]:checked')).map(el => el.value);

    // Filter products
    let filtered = PRODUCTS.filter(product => {
        // Price filter
        if (product.price < activeFilters.price[0] || product.price > activeFilters.price[1]) return false;

        // Roast filter
        if (activeFilters.roast.length > 0 && !activeFilters.roast.includes(product.roast)) return false;

        // Taste filter
        if (activeFilters.taste.length > 0) {
            const productTastes = getTasteCategories(product.taste);
            if (!activeFilters.taste.some(t => productTastes.includes(t))) return false;
        }

        // Method filter
        if (activeFilters.method.length > 0) {
            if (!activeFilters.method.some(m => product.method.includes(m))) return false;
        }

        return true;
    });

    // Update counter
    const counter = document.getElementById('results-count');
    if (counter) counter.textContent = filtered.length;

    // Render products
    renderProducts(filtered);

    // Show/hide no results
    const noResults = document.getElementById('no-results');
    const grid = document.getElementById('products-grid');
    if (noResults && grid) {
        noResults.style.display = filtered.length === 0 ? 'block' : 'none';
        grid.style.display = filtered.length === 0 ? 'none' : 'grid';
    }
}

function getTasteCategories(tastes) {
    const categories = [];
    if (tastes.includes('🍫') || tastes.includes('🥜')) categories.push('chocolate');
    if (tastes.includes('🍓') || tastes.includes('🥭') || tastes.includes('🍋')) categories.push('fruity');
    if (tastes.includes('🌸')) categories.push('floral');
    if (tastes.includes('🫐') || tastes.includes('🍷')) categories.push('spicy');
    return categories;
}

function clearAllFilters() {
    const priceMin = document.getElementById('price-min');
    const priceMax = document.getElementById('price-max');
    if (priceMin && priceMax) {
        priceMin.value = 0;
        priceMax.value = 500;
        document.getElementById('price-min-display').textContent = 0;
        document.getElementById('price-max-display').textContent = 500;
    }
    document.querySelectorAll('.filter-checkbox input').forEach(cb => cb.checked = false);
    activeFilters = { price: [0, 500], roast: [], taste: [], method: [] };
    applyFilters();
}

function sortProducts(sortBy) {
    let sorted = [...PRODUCTS];
    switch (sortBy) {
        case 'price-asc':
            sorted.sort((a, b) => a.price - b.price);
            break;
        case 'price-desc':
            sorted.sort((a, b) => b.price - a.price);
            break;
        case 'new':
            sorted.reverse();
            break;
        default:
            break;
    }
    renderProducts(sorted);
}

function switchView(e) {
    document.querySelectorAll('.view-btn').forEach(b => b.classList.remove('active'));
    e.currentTarget.classList.add('active');
    const view = e.currentTarget.dataset.view;
    const grid = document.getElementById('products-grid');
    if (view === 'list') {
        grid.style.gridTemplateColumns = '1fr';
    } else {
        grid.style.gridTemplateColumns = 'repeat(auto-fill, minmax(280px, 1fr))';
    }
}

function renderProducts(products) {
    const grid = document.getElementById('products-grid');
    if (!grid) return;
    grid.innerHTML = products.map(p => createProductCard(p)).join('');
}

// Make functions global
window.clearAllFilters = clearAllFilters;
window.sortProducts = sortProducts;

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initShopFilters);
} else {
    initShopFilters();
}
