# app/routes/amin_product.py

from flask import Blueprint, render_template, request, redirect, url_for,session
from app.models import Product
from app.forms import DeleteForm, AddForm,EditForm,CardForm

# blueprint للصفحة الرئيسية فقط
bp = Blueprint('admin_product', __name__)

@bp.route('/admin_product', methods=['GET', 'POST'])
def admin():
    
    if  not session.get('email') or not session.get('id'):
        return redirect(url_for('home.home'))
    
    add_card = CardForm()
    delete_form = DeleteForm()
    product = Product.query.all()
    
    return render_template('admin_product.html', add_card=add_card, delete_form=delete_form, product=product)