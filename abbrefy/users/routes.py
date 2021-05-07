from flask import Blueprint, render_template
from datetime import datetime
# attaching the users blueprint
users = Blueprint('users', __name__)

# the signup route


@users.route('/auth/signup/', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html', datetime=datetime)


# the signin route
@users.route('/auth/signin/', methods=['GET', 'POST'])
def signin():
    return render_template('signin.html', datetime=datetime)
