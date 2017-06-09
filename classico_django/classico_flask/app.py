import settings
import logging.config

from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt import JWT
from flask_sqlalchemy import SQLAlchemy
from security import authenticate, identity

from api.stack.endpoints.stack import ns as stack_namespace
from api.user.endpoints.user import ns as user_namespace
from api.board.endpoints.board import ns as board_namespace

import requests
from bs4 import BeautifulSoup

from api.stack.endpoints.stack import Stack, StackList

# # # # # # # # # # # # # # # #
# Setting REST App
app = Flask(__name__)
app.secret_key = 'shooney'

# # # # # # # # # # # # # # # #
# /auth Security
jwt = JWT(app, authenticate, identity)


api = Api(app)
api.add_resource(Stack, '/stack/<string:name>')
api.add_resource(StackList, '/stacks')


# # # # # # # # # # # # # # # #
def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


# # # # # # # # # # # # # # # #
def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)

    # Add Namespace URL
    api.add_namespace(stack_namespace)
    api.add_namespace(user_namespace)
    api.add_namespace(board_namespace)
    flask_app.register_blueprint(blueprint)

    db = SQLAlchemy(app)
    db.create_all()
    db.init_app(flask_app)


# # # # # # # # # # # # # # # #
def main():
    initialize_app(app)
    app.run(debug=settings.FLASK_DEBUG, port=5000)





if __name__ == "__main__":
    main()

# BeautifulSoup Part
page = requests.get("https://stackshare.io/javascript")
page
page.status_code
soup = BeautifulSoup(page.content, 'html.parser')
