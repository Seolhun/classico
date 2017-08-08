from flask_jwt import JWT

from resources.api.api_url import api, cors
from resources.render.render_url import cors, cache
# Classico setting information
from setting import settings
from setting.build_app import app
# Classico Database Config
from setting.databases import db, mongo
from setting.logging import logger
# Classico Security Config
from setting.security import bcrypt, authenticate, identity


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.SERVER_NAME
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


def initialize_app(flask_app):
    # Init MariaDB
    db.init_app(flask_app)

    # Create Database When generated First Request
    @flask_app.before_first_request
    def create_tables():
        db.create_all()

    # Init MongoDB
    mongo.init_app(flask_app, config_prefix='MONGO')

    # Init  Flask Cache
    cache.init_app(flask_app, config={'CACHE_TYPE': 'simple'})

    # When happens error - Bcrpyt : pip uninstall py-bcrypt => pip install py-bcrypt
    # Init Bcrypt
    bcrypt.init_app(flask_app)

    # Init CORS
    cors.init_app(flask_app)

    # Init RESTful API
    api.init_app(flask_app)

    # Init JWT
    JWT(flask_app, authenticate, identity)


if __name__ == '__main__':
    configure_app(app)
    initialize_app(app)
    logger.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))

    app.run(port=5000, debug=True)
