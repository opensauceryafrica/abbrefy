from flask import Blueprint, render_template, redirect, url_for, request, jsonify, flash, session
from datetime import datetime
from abbrefy.users.forms import RegistrationForm, LoginForm
from abbrefy.users.models import User
from abbrefy.users.tools import login_required, no_login_required, validate_username
# attaching the users blueprint
users = Blueprint('users', __name__)


# the signup route
@users.route('/auth/signup/', methods=['GET', 'POST'])
@no_login_required
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
@no_login_required
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
        user = User().signin(data)

        if user == False:
            flash('Invalid Signin Details', "danger")

        else:
            username = user['username']
            flash(f'Welcome back {username}', "success")
            return redirect(url_for('users.dashboard', username=username))

    return render_template('signin.html', datetime=datetime, site_title=site_title, form=form)


# the dashboard route
@users.route('/<string:username>/dashboard/', methods=['GET', 'POST'])
@login_required
def dashboard(user, username):

    site_title = "Abbrefy | Grow As You Abbrefy"
    links = User.my_links(user)

    return render_template('dashboard.html', datetime=datetime, site_title=site_title, links=links, len=len)


# the signout route
@users.route('/auth/signout/', methods=['GET'])
@login_required
def signout(user):
    response = User.signout()
    if response:
        return redirect(url_for('main.home'))


# the update profile route
@users.route('/auth/profile/', methods=['POST'])
@login_required
def profile(user):
    try:

        # getting the request data
        data = request.get_json()
        # validating the data was sent
        if not data:
            return jsonify({"status": False, "error": "DATA_ERROR"}), 400

        if not validate_username(data['usernameData']):
            return jsonify({"status": False,
                            "error": "DATA_VALIDATION_ERROR"}), 200

        # creating the URL object and abbrefying it
        if not "current_user" in session:
            return jsonify({"status": False, "error": "AUTHORIZATION_ERROR"}), 401

        user = session['current_user']['public_id']
        response = User().update_profile(user, data)
        print(response)

        if response['status'] == False:
            return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400

        return jsonify({"status": True, "message": "UPDATE_SUCCESS", "data": response}), 200

    # handling errors
    except KeyError:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400

    except:
        return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400
