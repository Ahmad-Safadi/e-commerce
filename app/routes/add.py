from flask import Blueprint, render_template, redirect,url_for,session
from app.forms import AddForm
from app.models import Product
from app import db

bp = Blueprint('add', __name__)

@bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if  not session.get('email') or not session.get('id'):
        return redirect(url_for('home.home'))
    
    
    form = AddForm()
    size_error = ''
    type_error = ''
    error = False
    if form.validate_on_submit():
        if form.send.data:
            name = form.name.data
            price = form.price.data
            description = form.description.data
            
            #====Image Size====#
            image_file = form.image.data
            image_file.seek(0, 2)
            file_size = image_file.tell()
            image_file.seek(0)
            MAX_SIZE = 2 * 1024 * 1024
            #====End Image Size====#
            
            #====Image.====#
            image = image_file.read()
            allowed_mimetypes = ['image/png','image/jpeg', 'image/jpg','image/gif', 'image/webp','image/bmp','image/svg+xml','image/tiff']
            mimetype = image_file.mimetype
            #====End Image====#
            
            #====Checks====#
            if mimetype not in allowed_mimetypes:
                type_error = 'This file format is not supported. Please upload a valid image.'
                error = True
            if file_size > MAX_SIZE:
                 size_error = 'The file size must be less than 2 MB.'
                 error = True
                 
            if type_error or size_error:
                return render_template('add.html', form=form, type_error=type_error, size_error=size_error)
            #====End Checks====#
            else:
                new_product = Product(name=name, price=price, description=description, image=image, image_mimetype=mimetype)
                db.session.add(new_product)
                db.session.commit()
                return redirect(url_for('admin_product.admin'))
            
            
            
            
    return render_template('add.html', form=form,type_error=type_error,size_error=size_error)