from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField
from wtforms.validators import DataRequired, Length, Email


# Sets up the Registration Form template with Flask-WTForms. This is used to generate the form details in
# templates/register.html with the correct validators.

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    minimum_viewers = DecimalField('Minimum Viewers', places=4, validators=[DataRequired()])
    offer = DecimalField('Price Purchase')
    submit = SubmitField('Create')


# The Login Form, similar to Registration Form is used in login.html to generate the form's data on the screen.

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
