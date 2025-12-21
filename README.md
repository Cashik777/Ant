# EthioDirect

Premium Ethiopian specialty coffee e-commerce website with full multilingual support.

## Features

- 🌍 **Multilingual** — Ukrainian, Russian, English with instant switching
- ☕ **Specialty Coffee** — Ethiopian single-origin beans
- 📦 **Subscription Service** — Coffee club with personalized recommendations
- 🎁 **Gift Certificates** — Digital gift cards
- 📱 **Responsive** — Mobile-first design

## Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **i18n**: Custom lightweight engine (no dependencies)
- **Styling**: Custom CSS with CSS variables

## i18n System

Custom production-ready internationalization engine:
- No external dependencies
- Browser language detection
- Fallback chain: current → EN → UK
- Nested key support (`nav.catalog`)
- Interpolation (`{{count}} items`)
- Attribute translation (placeholder, title, alt, aria-label)
- localStorage persistence

### Adding New Language

1. Create `locales/de.json` (copy structure from `uk.json`)
2. Add to `supportedLangs` in `js/i18n.js`
3. Add button in header

## Pages

- Home (index.html)
- Catalog (shop.html)
- Subscription (subscription.html)
- Gift Cards (gift-certificates.html)
- Blog (blog.html + articles)
- About (about.html)
- FAQ (faq.html)
- Contacts (contacts.html)
- Delivery (delivery.html)
- Account (account.html)

## Development

```bash
# Start local server
python -m http.server 8080

# Open in browser
http://localhost:8080
```

## License

MIT
