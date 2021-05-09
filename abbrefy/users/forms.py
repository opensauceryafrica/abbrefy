# importing the required modules
import safe
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from abbrefy.users.models import User
# importing the required modules end


# defining the registration form class
class RegistrationForm(FlaskForm):

    username = StringField("Username", validators=[Regexp('[_+0-9a-zA-Z]+', message='Can only contain letters, numbers, underscores'),
                                                   DataRequired(), Length(min=3, max=10, message="Must be between 3 and 10 characters")], render_kw={
        'autocomplete': 'username'})
    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={
        'autocomplete': 'email'})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
                             'autocomplete': 'new-password'})
    confirm_password = PasswordField("Confirm Password", validators=[
        DataRequired(), EqualTo("password", message="Your Passwords Don't Match")], render_kw={
        'autocomplete': 'new-password'})
    submit = SubmitField('Sign Up')

    # validate password strength
    def validate_password(self, password):
        strong = safe.check(password.data)
        if not strong:
            raise ValidationError('Password not strong enough')

    # setting up custom validation to check if username exists
    def validate_username(self, username):
        if User.check_username(username.data):
            raise ValidationError('That Username Has Been Taken')

    # setting up custom validation to check if email exists
    def validate_email(self, email):
        if User.check_email(email.data):
            raise ValidationError('That Email Has Been Taken')
# defining the registration form class end


# defining the login form class end
class LoginForm(FlaskForm):

    identifier = StringField("Email or Username", validators=[DataRequired()], render_kw={
        'autocomplete': 'email'})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
                             'autocomplete': 'current-password'})
    submit = SubmitField('Sign In')
# defining the login form class end
