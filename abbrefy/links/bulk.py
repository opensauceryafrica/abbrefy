import csv
from math import floor
import requests as r
import time
from random import random
from firebase_admin import storage
import os
from flask import current_app
from abbrefy.links.models import Link
import urllib.request as opener


def upload_file(where, to, download=False):

    # Put your local file path
    # fileName = os.path.join(
    #     '/app/abbrefy', 'static/csv', to)
    bucket = storage.bucket()
    blob = bucket.blob(f'Abbrefy/{to}')
    blob.upload_from_filename(where)

    # Opt : if you want to make public access from the URL
    blob.make_public()

    fileName = ''

    if download:
        fileName = download_file(to)

    return to, blob.public_url


def download_file(where):

    # Put your local file path
    fileName = os.path.join(
        '/app/abbrefy', 'static/csv', where)

    bucket = storage.bucket()
    blob = bucket.blob(f'Abbrefy/{where}')
    blob.download_to_filename(fileName)

    return fileName


def unordered_bulk_abbrefy(file, key):

    f = opener.urlopen(file)

    reader = csv.reader(f, delimiter=',')
    line = 0

    for row in reader:
        if line == 100:
            return True
        if line == 0:
            line += 1
            continue
        else:

            url = 'http://abbrefy.xyz/api/v1/url/abbrefy/'

            h = {
                "apiKey": key
            }

            b = {
                "url": row[0]
            }

            resp = r.post(url=url, json=b, headers=h)
            res = resp.json()

            if len(row) > 1 and row[1]:
                url = 'http://abbrefy.xyz/api/v1/url/update/'

                h = {
                    "apiKey": key
                }

                b = {
                    "slug": row[1],
                    "idSlug": res['slug'],
                }

                respo = r.put(url=url, json=b, headers=h)
                res = respo.json()

    return True


def ordered_bulk_abbrefy(file, author, origin):

    key = 'd08604dafe2e4da988c6eb8818dce872'

    i = len(key)

    name = f'{key[int(random() * i):int(random() * i)]}{floor(time.time() * 1000)}.csv'

    location = os.path.join(
        '/app/abbrefy', 'static/origin', name)

    f = opener.urlopen(file)

    reader = csv.reader(f, delimiter=',')
    line = 0

    for row in reader:
        if line == 100:
            return True, location, name
        if line == 0:
            line += 1
            pass
        else:

            url = 'http://abbrefy.xyz/api/v1/url/abbrefy/'

            h = {
                "apiKey": key
            }

            b = {
                "url": row[0]
            }

            resp = r.post(url=url, json=b, headers=h)
            res = resp.json()

            initial = res['url']

            if len(row) > 1 and row[1]:
                url = 'http://abbrefy.xyz/api/v1/url/update/'

                h = {
                    "apiKey": key
                }

                b = {
                    "slug": row[1],
                    "idSlug": res['slug'],
                }

                respo = r.put(url=url, json=b, headers=h)
                res = respo.json()

            with open(location, 'a') as l:

                if 'url' in res:
                    l.write(res['url'] + '\n')
                    l.close()
                elif 'data' in res and 'url' in res['data']:
                    l.write(res['data']['url'] + '\n')
                    l.close()
                else:
                    l.write(res['error'] +
                            ',--- USED INSTEAD ---,' + initial + '\n')
                    l.close()

    # uploading the newly created csv to firebase
    slug, _ = upload_file(location, name)

    # saving the information to the database
    new_link = Link(author=author)
    response = new_link.bulk_abbrefy(location=slug, origin=origin)

    return True  # , location, name
