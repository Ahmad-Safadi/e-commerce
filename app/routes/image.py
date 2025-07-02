#image.py

from flask import Blueprint, Response
from app.models import Product
from app import db

bp = Blueprint('image_bp', __name__)

@bp.route('/image/<int:id>')
def image(id):
    product = Product.query.get_or_404(id)
    return Response(product.image, mimetype=product.image_mimetype)