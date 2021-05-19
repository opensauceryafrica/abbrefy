from flask import Blueprint, render_template, send_from_directory, request, current_app
from datetime import datetime
from abbrefy.users.tools import no_login_required


# attaching the main blueprint
main = Blueprint('main', __name__)


# serving sitemap and robots file for webcrawlers
@main.route('/robots.txt')
@main.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(current_app.static_folder, request.path[1:])


# the home route
@main.route('/')
@main.route('/home/')
@no_login_required
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
@no_login_required
def why():
    return render_template('about.html', datetime=datetime)


# the solutions route
@main.route('/pages/our-solutions#')
def solutions():
    return render_template('solutions.html', datetime=datetime)


# the features route
@main.route('/pages/features#')
@no_login_required
def features():
    return render_template('features.html', datetime=datetime)
