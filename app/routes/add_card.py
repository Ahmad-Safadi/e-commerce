# add_card.py

from flask import Blueprint, redirect, url_for, flash, session
from app.models import Product, CartItem, User
from app.forms import CardForm
from app import db

# blueprint للتعديل
bp = Blueprint('add_card', __name__)

@bp.route('/add_card/<int:id>', methods=['POST'])
def card(id):

    form = CardForm()
    if form.validate_on_submit():
        product = Product.query.get_or_404(id)
        user_id = session.get('id')
        cart_item = CartItem.query.filter_by(user_id=user_id, product_id=product.id).first()
        if cart_item:
            cart_item.quantity += 1
            db.session.commit()
        else:
            new_card = CartItem(
                user_id = user_id,
                product_id=product.id,
                product_name=product.name,
                price_at_time=product.price,
                quantity=1
            )
            db.session.add(new_card)
            db.session.commit()

        if 'id' in session:
            user = User.query.get(session['id'])
            if user and user.role == 'Admin':
                return redirect(url_for('admin_product.admin'))
            else:
                return redirect(url_for('user_product.user'))