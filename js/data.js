/* ===== MOCK DATA ===== */

const PRODUCTS = [
    {
        id: 1,
        name: 'Sidamo Gr.2',
        type: 'grain',
        roast: 'medium',
        price: 380,
        weight: 250,
        image: 'https://images.unsplash.com/photo-1587734195507-6b7c8b6a3e5a?auto=format&fit=crop&w=600&q=80',
        tags: ['Fruity', 'Floral'],
        desc: 'Яркие ноты лимона и бергамота с цветочным послевкусием.'
    },
    {
        id: 2,
        name: 'Yirgacheffe Kochere',
        type: 'grain',
        roast: 'light',
        price: 420,
        weight: 250,
        image: 'https://images.unsplash.com/photo-1510707577719-ae7c9b788690?auto=format&fit=crop&w=600&q=80',
        tags: ['Berry', 'Tea-like'],
        desc: 'Легендарный сорт. Чайное тело, ноты жасмина и персика.'
    },
    {
        id: 3,
        name: 'Harrar Longberry',
        type: 'grain',
        roast: 'dark',
        price: 400,
        weight: 250,
        image: 'https://images.unsplash.com/photo-1511537190424-bbbab87ac5eb?auto=format&fit=crop&w=600&q=80',
        tags: ['Chocolate', 'Spicy'],
        desc: 'Древний сорт. Насыщенный вкус шоколада и черники. Идеален для эспрессо.'
    },
    {
        id: 4,
        name: 'Guji Highland',
        type: 'grain',
        roast: 'medium',
        price: 450,
        weight: 250,
        image: 'https://images.unsplash.com/photo-1621262974917-76b4a39f60af?auto=format&fit=crop&w=600&q=80',
        tags: ['Sweet', 'Complex'],
        desc: 'Сложный букет с оттенками клубники и темного шоколада.'
    },
    {
        id: 5,
        name: 'Espresso Blend',
        type: 'ground',
        roast: 'dark',
        price: 350,
        weight: 500,
        image: 'https://images.unsplash.com/photo-1517487881594-2787fef5ebf7?auto=format&fit=crop&w=600&q=80',
        tags: ['Strong', 'Classic'],
        desc: 'Авторская смесь для утреннего пробуждения. Плотная крема.'
    },
    {
        id: 6,
        name: 'Drip Packs (10pcs)',
        type: 'capsules',
        roast: 'medium',
        price: 300,
        weight: 120,
        image: 'https://images.unsplash.com/photo-1627521741517-5bd2789196b2?auto=format&fit=crop&w=600&q=80',
        tags: ['Convenient', 'Travel'],
        desc: 'Удобный дрип-кофе в дорогу. Микс лучших эфиопских сортов.'
    }
];

const SUBSCRIPTION_PLANS = [
    {
        id: 'start',
        name: 'Знакомство',
        desc: '1 пачка (250г) в месяц. Идеально для начала.',
        price: 350
    },
    {
        id: 'lover',
        name: 'Любитель',
        desc: '3 пачки (750г) в месяц. Хватит на каждое утро.',
        price: 950
    },
    {
        id: 'pro',
        name: 'Профи',
        desc: '2кг в месяц. Для большой семьи или офиса.',
        price: 2400
    }
];
