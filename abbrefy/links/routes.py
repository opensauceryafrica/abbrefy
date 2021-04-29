from flask import Blueprint

# attaching the links blueprint
links = Blueprint('links', __name__)


@links.route('/profile/links/', methods=['GET', 'POST'])
def my_links():
    return
