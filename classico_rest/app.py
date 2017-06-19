import settings

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT

# URL Because of Password '@'
from urllib import parse

from security import authenticate, identity
from endpoint.user.user import UserList, UserRegister
from endpoint.stack.stack import Stack, StackList
from endpoint.stack.stack_scrap import StackScrap, StackScrapPost

from flask_swagger import swagger

from db import db, mongo
from security import bcrypt

# Config Part
app = Flask(__name__)

# Swagger
swag = swagger(app)

app.secret_key = 'shooney'

app.config['FLASK_SERVER_NAME'] = settings.FLASK_SERVER_NAME
app.config['FLASK_DEBUG'] = settings.FLASK_DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = settings.SQLALCHEMY_ECHO

# app.config['MONGOALCHEMY_USER'] = settings.MONGOALCHEMY_USER
# app.config['MONGOALCHEMY_PASSWORD'] = parse.quote('blue1220@')
# app.config['MONGOALCHEMY_DATABASE'] = settings.MONGOALCHEMY_DATABASE
# app.config['MONGOALCHEMY_SERVER'] = settings.MONGOALCHEMY_SERVER
# app.config['MONGOALCHEMY_PORT'] = settings.MONGOALCHEMY_PORT

# Add Resources Part
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

# Stack Part
api.add_resource(Stack, '/stack/<string:stack_name>')
api.add_resource(StackList, '/stacks')

# Stack Scrap Part
api.add_resource(StackScrap, '/scrap/<string:stack_name>')
api.add_resource(StackScrapPost, '/scrap')

# User Part
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')


# https://pythonhosted.org/Flask-MongoAlchemy/ 참고할 것
@app.route('/news/<string:news_id>')
def news(news_id):
    news = mongo.NewsData.find_one_or_404({'_id': news_id})
    return jsonify({'news': news})


@app.route("/spec")
def spec():
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Classico RESTful API"
    return jsonify(swag)


if __name__ == '__main__':
    db.init_app(app)
    # mongo.init_app(app)

    # When happends error - Bcrpyt : pip uninstall py-bcrypt => pip install py-bcrypt
    bcrypt.init_app(app)
    app.run(port=5000, debug=True)
