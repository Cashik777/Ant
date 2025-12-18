// FAQ Filtering
function filterFAQ(category) {
    const items = document.querySelectorAll('.faq-item');
    const buttons = document.querySelectorAll('.faq-categories .filter-btn');

    // Update active button
    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    // Filter items
    items.forEach(item => {
        if (category === 'all' || item.dataset.category === category) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

// Make global
window.filterFAQ = filterFAQ;
