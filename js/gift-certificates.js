// Gift Certificates JavaScript

let selectedAmount = 500;

// Initialize expiry date (1 year from now)
function initExpiryDate() {
    const date = new Date();
    date.setFullYear(date.getFullYear() + 1);
    const formatted = date.toLocaleDateString('uk-UA', { day: '2-digit', month: '2-digit', year: 'numeric' });
    document.getElementById('expiryDate').textContent = formatted;
}

// Select amount
function selectAmount(amount) {
    selectedAmount = parseFloat(amount) || 500;

    // Update buttons
    document.querySelectorAll('.amount-btn').forEach(btn => {
        btn.style.border = '2px solid #ddd';
        btn.style.background = 'white';
        btn.style.color = 'var(--text)';
    });

    const btn = document.querySelector(`[data-amount="${amount}"]`);
    if (btn) {
        btn.style.border = '2px solid var(--primary)';
        btn.style.background = 'var(--primary)';
        btn.style.color = 'white';
    }

    // Update preview and price
    document.getElementById('previewAmount').textContent = selectedAmount;
    document.getElementById('totalPrice').textContent = selectedAmount;

    // Clear custom input if preset selected
    if (btn) {
        document.getElementById('customAmount').value = '';
    }
}

// Update preview
function updatePreview() {
    const recipient = document.getElementById('recipientName').value || '_____________';
    const sender = document.getElementById('senderName').value || '_____________';
    const message = document.getElementById('giftMessage').value;

    document.getElementById('previewRecipient').textContent = recipient;
    document.getElementById('previewSender').textContent = sender;

    const messageBlock = document.getElementById('previewMessageBlock');
    if (message.trim()) {
        document.getElementById('previewMessage').textContent = `"${message}"`;
        messageBlock.style.display = 'block';
    } else {
        messageBlock.style.display = 'none';
    }
}

// Purchase certificate
function purchaseCertificate() {
    const recipientName = document.getElementById('recipientName').value;
    const senderName = document.getElementById('senderName').value;
    const recipientEmail = document.getElementById('recipientEmail').value;
    const message = document.getElementById('giftMessage').value;

    // Validation
    if (!recipientName || !senderName || !recipientEmail) {
        alert('Будь ласка, заповніть всі обов\'язкові поля');
        return;
    }

    if (!recipientEmail.includes('@')) {
        alert('Будь ласка, введіть коректний email');
        return;
    }

    // Create certificate data
    const certificate = {
        amount: selectedAmount,
        recipientName,
        senderName,
        recipientEmail,
        message,
        date: new Date().toISOString(),
        code: generateCode()
    };

    // Save to localStorage
    let certificates = JSON.parse(localStorage.getItem('giftCertificates') || '[]');
    certificates.push(certificate);
    localStorage.setItem('giftCertificates', JSON.stringify(certificates));

    // Show success message
    alert(`Дякуємо за покупку!\n\nСертифікат на ${selectedAmount}₴ буде відправлено на email:\n${recipientEmail}\n\nКод: ${certificate.code}`);

    // Add to cart simulation
    addToCart({
        name: `Подарунковий сертифікат ${selectedAmount}₴`,
        price: selectedAmount,
        quantity: 1,
        image: 'https://images.unsplash.com/photo-1549399542-7e3f8b79c341?w=200'
    });

    // Reset form
    document.getElementById('recipientName').value = '';
    document.getElementById('senderName').value = '';
    document.getElementById('recipientEmail').value = '';
    document.getElementById('giftMessage').value = '';
    updatePreview();
}

// Generate unique code
function generateCode() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let code = '';
    for (let i = 0; i < 12; i++) {
        if (i > 0 && i % 4 === 0) code += '-';
        code += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return code;
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    initExpiryDate();
    selectAmount(500);
});

// Make functions global
window.selectAmount = selectAmount;
window.updatePreview = updatePreview;
window.purchaseCertificate = purchaseCertificate;
