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
@main.route('/pages/about/')
def about():
    return render_template('about.html', datetime=datetime)


# the abbrefy101 route
@main.route('/pages/abbrefy101/')
def abbrefy101():
    return render_template('about.html', datetime=datetime)


# the why abbrefy route
@main.route('/pages/why-abbrefy/')
def why():
    return render_template('about.html', datetime=datetime)


# the solutions route
@main.route('/pages/our-solutions#')
def solutions():
    return render_template('solutions.html', datetime=datetime)


# the features route
@main.route('/pages/features#')
def features():
    return render_template('features.html', datetime=datetime)
