from setting.databases import db
from flask import Flask
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

# Config Part
app = Flask(__name__)

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

# # MongoDB Session Test
# session = Session.connect('shooney')


# # https://pythonhosted.org/Flask-MongoAlchemy/ 참고할 것
# @app.route('/news/<string:NEWS_IDX>')
# def news(NEWS_IDX):
#     print("------" + NEWS_IDX + "------")
#     query = mongo.session.query(NewsData)
#     # news = query.filter(NewsData.NEWS_IDX == NEWS_IDX).all()
#     news = session.query(NewsData).filter(NewsData.NEWS_IDX == NEWS_IDX).first()
#     # return session.query(Product).filter({"mongo_id": {in_: self.product_ids}})
#     return jsonify({'news': news})


# @app.route('/protected')
# @jwt_required()
# def protected():
#     return '%s' % current_identity
#
#
# @app.route("/spec")
# def spec():
#     swag['info']['version'] = "1.0"
#     swag['info']['title'] = "Classico RESTful API"
#     return jsonify(swag)


if __name__ == '__main__':
    db.init_app(app)
    # mongo.init_app(app)

    # When happends error - Bcrpyt : pip uninstall py-bcrypt => pip install py-bcrypt
    bcrypt.init_app(app)
    app.run(port=5000, debug=True)
