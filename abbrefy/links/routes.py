from flask import Blueprint, render_template, session, redirect, request, jsonify, url_for
from abbrefy.links.models import Link
from abbrefy.users.models import User
from datetime import datetime
from validators.url import url
# attaching the links blueprint
links = Blueprint('links', __name__)


# the link abbrefy route
@links.route('/api/hidden/url/abbrefy/', methods=['POST'])
def abbrefy():
    data = request.get_json()
    if not data:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400
    if not url(data['url']):
        return jsonify({"status": False, "error": "URL_ERROR"}), 400
    if request.origin in data['url']:
        return jsonify({"status": False, "error": "DUPLICATE_ERROR"}), 400
    # author = User.check_email(data['author'])['public_id']
    author = None
    if "current_user" in session:
        author = session['current_user']['public_id']
    new_link = Link(url=data['url'],
                    author=author)
    response = new_link.abbrefy()
    return jsonify(response)


# the link abbrefy route
@links.route('/<string:slug>', methods=['GET'])
def router(slug):
    origin = Link().get_url(slug)
    if not origin:
        return redirect(url_for('main.home'))
    if "https://" not in origin and "http://" not in origin:
        return redirect("https://" + origin)
    else:
        return redirect(origin)
