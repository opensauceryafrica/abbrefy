from uuid import uuid4
from abbrefy import mongo
from datetime import datetime
from abbrefy.links.tools import generate_slug, get_title
from flask import url_for


class Link:

    # initializing the class
    def __init__(self, url=None, author=None, title=None):
        self.url = url
        self.author = author
        self.title = get_title(self.url)

    # slug retrieval helper function
    def get_origin(self, slug):
        if self.check_slug(slug):
            return self.check_slug(slug)['origin']
        return None

    # link object retrieval helper function
    def get_link(self, slug):
        link = self.check_slug(slug)
        if link:
            del link['_id']
            return link
        return None

    # slug validator helper function
    @staticmethod
    def check_slug(slug):
        return mongo.db.links.find_one({"slug": slug})

    # slug generator helper function
    def new_slug(self):
        slug = generate_slug()
        if self.check_slug(slug):
            new_slug()
        return slug

    # updating a link data
    @staticmethod
    def update_link(filter, new, update):

        try:
            # adding link object to db
            mongo.db.links.update_one(filter, update)
        except:
            response = {
                "status": False,
                "error": "Something went wrong. Please try again."
            }
            return response

        response = {

            "status": True,
            "message": "Abbrefy link update successful.",
            "origin": new['origin'],
            "url": url_for("links.router", slug=new['slug'], _external=True),
            "title": new['title'],
            "clicks": new['clicks']
        }

        return response

    # abbrefy helper function
    def abbrefy(self):

        try:
            slug = self.new_slug()

            # creating the link object
            link = {
                "author": self.author,
                "public_id": uuid4().hex,
                "date_created": datetime.utcnow(),
                "origin": self.url,
                "slug": slug,
                "stealth": False,
                "clicks": 0,
                "audience": [],
                "title": self.title
            }

            # adding link object to db
            mongo.db.links.insert_one(link)
        except:
            response = {
                "status": False,
                "error": "Something went wrong. Please try again."
            }
            return response

        response = {
            "status": True,
            "message": "URL abbrefy successful.",
            "origin": self.url,
            "url": url_for("links.router", slug=slug, _external=True),
            "title": self.title}

        return response
