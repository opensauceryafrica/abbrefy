from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash
from datetime import datetime
from abbrefy.users.forms import RegistrationForm, LoginForm
from abbrefy.users.models import User
# attaching the users blueprint
users = Blueprint('users', __name__)


# the signup route
@users.route('/auth/signup/', methods=['GET', 'POST'])
def signup():

    # instantiationg the form
    form = RegistrationForm()

    # defining the site title
    site_title = "Abbrefy | Power With Every Link"

    # handling form validation
    if form.validate_on_submit():

        new_user = User(form.username.data,
                        form.email.data, form.password.data)

        response = new_user.signup()

        # sending flased message
        if response == True:
            flash(
                "Welcome to Abbrefy", "success")
            return redirect(url_for('users.dashboard', username=form.username.data))

        else:
            # sending flased message
            flash(
                "Sign Up Failed. Please Try Again", "danger")

    return render_template('signup.html', datetime=datetime, form=form, site_title=site_title)


# the signin route
@users.route('/auth/signin/', methods=['GET', 'POST'])
def signin():

    # instantiationg the form
    form = LoginForm()
    # defining the site title
    site_title = "Abbrefy | Power With Every Link"

    # handling form validation
    if form.validate_on_submit():
        data = {
            "identifier": form.identifier.data,
            "password": form.password.data
        }
        user = User.signin(data)

        if user == False:
            flash('Invalid Signin Details', "danger")

        else:
            username = user['username']
            flash(f'Welcome back {username}', "success")
            return redirect(url_for('users.dashboard', username=username))

    return render_template('signin.html', datetime=datetime, site_title=site_title, form=form)


# the dashboard route
@users.route('/<string:username>/dashboard/', methods=['GET', 'POST'])
def dashboard(username):

    site_title = "Abbrefy | Grow With Every Link"

    return render_template('dashboard.html', datetime=datetime, site_title=site_title)
