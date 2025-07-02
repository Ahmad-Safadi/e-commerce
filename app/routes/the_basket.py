# app/routes/basket.py

from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import CartItem
from app.forms import Delete_Quantity,Add_Quantity

# blueprint للصفحة الرئيسية فقط
bp = Blueprint('the_basket', __name__)

@bp.route('/the_basket', methods=['GET', 'POST'])
def basket():
    total_price = 0
    error_message = ''
    if  not session.get('email') or not session.get('id'):
        return redirect(url_for('home.home'))
    
    try:
        delete_quantity = Delete_Quantity()
        add_quantity = Add_Quantity()
        user_id = session.get('id')
        carditem = CartItem.query.filter_by(user_id=user_id).all()
        
        total_price = sum(i.price_at_time * i.quantity for i in carditem)
        
        
    except Exception as e:
        error_message = f"Operation failed due to the following error: {e}"
    
    return render_template('the_basket.html',carditem=carditem,delete_quantity=delete_quantity, add_quantity = add_quantity, error_message=error_message, total_price=total_price)