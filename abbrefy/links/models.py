from uuid import uuid4
from abbrefy import mongo
from datetime import datetime
from abbrefy.links.tools import generate_slug
from flask import url_for


class Link:

    # initializing the class
    def __init__(self, url=None, author=None):
        self.url = url
        self.author = author

    # slug retrieval helper function
    def get_url(self, slug):
        if self.check_slug(slug):
            return self.check_slug(slug)['origin']
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
                "audience": []
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
            "url": url_for("links.router", slug=slug, _external=True)
        }

        return response
