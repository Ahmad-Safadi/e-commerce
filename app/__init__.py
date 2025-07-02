#__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


csrf = CSRFProtect()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.secret_key = 'YourSecretKey'
    app.config['SECRET_KEY'] =  'YourSecretKey'
    
    db.init_app(app)
    csrf.init_app(app)

    from .routes import home, admin_product, user_product, sign_in, sign_up, add, image, edit, delete, add_card,the_basket,add_product,less_product, log_out
    app.register_blueprint(home.bp)
    app.register_blueprint(admin_product.bp)
    app.register_blueprint(user_product.bp)
    app.register_blueprint(sign_in.bp)
    app.register_blueprint(sign_up.bp)
    app.register_blueprint(add.bp)
    app.register_blueprint(image.bp)
    app.register_blueprint(edit.bp)
    app.register_blueprint(delete.bp)
    app.register_blueprint(add_card.bp)
    app.register_blueprint(the_basket.bp)
    app.register_blueprint(add_product.bp)
    app.register_blueprint(less_product.bp)
    app.register_blueprint(log_out.bp)
    return app