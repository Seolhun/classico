# Classico Dependencies
from flask import Flask
from flask_jwt import JWT
from flask_swagger import swagger
from raven.contrib.flask import Sentry

from resources.api.api_url import api, cors
# Classico setting information
from setting import settings
# Classico Database Config
from setting.databases import db, mongo
from setting.logging import logger
# Classico Security Config
from setting.security import authenticate, identity, CONFIG_DEFAULTS
from setting.security import bcrypt

# Sentry : Monitoring System

app = Flask(__name__)
sentry = Sentry(app, dsn='https://2519ad4fac6f453b9f3d28364c9544fb:2f17efbd161243ce889d3a03a8a5eaf4@sentry.io/200070')


def configure_app(flask_app):
    flask_app.config['FLASK_SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['FLASK_DEBUG'] = settings.FLASK_DEBUG

    # MariaDB SQLAlchemy Configuration
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SQLALCHEMY_ECHO'] = settings.SQLALCHEMY_ECHO

    # MongoDB PyMongo Configuration
    flask_app.config['MONGO_USERNAME'] = settings.MONGO_USERNAME
    flask_app.config['MONGO_PASSWORD'] = settings.MONGO_PASSWORD
    flask_app.config['MONGO_HOST'] = settings.MONGO_HOST
    flask_app.config['MONGO_PORT'] = settings.MONGO_PORT
    flask_app.config['MONGO_DBNAME'] = settings.MONGO_DBNAME

    # JWT Setting
    flask_app.config['SECRET_KEY'] = 'super-secret'
    flask_app.debug = True


def initialize_app(flask_app):
    # Swagger
    swag = swagger(flask_app)

    # Init JWT Config
    for key, value in CONFIG_DEFAULTS.items():
        app.config.setdefault(key, value)
    app.config.setdefault('JWT_SECRET_KEY', app.config['SECRET_KEY'])
    jwt = JWT(app, authenticate, identity)  # /auth

    # Init MariaDB
    db.init_app(flask_app)
    # Init MongoDB
    mongo.init_app(flask_app, config_prefix='MONGO')

    # Init Resource API
    api.init_app(flask_app)

    # When happens error - Bcrpyt : pip uninstall py-bcrypt => pip install py-bcrypt
    # Init Bcrypt
    bcrypt.init_app(flask_app)

    # Init CORS
    cors.init_app(app)


# Create Database When generated First Request
@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    configure_app(app)
    initialize_app(app)
    logger.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))

    app.run(port=5000, debug=True)
