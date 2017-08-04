from flask import Flask
# from flask import render_template, request
from flask_jwt import JWT
from flask_restful import Api
from flask_swagger import swagger
from setting.security import authenticate, identity
from setting.security import bcrypt

from endpoint.question.okky.okky_scrap import OkkyScrap, OkkyScrapPost
from endpoint.stack.stack import Stack, StackList
from endpoint.stack.stack_scrap import StackScrap, StackScrapPost
from endpoint.user.user import UserList, UserRegister, User

from setting import settings
from setting.databases import db
from setting.databases import mongo


# Config Part
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='$$',
        block_end_string='$$',
        variable_start_string='$',
        variable_end_string='$',
        comment_start_string='$#',
        comment_end_string='#$',
    ))


app = CustomFlask(__name__)

app.config['FLASK_SERVER_NAME'] = settings.FLASK_SERVER_NAME
app.config['FLASK_DEBUG'] = settings.FLASK_DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = settings.SQLALCHEMY_ECHO

app.config['MONGOALCHEMY_USER'] = settings.MONGOALCHEMY_USER
app.config['MONGOALCHEMY_PASSWORD'] = settings.MONGOALCHEMY_PASSWORD
app.config['MONGOALCHEMY_DATABASE'] = settings.MONGOALCHEMY_DATABASE
app.config['MONGOALCHEMY_SERVER'] = settings.MONGOALCHEMY_SERVER
app.config['MONGOALCHEMY_PORT'] = settings.MONGOALCHEMY_PORT

# JWT Setting
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_USERNAME_KEY'] = 'nickname'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'password'

app.debug = True
jwt = JWT(app, authenticate, identity)  # /auth

# Swagger
swag = swagger(app)


# Create Database When generated First Request
@app.before_first_request
def create_tables():
    db.create_all()


# Add Resources Part
api = Api(app)

# Stack Part
api.add_resource(Stack, '/stack/<string:stack_name>')
api.add_resource(StackList, '/stacks')

# Stack Scrap Part
api.add_resource(StackScrap, '/scrap/stack/<string:stack_name>')
api.add_resource(StackScrapPost, '/scrap/stack')

# Stack Scrap Part
api.add_resource(OkkyScrap, '/scrap/okky/<int:id>')
api.add_resource(OkkyScrapPost, '/scrap/okky')

# User Part
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<string:nickname>')
api.add_resource(UserList, '/users')

if __name__ == '__main__':
    db.init_app(app)
    mongo.init_app(app)

    # When happends error - Bcrpyt : pip uninstall py-bcrypt => pip install py-bcrypt
    bcrypt.init_app(app)
    app.run(port=5000, debug=True)
