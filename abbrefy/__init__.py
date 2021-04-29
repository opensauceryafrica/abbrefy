from flask import Flask
from flask_pymongo import PyMongo
from abbrefy.config import Config

# mongo = PyMongo()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # mongo.init_app(app)

    from abbrefy.users.routes import users
    from abbrefy.links.routes import links
    from abbrefy.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(links)
    app.register_blueprint(main)

    return app
