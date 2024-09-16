import os
import pymysql  # noqa: F401
import redis
import secrets

from datetime import timedelta
from distutils.util import strtobool
from dotenv import load_dotenv


"""
no environ variables should exist locally
all env variables should be set explicitly by project .env or runner/secrets
"""
if not os.environ.get('THERE_IS_NO_ENVIRONMENT'):
    load_dotenv()


"""
ref project abspath
"""
basedir = os.path.abspath(os.path.dirname(__file__))


def base_config():
    """
    finalized config for the app factory to consume
    """
    base_config = ProConfig if Config.IS_PRODUCTION else DevConfig

    if os.environ.get('USE_TEST_API'):
        print(' * TestConfig ENABLED')
        base_config = TestConfig

    return base_config


class Config:
    """
    base config
    """
    SERVER_PORT = 5000
    SECRET_KEY = secrets.token_hex(64)
    BASE_DIR = basedir
    DOMAIN_NAME = os.environ['DOMAIN_NAME']
    SESSION_ID = os.environ['SESSION_ID']
    SESSION_ID_EMAIL = os.environ['SESSION_ID_EMAIL']
    SELLER_EMAIL = 'rapid537@zoho.com'
    EMAIL_FROM_ADDRESS = os.environ['EMAIL_FROM_ADDRESS']
    EMAIL_FROM_PW = os.environ['SMTP_PW']
    JWT_BYPASS = strtobool(os.environ['JWT_BYPASS'])
    FSD_ENVIRONMENT = os.environ['FSD_ENVIRONMENT']
    IS_PRODUCTION = True if (
        os.environ['FSD_ENVIRONMENT'] == 'production'
    ) else False

    """
    api tokens
    """
    # register sandbox api tokens here

    """
    mysql config
    """
    sqldb_base = 'mysql+pymysql://root:'
    sqldb_root_pw = os.environ["MYSQL_ROOT_PASSWORD"]
    sqldb_url = os.environ["MYSQL_URL"]
    sqldb_name = os.environ["MYSQL_DATABASE"]
    sqldb_uri = f'{sqldb_base}{sqldb_root_pw}@{sqldb_url}/{sqldb_name}'

    """
    ORM config
    """
    SQLALCHEMY_DATABASE_URI = sqldb_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """
    session config
    """
    SESSION_REDIS_PASSWORD = os.environ['SESSION_REDIS_PASSWORD']
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_NAME = 'studio_session'
    SESSION_REDIS = redis.from_url(f'redis://:{SESSION_REDIS_PASSWORD}@0.0.0.0:9000')

    """
    jwt extended config
    """
    JWT_SECRET_KEY = secrets.token_hex(64)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=5)
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_CSRF_METHODS = ['GET', 'POST', 'DELETE']

    """
    flask-caching
    """
    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_HOST = '0.0.0.0'
    CACHE_REDIS_PORT = '9000'
    CACHE_REDIS_PASSWORD = os.environ["CACHE_REDIS_PASSWORD"]


class DevConfig(Config):
    SECURE_COOKIE = False
    STUDIO_DOMAIN = 'code.dev.com'
    JWT_BYPASS = False
    BLOCK_OUTBOUND_EMAIL = True


class ProConfig(Config):
    SECURE_COOKIE = True
    STUDIO_DOMAIN = Config.DOMAIN_NAME
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Strict'
    SELLER_EMAIL = 'example@mail.net'


class TestConfig(DevConfig):
    SERVER_PORT = 5001
    BLOCK_OUTBOUND_EMAIL = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:7001/fsd_studio_test_db'
    FSD_ENVIRONMENT = 'testing'
    TESTING = True
    ENV = 'testing'
    FLASK_ENV = 'development'

    """
    ------------
    USE_TEST_API
    ------------
    EXPORT on (*flask run) to enable TestConfig
    this applies to cypress (*flask commands) as well as the flask TEST server(:5001)
    """
    USE_TEST_API = True
