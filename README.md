# Flask E-Commerce Platform

A web application built with Flask that provides product management and shopping cart functionality with role-based user access.

---

## Key Features

### User Authentication  
- User registration with email uniqueness check  
- Secure password hashing using Werkzeug  
- Role-based access control (Admin/User)  
- Session management storing email and user ID

### Admin Functions  
- Product management via `/admin_product` dashboard  
- Add new products with image upload (`/add`)  
- Edit and delete products (`/edit/<id>`, `/delete/<id>`)  
- Image upload validation (PNG, JPEG, JPG, GIF, WebP, BMP, SVG, TIFF)  
- Maximum file size: 2MB  
- Admins can also add products to the cart

### User Shopping  
- Browse product catalog at `/user_product`  
- Shopping cart functionality at `/the_basket`  
- Add items to cart, increase/decrease quantities  
- Automatic total price calculation

### Technical Features  
- Image serving via `/image/<id>` endpoint  
- Session-based authentication for protected routes  
- Form validation using WTForms  
- Database operations with SQLAlchemy  
- Organized code with Flask Blueprints

---
