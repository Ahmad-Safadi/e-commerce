# app/routes/Home.py

from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import Product
from app.forms import CardForm

# blueprint للصفحة الرئيسية فقط
bp = Blueprint('user_product', __name__)

@bp.route('/user_product', methods=['GET', 'POST'])
def user():
    
    if  not session.get('email') or not session.get('id'):
        return redirect(url_for('home.home'))
    
    
    add_card = CardForm()
        
    product = Product.query.all()
    return render_template('user_product.html',product=product,add_card=add_card)