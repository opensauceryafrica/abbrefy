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
from firebase_admin import credentials, initialize_app

pJSON = 'emmyh-coin-firebase-adminsdk-qs8br-b5c695d98a.json'
bucket = 'emmyh-coin.appspot.com'
# r"C:\Users\Samperfect\Downloads\Codes\Projects\abbrefy\abbrefy"
root_path = '/app/abbrefy'


def upload_file(where, to, download=False):

    # Put your local file path
    # fileName = os.path.join(
    #     root_path, 'static/csv', to)
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
        root_path, 'static/csv', where)

    bucket = storage.bucket()
    blob = bucket.blob(f'Abbrefy/{where}')
    blob.download_to_filename(fileName)

    return fileName


def unordered_bulk_abbrefy(file, key):

    i = len(key)

    temp = f'{key[int(random() * i):int(random() * i)]}{floor(time.time() * 1000)}.csv'

    tempo = os.path.join(
        root_path, 'static/origin', temp)

    f = opener.urlopen(file)

    data = f.read().decode('utf-8')

    with open(tempo, 'w') as t:
        t.write(data)
        t.close()

    with open(tempo) as f:

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
                line += 1

    return True


def ordered_bulk_abbrefy(file, author, origin):

    key = 'd08604dafe2e4da988c6eb8818dce872'

    i = len(key)

    name = f'{key[int(random() * i):int(random() * i)]}{floor(time.time() * 1000)}.csv'
    time.sleep(2)
    temp = f'{key[int(random() * i):int(random() * i)]}{floor(time.time() * 1000)}.csv'

    location = os.path.join(
        root_path, 'static/origin', name)
    tempo = os.path.join(
        root_path, 'static/origin', temp)

    f = opener.urlopen(file)

    data = f.read().decode('utf-8')

    print(data)

    with open(tempo, 'w') as t:
        t.write(data)
        t.close()

    with open(tempo) as f:
        reader = csv.reader(f, delimiter=',')
        line = 0

        for row in reader:

            print(row)

            if line == 100:
                return True, location, name
            if line == 0:
                line += 1
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
                line += 1

        # uploading the newly created csv to firebase
        # Init firebase with your credentials
        cred = credentials.Certificate(
            os.path.join(root_path, 'static', pJSON))
        initialize_app(cred, {'storageBucket': bucket})
        slug, _ = upload_file(location, name)

        # saving the information to the database
        new_link = Link(author=author)
        response = new_link.bulk_abbrefy(location=slug, origin=origin)
        print(response)

    return True  # , location, name


# path = 'https://storage.googleapis.com/emmyh-coin.appspot.com/Abbrefy/16329178662673227421.csv'

# ordered_bulk_abbrefy(path, '293283b1d5044b869fe5596532b7bc9e',
#                      '1632879672772.csv')
