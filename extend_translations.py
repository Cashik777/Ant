# Add comprehensive translations for quiz, about, contacts, and all pages
# This script extends translations.js with complete page content translations

quiz_translations_uk = """
        // Quiz page - content
        quiz_badge: '5 ПИТАНЬ • 2 ХВИЛИНИ',
        quiz_title: 'Знайдіть свою ідеальну каву',
        quiz_subtitle: 'Відповідайте на прості питання — і ми підберемо сорт, який точно вам сподобається',
        quiz_benefit1: 'Знижка -10% на результат',
        quiz_benefit2: 'Миттєва рекомендація',
        quiz_benefit3: '98% точність',
        quiz_step1: 'Спосіб',
        quiz_step2: 'Смак',
        quiz_step3: 'Метод',
        quiz_step4: 'Міцність',
        quiz_step5: 'Обсяг',
        quiz_q1: 'Як ви зазвичай п\\'єте каву?',
        quiz_q1_sub: 'Оберіть найближчий варіант',
        quiz_q1_opt1: 'Чорна, без нічого',
        quiz_q1_opt1_desc: 'Максимальний смак зерна',
        quiz_q1_opt2: 'З молоком',
        quiz_q1_opt2_desc: 'Капучіно, лате, флет-вайт',
        quiz_q1_opt3: 'З молоком і цукром',
        quiz_q1_opt3_desc: 'Солодко та ніжно',
        quiz_q2: 'Які смаки вам подобаються?',
        quiz_q2_sub: 'Оберіть улюблений профіль',
        quiz_q2_opt1: 'Фруктові, ягідні',
        quiz_q2_opt1_desc: 'Яскрава кислинка, свіжість',
        quiz_q2_opt2: 'Шоколадні, горіхові',
        quiz_q2_opt2_desc: 'Класичний, насичений смак',
        quiz_q2_opt3: 'Квіткові, чайні',
        quiz_q2_opt3_desc: 'Ніжний, делікатний аромат',
        quiz_q3: 'Як ви готуєте каву вдома?',
        quiz_q3_sub: 'Від цього залежить рекомендація обсмажки',
        quiz_q3_opt1: 'Еспресо-машина',
        quiz_q3_opt1_desc: 'Автомат або ріжкова',
        quiz_q3_opt2: 'Пуровер / Кемекс',
        quiz_q3_opt2_desc: 'Фільтр-методи',
        quiz_q3_opt3: 'Турка / Мока',
        quiz_q3_opt3_desc: 'Традиційний спосіб',
        quiz_q3_opt4: 'Френч-прес',
        quiz_q3_opt4_desc: 'Імерсійне заварювання',
        quiz_q4: 'Наскільки міцну каву ви любите?',
        quiz_q4_sub: 'Це вплине на рекомендацію обсмажки',
        quiz_next: 'Далі',
        quiz_back: 'Назад',
        quiz_result_title: 'Ваша ідеальна кава:',
        quiz_add_to_cart: 'Додати до кошика',
        quiz_restart: 'Пройти тест знову',

        // About page - content
        about_badge: 'НАША ІСТОРІЯ',
        about_title: 'Від ефіопських гір до вашої чашки',
        about_text: 'Ми — команда кавоманів, які побудували прямий ланцюг поставок з Ефіопії, щоб ви могли насолоджуватися справжнім смаком specialty кави без посередників.',
        about_feature1: 'Прямі закупки',
        about_feature2: 'Свіжа обсмажка',
        about_feature3: '85+ балів SCA',
        about_stat1: 'Задоволених клієнтів',
        about_stat2: 'Балів SCA Specialty',
        about_stat3: 'Від замовлення до доставки',
        about_stat4: 'Пряме походження',
        about_why_title: 'Чому Ефіопія?',
        about_why_text1: 'Ефіопія — батьківщина кави. Саме тут, на висотах 1800-2200 метрів, зростають унікальні сорти Арабіки, яких немає більше ніде у світі.',
        about_why_text2: 'Кожен наш лот — це окрема історія, окремий терруар, окремий смаковий профіль.',
        about_floral: 'Квіткові ноти',
        about_berry: 'Ягідний смак',
        about_chocolate: 'Шоколадна солодкість',
        about_values_title: 'Наші цінності',
        about_value1_title: 'Свіжа обсмажка',
        about_value1_text: 'Смажимо лише під замовлення. Ви отримуєте каву на піку її смаку.',
        about_value2_title: 'Чесна торгівля',
        about_value2_text: 'Працюємо напряму з фермерами і платимо справедливу ціну.',
        about_value3_title: 'Тільки Specialty',
        about_value3_text: '85+ балів за шкалою SCA. Це лише 3% кави у світі.',
        about_journey_title: 'Наш шлях',
        about_process_title: 'Наш процес',
        about_team_title: 'Наша команда',
        about_cta_title: 'Готові спробувати?',
        about_cta_text: 'Приєднуйтесь до 2500+ кавоманів, які вже обрали EthioDirect',
        about_cta_btn: 'Обрати свою каву',
        about_contact_btn: "Зв'язатися з нами",

        // Contacts page - content
        contacts_badge: 'Ми на зв\\'язку',
        contacts_title: 'Контакти',
        contacts_subtitle: 'Маєте питання, пропозиції або хочете замовити каву для офісу? Напишіть нам!',
        contacts_phone: 'Телефон',
        contacts_phone_hours: 'Пн-Пт: 9:00-18:00',
        contacts_email: 'Email',
        contacts_email_response: 'Відповідаємо протягом 24 годин',
        contacts_address: 'Адреса',
        contacts_address_desc: 'Пункт видачі та офіс',
        contacts_messengers: 'Месенджери',
        contacts_form_title: 'Напишіть нам',
        contacts_form_name: "Ім'я",
        contacts_form_name_placeholder: "Ваше ім'я",
        contacts_form_email: 'Email',
        contacts_form_topic: 'Тема',
        contacts_form_topic_general: 'Загальне питання',
        contacts_form_topic_order: 'Питання по замовленню',
        contacts_form_topic_b2b: 'B2B / Оптові закупки',
        contacts_form_topic_collab: 'Співпраця',
        contacts_form_topic_other: 'Інше',
        contacts_form_message: 'Повідомлення',
        contacts_form_message_placeholder: 'Ваше повідомлення...',
        contacts_form_send: 'Надіслати',
        contacts_social_title: 'Слідкуйте за нами',
"""

quiz_translations_ru = """
        // Quiz page - content
        quiz_badge: '5 ВОПРОСОВ • 2 МИНУТЫ',
        quiz_title: 'Найдите свой идеальный кофе',
        quiz_subtitle: 'Ответьте на простые вопросы — и мы подберём сорт, который точно вам понравится',
        quiz_benefit1: 'Скидка -10% на результат',
        quiz_benefit2: 'Мгновенная рекомендация',
        quiz_benefit3: '98% точность',
        quiz_step1: 'Способ',
        quiz_step2: 'Вкус',
        quiz_step3: 'Метод',
        quiz_step4: 'Крепость',
        quiz_step5: 'Объём',
        quiz_q1: 'Как вы обычно пьёте кофе?',
        quiz_q1_sub: 'Выберите ближайший вариант',
        quiz_q1_opt1: 'Чёрный, без ничего',
        quiz_q1_opt1_desc: 'Максимальный вкус зерна',
        quiz_q1_opt2: 'С молоком',
        quiz_q1_opt2_desc: 'Капучино, латте, флэт-уайт',
        quiz_q1_opt3: 'С молоком и сахаром',
        quiz_q1_opt3_desc: 'Сладко и нежно',
        quiz_q2: 'Какие вкусы вам нравятся?',
        quiz_q2_sub: 'Выберите любимый профиль',
        quiz_q2_opt1: 'Фруктовые, ягодные',
        quiz_q2_opt1_desc: 'Яркая кислинка, свежесть',
        quiz_q2_opt2: 'Шоколадные, ореховые',
        quiz_q2_opt2_desc: 'Классический, насыщенный вкус',
        quiz_q2_opt3: 'Цветочные, чайные',
        quiz_q2_opt3_desc: 'Нежный, деликатный аромат',
        quiz_q3: 'Как вы готовите кофе дома?',
        quiz_q3_sub: 'От этого зависит рекомендация обжарки',
        quiz_q3_opt1: 'Эспрессо-машина',
        quiz_q3_opt1_desc: 'Автомат или рожковая',
        quiz_q3_opt2: 'Пуровер / Кемекс',
        quiz_q3_opt2_desc: 'Фильтр-методы',
        quiz_q3_opt3: 'Турка / Мока',
        quiz_q3_opt3_desc: 'Традиционный способ',
        quiz_q3_opt4: 'Френч-пресс',
        quiz_q3_opt4_desc: 'Иммерсионное заваривание',
        quiz_q4: 'Насколько крепкий кофе вы любите?',
        quiz_q4_sub: 'Это повлияет на рекомендацию обжарки',
        quiz_next: 'Далее',
        quiz_back: 'Назад',
        quiz_result_title: 'Ваш идеальный кофе:',
        quiz_add_to_cart: 'Добавить в корзину',
        quiz_restart: 'Пройти тест снова',

        // About page - content
        about_badge: 'НАША ИСТОРИЯ',
        about_title: 'От эфиопских гор до вашей чашки',
        about_text: 'Мы — команда кофеманов, которые построили прямую цепочку поставок из Эфиопии, чтобы вы могли наслаждаться настоящим вкусом specialty кофе без посредников.',
        about_feature1: 'Прямые закупки',
        about_feature2: 'Свежая обжарка',
        about_feature3: '85+ баллов SCA',
        about_stat1: 'Довольных клиентов',
        about_stat2: 'Баллов SCA Specialty',
        about_stat3: 'От заказа до доставки',
        about_stat4: 'Прямое происхождение',
        about_why_title: 'Почему Эфиопия?',
        about_why_text1: 'Эфиопия — родина кофе. Именно здесь, на высотах 1800-2200 метров, растут уникальные сорта Арабики, которых нет больше нигде в мире.',
        about_why_text2: 'Каждый наш лот — это отдельная история, отдельный терруар, отдельный вкусовой профиль.',
        about_floral: 'Цветочные ноты',
        about_berry: 'Ягодный вкус',
        about_chocolate: 'Шоколадная сладость',
        about_values_title: 'Наши ценности',
        about_value1_title: 'Свежая обжарка',
        about_value1_text: 'Обжариваем только под заказ. Вы получаете кофе на пике его вкуса.',
        about_value2_title: 'Честная торговля',
        about_value2_text: 'Работаем напрямую с фермерами и платим справедливую цену.',
        about_value3_title: 'Только Specialty',
        about_value3_text: '85+ баллов по шкале SCA. Это лишь 3% кофе в мире.',
        about_journey_title: 'Наш путь',
        about_process_title: 'Наш процесс',
        about_team_title: 'Наша команда',
        about_cta_title: 'Готовы попробовать?',
        about_cta_text: 'Присоединяйтесь к 2500+ кофеманов, которые уже выбрали EthioDirect',
        about_cta_btn: 'Выбрать свой кофе',
        about_contact_btn: 'Связаться с нами',

        // Contacts page - content
        contacts_badge: 'Мы на связи',
        contacts_title: 'Контакты',
        contacts_subtitle: 'Есть вопросы, предложения или хотите заказать кофе для офиса? Напишите нам!',
        contacts_phone: 'Телефон',
        contacts_phone_hours: 'Пн-Пт: 9:00-18:00',
        contacts_email: 'Email',
        contacts_email_response: 'Отвечаем в течение 24 часов',
        contacts_address: 'Адрес',
        contacts_address_desc: 'Пункт выдачи и офис',
        contacts_messengers: 'Мессенджеры',
        contacts_form_title: 'Напишите нам',
        contacts_form_name: 'Имя',
        contacts_form_name_placeholder: 'Ваше имя',
        contacts_form_email: 'Email',
        contacts_form_topic: 'Тема',
        contacts_form_topic_general: 'Общий вопрос',
        contacts_form_topic_order: 'Вопрос по заказу',
        contacts_form_topic_b2b: 'B2B / Оптовые закупки',
        contacts_form_topic_collab: 'Сотрудничество',
        contacts_form_topic_other: 'Другое',
        contacts_form_message: 'Сообщение',
        contacts_form_message_placeholder: 'Ваше сообщение...',
        contacts_form_send: 'Отправить',
        contacts_social_title: 'Следите за нами',
"""

quiz_translations_en = """
        // Quiz page - content
        quiz_badge: '5 QUESTIONS • 2 MINUTES',
        quiz_title: 'Find Your Perfect Coffee',
        quiz_subtitle: 'Answer simple questions — and we will find the perfect coffee for you',
        quiz_benefit1: '-10% discount on result',
        quiz_benefit2: 'Instant recommendation',
        quiz_benefit3: '98% accuracy',
        quiz_step1: 'Style',
        quiz_step2: 'Taste',
        quiz_step3: 'Method',
        quiz_step4: 'Strength',
        quiz_step5: 'Volume',
        quiz_q1: 'How do you usually drink coffee?',
        quiz_q1_sub: 'Choose the closest option',
        quiz_q1_opt1: 'Black, nothing added',
        quiz_q1_opt1_desc: 'Maximum bean flavor',
        quiz_q1_opt2: 'With milk',
        quiz_q1_opt2_desc: 'Cappuccino, latte, flat white',
        quiz_q1_opt3: 'With milk and sugar',
        quiz_q1_opt3_desc: 'Sweet and gentle',
        quiz_q2: 'What flavors do you like?',
        quiz_q2_sub: 'Choose your favorite profile',
        quiz_q2_opt1: 'Fruity, berry',
        quiz_q2_opt1_desc: 'Bright acidity, freshness',
        quiz_q2_opt2: 'Chocolate, nutty',
        quiz_q2_opt2_desc: 'Classic, rich taste',
        quiz_q2_opt3: 'Floral, tea-like',
        quiz_q2_opt3_desc: 'Gentle, delicate aroma',
        quiz_q3: 'How do you brew coffee at home?',
        quiz_q3_sub: 'This affects roast recommendation',
        quiz_q3_opt1: 'Espresso machine',
        quiz_q3_opt1_desc: 'Automatic or manual',
        quiz_q3_opt2: 'Pour over / Chemex',
        quiz_q3_opt2_desc: 'Filter methods',
        quiz_q3_opt3: 'Turkish / Moka',
        quiz_q3_opt3_desc: 'Traditional way',
        quiz_q3_opt4: 'French press',
        quiz_q3_opt4_desc: 'Immersion brewing',
        quiz_q4: 'How strong do you like your coffee?',
        quiz_q4_sub: 'This will affect roast recommendation',
        quiz_next: 'Next',
        quiz_back: 'Back',
        quiz_result_title: 'Your perfect coffee:',
        quiz_add_to_cart: 'Add to Cart',
        quiz_restart: 'Take Quiz Again',

        // About page - content
        about_badge: 'OUR STORY',
        about_title: 'From Ethiopian Mountains to Your Cup',
        about_text: "We're a team of coffee lovers who built a direct supply chain from Ethiopia, so you can enjoy the real taste of specialty coffee without middlemen.",
        about_feature1: 'Direct purchases',
        about_feature2: 'Fresh roast',
        about_feature3: '85+ SCA points',
        about_stat1: 'Happy Customers',
        about_stat2: 'SCA Specialty Points',
        about_stat3: 'Order to Delivery',
        about_stat4: 'Direct Origin',
        about_why_title: 'Why Ethiopia?',
        about_why_text1: "Ethiopia is the birthplace of coffee. Here, at 1800-2200 meters altitude, grow unique Arabica varieties found nowhere else in the world.",
        about_why_text2: 'Each of our lots is a separate story, a separate terroir, a separate flavor profile.',
        about_floral: 'Floral notes',
        about_berry: 'Berry taste',
        about_chocolate: 'Chocolate sweetness',
        about_values_title: 'Our Values',
        about_value1_title: 'Fresh Roast',
        about_value1_text: 'We roast only to order. You get coffee at its peak flavor.',
        about_value2_title: 'Fair Trade',
        about_value2_text: 'We work directly with farmers and pay a fair price.',
        about_value3_title: 'Only Specialty',
        about_value3_text: '85+ points on SCA scale. This is only 3% of coffee in the world.',
        about_journey_title: 'Our Journey',
        about_process_title: 'Our Process',
        about_team_title: 'Our Team',
        about_cta_title: 'Ready to Try?',
        about_cta_text: 'Join 2500+ coffee lovers who already chose EthioDirect',
        about_cta_btn: 'Choose Your Coffee',
        about_contact_btn: 'Contact Us',

        // Contacts page - content
        contacts_badge: "We're here for you",
        contacts_title: 'Contact Us',
        contacts_subtitle: 'Have questions, suggestions or want to order coffee for your office? Write to us!',
        contacts_phone: 'Phone',
        contacts_phone_hours: 'Mon-Fri: 9:00-18:00',
        contacts_email: 'Email',
        contacts_email_response: 'We respond within 24 hours',
        contacts_address: 'Address',
        contacts_address_desc: 'Pickup point and office',
        contacts_messengers: 'Messengers',
        contacts_form_title: 'Write to Us',
        contacts_form_name: 'Name',
        contacts_form_name_placeholder: 'Your name',
        contacts_form_email: 'Email',
        contacts_form_topic: 'Subject',
        contacts_form_topic_general: 'General question',
        contacts_form_topic_order: 'Order question',
        contacts_form_topic_b2b: 'B2B / Wholesale',
        contacts_form_topic_collab: 'Collaboration',
        contacts_form_topic_other: 'Other',
        contacts_form_message: 'Message',
        contacts_form_message_placeholder: 'Your message...',
        contacts_form_send: 'Send',
        contacts_social_title: 'Follow Us',
"""

# Create translation extension
translation_extension = '''
    // 26. Translate Quiz page 
    const quizBadge = document.querySelector('.quiz-badge');
    if (quizBadge) quizBadge.innerHTML = `<i class="fas fa-magic"></i> ${t.quiz_badge}`;
    
    const quizH1 = document.querySelector('.quiz-hero h1');
    if (quizH1) quizH1.innerHTML = t.quiz_title.replace(' ', '<br>');
    
    const quizSubtitle = document.querySelector('.quiz-hero-content > p');
    if (quizSubtitle) quizSubtitle.textContent = t.quiz_subtitle;
    
    const benefitPills = document.querySelectorAll('.benefit-pill');
    if (benefitPills.length >= 3) {
        benefitPills[0].innerHTML = `<i class="fas fa-gift"></i> ${t.quiz_benefit1}`;
        benefitPills[1].innerHTML = `<i class="fas fa-bolt"></i> ${t.quiz_benefit2}`;
        benefitPills[2].innerHTML = `<i class="fas fa-thumbs-up"></i> ${t.quiz_benefit3}`;
    }
    
    const stepLabels = document.querySelectorAll('.step-label');
    if (stepLabels.length >= 5) {
        stepLabels[0].textContent = t.quiz_step1;
        stepLabels[1].textContent = t.quiz_step2;
        stepLabels[2].textContent = t.quiz_step3;
        stepLabels[3].textContent = t.quiz_step4;
        stepLabels[4].textContent = t.quiz_step5;
    }

    // 27. Translate About page
    const aboutBadge = document.querySelector('.hero-badge');
    if (aboutBadge && document.querySelector('.about-hero')) {
        aboutBadge.innerHTML = `<i class="fas fa-heart"></i> ${t.about_badge}`;
    }
    
    const aboutH1 = document.querySelector('.about-hero h1');
    if (aboutH1) aboutH1.textContent = t.about_title;
    
    const aboutText = document.querySelector('.hero-text');
    if (aboutText && document.querySelector('.about-hero')) {
        aboutText.textContent = t.about_text;
    }
    
    const heroFeatures = document.querySelectorAll('.hero-feature');
    if (heroFeatures.length >= 3 && document.querySelector('.about-hero')) {
        heroFeatures[0].innerHTML = `<i class="fas fa-check-circle"></i> ${t.about_feature1}`;
        heroFeatures[1].innerHTML = `<i class="fas fa-check-circle"></i> ${t.about_feature2}`;
        heroFeatures[2].innerHTML = `<i class="fas fa-check-circle"></i> ${t.about_feature3}`;
    }
    
    const statLabels = document.querySelectorAll('.stat-label');
    if (statLabels.length >= 4) {
        statLabels[0].textContent = t.about_stat1;
        statLabels[1].textContent = t.about_stat2;
        statLabels[2].textContent = t.about_stat3;
        statLabels[3].textContent = t.about_stat4;
    }
    
    const missionH2 = document.querySelector('.mission-content h2');
    if (missionH2) missionH2.textContent = t.about_why_title;
    
    const valueCards = document.querySelectorAll('.value-card');
    if (valueCards.length >= 3) {
        valueCards[0].querySelector('h3').textContent = t.about_value1_title;
        valueCards[0].querySelector('p').textContent = t.about_value1_text;
        valueCards[1].querySelector('h3').textContent = t.about_value2_title;
        valueCards[1].querySelector('p').textContent = t.about_value2_text;
        valueCards[2].querySelector('h3').textContent = t.about_value3_title;
        valueCards[2].querySelector('p').textContent = t.about_value3_text;
    }

    // 28. Translate Contacts page
    const contactsBadge = document.querySelector('.section .badge');
    if (contactsBadge && window.location.href.includes('contacts')) {
        contactsBadge.textContent = t.contacts_badge;
    }
    
    const contactsH1 = document.querySelector('main h1');
    if (contactsH1 && window.location.href.includes('contacts')) {
        contactsH1.textContent = t.contacts_title;
    }
    
    const contactCards = document.querySelectorAll('.contact-card h3');
    if (contactCards.length >= 4) {
        contactCards[0].textContent = t.contacts_phone;
        contactCards[1].textContent = t.contacts_email;
        contactCards[2].textContent = t.contacts_address;
        contactCards[3].textContent = t.contacts_messengers;
    }
    
    const contactFormH2 = document.querySelector('.contact-form')?.closest('.section')?.querySelector('h2');
    if (contactFormH2) contactFormH2.textContent = t.contacts_form_title;
    
    const socialTitle = document.querySelector('.section.bg-white.text-center h2');
    if (socialTitle && window.location.href.includes('contacts')) {
        socialTitle.textContent = t.contacts_social_title;
    }
'''

print("Translations extension content created")
print(f"UK translations: {len(quiz_translations_uk)} chars")
print(f"RU translations: {len(quiz_translations_ru)} chars") 
print(f"EN translations: {len(quiz_translations_en)} chars")
print(f"Translation function extension: {len(translation_extension)} chars")
