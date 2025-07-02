# Flask E-Commerce Platform

A web application built with Flask that provides product management and shopping cart functionality with role-based user access.

## Features

### User Authentication
- User registration and login system
- Password hashing with Werkzeug security
- Role-based access (Admin/User roles)
- Session management with email and user ID storage

### Admin Functions
- Product management through `/admin_product` route
- Add new products with image upload at `/add`
- Edit existing products at `/edit/<id>`
- Delete products at `/delete/<id>`
- Image upload with validation (PNG, JPEG, JPG, GIF, WebP, BMP, SVG, TIFF)
- File size limit of 2MB
- Admin users can also add items to cart

### User Shopping
- Product catalog browsing at `/user_product`
- Shopping cart functionality at `/the_basket`
- Add items to cart via `/add_card/<id>`
- Increase cart quantities at `/add_product/<id>`
- Decrease cart quantities at `/less_product/<id>`
- Automatic total price calculation

### Technical Features
- Image serving through `/image/<id>` endpoint
- Session-based authentication checks
- Form validation using WTForms
- Database operations with SQLAlchemy
- Blueprint-based route organization

## Route Structure

```
├── add.py              # Add new products (GET/POST /add)
├── add_card.py         # Add items to cart (POST /add_card/<id>)
├── add_product.py      # Increase cart quantity (POST /add_product/<id>)
├── admin_product.py    # Admin dashboard (GET/POST /admin_product)
├── delete.py           # Delete products (POST /delete/<id>)
├── edit.py             # Edit products (GET/POST /edit/<id>)
├── home.py             # Home page with role routing (GET /)
├── image.py            # Serve product images (GET /image/<id>)
├── less_product.py     # Decrease cart quantity (POST /less_product/<id>)
├── log_out.py          # User logout (GET /log_out)
├── sign_in.py          # User login (GET/POST /signin)
├── sign_up.py          # User registration (GET/POST /signup)
├── the_basket.py       # Shopping cart page (GET/POST /the_basket)
└── user_product.py     # User product catalog (GET/POST /user_product)
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-ecommerce.git
   cd flask-ecommerce
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py  # or flask run
   ```

## User Flow

### Registration Process
- Navigate to `/signup`
- Minimum 2 characters for name
- Minimum 8 characters for password
- Email uniqueness validation
- Default role assigned as 'User'

### Login Process
- Navigate to `/signin`
- Email and password validation
- Admin users redirect to `/admin_product`
- Regular users redirect to `/user_product`

### Admin Workflow
1. Access admin dashboard at `/admin_product`
2. Add products via form with image upload
3. Edit existing products (name, price, description, image)
4. Delete products with confirmation
5. All products displayed with management options

### User Workflow
1. Browse products at `/user_product`
2. Add items to cart (creates new CartItem or increments existing)
3. Manage cart at `/the_basket`
4. Adjust quantities using +/- buttons
5. View calculated total price

## Image Upload System

From `add.py` implementation:
- **Supported formats**: PNG, JPEG, JPG, GIF, WebP, BMP, SVG, TIFF
- **Size limit**: 2MB maximum
- **Storage**: Binary data in database with MIME type
- **Validation**: File type and size checking with error messages
- **Serving**: Dedicated endpoint with proper MIME type headers

## Cart Management

From route analysis:
- **Add to cart**: Creates new CartItem or increments existing quantity
- **Quantity control**: Separate routes for increase/decrease
- **Price storage**: `price_at_time` field preserves pricing
- **User isolation**: Cart items filtered by `user_id` from session
- **Automatic cleanup**: Items with quantity 1 are deleted when decreased

## Security Implementation

Based on code analysis:
- Session validation on protected routes
- Password hashing in registration
- CSRF protection through WTForms
- File upload validation
- User role verification for admin access
- Session clearing on logout

## Database Models Used

From imports and usage:
- **User**: Contains email, password, role fields
- **Product**: Contains name, price, description, image, image_mimetype
- **CartItem**: Contains user_id, product_id, product_name, price_at_time, quantity

## Error Handling

Observed in routes:
- Image upload validation with user feedback
- Session requirement checks with redirects
- Database operation error handling
- Form validation error display
- 404 handling for missing resources
