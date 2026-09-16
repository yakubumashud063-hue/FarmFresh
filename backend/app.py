"""
FarmFresh - Backend API Server
A Flask-based backend for the FarmFresh platform connecting buyers and sellers of farm products.

Author: Mashud Yakubu
"""

from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_cors import CORS
from datetime import datetime
import uuid
import hashlib

app = Flask(__name__, 
            template_folder='../templates',
            static_folder='../static')
app.secret_key = 'farmfresh-secret-key-change-in-production'
CORS(app)

# In-memory database (replace with actual database in production)
users_db = {}
products_db = [
    {
        'id': 1,
        'name': "Fresh Organic Tomatoes",
        'category': "vegetables",
        'price': 3.50,
        'unit': "kg",
        'farmer_id': 1,
        'farmer_name': "John K.",
        'description': "Freshly harvested organic tomatoes",
        'stock': 100,
        'organic': True,
        'created_at': datetime.now().isoformat()
    },
    {
        'id': 2,
        'name': "Organic Honey Crisp Apples",
        'category': "fruits",
        'price': 4.20,
        'unit': "kg",
        'farmer_id': 2,
        'farmer_name': "Sarah M.",
        'description': "Sweet and crispy organic apples",
        'stock': 75,
        'organic': True,
        'created_at': datetime.now().isoformat()
    },
    {
        'id': 3,
        'name': "Fresh Farm Eggs",
        'category': "dairy",
        'price': 5.00,
        'unit': "dozen",
        'farmer_id': 3,
        'farmer_name': "Mike R.",
        'description': "Free-range farm fresh eggs",
        'stock': 50,
        'organic': False,
        'created_at': datetime.now().isoformat()
    },
    {
        'id': 4,
        'name': "Organic Carrots",
        'category': "vegetables",
        'price': 2.80,
        'unit': "kg",
        'farmer_id': 4,
        'farmer_name': "Emily W.",
        'description': "Crunchy organic carrots",
        'stock': 120,
        'organic': True,
        'created_at': datetime.now().isoformat()
    },
    {
        'id': 5,
        'name': "Whole Wheat Grain",
        'category': "grains",
        'price': 1.50,
        'unit': "kg",
        'farmer_id': 5,
        'farmer_name': "David L.",
        'description': "Premium whole wheat grains",
        'stock': 200,
        'organic': False,
        'created_at': datetime.now().isoformat()
    },
    {
        'id': 6,
        'name': "Fresh Strawberries",
        'category': "fruits",
        'price': 6.00,
        'unit': "kg",
        'farmer_id': 6,
        'farmer_name': "Lisa P.",
        'description': "Sweet and juicy strawberries",
        'stock': 40,
        'organic': True,
        'created_at': datetime.now().isoformat()
    }
]

farmers_db = [
    {
        'id': 1,
        'name': "John Kamara",
        'email': "john.k@farmfresh.com",
        'location': "Northern Region, GH",
        'rating': 5.0,
        'reviews_count': 45,
        'products': ["Tomatoes", "Peppers", "Onions"],
        'verified': True,
        'joined_date': "2023-01-15",
        'bio': "Experienced farmer specializing in organic vegetables"
    },
    {
        'id': 2,
        'name': "Sarah Mensah",
        'email': "sarah.m@farmfresh.com",
        'location': "Ashanti Region, GH",
        'rating': 5.0,
        'reviews_count': 62,
        'products': ["Apples", "Oranges", "Mangoes"],
        'verified': True,
        'joined_date': "2023-02-20",
        'bio': "Fruit orchard owner with 10 years of experience"
    },
    {
        'id': 3,
        'name': "Michael Roberts",
        'email': "mike.r@farmfresh.com",
        'location': "Eastern Region, GH",
        'rating': 4.5,
        'reviews_count': 38,
        'products': ["Eggs", "Chicken", "Duck"],
        'verified': True,
        'joined_date': "2023-03-10",
        'bio': "Poultry farmer committed to ethical farming practices"
    },
    {
        'id': 4,
        'name': "Emily Williams",
        'email': "emily.w@farmfresh.com",
        'location': "Volta Region, GH",
        'rating': 5.0,
        'reviews_count': 51,
        'products': ["Carrots", "Lettuce", "Cabbage"],
        'verified': True,
        'joined_date': "2023-01-25",
        'bio': "Organic vegetable farmer passionate about sustainable agriculture"
    }
]

messages_db = []
negotiations_db = []


# Routes
@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')


# Authentication Routes
@app.route('/api/auth/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()
    
    required_fields = ['name', 'email', 'password', 'user_type']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    email = data['email'].lower()
    if email in users_db:
        return jsonify({'error': 'Email already registered'}), 409
    
    # Hash password (in production, use proper password hashing like bcrypt)
    hashed_password = hashlib.sha256(data['password'].encode()).hexdigest()
    
    user_id = str(uuid.uuid4())
    users_db[email] = {
        'id': user_id,
        'name': data['name'],
        'email': email,
        'password': hashed_password,
        'user_type': data['user_type'],  # 'buyer' or 'seller'
        'verified': False,
        'created_at': datetime.now().isoformat(),
        'profile': {}
    }
    
    return jsonify({
        'message': 'Registration successful',
        'user': {
            'id': user_id,
            'name': data['name'],
            'email': email,
            'user_type': data['user_type']
        }
    }), 201


@app.route('/api/auth/login', methods=['POST'])
def login():
    """Login user"""
    data = request.get_json()
    
    email = data.get('email', '').lower()
    password = data.get('password', '')
    
    if not email or not password:
        return jsonify({'error': 'Email and password required'}), 400
    
    user = users_db.get(email)
    if not user:
        return jsonify({'error': 'Invalid credentials'}), 401
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if user['password'] != hashed_password:
        return jsonify({'error': 'Invalid credentials'}), 401
    
    session['user_id'] = user['id']
    session['email'] = email
    
    return jsonify({
        'message': 'Login successful',
        'user': {
            'id': user['id'],
            'name': user['name'],
            'email': email,
            'user_type': user['user_type'],
            'verified': user['verified']
        }
    }), 200


@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """Logout user"""
    session.clear()
    return jsonify({'message': 'Logout successful'}), 200


@app.route('/api/auth/me', methods=['GET'])
def get_current_user():
    """Get current logged-in user"""
    if 'email' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    user = users_db.get(session['email'])
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'id': user['id'],
        'name': user['name'],
        'email': user['email'],
        'user_type': user['user_type'],
        'verified': user['verified']
    }), 200


# Product Routes
@app.route('/api/products', methods=['GET'])
def get_products():
    """Get all products with optional filtering"""
    category = request.args.get('category')
    organic = request.args.get('organic')
    search = request.args.get('search')
    
    filtered = products_db.copy()
    
    if category:
        filtered = [p for p in filtered if p['category'] == category]
    
    if organic == 'true':
        filtered = [p for p in filtered if p['organic']]
    
    if search:
        search_lower = search.lower()
        filtered = [p for p in filtered if 
                    search_lower in p['name'].lower() or 
                    search_lower in p['description'].lower() or
                    search_lower in p['farmer_name'].lower()]
    
    return jsonify(filtered), 200


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a specific product"""
    product = next((p for p in products_db if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    return jsonify(product), 200


@app.route('/api/products', methods=['POST'])
def create_product():
    """Create a new product (for sellers)"""
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    data = request.get_json()
    required_fields = ['name', 'category', 'price', 'unit', 'description']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    user = users_db.get(session['email'])
    if user['user_type'] != 'seller':
        return jsonify({'error': 'Only sellers can create products'}), 403
    
    new_id = max(p['id'] for p in products_db) + 1 if products_db else 1
    new_product = {
        'id': new_id,
        'name': data['name'],
        'category': data['category'],
        'price': float(data['price']),
        'unit': data['unit'],
        'farmer_id': user['id'],
        'farmer_name': user['name'],
        'description': data['description'],
        'stock': int(data.get('stock', 0)),
        'organic': data.get('organic', False),
        'created_at': datetime.now().isoformat()
    }
    
    products_db.append(new_product)
    
    return jsonify(new_product), 201


# Farmer Routes
@app.route('/api/farmers', methods=['GET'])
def get_farmers():
    """Get all farmers"""
    verified_only = request.args.get('verified_only')
    location = request.args.get('location')
    
    filtered = farmers_db.copy()
    
    if verified_only == 'true':
        filtered = [f for f in filtered if f['verified']]
    
    if location:
        filtered = [f for f in filtered if location.lower() in f['location'].lower()]
    
    return jsonify(filtered), 200


@app.route('/api/farmers/<int:farmer_id>', methods=['GET'])
def get_farmer(farmer_id):
    """Get a specific farmer"""
    farmer = next((f for f in farmers_db if f['id'] == farmer_id), None)
    if not farmer:
        return jsonify({'error': 'Farmer not found'}), 404
    
    # Get farmer's products
    farmer_products = [p for p in products_db if p['farmer_id'] == farmer_id]
    
    result = farmer.copy()
    result['products_list'] = farmer_products
    
    return jsonify(result), 200


# Messaging Routes
@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Get messages for current user"""
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    user_email = session['email']
    user_messages = [m for m in messages_db if m['sender'] == user_email or m['recipient'] == user_email]
    
    return jsonify(user_messages), 200


@app.route('/api/messages', methods=['POST'])
def send_message():
    """Send a message"""
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    data = request.get_json()
    required_fields = ['recipient', 'content', 'subject']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    message_id = str(uuid.uuid4())
    message = {
        'id': message_id,
        'sender': session['email'],
        'recipient': data['recipient'],
        'subject': data['subject'],
        'content': data['content'],
        'read': False,
        'created_at': datetime.now().isoformat()
    }
    
    messages_db.append(message)
    
    return jsonify(message), 201


# Negotiation Routes
@app.route('/api/negotiations', methods=['POST'])
def create_negotiation():
    """Create a price negotiation"""
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    data = request.get_json()
    required_fields = ['product_id', 'offered_price', 'message']
    
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    product = next((p for p in products_db if p['id'] == data['product_id']), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    negotiation_id = str(uuid.uuid4())
    negotiation = {
        'id': negotiation_id,
        'product_id': data['product_id'],
        'product_name': product['name'],
        'buyer_id': session['user_id'],
        'buyer_email': session['email'],
        'seller_id': product['farmer_id'],
        'original_price': product['price'],
        'offered_price': float(data['offered_price']),
        'message': data['message'],
        'status': 'pending',  # pending, accepted, rejected, countered
        'created_at': datetime.now().isoformat()
    }
    
    negotiations_db.append(negotiation)
    
    return jsonify(negotiation), 201


@app.route('/api/negotiations', methods=['GET'])
def get_negotiations():
    """Get negotiations for current user"""
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    user_id = session['user_id']
    user_negotiations = [n for n in negotiations_db if n['buyer_id'] == user_id or n['seller_id'] == user_id]
    
    return jsonify(user_negotiations), 200


@app.route('/api/negotiations/<negotiation_id>/respond', methods=['POST'])
def respond_to_negotiation(negotiation_id):
    """Respond to a negotiation (accept/reject/counter)"""
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required'}), 401
    
    negotiation = next((n for n in negotiations_db if n['id'] == negotiation_id), None)
    if not negotiation:
        return jsonify({'error': 'Negotiation not found'}), 404
    
    if negotiation['seller_id'] != session['user_id']:
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    action = data.get('action')  # accept, reject, counter
    
    if action not in ['accept', 'reject', 'counter']:
        return jsonify({'error': 'Invalid action'}), 400
    
    negotiation['status'] = action
    negotiation['responded_at'] = datetime.now().isoformat()
    
    if action == 'counter':
        negotiation['counter_price'] = float(data.get('counter_price', 0))
    
    return jsonify(negotiation), 200


# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    }), 200


if __name__ == '__main__':
    print("=" * 60)
    print("FarmFresh Backend Server")
    print("Author: Mashud Yakubu")
    print("=" * 60)
    print("\nStarting server...")
    print("Frontend: http://localhost:5000")
    print("API Base: http://localhost:5000/api")
    print("\nAvailable endpoints:")
    print("  GET  /                    - Main page")
    print("  POST /api/auth/register   - Register new user")
    print("  POST /api/auth/login      - Login user")
    print("  POST /api/auth/logout     - Logout user")
    print("  GET  /api/products        - Get all products")
    print("  GET  /api/products/<id>   - Get specific product")
    print("  POST /api/products        - Create product (sellers)")
    print("  GET  /api/farmers         - Get all farmers")
    print("  GET  /api/farmers/<id>    - Get specific farmer")
    print("  GET  /api/messages        - Get user messages")
    print("  POST /api/messages        - Send message")
    print("  POST /api/negotiations    - Create negotiation")
    print("  GET  /api/negotiations    - Get user negotiations")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
