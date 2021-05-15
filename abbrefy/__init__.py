# importing modules
from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from abbrefy.config import Config
from flask_cors import CORS

# instantiating  pymongo
mongo = PyMongo()
# mongo = "make"

# instantiating bcrypt for password hash
bcrypt = Bcrypt()

# setting up CORS
cors = CORS()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)
    mongo.init_app(application)
    bcrypt.init_app(application)
    cors.init_app(application)

    from abbrefy.users.routes import users
    from abbrefy.links.routes import links
    from abbrefy.main.routes import main
    application.register_blueprint(users)
    application.register_blueprint(links)
    application.register_blueprint(main)

    return application
