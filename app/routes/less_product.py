from flask import Blueprint, redirect, url_for, flash
from app.models import Product,CartItem, db
from app.forms import Delete_Quantity

# blueprint للتعديل
bp = Blueprint('less_product', __name__)

@bp.route('/less_product/<int:id>', methods=['POST'])
def less(id):
    cart_item = CartItem.query.get_or_404(id)
    
    delete_quantity = Delete_Quantity()
    
    if delete_quantity.validate_on_submit():
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            db.session.commit()
        else:
            db.session.delete(cart_item)
            db.session.commit()
        
        return redirect(url_for('the_basket.basket'))