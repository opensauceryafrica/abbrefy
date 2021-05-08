# importing the required modules
import safe
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
# from ss.models import User
# from flask_login import current_user
# importing the required modules end

# forbiden usernames to allow for routes consistency
FORBIDEN_NAMES = ['signin', 'signup', 'signout', 'about', 'collections']


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
    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data.lower()).first()
    #     if user or username.data.lower() in FORBIDEN_NAMES:
    #         raise ValidationError('That Username Has Been Taken')

    # setting up custom validation to check if email exists
    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data.lower()).first()
    #     if user:
    #         raise ValidationError('That Email Has Been Taken')
# defining the registration form class end


# defining the login form class end
class LoginForm(FlaskForm):

    email = StringField("Email", validators=[DataRequired(), Email()], render_kw={
        'autocomplete': 'email'})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={
                             'autocomplete': 'current-password'})
    remember_me = BooleanField("Remember Me")
    submit = SubmitField('Sign In')
# defining the login form class end
