// Sample Data
const products = [
    {
        id: 1,
        name: "Fresh Organic Tomatoes",
        category: "vegetables",
        price: "$3.50/kg",
        farmer: "John K.",
        farmerInitials: "JK",
        icon: "🍅"
    },
    {
        id: 2,
        name: "Organic Honey Crisp Apples",
        category: "fruits",
        price: "$4.20/kg",
        farmer: "Sarah M.",
        farmerInitials: "SM",
        icon: "🍎"
    },
    {
        id: 3,
        name: "Fresh Farm Eggs",
        category: "dairy",
        price: "$5.00/dozen",
        farmer: "Mike R.",
        farmerInitials: "MR",
        icon: "🥚"
    },
    {
        id: 4,
        name: "Organic Carrots",
        category: "vegetables",
        price: "$2.80/kg",
        farmer: "Emily W.",
        farmerInitials: "EW",
        icon: "🥕"
    },
    {
        id: 5,
        name: "Whole Wheat Grain",
        category: "grains",
        price: "$1.50/kg",
        farmer: "David L.",
        farmerInitials: "DL",
        icon: "🌾"
    },
    {
        id: 6,
        name: "Fresh Strawberries",
        category: "fruits",
        price: "$6.00/kg",
        farmer: "Lisa P.",
        farmerInitials: "LP",
        icon: "🍓"
    },
    {
        id: 7,
        name: "Organic Milk",
        category: "dairy",
        price: "$4.50/liter",
        farmer: "Tom H.",
        farmerInitials: "TH",
        icon: "🥛"
    },
    {
        id: 8,
        name: "Green Leafy Spinach",
        category: "organic",
        price: "$2.00/bunch",
        farmer: "Anna B.",
        farmerInitials: "AB",
        icon: "🥬"
    }
];

const farmers = [
    {
        id: 1,
        name: "John Kamara",
        location: "Northern Region, GH",
        rating: 5,
        products: ["Tomatoes", "Peppers", "Onions"],
        initials: "JK",
        verified: true
    },
    {
        id: 2,
        name: "Sarah Mensah",
        location: "Ashanti Region, GH",
        rating: 5,
        products: ["Apples", "Oranges", "Mangoes"],
        initials: "SM",
        verified: true
    },
    {
        id: 3,
        name: "Michael Roberts",
        location: "Eastern Region, GH",
        rating: 4,
        products: ["Eggs", "Chicken", "Duck"],
        initials: "MR",
        verified: true
    },
    {
        id: 4,
        name: "Emily Williams",
        location: "Volta Region, GH",
        rating: 5,
        products: ["Carrots", "Lettuce", "Cabbage"],
        initials: "EW",
        verified: true
    }
];

// DOM Elements
const productsGrid = document.getElementById('productsGrid');
const farmersGrid = document.getElementById('farmersGrid');
const filterBtns = document.querySelectorAll('.filter-btn');
const loginBtn = document.getElementById('loginBtn');
const signupBtn = document.getElementById('signupBtn');
const loginModal = document.getElementById('loginModal');
const signupModal = document.getElementById('signupModal');
const closeLoginModal = document.getElementById('closeLoginModal');
const closeSignupModal = document.getElementById('closeSignupModal');
const showSignup = document.getElementById('showSignup');
const showLogin = document.getElementById('showLogin');
const loginForm = document.getElementById('loginForm');
const signupForm = document.getElementById('signupForm');
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const navLinks = document.querySelector('.nav-links');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    renderProducts(products);
    renderFarmers(farmers);
    setupEventListeners();
});

// Render Products
function renderProducts(productsToRender) {
    productsGrid.innerHTML = '';
    productsToRender.forEach(product => {
        const productCard = document.createElement('div');
        productCard.className = 'product-card';
        productCard.innerHTML = `
            <div class="product-image">${product.icon}</div>
            <div class="product-info">
                <span class="product-category">${product.category}</span>
                <h3 class="product-title">${product.name}</h3>
                <div class="product-farmer">
                    <div class="farmer-avatar">${product.farmerInitials}</div>
                    <span>${product.farmer}</span>
                </div>
                <div class="product-price">${product.price}</div>
                <div class="product-actions">
                    <button class="btn btn-primary" onclick="openMessageModal('${product.name}', '${product.farmer}')">Message</button>
                    <button class="btn btn-outline" onclick="openNegotiationModal('${product.name}', '${product.price}')">Negotiate</button>
                </div>
            </div>
        `;
        productsGrid.appendChild(productCard);
    });
}

// Render Farmers
function renderFarmers(farmersToRender) {
    farmersGrid.innerHTML = '';
    farmersToRender.forEach(farmer => {
        const stars = '★'.repeat(farmer.rating) + '☆'.repeat(5 - farmer.rating);
        const farmerCard = document.createElement('div');
        farmerCard.className = 'farmer-card';
        farmerCard.innerHTML = `
            <div class="farmer-image">${farmer.initials}</div>
            <h3 class="farmer-name">${farmer.name}</h3>
            <div class="farmer-location">
                <i class="fas fa-map-marker-alt"></i>
                <span>${farmer.location}</span>
            </div>
            <div class="farmer-rating">${stars}</div>
            ${farmer.verified ? '<span class="verified-badge"><i class="fas fa-check-circle"></i> Verified Farmer</span>' : ''}
            <div class="farmer-products">
                ${farmer.products.map(product => `<span class="product-tag">${product}</span>`).join('')}
            </div>
            <button class="btn btn-primary btn-block" onclick="viewFarmerProfile(${farmer.id})">View Profile</button>
        `;
        farmersGrid.appendChild(farmerCard);
    });
}

// Setup Event Listeners
function setupEventListeners() {
    // Filter buttons
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const filter = btn.dataset.filter;
            if (filter === 'all') {
                renderProducts(products);
            } else {
                const filtered = products.filter(p => p.category === filter || (filter === 'organic' && p.category === 'organic'));
                renderProducts(filtered);
            }
        });
    });

    // Modal controls
    loginBtn.addEventListener('click', () => {
        loginModal.classList.add('active');
    });

    signupBtn.addEventListener('click', () => {
        signupModal.classList.add('active');
    });

    closeLoginModal.addEventListener('click', () => {
        loginModal.classList.remove('active');
    });

    closeSignupModal.addEventListener('click', () => {
        signupModal.classList.remove('active');
    });

    showSignup.addEventListener('click', (e) => {
        e.preventDefault();
        loginModal.classList.remove('active');
        signupModal.classList.add('active');
    });

    showLogin.addEventListener('click', (e) => {
        e.preventDefault();
        signupModal.classList.remove('active');
        loginModal.classList.add('active');
    });

    // Close modals when clicking outside
    window.addEventListener('click', (e) => {
        if (e.target === loginModal) {
            loginModal.classList.remove('active');
        }
        if (e.target === signupModal) {
            signupModal.classList.remove('active');
        }
    });

    // Form submissions
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('loginEmail').value;
        const password = document.getElementById('loginPassword').value;
        
        // Simulate login (in production, this would call the backend)
        alert(`Login attempt with: ${email}\n\nBackend integration required for actual authentication.`);
        loginModal.classList.remove('active');
    });

    signupForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const name = document.getElementById('signupName').value;
        const email = document.getElementById('signupEmail').value;
        const type = document.getElementById('signupType').value;
        
        // Simulate signup (in production, this would call the backend)
        alert(`Signup attempt:\nName: ${name}\nEmail: ${email}\nType: ${type}\n\nBackend integration required for actual registration.`);
        signupModal.classList.remove('active');
    });

    // Mobile menu
    mobileMenuBtn.addEventListener('click', () => {
        navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
        navLinks.style.flexDirection = 'column';
        navLinks.style.position = 'absolute';
        navLinks.style.top = '100%';
        navLinks.style.left = '0';
        navLinks.style.right = '0';
        navLinks.style.background = 'var(--white)';
        navLinks.style.padding = '20px';
        navLinks.style.boxShadow = 'var(--shadow)';
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Search functionality
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.querySelector('.hero-search .btn-primary');
    
    searchBtn.addEventListener('click', performSearch);
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            performSearch();
        }
    });
}

// Perform Search
function performSearch() {
    const query = searchInput.value.toLowerCase().trim();
    if (!query) {
        renderProducts(products);
        return;
    }
    
    const filtered = products.filter(p => 
        p.name.toLowerCase().includes(query) ||
        p.category.toLowerCase().includes(query) ||
        p.farmer.toLowerCase().includes(query)
    );
    
    renderProducts(filtered);
    
    // Scroll to products section
    document.getElementById('products').scrollIntoView({ behavior: 'smooth' });
}

// Open Message Modal (placeholder)
function openMessageModal(productName, farmerName) {
    alert(`Message ${farmerName} about: ${productName}\n\nMessaging feature requires backend integration.`);
}

// Open Negotiation Modal (placeholder)
function openNegotiationModal(productName, price) {
    const offer = prompt(`Negotiate price for ${productName}\nCurrent price: ${price}\n\nYour offer:`);
    if (offer) {
        alert(`Offer of ${offer} sent to farmer!\n\nNegotiation feature requires backend integration.`);
    }
}

// View Farmer Profile (placeholder)
function viewFarmerProfile(farmerId) {
    const farmer = farmers.find(f => f.id === farmerId);
    if (farmer) {
        alert(`Viewing profile of ${farmer.name}\nLocation: ${farmer.location}\nProducts: ${farmer.products.join(', ')}\n\nFarmer profile page requires backend integration.`);
    }
}

// Console log for development
console.log('FarmFresh initialized successfully!');
console.log('Products loaded:', products.length);
console.log('Farmers loaded:', farmers.length);
