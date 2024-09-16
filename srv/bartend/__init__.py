import config
import logging

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from bartend import factory


BASE_CONFIG = config.base_config()
log = logging.getLogger('werkzeug')
bcrypt = Bcrypt()
cache = Cache()
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
session = Session()
redis = BASE_CONFIG.SESSION_REDIS


def create_app():
    app = Flask(__name__, static_url_path='/')
    init_base_config(app)
    init_extensions(app)
    register_error_handlers(app)
    # register_commands(app)
    config_log(log)
    return app


def init_base_config(app):
    app.url_map.strict_slashes = False
    app.config.from_object(BASE_CONFIG)
    CORS(app, supports_credentials=True)

    if not BASE_CONFIG.IS_PRODUCTION:
        app.debug = True


def init_extensions(app):
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    session.init_app(app)


def register_error_handlers(app):
    factory.error_handlers(app, jwt)


# def register_commands(app):
#     from tests.commands import cy_commands

#     cy_commands(app)


def config_log(log):
    log.setLevel(logging.WARNING) if BASE_CONFIG.IS_PRODUCTION else log.setLevel(logging.DEBUG)


app = create_app()


""" always register routes last """
factory.easy_blueprints(BASE_CONFIG)
