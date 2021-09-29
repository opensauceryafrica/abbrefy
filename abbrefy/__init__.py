# importing modules
from flask import Flask, app
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from abbrefy.config import Config
from flask_cors import CORS
from flask_mail import Mail
from firebase_admin import credentials, initialize_app
import os

# instantiating  pymongo
mongo = PyMongo()
# mongo = "make"

# instantiating bcrypt for password hash
bcrypt = Bcrypt()

# instantiating mail for sending emails
Mail = Mail()

# setting up CORS
cors = CORS()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)
    mongo.init_app(application)
    bcrypt.init_app(application)
    cors.init_app(application)
    Mail.init_app(application)

    os.environ['ROOT_PATH'] = application.root_path

    # Init firebase with your credentials
    cred = credentials.Certificate(os.path.join(
        application.root_path, 'static', os.environ.get('Private_Key_JSON')))
    initialize_app(
        cred, {'storageBucket': os.environ.get('Image_Bucket')})

    from abbrefy.users.routes import users
    from abbrefy.links.routes import links
    from abbrefy.main.routes import main
    from abbrefy.links.links_api import linksApi
    from abbrefy.users.users_api import usersApi
    application.register_blueprint(users)
    application.register_blueprint(links)
    application.register_blueprint(main)
    application.register_blueprint(linksApi)
    application.register_blueprint(usersApi)

    return application
