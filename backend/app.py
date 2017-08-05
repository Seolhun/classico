from flask import Flask
from flask_jwt import JWT

from flask_restful import Api
from flask_swagger import swagger
# Sentry : Monitoring System
from raven.contrib.flask import Sentry

from endpoint.news.news import News
from endpoint.question.okky.okky_scrap import OkkyScrap, OkkyScrapPost
from endpoint.stack.stack import Stack, StackList
from endpoint.stack.stack_scrap import StackScrap, StackScrapPost
from endpoint.user.user import UserList, UserRegister, User
# Classico Configuation inofrmation
from setting import settings
from setting.databases import db, mongo
# Classico Database Configuation
from setting.security import authenticate, identity
from setting.security import bcrypt

app = Flask(__name__)

sentry = Sentry(app, dsn='https://2519ad4fac6f453b9f3d28364c9544fb:2f17efbd161243ce889d3a03a8a5eaf4@sentry.io/200070')

app.config['FLASK_SERVER_NAME'] = settings.FLASK_SERVER_NAME
app.config['FLASK_DEBUG'] = settings.FLASK_DEBUG

# MariaDB SQLAlchemy Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_ECHO'] = settings.SQLALCHEMY_ECHO

# MongoDB PyMongo Configuration
app.config['MONGO_USERNAME'] = settings.MONGO_USERNAME
app.config['MONGO_PASSWORD'] = settings.MONGO_PASSWORD
app.config['MONGO_HOST'] = settings.MONGO_HOST
app.config['MONGO_PORT'] = settings.MONGO_PORT
app.config['MONGO_DBNAME'] = settings.MONGO_DBNAME

# JWT Setting
app.config['SECRET_KEY'] = 'super-secret'
app.config['JWT_AUTH_USERNAME_KEY'] = 'nickname'
app.config['JWT_AUTH_PASSWORD_KEY'] = 'password'


# Create Database When generated First Request
@app.before_first_request
def create_tables():
    db.create_all()


app.debug = True
jwt = JWT(app, authenticate, identity)  # /auth

# Swagger
swag = swagger(app)

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

# Mongo Part
api.add_resource(News, '/news/<string:index>')

if __name__ == '__main__':
    db.init_app(app)

    # MongoDB Injection
    mongo.init_app(app, config_prefix='MONGO')

    # When happends error - Bcrpyt : pip uninstall py-bcrypt => pip install py-bcrypt
    bcrypt.init_app(app)
    app.run(port=5000, debug=True)
