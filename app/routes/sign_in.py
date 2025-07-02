# app/routes/SignIn.py

from flask import Blueprint, render_template, request, redirect, url_for, session
from app.models import Product,User
from app.forms import SignInForm
from app import db
from werkzeug.security import check_password_hash


bp = Blueprint('signin', __name__)

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    error_message = ''
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password): 
            session['email'] = user.email
            session['id'] = user.id
            if user.role == 'Admin':
                return redirect(url_for('admin_product.admin'))
                
            else:
                return redirect(url_for('user_product.user'))
        else:
            error_message = 'Invalid email or password. Please try again.'
    
    

    
    return render_template('sign_in.html', form=form,error_message=error_message)
        
  