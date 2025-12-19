/* === GOOGLE ANALYTICS & CONVERSION TRACKING === */

// Google Analytics 4
window.dataLayer = window.dataLayer || [];
function gtag() { dataLayer.push(arguments); }
gtag('js', new Date());

// Replace G-XXXXXXXXXX with your actual GA4 Measurement ID
gtag('config', 'G-XXXXXXXXXX');

// Custom event tracking
function trackEvent(eventName, eventParams = {}) {
    gtag('event', eventName, eventParams);
}

// E-commerce tracking
function trackPurchase(transactionData) {
    gtag('event', 'purchase', {
        transaction_id: transactionData.id,
        value: transactionData.total,
        currency: 'UAH',
        items: transactionData.items
    });
}

// Quiz completion tracking
function trackQuizCompletion(result) {
    gtag('event', 'quiz_complete', {
        recommended_product: result.product.name,
        quiz_duration: result.duration
    });
}

// Subscription conversion
function trackSubscription(plan) {
    gtag('event', 'subscribe', {
        plan_name: plan.name,
        plan_value: plan.price
    });
}

// Add to cart tracking
function trackAddToCart(product) {
    gtag('event', 'add_to_cart', {
        currency: 'UAH',
        value: product.price,
        items: [{
            item_id: product.id,
            item_name: product.name,
            price: product.price
        }]
    });
}

// Newsletter signup
function trackNewsletterSignup(email) {
    gtag('event', 'newsletter_signup', {
        method: 'footer_form'
    });
}

// Make functions global
window.trackEvent = trackEvent;
window.trackPurchase = trackPurchase;
window.trackQuizCompletion = trackQuizCompletion;
window.trackSubscription = trackSubscription;
window.trackAddToCart = trackAddToCart;
window.trackNewsletterSignup = trackNewsletterSignup;
