from flask import Blueprint, redirect, url_for, flash
from app.models import Product,CartItem, db
from app.forms import Add_Quantity

# blueprint للتعديل
bp = Blueprint('add_product', __name__)

@bp.route('/add_product/<int:id>', methods=['POST'])
def add(id):
    cart_item = CartItem.query.get_or_404(id)
    
    add_quantity = Add_Quantity()
    
    if add_quantity.validate_on_submit():
            cart_item.quantity += 1
            db.session.commit()
        
            return redirect(url_for('the_basket.basket'))