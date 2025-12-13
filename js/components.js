/* ===== COMPONENTS INJECTION ===== */

document.addEventListener('DOMContentLoaded', () => {
    injectHeader();
    injectFooter();
    updateCartBadge();
    initMobileMenu();
    highlightActiveLink();
});

function injectHeader() {
    const headerHTML = `
    <header class="main-header">
        <div class="container header-inner">
            <a href="index.html" class="logo">
                <i class="fas fa-coffee"></i>
                <span>EthioDirect</span>
            </a>
            
            <nav class="nav-menu" id="navMenu">
                <a href="index.html" class="nav-link" data-page="home">Главная</a>
                <a href="shop.html" class="nav-link" data-page="shop">Магазин</a>
                <a href="subscription.html" class="nav-link" data-page="subscription">Подписка</a>
                <a href="about.html" class="nav-link" data-page="about">О кофе</a>
                <a href="b2b.html" class="nav-link" data-page="b2b">B2B</a>
                <a href="contacts.html" class="nav-link" data-page="contacts">Контакты</a>
            </nav>
            
            <div class="header-actions">
                <a href="account.html" class="icon-btn" title="Личный кабинет">
                    <i class="far fa-user"></i>
                </a>
                <a href="cart.html" class="icon-btn" title="Корзина">
                    <i class="fas fa-shopping-bag"></i>
                    <span class="badge" id="cartBadge">0</span>
                </a>
                <div class="mobile-toggle" id="mobileToggle" style="display: none;">
                    <i class="fas fa-bars"></i>
                </div>
            </div>
        </div>
    </header>
    `;

    // Вставляем хедер в начало body
    document.body.insertAdjacentHTML('afterbegin', headerHTML);
}

function injectFooter() {
    const footerHTML = `
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-about">
                    <div class="logo mb-2" style="color: white;">
                        <i class="fas fa-coffee" style="color: var(--secondary);"></i>
                        <span>EthioDirect</span>
                    </div>
                    <p>Прямые поставки премиального кофе с высокогорий Эфиопии. Обжарка в Одессе перед отправкой.</p>
                    <div class="social-links">
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-facebook-f"></i></a>
                        <a href="#"><i class="fab fa-telegram-plane"></i></a>
                    </div>
                </div>
                
                <div class="footer-col">
                    <h4>Магазин</h4>
                    <ul>
                        <li><a href="shop.html?type=all">Весь кофе</a></li>
                        <li><a href="shop.html?type=grain">В зёрнах</a></li>
                        <li><a href="shop.html?type=ground">Молотый</a></li>
                        <li><a href="shop.html?type=capsules">Капсулы</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h4>Клиентам</h4>
                    <ul>
                        <li><a href="subscription.html">Подписка</a></li>
                        <li><a href="delivery.html">Доставка и оплата</a></li>
                        <li><a href="blog.html">Блог</a></li>
                        <li><a href="account.html">Личный кабинет</a></li>
                    </ul>
                </div>
                
                <div class="footer-col">
                    <h4>Контакты</h4>
                    <ul>
                        <li><a href="tel:+380000000000">+380 (XX) XXX-XX-XX</a></li>
                        <li><a href="mailto:hello@ethiodirect.ua">hello@ethiodirect.ua</a></li>
                        <li>Одесса, Украина</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2025 EthioDirect. Все права защищены.</p>
            </div>
        </div>
    </footer>
    `;

    // Вставляем футер перед закрывающим тегом body, но скрипты обычно в конце, поэтому просто appendChild
    document.body.insertAdjacentHTML('beforeend', footerHTML);
}

function initMobileMenu() {
    // Ждем небольшой таймаут, так как хедер вставляется динамически
    setTimeout(() => {
        const toggle = document.getElementById('mobileToggle');
        const menu = document.getElementById('navMenu');

        if (toggle && menu) {
            toggle.addEventListener('click', () => {
                menu.classList.toggle('active');
                const i = toggle.querySelector('i');
                if (menu.classList.contains('active')) {
                    i.classList.remove('fa-bars');
                    i.classList.add('fa-times');
                } else {
                    i.classList.remove('fa-times');
                    i.classList.add('fa-bars');
                }
            });
        }
    }, 100);
}

function highlightActiveLink() {
    setTimeout(() => {
        const path = window.location.pathname;
        const page = path.split('/').pop().replace('.html', '') || 'home';

        const links = document.querySelectorAll('.nav-link');
        links.forEach(link => {
            if (link.dataset.page === page) {
                link.classList.add('active');
            }
        });
    }, 100);
}

function updateCartBadge() {
    // В будущем будет брать данные из localStorage
    const count = 0;
    setTimeout(() => {
        const badge = document.getElementById('cartBadge');
        if (badge) badge.innerText = count;
    }, 100);
}
