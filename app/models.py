# models.py

from app import db
from sqlalchemy import LargeBinary

# models.py
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    image = db.Column(LargeBinary)
    image_mimetype = db.Column(db.String(100))
    price = db.Column(db.Float)
    description = db.Column(db.String(200))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(150))

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product_name = db.Column(db.String(150), nullable=False)
    price_at_time = db.Column(db.Float, nullable=False)  # السعر وقت الإضافة للسلة
    quantity = db.Column(db.Integer, nullable=False, default=1)