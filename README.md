# Flask E-Commerce Platform

A comprehensive e-commerce web application built with Flask that provides complete product management and shopping cart functionality with role-based user access.

## Core Features

### Authentication & User Management
- User registration with email validation
- Secure login system with password hashing
- Role-based access (Admin/User)
- Session management and logout

### Admin Dashboard
- Product catalog management (add/edit/delete)
- Image upload with format validation (PNG, JPEG, JPG, GIF, WebP, BMP, SVG, TIFF)
- File size restrictions (2MB maximum)
- Real-time product updates

### Shopping Experience
- Product browsing for registered users
- Shopping cart with quantity controls
- Add/remove items functionality
- Automatic total price calculation
- Cart persistence across sessions

### Technical Implementation
- Blueprint-based route organization
- SQLAlchemy ORM for database operations
- WTForms for form validation and CSRF protection
- Binary image storage with MIME type handling
- Error handling and user feedback

## Technology Stack

**Backend:**
- Flask 2.3.3 (Web framework)
- SQLAlchemy 3.0.5 (Database ORM)
- WTForms 1.2.1 (Form handling)
- Werkzeug 2.3.7 (Security utilities)

**Frontend:**
- HTML5 templates with Jinja2
- CSS3 styling
- Responsive design

**Database:**
- SQLAlchemy models for User, Product, and CartItem
- Relational data structure with foreign keys

## Installation Guide

### Prerequisites
- Python 3.8+
- pip package manager

### Setup Steps

1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/flask-ecommerce.git
   cd flask-ecommerce
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. **Launch Application**
   ```bash
   flask run
   ```

Access at: `http://localhost:5000`

## Application Structure

```
project/
├── app/
│   ├── routes/
│   │   ├── add.py              # Product creation with image upload
│   │   ├── add_card.py         # Cart item addition
│   │   ├── add_product.py      # Cart quantity increase
│   │   ├── admin_product.py    # Admin product management
│   │   ├── delete.py           # Product deletion
│   │   ├── edit.py             # Product modification
│   │   ├── home.py             # Landing and routing logic
│   │   ├── image.py            # Image serving endpoint
│   │   ├── less_product.py     # Cart quantity decrease
│   │   ├── log_out.py          # Session termination
│   │   ├── sign_in.py          # User authentication
│   │   ├── sign_up.py          # User registration
│   │   ├── the_basket.py       # Shopping cart display
│   │   └── user_product.py     # Product catalog for users
│   ├── models.py               # Database schema definitions
│   ├── forms.py                # WTForms class definitions
│   └── __init__.py
├── templates/                  # HTML template files
├── static/                     # CSS and static assets
└── requirements.txt
```

## Database Schema

### User Model
- `id`: Primary key
- `name`: User display name (minimum 2 characters)
- `email`: Unique identifier and login credential
- `password`: Hashed password (minimum 8 characters)
- `role`: Access level (Admin/User)

### Product Model
- `id`: Primary key
- `name`: Product title
- `price`: Decimal pricing
- `description`: Product details
- `image`: Binary image data
- `image_mimetype`: File type for proper serving

### CartItem Model
- `id`: Primary key
- `user_id`: Foreign key to User
- `product_id`: Foreign key to Product
- `product_name`: Cached product name
- `price_at_time`: Price when added (prevents price change issues)
- `quantity`: Item count

## User Workflow

### New User Registration
1. Access `/signup` endpoint
2. Complete registration form with validation
3. Password hashing applied automatically
4. Redirect to login page

### Admin Operations
1. Login redirects to admin dashboard (`/admin_product`)
2. Add products with image upload and validation
3. Edit existing products (including image replacement)
4. Delete products with confirmation
5. Add items to personal cart

### User Shopping Experience
1. Login redirects to product catalog (`/user_product`)
2. Browse available products
3. Add items to cart with automatic quantity handling
4. Manage cart at `/the_basket` with increase/decrease options
5. View real-time total calculations

## Security Features

- **Password Security**: Werkzeug password hashing
- **Session Management**: Flask session with user ID and email storage
- **File Upload Security**: MIME type validation and size restrictions
- **CSRF Protection**: WTForms token validation
- **SQL Injection Prevention**: SQLAlchemy ORM parameterized queries
- **Access Control**: Route-level authentication checks

## Image Handling System

The application includes a robust image management system:

- **Upload Validation**: Checks file type against allowed MIME types
- **Size Restriction**: 2MB maximum file size with user feedback
- **Storage Method**: Binary data in database with MIME type preservation
- **Serving Endpoint**: Dedicated `/image/<id>` route for image delivery
- **Format Support**: Comprehensive image format compatibility

## Error Handling

- Form validation errors display to users
- File upload error messages for size/type issues
- Database operation error catching
- Session validation on protected routes
- 404 handling for missing products/cart items

## Development Notes

The application uses Flask Blueprints for modular route organization, making it scalable and maintainable. Each route file handles specific functionality, and the session-based authentication ensures secure user state management across requests.

Cart functionality includes smart quantity management - existing items increment quantity while new items create fresh cart entries. The price-at-time storage prevents issues with price changes affecting existing cart contents.
