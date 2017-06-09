from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from api.restplus import api

ns = api.namespace('user/', description='Operations related to User')

users = []


# User Part
class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True, help='Password to create user')

    def post(self, name):
        try:
            # Parse the arguments
            data = User.parser.parse_args()
            password = data['password']
            user = {'name': name, 'password': password}

            # Connection 연결
            users.append(user)
            return {'user': user}
            # return {'Email': _email, 'Password': _password}
        except Exception as err:
            return {"OS error: {0}".format(err)}


class UserList(Resource):
    @jwt_required()
    def get(self):
        return {'users': users}
