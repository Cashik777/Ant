// B2B ROI Calculator
function calculateROI() {
    const kg = parseFloat(document.getElementById('roi-kg').value) || 0;
    const currentPrice = parseFloat(document.getElementById('roi-price').value) || 0;

    // EthioDirect average B2B price for 50kg+
    const ourPrice = 550;

    // Calculate monthly savings
    const currentCost = kg * currentPrice;
    const ourCost = kg * ourPrice;
    const monthlySavings = currentCost - ourCost;

    // Show result
    const resultDiv = document.getElementById('roi-result');
    const savingsSpan = document.getElementById('roi-savings');

    if (monthlySavings > 0) {
        savingsSpan.textContent = Math.round(monthlySavings) + '₴';
        savingsSpan.style.color = 'var(--accent)';
        resultDiv.style.display = 'block';
    } else {
        savingsSpan.textContent = '0₴';
        savingsSpan.style.color = '#999';
        resultDiv.style.display = 'block';

        // Add message
        const note = resultDiv.querySelector('p');
        note.textContent = '* Ваша поточна ціна вже дуже конкурентна! Але ми пропонуємо стабільну якість specialty кави.';
    }
}

// B2B form submission
function submitB2BForm(event) {
    event.preventDefault();

    const form = event.target;
    const formData = {
        name: form.querySelector('input[type="text"]').value,
        email: form.querySelector('input[type="email"]').value,
        phone: form.querySelector('input[type="tel"]').value,
        businessType: form.querySelector('select').value,
        volume: form.querySelector('input[type="number"]').value,
        comment: form.querySelector('textarea').value
    };

    // Save to localStorage
    let b2bLeads = JSON.parse(localStorage.getItem('b2bLeads') || '[]');
    b2bLeads.push({
        ...formData,
        timestamp: new Date().toISOString()
    });
    localStorage.setItem('b2bLeads', JSON.stringify(b2bLeads));

    // Show success
    alert('Дякуємо за заявку! Ми зв\'яжемось з вами протягом 24 годин.');
    form.reset();
}

// Make functions global
window.calculateROI = calculateROI;
window.submitB2BForm = submitB2BForm;
