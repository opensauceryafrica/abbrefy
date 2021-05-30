from flask import Blueprint, render_template, session, redirect, request, jsonify, url_for, flash
from abbrefy.links.models import Link
from abbrefy.users.models import User
from datetime import datetime
from validators.url import url
from abbrefy.links.tools import check_duplicate, get_title
import os
import requests
# attaching the links blueprint
links = Blueprint('links', __name__)


# the link abbrefy route
@links.route('/api/hidden/url/abbrefy/', methods=['POST'])
def abbrefy():
    # getting the request data
    data = request.get_json()
    # validating the data was sent
    if not data:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400
    # validating that data sent is a URL
    if not url(data['url']):
        return jsonify({"status": False, "error": "URL_ERROR"}), 400
    # validating that URL isn't already abbrefied
    slug = check_duplicate(data['url'])
    if slug and Link.check_slug(slug):
        return jsonify({"status": False, "error": "DUPLICATE_ERROR"}), 400
    # creating the URL object and abbrefying it
    author = None
    if "current_user" in session:
        author = session['current_user']['public_id']
    new_link = Link(url=data['url'],
                    author=author)
    response = new_link.abbrefy()
    return jsonify(response)


# the link abbrefy route
@links.route('/<string:slug>/', methods=['GET'])
def router(slug):
    # Getting IP address and querying user location
    try:
        ip_address = request.access_route[0] or request.remote_addr
        location = requests.get(os.environ.get(
            'IP_GEOLOCATOR') + str(ip_address)).json()['country']
    except:
        location = "Unknown"
    # querying the database for the origin URL
    origin = Link().get_origin(slug)
    link = Link().get_link(slug)
    # checkking of an origin was found and handling error
    if not origin:
        flash('We couldn\'t find that link', 'danger')
        return redirect(url_for('main.home'))
    # checking if stealth mode is activated
    if link and link['stealth'] == True:
        flash('The author has made that link private', 'danger')
        return redirect(url_for('main.home'))
    # updating the number of clicks
    filter = {"slug": slug}
    new = link
    new['clicks'] += 1
    # updating the audience of the link object
    if location not in link['audience']:
        link['audience'].append(location)
        new['audience'] = link['audience']
        update = {
            "$set": {"clicks": new['clicks'], "audience": new['audience']}}
    else:
        update = {"$set": {"clicks": new['clicks']}}
    response = Link.update_link(filter, new, update)
    # updating origin to match URL standard and redirecting
    if "https://" not in origin and "http://" not in origin:
        return redirect("https://" + origin)
    else:
        return redirect(origin)


@links.route('/api/hidden/url/update/', methods=['UPDATE'])
def update():
    data = request.get_json()
    # validating the data was sent
    if not data:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400
    # validating that URL isn't already abbrefied
    try:
        # checking if the link exists on abbrefy
        if not Link.check_slug(data['idSlug']):
            return jsonify({"status": False, "error": "EXISTENCE_ERROR"}), 400

        if "slug" in data:
            if data['slug'] and Link.check_slug(data['slug']):
                return jsonify({"status": False, "error": "USAGE_ERROR"}), 400

        # creating the URL object and abbrefying it
        if not "current_user" in session:
            return jsonify({"status": False, "error": "AUTHORIZATION_ERROR"}), 401
        link = Link().get_link(data['idSlug'])
        author = session['current_user']['public_id']
        if link['author'] != author:
            return jsonify({"status": False, "error": "AUTHORIZATION_ERROR"}), 401

         # updating the Link object and saving to the database
        update_data = {}
        for key in data:
            if key == "idSlug":
                continue
            update_data[key] = data[key]
            link[key] = data[key]
        filter = {"slug": data['idSlug']}
        update = {"$set": update_data}
        # print(update_data)

        response = Link.update_link(filter, link, update)
        return jsonify({"status": True, "message": "UPDATE_SUCCESS", "data": response}), 201

    except KeyError:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400

    except:
        return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400


@links.route('/api/hidden/url/delete/', methods=['DELETE'])
def delete():
    data = request.get_json()
    # validating the data was sent
    if not data:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400
    # validating that URL isn't already abbrefied
    try:
        # checking if the link exists on abbrefy
        if not Link.check_slug(data['idSlug']):
            return jsonify({"status": False, "error": "EXISTENCE_ERROR"}), 400

        # creating the URL object and abbrefying it
        if not "current_user" in session:
            return jsonify({"status": False, "error": "AUTHORIZATION_ERROR"}), 401

        # retrieving the link from the DB
        link = Link().get_link(data['idSlug'])
        author = session['current_user']['public_id']

        if link['author'] != author:
            return jsonify({"status": False, "error": "AUTHORIZATION_ERROR"}), 401

        response = Link.delete(link)
        if response['status'] == False:
            return jsonify({"status": False, "error": "UNKNOWN_ERROR"})

        return jsonify({"status": True, "message": "DELETE_SUCCESS", "data": response}), 200

    except KeyError:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400

    except:
        return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400
