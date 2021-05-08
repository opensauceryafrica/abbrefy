from uuid import uuid4
from abbrefy import bcrypt, mongo
from datetime import datetime
from flask import jsonify


# the User class
class User:

    def __init__(self, username, email, password):
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

    # signin helper function
    @staticmethod
    def signin(signin_data):
        # querying user from db with username
        user = mongo.db.users.find_one(
            {"username": signin_data['identifier'].lower()})

        # validating user and password
        if user and bcrypt.check_password_hash(user["password"], signin_data['password']):
            return user

        else:
            # querying user from db  with email
            user = mongo.db.users.find_one(
                {"email": signin_data['identifier']})

            # validating user and password
            if user and bcrypt.check_password_hash(user["password"], signin_data['password']):
                return user

        return False

    @staticmethod
    def check_email(email):
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def check_username(username):
        return mongo.db.users.find_one({"username": username})
