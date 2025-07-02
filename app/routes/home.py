# app/routes/Home.py

from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import User

# blueprint للصفحة الرئيسية فقط
bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    if session.get('email') and session.get('id'):
        id = session.get('id')
        user = User.query.filter_by(id=id).first()
        
        if user and user.role == 'Admin': 
            return redirect(url_for('admin_product.admin'))
        if user and user.role == 'User':
            return redirect(url_for('user_product.user'))

    return render_template('home.html')