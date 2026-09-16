

# Farm Fresh

A professional web application platform connecting buyers and sellers of farm products directly.

## Features Implemented

### Frontend Features
- **Modern Responsive Design** - Professional UI with smooth animations and mobile-first approach
- **Product Listings** - Browse farm products with filtering by category (vegetables, fruits, dairy, grains, organic)
- **Farmer Profiles** - View verified farmer profiles with ratings, locations, and product offerings
- **Search Functionality** - Real-time search across products, farmers, and categories
- **User Authentication UI** - Login and registration modals with form validation
- **Messaging Interface** - Direct buyer-seller communication system (UI ready)
- **Price Negotiation** - Interactive negotiation feature for bulk orders
- **Testimonials Section** - User reviews and ratings display
- **How It Works Guide** - Step-by-step onboarding process

### Backend API Features
- **User Authentication** - Registration, login, logout with session management
- **User Verification System** - Seller verification badges and trust indicators
- **Product Management** - CRUD operations for farm products
- **Farmer Directory** - Searchable farmer database with location filtering
- **Messaging System** - Secure buyer-seller messaging
- **Price Negotiation** - Full negotiation workflow (offer, accept, reject, counter)
- **Geolocation Support** - Location-based farmer and product search
- **RESTful API** - Clean API endpoints for frontend integration

## Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python 3, Flask
- **Styling**: Custom CSS with CSS Variables, Flexbox, Grid
- **Icons**: Font Awesome 6.4.0
- **API**: RESTful JSON API

## Project Structure
```
farmfresh/
├── backend/
│   └── app.py              # Flask backend server
├── static/
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # Frontend JavaScript
│   └── images/             # Image assets
├── templates/
│   └── index.html          # Main HTML template
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd farmfresh
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend server:
```bash
python backend/app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/me` - Get current user

### Products
- `GET /api/products` - Get all products (with optional filters: category, organic, search)
- `GET /api/products/<id>` - Get specific product
- `POST /api/products` - Create new product (sellers only)

### Farmers
- `GET /api/farmers` - Get all farmers (with optional filters: verified_only, location)
- `GET /api/farmers/<id>` - Get specific farmer with products

### Messaging
- `GET /api/messages` - Get user messages
- `POST /api/messages` - Send new message

### Negotiations
- `POST /api/negotiations` - Create price negotiation
- `GET /api/negotiations` - Get user negotiations
- `POST /api/negotiations/<id>/respond` - Respond to negotiation (accept/reject/counter)

## Professional Features

### 1. Trust & Verification System
- Verified farmer badges
- User ratings and reviews
- Profile authentication
- Transaction history tracking

### 2. Advanced Search & Geolocation
- Location-based farmer search
- Product category filtering
- Seasonal availability indicators
- Interactive map integration (ready for implementation)

## Future Enhancements
- Database integration (PostgreSQL/MongoDB)
- Payment gateway integration
- Email notifications
- Mobile app development
- Real-time chat with WebSockets
- Image upload for products
- Order tracking system
- Multi-language support

## Author
**Mashud Yakubu**

## License
This project is open source and available under the MIT License.

## Contact
- Email: info@farmfresh.com
- Website: www.farmfresh.com

---

© 2024 FarmFresh. Connecting farmers and buyers for a fresher, healthier future.
