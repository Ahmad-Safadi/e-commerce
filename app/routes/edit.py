# app/routes/Edit.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Product
from app import db
from app.forms import EditForm

# blueprint للتعديل
bp = Blueprint('edit_routes', __name__)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    product = Product.query.get_or_404(id)
    form = EditForm()
    
            
    if request.method == 'GET':
        form.name.data = product.name
        form.price.data = product.price
        form.description.data = product.description
        
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.description = form.description.data
        
        if form.image.data:
            product.image = form.image.data.read()
            product.image_mimetype = form.image.data.mimetype

        db.session.commit()
        flash('تم تحديث المنتج بنجاح!', 'success')
        return redirect(url_for('admin_product.admin'))

    return render_template('edit.html', form=form, product=product)