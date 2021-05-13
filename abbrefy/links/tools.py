from uuid import uuid4
import random
from flask import request
from bs4 import BeautifulSoup as bs
import requests


# URL title helper function
def get_title(url):
    try:
        response = requests.get(url).content
        soup = bs(response, "html.parser")
        title = soup.find('title').text
        return title
    except:
        return None


# duplicate link helper function
def check_duplicate(url):
    url = url.split('/')
    return url[3] if len(url) >= 4 else None


# sorter helper function
def sorter(length=7):
    end = random.choice(range(33))
    start = end - length
    if start < 0:
        start, end = sorter()
    return start, end


# function for generating a reset token
def generate_slug():
    slug = uuid4().hex
    start, end = sorter()
    return slug[start:end]
