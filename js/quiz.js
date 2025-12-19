/* === COFFEE QUIZ LOGIC === */

const quizQuestions = [
    {
        id: 1,
        question: "Як ви зазвичай п'єте каву?",
        options: [
            { value: 'black', icon: '☕', title: 'Чорна кава', desc: 'Еспресо, фільтр, americana' },
            { value: 'milk', icon: '🥛', title: 'З молоком', desc: 'Капучино, лате, флет-вайт' },
            { value: 'alternative', icon: '⚗️', title: 'Альтернатива', desc: 'Кемекс, V60, аеропрес' }
        ]
    },
    {
        id: 2,
        question: "Яка кислинка вам подобається?",
        options: [
            { value: 'bright', icon: '🍋', title: 'Яскрава фруктова', desc: 'Як лимонад або ягоди' },
            { value: 'balanced', icon: '⚖️', title: 'Помірна збалансована', desc: 'Приємна, не домінуюча' },
            { value: 'minimal', icon: '🍫', title: 'Мінімальна', desc: 'Без кислинки, м\'яка' }
        ]
    },
    {
        id: 3,
        question: "Який смаковий профіль ви віддаєте перевагу?",
        options: [
            { value: 'fruity', icon: '🍓', title: 'Фруктові ноти', desc: 'Ягоди, цитрусові, тропічні фрукти' },
            { value: 'chocolate', icon: '🍫', title: 'Шоколадно-горіхові', desc: 'Какао, гор��хи, карамель' },
            { value: 'floral', icon: '🌸', title: 'Квіткові', desc: 'Жасмін, бергамот, делікатні' },
            { value: 'wine', icon: '🍷', title: 'Винні та складні', desc: 'Багатогранні, незвичайні' }
        ]
    },
    {
        id: 4,
        question: "Коли ви п'єте каву?",
        options: [
            { value: 'morning', icon: '🌅', title: 'Ранок', desc: 'Для енергії та пробудження' },
            { value: 'day', icon: '☀️', title: 'Протягом дня', desc: 'Для продуктивності' },
            { value: 'afternoon', icon: '🌆', title: 'Після обіду', desc: 'Для задоволення' }
        ]
    },
    {
        id: 5,
        question: "Скільки кави випиваєте на тиждень?",
        options: [
            { value: 'light', icon: '1️⃣', title: '1-7 чашок', desc: 'Помірне споживання' },
            { value: 'medium', icon: '2️⃣', title: '8-14 чашок', desc: 'Регулярне споживання' },
            { value: 'heavy', icon: '3️⃣', title: '15+ чашок', desc: 'Кавовий ентузіаст' }
        ]
    }
];

let currentQuestionIndex = 0;
let userAnswers = {};

// Initialize quiz
function initQuiz() {
    currentQuestionIndex = 0;
    userAnswers = {};
    renderQuestion();
}

// Render current question
function renderQuestion() {
    const question = quizQuestions[currentQuestionIndex];
    const progress = ((currentQuestionIndex + 1) / quizQuestions.length) * 100;

    // Update progress bar
    document.querySelector('.quiz-progress-bar').style.width = progress + '%';

    // Render question
    const html = `
        <div class="quiz-question">
            <p style="color:var(--text-muted); margin-bottom:10px; font-weight:600;">
                Питання ${currentQuestionIndex + 1} з ${quizQuestions.length}
            </p>
            <h3>${question.question}</h3>
            <div class="quiz-options">
                ${question.options.map(option => `
                    <div class="quiz-option" data-value="${option.value}" onclick="selectOption('${option.value}', ${question.id})">
                        <div class="quiz-option-icon">${option.icon}</div>
                        <div class="quiz-option-text">
                            <strong>${option.title}</strong>
                            <span>${option.desc}</span>
                        </div>
                    </div>
                `).join('')}
            </div>
            <div class="quiz-buttons">
                ${currentQuestionIndex > 0 ? `
                    <button class="btn btn-secondary" onclick="previousQuestion()">
                        <i class="fas fa-arrow-left"></i> Назад
                    </button>
                ` : ''}
            </div>
        </div>
    `;

    document.getElementById('quiz-content').innerHTML = html;

    // Restore previous answer if exists
    if (userAnswers[question.id]) {
        const selected = document.querySelector(`[data-value="${userAnswers[question.id]}"]`);
        if (selected) selected.classList.add('selected');
    }
}

// Select option
function selectOption(value, questionId) {
    userAnswers[questionId] = value;

    // Visual feedback
    document.querySelectorAll('.quiz-option').forEach(opt => opt.classList.remove('selected'));
    event.currentTarget.classList.add('selected');

    // Auto advance after short delay
    setTimeout(() => {
        if (currentQuestionIndex < quizQuestions.length - 1) {
            nextQuestion();
        } else {
            showResults();
        }
    }, 300);
}

// Next question
function nextQuestion() {
    currentQuestionIndex++;
    renderQuestion();
}

// Previous question
function previousQuestion() {
    currentQuestionIndex--;
    renderQuestion();
}

// Calculate recommendation
function getRecommendation() {
    const answers = userAnswers;

    // Simple recommendation logic
    if (answers[2] === 'bright' && answers[3] === 'fruity') {
        return PRODUCTS.find(p => p.name.includes('Yirgacheffe')) || PRODUCTS[1];
    } else if (answers[1] === 'milk' && answers[3] === 'chocolate') {
        return PRODUCTS.find(p => p.name.includes('Sidamo')) || PRODUCTS[0];
    } else if (answers[2] === 'minimal' && answers[3] === 'chocolate') {
        return PRODUCTS.find(p => p.name.includes('Espresso')) || PRODUCTS[3];
    } else if (answers[1] === 'alternative' && answers[3] === 'fruity') {
        return PRODUCTS.find(p => p.name.includes('Guji')) || PRODUCTS[2];
    } else if (answers[3] === 'wine') {
        return PRODUCTS.find(p => p.name.includes('Harrar')) || PRODUCTS[5];
    } else {
        return PRODUCTS.find(p => p.name.includes('Limmu')) || PRODUCTS[4];
    }
}

// Show results
function showResults() {
    const product = getRecommendation();
    const consumption = userAnswers[5];

    const subscribeBags = consumption === 'light' ? 1 : consumption === 'medium' ? 2 : 4;

    const html = `
        <div class="quiz-result">
            <h2 style="margin-bottom:20px;">Ваша ідеальна кава! 🎉</h2>
            
            <div class="quiz-result-product">
                <img src="${product.image}" alt="${product.name}">
                <h2>${product.name}</h2>
                <p style="font-size:1.1rem; color:var(--text-light); margin-bottom:20px;">${product.desc}</p>
                
                <div class="quiz-result-profile">
                    <span class="profile-tag">🔥 ${product.roast}</span>
                    <span class="profile-tag">📍 ${product.region}</span>
                    <span class="profile-tag">⚙️ ${product.process}</span>
                </div>
                
                <div style="font-size:2rem; color:var(--secondary); font-weight:700; margin:20px 0;">
                    ${product.price} ₴
                </div>
            </div>
            
            <div class="quiz-result-why">
                <h4>Чому саме цей сорт?</h4>
                <p>На основі ваших відповідей, ${product.name} ідеально підходить для вас. Цей сорт має те, що ви шукаєте: правильний баланс смаку, обсмажки та методу приготування.</p>
            </div>
            
            <div style="display:flex; gap:15px; justify-content:center; flex-wrap:wrap; margin-top:40px;">
                <button class="btn btn-primary btn-large" onclick="addToCart({
                    id: ${product.id},
                    name: '${product.name}',
                    price: ${product.price},
                    weight: ${product.weight},
                    image: '${product.image}'
                })">
                    <i class="fas fa-shopping-bag"></i>
                    Купити зараз — ${product.price}₴
                </button>
                <a href="subscription.html?product=${product.id}&bags=${subscribeBags}" class="btn btn-secondary btn-large">
                    <i class="fas fa-star"></i>
                    Підписка зі знижкою 10%
                </a>
            </div>
            
            <button class="btn btn-text" onclick="initQuiz()" style="margin-top:30px;">
                <i class="fas fa-redo"></i> Пройти тест заново
            </button>
        </div>
    `;

    document.getElementById('quiz-content').innerHTML = html;
    document.querySelector('.quiz-progress-bar').style.width = '100%';

    // Store result in localStorage
    localStorage.setItem('quizResult', JSON.stringify({
        product: product,
        answers: userAnswers,
        date: new Date().toISOString()
    }));
}

// Make functions global
window.initQuiz = initQuiz;
window.selectOption = selectOption;
window.nextQuestion = nextQuestion;
window.previousQuestion = previousQuestion;

// Auto-start quiz on page load
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initQuiz);
} else {
    initQuiz();
}
