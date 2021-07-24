# importing modules
from functools import wraps
from flask import session, flash, redirect, url_for, request, jsonify, current_app
import re
from abbrefy.users.models import User
import jwt
from flask_mail import Message
from threading import Thread
from abbrefy import Mail
from time import time


# login in required decorator
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'current_user' in session:
            if session['is_authenticated'] and "current_user" in session:
                user = session['current_user']

        else:
            flash('You must be signed in to access that page', 'danger')
            return redirect(url_for('users.signin'))

        return f(user, *args, **kwargs)

    return decorated


# login in required decorator
def no_login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'is_authenticated' in session:
            if session["is_authenticated"] == True:
                return redirect(url_for('users.dashboard'))

        return f(*args, **kwargs)

    return decorated


# login in required decorator
def api_key_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not "apiKey" in request.headers:
            return jsonify({"status": False, "error": "Please provide your API key."})

        apiKey = request.headers.get('apiKey')

        user = User.get_key_owner(apiKey)

        if not user:
            return jsonify({"status": False, "error": "Invalid API key provided."})

        return f(user, *args, **kwargs)

    return decorated


# helper function for validating username
def validate_username(username):
    validator = "^[a-zA-Z0-9_]+$"
    validated = re.match(validator, username)
    if not validated:
        return False
    return True


# send email with thread
def mail_thread(mail, app):
    with app.app_context():
        Mail.send(mail)


# send email function
def send_mail(user, email, exp_in=180):
    finder = jwt.encode({'public_id': user, 'exp': time(
    ) + exp_in}, current_app.config['SECRET_KEY'])

    mail = Message('Abbrefy Password Reset',
                   sender='Abbrefy', recipients=[email])
    link = url_for('users.reset', finder=finder, _external=True)
    mail.body = f'Below is the link to reset your password.\nThis link expires in 3 minutes.\n\n\n{link}'
    Thread(target=mail_thread, args=(
        mail, current_app._get_current_object())).start()
    return True


# find user using provided finder
def find_user(finder):
    try:
        user = jwt.decode(
            finder, current_app.config['SECRET_KEY'], algorithms='HS256')['public_id']
    except:
        return None
    return user
