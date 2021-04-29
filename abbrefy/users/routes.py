from flask import Blueprint

# attaching the users blueprint
users = Blueprint('users', __name__)


@users.route('/signup/', methods=['GET', 'POST'])
def signup():
    return
