# importing modules
from functools import wraps
from flask import session, flash, redirect, url_for

# login in required decorator
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
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
        if 'is_authenticated' in session and session["is_authenticated"] == True:
            return redirect(url_for('users.dashboard', username=session['current_user']['username']))

        return f(*args, **kwargs)

    return decorated