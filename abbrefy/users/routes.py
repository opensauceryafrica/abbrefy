from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from datetime import datetime
from abbrefy.users.forms import RegistrationForm, LoginForm
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

        return redirect(url_for('users.signup'))

    return render_template('signup.html', datetime=datetime, form=form, site_title=site_title)


# the signin route
@users.route('/auth/signin/', methods=['GET', 'POST'])
def signin():

    site_title = "Abbrefy | Power With Every Link"

    return render_template('signin.html', datetime=datetime, site_title=site_title)
