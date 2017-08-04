from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.mariadb.stack import StackModel


class Stack(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('stack_name', type=str, required=True, help="This stack_name field cannot be left blank!")

    def get(self, stack_name):
        stack = StackModel.find_by_stack_name(stack_name)
        if stack:
            return stack.json()
        return {'message': 'stack not found'}, 404

    def delete(self, stack_name):
        stack = StackModel.find_by_stack_name(stack_name)
        if stack:
            stack.delete_from_db()

        return {'message': 'stack deleted'}

    def put(self, stack_name):
        data = Stack.parser.parse_args()
        stack = StackModel.find_by_stack_name(stack_name)
        if stack:
            stack.stack_name = data['stack_name']
        else:
            stack = StackModel(stack_name)

        stack.save_to_db()

        return stack.json()


class StackList(Resource):
    @jwt_required()
    def post(self):
        return {"message": "An error occurred inserting the stack."}, 500

    def get(self):
        return {'stacks': list(map(lambda stack: stack.json(), StackModel.query.all()))}
