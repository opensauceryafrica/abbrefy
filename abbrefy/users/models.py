from uuid import uuid4
from abbrefy import bcrypt, mongo
from datetime import datetime
from flask import session


# the User class
class User:
    # initializing the class
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password

    # signup helper function
    def signup(self):

        try:
            user = {
                'public_id': uuid4().hex,
                'username': self.username.lower(),
                'email': self.email,
                'password': bcrypt.generate_password_hash(
                    self.password).decode('utf-8'),
                'join_date': datetime.utcnow()
            }

            mongo.db.users.insert_one(user)
        except:
            return False

        return True

    # creating a user session
    @staticmethod
    def init_session(user):
        session['is_authenticated'] = True
        del user['password']
        del user['_id']
        session['current_user'] = user
        session.permanent = True
        return user

    # signin helper function
    def signin(self, signin_data):
        # querying user from db with username
        user = mongo.db.users.find_one(
            {"username": signin_data['identifier'].lower()})

        # validating user and password
        if user and bcrypt.check_password_hash(user["password"], signin_data['password']):
            return self.init_session(user)

        else:
            # querying user from db  with email
            user = mongo.db.users.find_one(
                {"email": signin_data['identifier']})

            # validating user and password
            if user and bcrypt.check_password_hash(user["password"], signin_data['password']):
                return self.init_session(user)

        return False

    # signout helper function
    @staticmethod
    def signout():
        if session['is_authenticated'] and session['current_user']:
            session['is_authenticated'] = False
            del session['current_user']
        return True

    # email validator helper function
    @staticmethod
    def check_email(email):
        return mongo.db.users.find_one({"email": email})

    # username validator helper function
    @staticmethod
    def check_username(username):
        return mongo.db.users.find_one({"username": username})

    @staticmethod
    def my_links(user):
        links = mongo.db.links.find({"author": user['public_id']})
        return links
