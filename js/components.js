/* ===== COMPONENTS INJECTION v2.0 ===== */
/* This file injects common HTML structures like Header, Footer, and Cart Drawer */

document.addEventListener('DOMContentLoaded', () => {
    injectHeader();
    injectCartDrawer();
    injectFooter();
});

function injectHeader() {
    const html = `
    <header class="header">
        <div class="container header-inner">
            <a href="index.html" class="logo">
                <i class="fas fa-coffee"></i> EthioDirect
            </a>
            
            <nav class="nav-desktop">
                <a href="index.html" class="nav-link">Главная</a>
                <a href="shop.html" class="nav-link">Магазин</a>
                <a href="subscription.html" class="nav-link">Подписка</a>
                <a href="about.html" class="nav-link">О нас</a>
                <a href="contacts.html" class="nav-link">Контакты</a>
            </nav>
            
            <div class="header-controls">
                <div class="cart-trigger">
                    <i class="fas fa-shopping-bag"></i>
                    <span class="cart-count">0</span>
                </div>
                <!-- Mobile toggle could go here -->
            </div>
        </div>
    </header>
    `;
    document.body.insertAdjacentHTML('afterbegin', html);

    // Highlight active link
    const path = window.location.pathname.split('/').pop() || 'index.html';
    const links = document.querySelectorAll('.nav-link');
    links.forEach(l => {
        if (l.getAttribute('href') === path) l.classList.add('active');
    });
}

function injectCartDrawer() {
    const html = `
    <div class="cart-overlay"></div>
    <div class="cart-drawer">
        <div class="cart-header">
            <h3>Ваша корзина</h3>
            <button class="cart-close" style="background:none; border:none; font-size:1.5rem; cursor:pointer;">&times;</button>
        </div>
        <div class="cart-body" id="cart-items">
            <!-- Items injected by main.js -->
        </div>
        <div class="cart-footer">
            <div style="display:flex; justify-content:space-between; margin-bottom:20px; font-weight:700; font-size:1.2rem;">
                <span>Итого:</span>
                <span id="cart-total">0 ₴</span>
            </div>
            <button class="btn btn-primary" style="width:100%;" onclick="alert('Переход к оплате...')">Оформить заказ</button>
        </div>
    </div>
    `;
    document.body.insertAdjacentHTML('beforeend', html);
}

function injectFooter() {
    const html = `
    <footer class="footer">
        <div class="container">
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap:50px;">
                <div>
                    <h4 style="color:white; margin-bottom:20px;">EthioDirect</h4>
                    <p style="color:#888;">Премиальный эфиопский кофе с доставкой от фермера к вашей чашке за 72 часа.</p>
                </div>
                <div>
                    <h4 style="color:white; margin-bottom:20px;">Магазин</h4>
                    <ul style="color:#888; line-height:2;">
                        <li><a href="shop.html">Каталог</a></li>
                        <li><a href="subscription.html">Подписка</a></li>
                        <li><a href="b2b.html">Для бизнеса</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color:white; margin-bottom:20px;">Помощь</h4>
                    <ul style="color:#888; line-height:2;">
                        <li><a href="delivery.html">Доставка</a></li>
                        <li><a href="contacts.html">Контакты</a></li>
                        <li><a href="return.html">Возврат</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                &copy; 2025 EthioDirect Coffee Co. Odessa, Ukraine.
            </div>
        </div>
    </footer>
    `;
    document.body.insertAdjacentHTML('beforeend', html);
}
