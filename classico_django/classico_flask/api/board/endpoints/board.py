from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from api.restplus import api

ns = api.namespace('board/', description='Operations related to Board')

boards = []


# User Part
class Board(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True, help='Password to create user')

    def post(self):
        try:
            # Parse the arguments
            data = Board.parser.parse_args()
            title = data['title']
            board = {'title': title}

            # Connection 연결
            boards.append(board)
            return {'board': board}
            # return {'Email': _email, 'Password': _password}
        except Exception as err:
            return {"Exception : {0}".format(err)}


class BoardList(Resource):
    @jwt_required()
    def get(self):
        return {'boards': boards}
