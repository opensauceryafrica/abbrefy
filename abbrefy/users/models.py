from uuid import uuid4
from abbrefy import bcrypt, mongo
from datetime import datetime
from flask import session
import safe


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
                'email': self.email.lower(),
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
                {"email": signin_data['identifier'].lower()})

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
        return mongo.db.users.find_one({"email": email.lower()})

    # username validator helper function
    @staticmethod
    def check_username(username):
        return mongo.db.users.find_one({"username": username.lower()})

    # link retrieval helper function
    @staticmethod
    def my_links(user):
        links = mongo.db.links.find(
            {"author": user['public_id']}).sort('date_created', -1)
        return links

    # user retrieval helper function
    @staticmethod
    def get_user(public_id):
        return mongo.db.users.find_one({"public_id": public_id})

    # profile update helper function
    def update_profile(self, id, data):
        try:
            updateData = {}
            user = self.get_user(id)
            for key in data:
                # checking for username change
                if key == "usernameData":
                    if user['username'] == data[key]:
                        continue
                    updateData["username"] = data[key]
                # checking for password change
                if key == "passwordData":
                    if not (bcrypt.check_password_hash(user['password'], data[key]['oldPassword'])):
                        return False
                    strong = safe.check(data[key]['newPassword'])
                    if not strong:
                        return True
                    newPassword = bcrypt.generate_password_hash(
                        data[key]['newPassword']).decode("utf-8")
                    updateData["password"] = newPassword

            # creating the update and commiting to the DB
            if len(updateData) > 0:
                update = {"$set": updateData}
                filterData = {'public_id': user['public_id']}
                mongo.db.users.update_one(filterData, update)

            # getting the new data of the user
            userUpdate = self.get_user(id)
            # starting a new session for the user
            userData = self.init_session(userUpdate)

            response = {
                "status": True,
                "message": "Your profile has been updated successfully",
                "userData": userData
            }

        except:
            response = {
                "status": False,
                "error": "Something went wrong. Please try again."
            }
            # return response
        return response

    # generate API Key helper function
    def generate_api_key(self, id):

        try:
            # getting the user object
            user = self.get_user(id)
            # retrieving all the user's API keys
            userKeys = self.get_keys(user)
            # validating user hasn't created more than 2 API keys
            if userKeys.count() >= 2:
                return False

            # creating the API key object
            key = {
                "author": user['public_id'],
                "apiKey": uuid4().hex,
                "dateCreated": datetime.utcnow()
            }
            # adding the API key to the database
            mongo.db.keys.insert(key)

            del key["_id"]

        except:

            response = {
                "status": False,
                "message": "Something went wrong. Please try again."
            }

            return response

        response = {
            "status": True,
            "message": "API Key successfully generate",
            "apiData": key
        }
        return response

    # retrieve API Key helper function
    @staticmethod
    def get_key_owner(key):
        return mongo.db.keys.find_one({"apiKey": key})['author']

    # retrieve API Key helper function
    @staticmethod
    def get_keys(user):
        return mongo.db.keys.find({"author": user['public_id']})
