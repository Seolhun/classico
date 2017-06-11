from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.stack import StackModel


class Stack(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, name):
        stack = StackModel.find_by_name(name)
        if stack:
            return stack.__str__()
        return {'message': 'stack not found'}, 404

    @jwt_required()
    def post(self, name):
        if StackModel.find_by_name(name):
            return {'message': "An stack with name '{}' already exists.".format(name)}, 400

        data = Stack.parser.parse_args()
        stack = StackModel(name, data['price'])

        try:
            stack.save_to_db()
        except:
            return {"message": "An error occurred inserting the stack."}, 500

        return stack.__str__(), 201

    def delete(self, name):
        stack = StackModel.find_by_name(name)
        if stack:
            stack.delete_from_db()

        return {'message': 'stack deleted'}

    def put(self, name):
        data = Stack.parser.parse_args()

        stack = StackModel.find_by_name(name)

        if stack:
            stack.price = data['price']
        else:
            stack = StackModel(name, data['price'])

        stack.save_to_db()

        return stack.__str__()


class StackList(Resource):
    def get(self):
        return {'stacks': list(map(lambda x: x.__str__(), StackModel.query.all()))}
