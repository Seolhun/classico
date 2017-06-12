import settings
from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user.user import UserList, UserRegister
from resources.stack.stack import Stack, StackList
from resources.stack.stack_scrap import StackScrap, StackScrapPost
from flask_swagger import swagger

app = Flask(__name__)
app.config['FLASK_SERVER_NAME'] = settings.FLASK_SERVER_NAME
app.config['FLASK_DEBUG'] = settings.FLASK_DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = settings.SQLALCHEMY_ECHO
# app.config['RESTPLUS_SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
# app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
# app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
# app.config['RESTPLUS_ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP
app.secret_key = 'shooney'

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

# Stack Scrap Part
api.add_resource(Stack, '/stack/<string:stack_name>')
api.add_resource(StackList, '/stacks')

# Stack Scrap Part
api.add_resource(StackScrap, '/scrap/<string:stack_name>')
api.add_resource(StackScrapPost, '/scrap')

# User Part
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')


@app.route("/spec")
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Classico RESTful API"
    return jsonify(swag)


if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
