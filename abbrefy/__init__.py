from flask import Flask
from flask_pymongo import PyMongo
from abbrefy.config import Config

# mongo = PyMongo()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)

    # mongo.init_app(app)

    from abbrefy.users.routes import users
    from abbrefy.links.routes import links
    from abbrefy.main.routes import main
    application.register_blueprint(users)
    application.register_blueprint(links)
    application.register_blueprint(main)

    return application
