from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from api.restplus import api

ns = api.namespace('stack/', description='Operations related to Stack')
stacks = []


# Item Part
class Stack(Resource):
    # Force insert price
    parser = reqparse.RequestParser()

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, stacks), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, stacks), None) is not None:
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        # data = Stack.parser.parse_args()

        stack = {'name': name}
        stacks.append(stack)
        return stack, 201

    def delete(self, name):
        global stacks
        stack = list(filter(lambda x: x['name'] != name, stacks))
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Stack.parser.parse_args()

        stack = next(filter(lambda x: x['name'] == name, stacks), None)
        if stack is None:
            stack = {'name': name, 'price': data['price']}
            stacks.append(stack)
        else:
            stack.update(data)
        return stack


class StackList(Resource):
    def get(self):
        return {'stacks': stacks}
