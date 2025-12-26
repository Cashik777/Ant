import os
import re

base_dir = r'c:\Users\Dgello\.gemini\antigravity\scratch\EthioDirect'

# Map old key patterns to new namespace-based keys
# The i18n.js will automatically look in the page-specific namespace
key_mappings = {
    # delivery.html
    'delivery_page.title': 'page.title',
    'delivery_page.subtitle': 'page.subtitle',
    'delivery_page.methods_title': 'delivery.title',
    'delivery_page.nova_title': 'delivery.nova_poshta.title',
    'delivery_page.nova_desc': 'delivery.nova_poshta.description',
    'delivery_page.nova_time': 'delivery.nova_poshta.time',
    'delivery_page.nova_price': 'delivery.nova_poshta.price',
    'delivery_page.ukr_title': 'delivery.ukrposhta.title',
    'delivery_page.ukr_desc': 'delivery.ukrposhta.description',
    'delivery_page.ukr_time': 'delivery.ukrposhta.time',
    'delivery_page.ukr_price': 'delivery.ukrposhta.price',
    'delivery_page.courier_title': 'delivery.courier.title',
    'delivery_page.courier_desc': 'delivery.courier.description',
    'delivery_page.courier_time': 'delivery.courier.time',
    'delivery_page.courier_price': 'delivery.courier.price',
    'delivery_page.pickup_title': 'delivery.pickup.title',
    'delivery_page.pickup_desc': 'delivery.pickup.description',
    'delivery_page.pickup_time': 'delivery.pickup.time',
    'delivery_page.pickup_price': 'delivery.pickup.price',
    'delivery_page.payment_title': 'payment.title',
    'delivery_page.card_title': 'payment.card.title',
    'delivery_page.card_desc': 'payment.card.description',
    'delivery_page.cod_title': 'payment.cod.title',
    'delivery_page.cod_desc': 'payment.cod.description',
    'delivery_page.invoice_title': 'payment.invoice.title',
    'delivery_page.invoice_desc': 'payment.invoice.description',
    
    # faq.html  
    'faq_page.title': 'page.title',
    'faq_page.subtitle': 'page.subtitle',
    'faq_page.cat_ordering': 'categories.ordering',
    'faq_page.cat_delivery': 'categories.delivery',
    'faq_page.cat_payment': 'categories.payment',
    'faq_page.cat_products': 'categories.products',
    'faq_page.cat_subscription': 'categories.subscription',
    'faq_page.cat_returns': 'categories.returns',
    'faq_page.contact_title': 'contact.title',
    'faq_page.contact_text': 'contact.text',
    'faq_page.contact_btn': 'contact.button',
    
    # b2b.html
    'b2b_page.badge': 'hero.badge',
    'b2b_page.hero_title': 'hero.title',
    'b2b_page.hero_text': 'hero.text',
    'b2b_page.benefits_title': 'benefits.title',
    'b2b_page.wholesale_title': 'benefits.wholesale.title',
    'b2b_page.wholesale_text': 'benefits.wholesale.text',
    'b2b_page.fresh_title': 'benefits.fresh.title',
    'b2b_page.fresh_text': 'benefits.fresh.text',
    'b2b_page.delivery_title': 'benefits.delivery.title',
    'b2b_page.delivery_text': 'benefits.delivery.text',
    'b2b_page.manager_title': 'benefits.support.title',
    'b2b_page.manager_text': 'benefits.support.text',
    'b2b_page.training_title': 'benefits.training.title',
    'b2b_page.training_text': 'benefits.training.text',
    'b2b_page.equipment_title': 'benefits.equipment.title',
    'b2b_page.equipment_text': 'benefits.equipment.text',
    'b2b_page.who_title': 'segments.title',
    'b2b_page.cafes_title': 'segments.cafes.title',
    'b2b_page.cafes_text': 'segments.cafes.text',
    'b2b_page.restaurants_title': 'segments.restaurants.title',
    'b2b_page.restaurants_text': 'segments.restaurants.text',
    'b2b_page.offices_title': 'segments.offices.title',
    'b2b_page.offices_text': 'segments.offices.text',
    'b2b_page.hotels_title': 'segments.hotels.title',
    'b2b_page.hotels_text': 'segments.hotels.text',
    'b2b_page.form_title': 'form.title',
    'b2b_page.form_name': 'form.name',
    'b2b_page.form_company': 'form.company',
    'b2b_page.form_email': 'form.email',
    'b2b_page.form_phone': 'form.phone',
    'b2b_page.form_volume': 'form.volume',
    'b2b_page.form_message': 'form.message',
    'b2b_page.form_submit': 'form.submit',
    'b2b_page.cta_title': 'cta.title',
    'b2b_page.cta_text': 'cta.text',
    'b2b_page.cta_btn': 'cta.button',
    'b2b_page.cta_phone': 'cta.phone',
    
    # about.html
    'about_page.title': 'page.title',
    'about_page.subtitle': 'page.subtitle',
    'about_page.hero_title': 'hero.title',
    'about_page.hero_text': 'hero.text',
    'about_page.story_title': 'story.title',
    'about_page.story_p1': 'story.p1',
    'about_page.story_p2': 'story.p2',
    'about_page.story_p3': 'story.p3',
    'about_page.mission_title': 'mission.title',
    'about_page.mission_text': 'mission.text',
    'about_page.values_title': 'values.title',
    'about_page.quality_title': 'values.quality.title',
    'about_page.quality_text': 'values.quality.text',
    'about_page.transparency_title': 'values.transparency.title',
    'about_page.transparency_text': 'values.transparency.text',
    'about_page.fairness_title': 'values.fairness.title',
    'about_page.fairness_text': 'values.fairness.text',
    'about_page.freshness_title': 'values.freshness.title',
    'about_page.freshness_text': 'values.freshness.text',
    'about_page.team_title': 'team.title',
    'about_page.team_text': 'team.text',
    'about_page.cta_title': 'cta.title',
    'about_page.cta_btn': 'cta.button',
    
    # contacts.html
    'contacts_page.title': 'page.title',
    'contacts_page.subtitle': 'page.subtitle',
    'contacts_page.info_title': 'info.title',
    'contacts_page.phone_title': 'info.phone.title',
    'contacts_page.phone_hours': 'info.phone.hours',
    'contacts_page.email_title': 'info.email.title',
    'contacts_page.address_title': 'info.address.title',
    'contacts_page.social_title': 'info.social.title',
    'contacts_page.form_title': 'form.title',
    'contacts_page.form_name': 'form.name',
    'contacts_page.form_email': 'form.email',
    'contacts_page.form_phone': 'form.phone',
    'contacts_page.form_subject': 'form.subject',
    'contacts_page.form_message': 'form.message',
    'contacts_page.form_submit': 'form.submit',
    
    # shop.html
    'shop_page.title': 'page.title',
    'shop_page.subtitle': 'page.subtitle',
    'shop_page.filters_title': 'filters.title',
    'shop_page.filter_all': 'filters.all',
    'shop_page.filter_region': 'filters.region',
    'shop_page.filter_roast': 'filters.roast',
    'shop_page.filter_process': 'filters.process',
    'shop_page.filter_price': 'filters.price',
    'shop_page.sort': 'filters.sort',
    'shop_page.clear': 'filters.clear',
    
    # account.html
    'account_page.title': 'page.title',
    'account_page.welcome': 'page.welcome',
    'account_page.orders': 'tabs.orders',
    'account_page.profile': 'tabs.profile',
    'account_page.addresses': 'tabs.addresses',
    'account_page.subscriptions': 'tabs.subscriptions',
    'account_page.wishlist': 'tabs.wishlist',
    'account_page.settings': 'tabs.settings',
    'account_page.login': 'auth.login',
    'account_page.register': 'auth.register',
    'account_page.email': 'auth.email',
    'account_page.password': 'auth.password',
    'account_page.forgot': 'auth.forgot_password',
    'account_page.login_btn': 'auth.login_btn',
    'account_page.register_btn': 'auth.register_btn',
    
    # subscription.html
    'subscription_page.title': 'page.title',
    'subscription_page.subtitle': 'page.subtitle',
    'subscription_page.badge': 'hero.badge',
    'subscription_page.hero_title': 'hero.title',
    'subscription_page.hero_text': 'hero.text',
    'subscription_page.benefits_title': 'benefits.title',
    'subscription_page.discount_title': 'benefits.discount.title',
    'subscription_page.discount_text': 'benefits.discount.text',
    'subscription_page.fresh_title': 'benefits.fresh.title',
    'subscription_page.fresh_text': 'benefits.fresh.text',
    'subscription_page.flexible_title': 'benefits.flexible.title',
    'subscription_page.flexible_text': 'benefits.flexible.text',
    'subscription_page.steps_title': 'steps.title',
    'subscription_page.step1_title': 'steps.step1.title',
    'subscription_page.step1_text': 'steps.step1.text',
    'subscription_page.step2_title': 'steps.step2.title',
    'subscription_page.step2_text': 'steps.step2.text',
    'subscription_page.step3_title': 'steps.step3.title',
    'subscription_page.step3_text': 'steps.step3.text',
    'subscription_page.start': 'cta.start',
    
    # gift-certificates.html
    'gift_page.title': 'page.title',
    'gift_page.subtitle': 'page.subtitle',
    'gift_page.hero_title': 'hero.title',
    'gift_page.hero_text': 'hero.text',
    'gift_page.amounts_title': 'amounts.title',
    'gift_page.custom': 'amounts.custom',
    'gift_page.features_title': 'features.title',
    'gift_page.choice_title': 'features.choice.title',
    'gift_page.choice_text': 'features.choice.text',
    'gift_page.delivery_title': 'features.delivery.title',
    'gift_page.delivery_text': 'features.delivery.text',
    'gift_page.validity_title': 'features.validity.title',
    'gift_page.validity_text': 'features.validity.text',
    'gift_page.design_title': 'features.design.title',
    'gift_page.design_text': 'features.design.text',
    'gift_page.form_title': 'form.title',
    'gift_page.recipient_name': 'form.recipient_name',
    'gift_page.recipient_email': 'form.recipient_email',
    'gift_page.sender_name': 'form.sender_name',
    'gift_page.message': 'form.message',
    'gift_page.buy': 'cta.buy',
    
    # return.html (uses delivery namespace)
    'return_page.title': 'page.title',
    'return_page.subtitle': 'page.subtitle',
}

count = 0
files_updated = []

for root, dirs, files in os.walk(base_dir):
    dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', 'locales']]
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            for old_key, new_key in key_mappings.items():
                # Replace in data-i18n attributes
                content = content.replace(f'data-i18n="{old_key}"', f'data-i18n="{new_key}"')
                content = content.replace(f"data-i18n='{old_key}'", f"data-i18n='{new_key}'")
                content = content.replace(f'data-i18n-placeholder="{old_key}"', f'data-i18n-placeholder="{new_key}"')
                content = content.replace(f'data-i18n-title="{old_key}"', f'data-i18n-title="{new_key}"')
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f'Updated: {filepath}')
                files_updated.append(filepath)
                count += 1

print(f'\nTotal files updated: {count}')
print(f'Files: {files_updated}')
