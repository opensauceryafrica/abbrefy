from flask import Blueprint, render_template
from datetime import datetime


# attaching the main blueprint
main = Blueprint('main', __name__)


# the home route
@main.route('/')
@main.route('/home/')
def home():
    return render_template('home.html', datetime=datetime)


# the about route
@main.route('/about/')
def about():
    return render_template('about.html', datetime=datetime)
