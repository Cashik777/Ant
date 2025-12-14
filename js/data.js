/* ===== ETHIODIRECT DATA v3.0 ===== */

const PRODUCTS = [
    {
        id: 1,
        name: 'Ethiopia Sidamo Gr.2',
        desc: 'Классический эфиопский кофе с нотами черники и какао. Идеален для эспрессо и молочных напитков.',
        price: 380,
        weight: 250,
        roast: 'medium',
        taste: ['chocolate', 'berry'],
        region: 'Sidamo',
        process: 'washed',
        image: 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=800',
        tags: ['Sidamo', 'Medium', 'Washed']
    },
    {
        id: 2,
        name: 'Yirgacheffe Kochere',
        desc: 'Яркий и цветочный. Ноты бергамота, жасмина и лимона. Лучший выбор для фильтра.',
        price: 420,
        weight: 250,
        roast: 'light',
        taste: ['floral', 'citrus'],
        region: 'Yirgacheffe',
        process: 'washed',
        image: 'https://images.unsplash.com/photo-1583689426955-f21509a25b2a?w=800',
        tags: ['Yirgacheffe', 'Light', 'Floral']
    },
    {
        id: 3,
        name: 'Guji Highland Natural',
        desc: 'Сладкий, как варенье. Ноты клубники, манго и меда. Натуральная обработка.',
        price: 450,
        weight: 250,
        roast: 'medium-light',
        taste: ['fruity', 'sweet'],
        region: 'Guji',
        process: 'natural',
        image: 'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=800',
        tags: ['Guji', 'Natural', 'Sweet']
    },
    {
        id: 4,
        name: 'Espresso House Blend',
        desc: 'Наш фирменный бленд для эспрессо. Плотное тело, шоколад, орехи. Стабильный вкус каждый раз.',
        price: 350,
        weight: 250,
        roast: 'medium-dark',
        taste: ['chocolate', 'nutty'],
        region: 'Blend',
        process: 'mixed',
        image: 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=600&q=80',
        tags: ['Blend', 'Espresso', 'Classic']
    },
    {
        id: 5,
        name: 'Limmu Washed',
        desc: 'Чистый и сбалансированный. Ноты зеленого яблока и карамели. Универсальный профиль.',
        price: 390,
        weight: 250,
        roast: 'medium',
        taste: ['balanced', 'fruity'],
        region: 'Limmu',
        process: 'washed',
        image: 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=600&q=80',
        tags: ['Limmu', 'Medium', 'Balanced']
    },
    {
        id: 6,
        name: 'Harrar Natural',
        desc: 'Дикий и необычный. Ноты черники, вина и специй. Для искателей приключений.',
        price: 480,
        weight: 250,
        roast: 'light',
        taste: ['wild', 'berry', 'wine'],
        region: 'Harrar',
        process: 'natural',
        image: 'https://images.unsplash.com/photo-1442512595331-e89e7385a861?auto=format&fit=crop&w=600&q=80',
        tags: ['Harrar', 'Natural', 'Wild']
    }
];

// Subscription Plans
const SUBSCRIPTION_PLANS = [
    { id: 'starter', name: 'Знакомство', bags: 1, price: 350, desc: '1 пачка в месяц' },
    { id: 'regular', name: 'Любитель', bags: 3, price: 900, desc: '3 пачки в месяц (популярный)' },
    { id: 'office', name: 'Офис', bags: 8, price: 2200, desc: '2 кг в месяц' }
];
