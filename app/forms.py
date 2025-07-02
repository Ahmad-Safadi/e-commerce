#forms.py

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, StringField, PasswordField, IntegerField,FloatField
from wtforms.validators import DataRequired, Email, Length, Regexp

#=======Add Product=======#
class AddForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Only images are allowed!')])
    price = FloatField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    send = SubmitField('Send')
#======= End Add Product=======#

#=======Edit Product=======#
class EditForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'], 'Only images are allowed!')])
    price = FloatField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    update = SubmitField('Update')
#======= End Edit Product=======#

#=======Product Page=======#
class DeleteForm(FlaskForm):
    delete = SubmitField('Delete')
    
class CardForm(FlaskForm):
    add = SubmitField('add')
#=======End Product Page=======#

#=======Login=======#
class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=18)])
    submit = SubmitField('Send')

class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Send')

class LogOutForm(FlaskForm):
    logout = SubmitField('Log Out')
#=======End Login=======#


#=======Basket=======#
class Add_Quantity(FlaskForm):
    add = SubmitField('Add')
    
class Delete_Quantity(FlaskForm):
    less = SubmitField('Less')
#=======End Basket=======#