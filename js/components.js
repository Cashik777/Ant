/* ===== ETHIODIRECT COMPONENTS v3.0 ===== */

document.addEventListener('DOMContentLoaded', () => {
    injectHeader();
    injectDrawer();
    injectFooter();
});

/* --- HEADER --- */
function injectHeader() {
    const html = `
    <header class="header">
        <div class="container header-inner">
            <a href="index.html" class="logo">
                <i class="fas fa-seedling text-gold"></i>
                <span>EthioDirect</span>
            </a>
            
            <nav class="nav-desktop">
                <a href="shop.html" class="nav-link">Кофе</a>
                <a href="subscription.html" class="nav-link">Подписка</a>
                <a href="quiz.html" class="nav-link">Подобрать</a>
                <a href="about.html" class="nav-link">О нас</a>
                <a href="b2b.html" class="nav-link">B2B</a>
            </nav>
            
            <div class="header-actions">
                <a href="account.html" class="nav-link" title="Кабинет"><i class="far fa-user"></i></a>
                <div class="cart-trigger nav-link" style="cursor:pointer; position:relative;">
                    <i class="fas fa-shopping-bag"></i>
                    <span class="cart-count" style="position:absolute; top:-8px; right:-10px; background:var(--accent); color:white; font-size:10px; padding:2px 6px; border-radius:10px;">0</span>
                </div>
            </div>
            
            <button class="mobile-toggle" aria-label="Menu"><i class="fas fa-bars"></i></button>
        </div>
    </header>
    `;
    document.body.insertAdjacentHTML('afterbegin', html);
    highlightActiveLink();
}

function highlightActiveLink() {
    const path = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-link').forEach(link => {
        if (link.getAttribute('href') === path) {
            link.classList.add('active');
        }
    });
}

/* --- DRAWER CART --- */
function injectDrawer() {
    const html = `
    <div class="overlay"></div>
    <div class="drawer">
        <div class="drawer-header">
            <h3>Корзина</h3>
            <span class="cart-close" style="cursor:pointer; font-size:1.5rem; line-height:1;">&times;</span>
        </div>
        <div class="drawer-body" id="cart-list">
            <p class="text-muted text-center">Корзина пуста</p>
        </div>
        <div class="drawer-footer">
            <div style="display:flex; justify-content:space-between; margin-bottom:20px; font-weight:600;">
                <span>Итого</span>
                <span id="cart-total">0 ₴</span>
            </div>
            <button class="btn btn-primary" style="width:100%;">Оформить заказ</button>
            <a href="subscription.html" style="display:block; text-align:center; margin-top:15px; font-size:0.9rem; color:var(--accent);">Или оформите подписку со скидкой -10%</a>
        </div>
    </div>
    `;
    document.body.insertAdjacentHTML('beforeend', html);
}

/* --- FOOTER --- */
function injectFooter() {
    const html = `
    <footer class="footer" style="background: #1a1a1a; color: #999; padding: 80px 0 40px;">
        <div class="container">
            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 50px; margin-bottom: 60px;">
                <div>
                    <h4 style="color:white; margin-bottom:20px; font-size:1.1rem;">EthioDirect</h4>
                    <p style="font-size:0.9rem; line-height:1.8;">Specialty кофе напрямую из Эфиопии. Обжарка в Одессе.</p>
                    <div style="margin-top:20px; display:flex; gap:15px;">
                        <a href="#" style="color:#666;"><i class="fab fa-instagram"></i></a>
                        <a href="#" style="color:#666;"><i class="fab fa-telegram"></i></a>
                        <a href="#" style="color:#666;"><i class="fab fa-facebook"></i></a>
                    </div>
                </div>
                <div>
                    <h4 style="color:white; margin-bottom:20px; font-size:1.1rem;">Магазин</h4>
                    <ul style="list-style:none; line-height:2.2; font-size:0.9rem;">
                        <li><a href="shop.html" style="color:#888;">Весь кофе</a></li>
                        <li><a href="subscription.html" style="color:#888;">Подписка</a></li>
                        <li><a href="quiz.html" style="color:#888;">Подобрать кофе</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color:white; margin-bottom:20px; font-size:1.1rem;">Информация</h4>
                    <ul style="list-style:none; line-height:2.2; font-size:0.9rem;">
                        <li><a href="about.html" style="color:#888;">О нас</a></li>
                        <li><a href="blog.html" style="color:#888;">Блог</a></li>
                        <li><a href="delivery.html" style="color:#888;">Доставка</a></li>
                        <li><a href="contacts.html" style="color:#888;">Контакты</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color:white; margin-bottom:20px; font-size:1.1rem;">Партнерам</h4>
                    <ul style="list-style:none; line-height:2.2; font-size:0.9rem;">
                        <li><a href="b2b.html" style="color:#888;">Для кофеен</a></li>
                        <li><a href="b2b.html#office" style="color:#888;">Для офисов</a></li>
                        <li><a href="b2b.html#wholesale" style="color:#888;">Оптовые цены</a></li>
                    </ul>
                </div>
            </div>
            <div style="border-top:1px solid #333; padding-top:30px; display:flex; justify-content:space-between; flex-wrap:wrap; gap:20px; font-size:0.85rem;">
                <span>&copy; 2025 EthioDirect. Всі права захищені.</span>
                <div style="display:flex; gap:20px;">
                    <a href="privacy.html" style="color:#666;">Політика конфіденційності</a>
                    <a href="offer.html" style="color:#666;">Публічна оферта</a>
                </div>
            </div>
        </div>
    </footer>
    `;
    document.body.insertAdjacentHTML('beforeend', html);
}
