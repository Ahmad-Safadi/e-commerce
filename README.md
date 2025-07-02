# E-Commerce Flask Web Application

A full-featured e-commerce web application built with Flask, featuring user authentication, product management, and shopping cart functionality.

## 🚀 Features

### User Management
- **User Registration & Login**: Secure user authentication system
- **Role-based Access Control**: Admin and User roles with different permissions
- **Session Management**: Secure session handling and logout functionality

### Product Management (Admin)
- **Add Products**: Upload products with images, names, prices, and descriptions
- **Edit Products**: Modify existing product information and images
- **Delete Products**: Remove products from the catalog
- **Image Upload**: Support for multiple image formats (PNG, JPEG, JPG, GIF, WebP, BMP, SVG, TIFF)
- **File Validation**: Image size limit (2MB) and format validation

### Shopping Experience (Users)
- **Product Catalog**: Browse all available products
- **Shopping Cart**: Add products to cart with quantity management
- **Cart Management**: Increase/decrease quantities or remove items
- **Total Calculation**: Automatic price calculation for cart items

### Technical Features
- **Responsive Design**: HTML/CSS frontend for optimal user experience
- **Database Integration**: SQLAlchemy ORM for data management
- **Form Validation**: WTForms for secure form handling
- **Image Serving**: Dynamic image serving with proper MIME types
- **Error Handling**: Comprehensive error handling and user feedback

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy ORM
- **Frontend**: HTML5, CSS3
- **Forms**: WTForms
- **Authentication**: Werkzeug Security
- **Session Management**: Flask Sessions
- **File Upload**: Flask file handling

## 📋 Requirements

See `requirements.txt` for a complete list of dependencies.

### Core Dependencies
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- WTForms
- Werkzeug

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flask-ecommerce.git
   cd flask-ecommerce
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. **Run the application**
   ```bash
   flask run
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 📁 Project Structure

```
flask-ecommerce/
├── app/
│   ├── routes/
│   │   ├── add.py              # Add new products
│   │   ├── add_card.py         # Add items to cart
│   │   ├── add_product.py      # Increase cart quantities
│   │   ├── admin_product.py    # Admin product management
│   │   ├── delete.py           # Delete products
│   │   ├── edit.py             # Edit products
│   │   ├── home.py             # Home page routing
│   │   ├── image.py            # Image serving
│   │   ├── less_product.py     # Decrease cart quantities
│   │   ├── log_out.py          # User logout
│   │   ├── sign_in.py          # User login
│   │   ├── sign_up.py          # User registration
│   │   ├── the_basket.py       # Shopping cart
│   │   └── user_product.py     # User product catalog
│   ├── models.py               # Database models
│   ├── forms.py                # WTForms definitions
│   └── __init__.py             # App initialization
├── templates/                  # HTML templates
├── static/                     # CSS, JS, images
├── requirements.txt            # Python dependencies
└── app.py                      # Application entry point
```

## 🔐 User Roles

### Admin Users
- Manage product catalog (add, edit, delete)
- View all products
- Access admin dashboard
- Add products to cart

### Regular Users
- Browse product catalog
- Add products to shopping cart
- Manage cart quantities
- View cart and total prices

## 🖼️ Image Upload Specifications

- **Supported Formats**: PNG, JPEG, JPG, GIF, WebP, BMP, SVG, TIFF
- **Maximum File Size**: 2MB
- **Validation**: Automatic file type and size validation
- **Storage**: Binary storage in database with MIME type preservation

## 🛡️ Security Features

- Password hashing using Werkzeug security
- Session-based authentication
- CSRF protection via WTForms
- File upload validation
- Role-based access control
- SQL injection prevention through SQLAlchemy ORM

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Image files are stored in database (consider file system storage for production)
- No payment integration (ready for payment gateway integration)
- Limited search functionality

## 🔮 Future Enhancements

- [ ] Payment gateway integration
- [ ] Advanced search and filtering
- [ ] Product categories
- [ ] Order history
- [ ] Email notifications
- [ ] Product reviews and ratings
- [ ] Wishlist functionality
- [ ] Admin analytics dashboard

## 📞 Support

If you have any questions or need help with setup, please open an issue in the GitHub repository.

---

**Built with ❤️ using Flask**
