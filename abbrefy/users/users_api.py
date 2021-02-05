from flask import Blueprint, render_template, session, redirect, request, jsonify, url_for, flash
from abbrefy.links.models import Link
from abbrefy.users.models import User
from datetime import datetime
from validators.url import url
from abbrefy.links.tools import check_duplicate, get_title
from abbrefy.users.tools import api_key_required
from bson.json_util import dumps, loads
import os
import requests
import json
# attaching the links blueprint
usersApi = Blueprint('usersApi', __name__)


# the public API link route
@usersApi.route('/api/v1/me/links/')
@api_key_required
def links(user):

    try:

        if request.args.get('sort') == 'desc':

            # getting links for the user
            links = User.my_links(user)
            # keys = User.get_keys(user)
            links = dumps(links)
            links = json.loads(links)
        elif request.args.get('sort') == 'asc':
            # getting links for the user
            links = User.my_links_asc(user)
            # keys = User.get_keys(user)
            links = dumps(links)
            links = json.loads(links)
        else:
            # getting links for the user
            links = User.my_links(user)
            # keys = User.get_keys(user)
            links = dumps(links)
            links = json.loads(links)

        return jsonify({"status": True, "linkData": links})

    except:
        return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400


# the public API route
@usersApi.route('/api/v1/me/')
@api_key_required
def un(user):

    links = User.my_links(user)
    keys = User.get_keys(user)

    return render_template('dashboard.html', datetime=datetime, site_title=site_title, links=links, len=len, keys=keys)
