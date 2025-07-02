# app/routes/SignUp.py

from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Product,User
from app.forms import SignUpForm
from werkzeug.security import generate_password_hash
from app import db

# blueprint للصفحة الرئيسية فقط
bp = Blueprint('signup', __name__)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    email_error = ''
    password_error = ''
    name_error = ''
    has_error = False
    role = 'User'
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        email = form.email.data
        hashed_password = generate_password_hash(password)

        
        user = User.query.filter_by(email=email).first()
        
        if len(name.strip()) < 2:
            name_error = 'Name must be at least 2 characters.'
            has_error = True
        
        if len(password) < 8:
            password_error = 'Password must be at least 8 characters'
            has_error = True
        
        if user:
            email_error = 'This email is already used'
            has_error = True
        
        if not has_error:
            new_user = User(name=name,email=email,password=hashed_password,role=role)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('signin.signin'))
            
    return render_template('sign_up.html', form=form, name_error=name_error, password_error=password_error, email_error=email_error)