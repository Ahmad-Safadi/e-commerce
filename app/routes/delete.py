from flask import Blueprint, redirect, url_for, flash
from app.models import Product, db
from app.forms import DeleteForm

# blueprint للتعديل
bp = Blueprint('delete_routes', __name__)

@bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    
    form = DeleteForm()
    if form.validate_on_submit():
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('admin_product.admin'))