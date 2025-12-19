/* === TESTIMONIALS CAROUSEL LOGIC === */

let currentSlide = 0;
const testimonials = [
    {
        text: "Це не просто напій, це подорож. Я відчула різницю з першого ковтка. Тепер магазинна кава для мене просто не існує.",
        author: "Олена Кравченко",
        location: "Київ",
        product: "Guji Natural",
        avatar: "https://i.pravatar.cc/150?img=1",
        rating: 5
    },
    {
        text: "Швидка доставка і неймовірний аромат, який наповнює всю квартиру. Підписка — найкраще рішення для кавоманів!",
        author: "Андрій Мельник",
        location: "Львів",
        product: "Yirgacheffe",
        avatar: "https://i.pravatar.cc/150?img=12",
        rating: 5
    },
    {
        text: "Сервіс на висоті. Дуже зручно, що не треба думати, коли замовляти наступну пачку. А смак — просто космос!",
        author: "Марина Сидоренко",
        location: "Одеса",
        product: "Sidamo Gr.2",
        avatar: "https://i.pravatar.cc/150?img=5",
        rating: 5
    },
    {
        text: "Дякую за можливість спробувати різні сорти! Харрар — це мій фаворит. Винний, насичений, унікальний.",
        author: "Віктор Петренко",
        location: "Київ",
        product: "Harrar Natural",
        avatar: "https://i.pravatar.cc/150?img=14",
        rating: 5
    }
];

function initTestimonialsCarousel() {
    const container = document.querySelector('.testimonials-carousel');
    if (!container) return;

    renderCarousel();

    // Auto-play
    setInterval(() => {
        nextSlide();
    }, 5000);
}

function renderCarousel() {
    const container = document.querySelector('.testimonials-carousel');
    if (!container) return;

    const html = `
        <button class="carousel-btn prev" onclick="prevSlide()">
            <i class="fas fa-chevron-left"></i>
        </button>
        
        <div class="carousel-track" id="carousel-track">
            ${testimonials.map((t, index) => `
                <div class="carousel-slide">
                    <div class="testimonial-card-featured">
                        <img src="${t.avatar}" alt="${t.author}" class="testimonial-avatar">
                        <div class="testimonial-rating">
                            ${'★'.repeat(t.rating)}
                        </div>
                        <p class="testimonial-text">"${t.text}"</p>
                        <div class="testimonial-author">${t.author}</div>
                        <div class="testimonial-location">${t.location} • ${t.product}</div>
                    </div>
                </div>
            `).join('')}
        </div>
        
        <button class="carousel-btn next" onclick="nextSlide()">
            <i class="fas fa-chevron-right"></i>
        </button>
        
        <div class="carousel-dots">
            ${testimonials.map((_, index) => `
                <div class="carousel-dot ${index === 0 ? 'active' : ''}" onclick="goToSlide(${index})"></div>
            `).join('')}
        </div>
    `;

    container.innerHTML = html;
}

function updateCarousel() {
    const track = document.getElementById('carousel-track');
    const dots = document.querySelectorAll('.carousel-dot');

    if (track) {
        track.style.transform = `translateX(-${currentSlide * 100}%)`;
    }

    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentSlide);
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % testimonials.length;
    updateCarousel();
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + testimonials.length) % testimonials.length;
    updateCarousel();
}

function goToSlide(index) {
    currentSlide = index;
    updateCarousel();
}

// Make functions global
window.nextSlide = nextSlide;
window.prevSlide = prevSlide;
window.goToSlide = goToSlide;

// Initialize on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTestimonialsCarousel);
} else {
    initTestimonialsCarousel();
}
