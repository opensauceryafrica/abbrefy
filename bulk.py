import csv
from math import floor
import requests as r
import time
from random import random

key = "5a690b08d33a4f7e998565a0510b0e53"
file = 'links.csv'


def unordered_bulk_abbrefy(file, key):

    try:
        with open(file) as f:

            reader = csv.reader(f, delimiter=',')
            line = 0

            for row in reader:
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

    except:
        return False


def ordered_bulk_abbrefy(file):

    key = 'd08604dafe2e4da988c6eb8818dce872'

    i = len(key)

    location = f'{key[int(random() * i):int(random() * i)]}{floor(time.time() * 1000)}.csv'

    with open(file) as f:

        reader = csv.reader(f, delimiter=',')
        line = 0

        for row in reader:
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
                                ' --- USED INSTEAD ---  ' + initial + '\n')
                        l.close()

    return True, location
