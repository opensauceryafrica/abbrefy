from math import floor, log
from time import time
from flask import Blueprint, json, render_template, session, redirect, request, jsonify, url_for, flash, current_app
from abbrefy.links.models import Link
from abbrefy.users.models import User
from validators.url import url
from abbrefy.links.tools import check_duplicate, get_title
from abbrefy.users.tools import api_key_required, login_required
from abbrefy.links.bulk import upload_file, unordered_bulk_abbrefy, ordered_bulk_abbrefy, download_file
import os
from uuid import uuid4
import requests
from rq import Queue
from worker import conn
import json as JSON
from bson.json_util import dumps, loads

# attaching the links blueprint
links = Blueprint('links', __name__)

# creating a new redis queue object
q = Queue(connection=conn)


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
@links.route('/api/hidden/url/abbrefy/bulk/', methods=['POST'])
def bulk_abbrefy():

    # getting the request data
    data = request.form
    csvFile = request.files

    # validating a file was uploaded
    if not csvFile or not 'csv' in csvFile:
        return jsonify({"status": False, "error": "FILE_ERROR"}), 400

    # validating that the file was sent with the right identifier
    if csvFile['csv'].filename.split('.')[-1] != 'csv':
        return jsonify({"status": False, "error": "FILE_TYPE_ERROR"}), 400

    if not "current_user" in session:
        return jsonify({"status": False, "error": "AUTHORIZATION_ERROR"}), 401

    author = session['current_user']['public_id']
    try:
        # collecting the user's apiKey
        key = User.get_key(author)
    except:
        response = User().generate_api_key(author)

        if response == False:
            return jsonify({"status": False, "error": "KEY_LIMIT_EXCEEDED"}), 400

        if response['status'] == False:
            return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400
        
        key = User.get_key(author)

    # generating a new file name for the uploaded file
    to = str(floor(time() * 1000)) + uuid4().hex[0:7] + '.csv'

    # saving the csv file to firebase and disk storage
    if csvFile['csv'].filename == '':
        return jsonify({"status": False, "error": "FILE_ERROR"}), 400

    diskLoc = os.path.join(current_app.root_path,
                           'static/csv', str(floor(time())) + csvFile['csv'].filename)

    csvFile['csv'].save(diskLoc)

    origin, fileName = upload_file(diskLoc, to, download=True)

    if data and 'type' in data and data['type'] == 'unordered':

        # running an unordered bulk abbrefy based on user request.
        status = q.enqueue(unordered_bulk_abbrefy, fileName, key)
        # unordered_bulk_abbrefy(fileName, key)

        return jsonify({'status': True, 'message': 'Bulk Abbrefy Initiated'})

    # running an ordered bulk abbrefy based on user request.
    status = q.enqueue(ordered_bulk_abbrefy, fileName, author, origin)

    # uploading the newly created csv to firebase
    # slug, _ = upload_file(path, name)

    # # saving the information to the database
    # new_link = Link(author=author)
    # response = new_link.bulk_abbrefy(location=slug, origin=origin)
    return jsonify({'status': True, 'message': 'Bulk Abbrefy Initiated'})


# the abbrefy link router
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


# the abbrefy bulk links router
@links.route('/bulk/<string:slug>', methods=['GET'])
def bulk_router(slug):
    # checking if a slug was sent
    if not slug:
        flash('We couldn\'t find that CSV', 'danger')
        return redirect(url_for('main.home'))
    # checking if it is a CSV slug
    if not 'csv' in slug:
        flash('Only a CSV locator is recognized. Check your link and try again.', 'danger')
        return redirect(url_for('main.home'))
   # Getting IP address and querying user location
    try:
        ip_address = request.access_route[0] or request.remote_addr
        location = requests.get(os.environ.get(
            'IP_GEOLOCATOR') + str(ip_address)).json()['country']
    except:
        location = "Unknown"

    # downloading the link to the local disk file directory
    path = download_file(slug)

    # querying the database for the origin URL
    origin = Link().get_origin(slug)
    link = Link().get_link(slug)
    # checkking of an origin was found and handling error
    if not origin:
        flash('We couldn\'t find that CSV', 'danger')
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
    return redirect("http://abbrefy.xyz/static/csv/" + path.split('/')[-1])
    # return redirect("http://127.0.0.1:5000/static/" + path.split('/')[-1])


# the link update route
@links.route('/api/hidden/url/update/', methods=['UPDATE'])
@login_required
def update(user):
    data = request.get_json()
    # validating the data was sent
    if not data:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400
    # validating that URL isn't already abbrefied
    try:
        # checking if the link exists on abbrefy
        if not Link.check_slug(data['idSlug']):
            return jsonify({"status": False, "error": "EXISTENCE_ERROR"}), 404

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
            if key == "origin":
                # validating that data sent is a URL
                if not url(data[key]):
                    return jsonify({"status": False, "error": "URL_ERROR"}), 400
            update_data[key] = data[key]
            link[key] = data[key]
        filter = {"slug": data['idSlug']}
        update = {"$set": update_data}
        # print(update_data)

        response = Link.update_link(filter, link, update)
        if response['status'] == False:
            return jsonify({"status": False, "error": "UNKNOWN_ERROR"})
        return jsonify({"status": True, "message": "UPDATE_SUCCESS", "data": response}), 201

    except KeyError:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400

    except:
        return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400


# the link delete route
@links.route('/api/hidden/url/delete/', methods=['DELETE'])
@login_required
def delete(user):
    data = request.get_json()
    # validating the data was sent
    if not data:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400
    # validating that URL isn't already abbrefied
    try:
        # checking if the link exists on abbrefy
        if not Link.check_slug(data['idSlug']):
            return jsonify({"status": False, "error": "EXISTENCE_ERROR"}), 404

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
            return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400

        return jsonify({"status": True, "message": "DELETE_SUCCESS", "data": response}), 200

    except KeyError:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400

    except:
        return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400




# the abbrefy links search route
@links.route('/api/hidden/url/search/', methods=['POST'])
@login_required
def search(user):

    data = request.get_json()

    # validating the data was sent
    if not data:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400
    try:
        # searching for links that matches the query
        links = Link().search(data['term'], author=user['public_id'])

        if links['status'] == False:
            return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400

        return jsonify({"status": True, "message": "SEARCH_SUCCESS", "data": JSON.loads(dumps(links['links']))}), 200

    except KeyError:
        return jsonify({"status": False, "error": "DATA_ERROR"}), 400

    except Exception as e:
        print(e)
        return jsonify({"status": False, "error": "UNKNOWN_ERROR"}), 400

