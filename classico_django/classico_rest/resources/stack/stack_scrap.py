from flask_restful import Resource, reqparse
from models.stack import StackModel, SimilarStackModel

import requests
from bs4 import BeautifulSoup


class StackScrap(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="This name field cannot be left blank!")

    def get(self, name):
        stack = StackModel.find_by_name(name)
        if stack:
            stack.delete_from_db()
        return {'message': 'stack deleted'}

    def delete(self, name):
        stack = StackModel.find_by_name(name)
        if stack:
            stack.delete_from_db()
        return {'message': 'stack deleted'}

    def put(self, name):
        stack = StackModel.find_by_name(name)
        if stack:
            stack.name = StackScrap.data['name']
        else:
            stack = StackModel(name)

        stack.save_to_db()
        return {'stack': stack}


# Stack scrap function
class StackScrapPost(Resource):
    def post(self):
        data = StackScrap.parser.parse_args()
        url_name = data['name']
        page = requests.get('https://stackshare.io/' + url_name)
        soup = BeautifulSoup(page.content, 'html.parser')

        similar = []
        stack_name = soup.find("meta", attrs={"name": "keywords"})['content']
        if stack_name != url_name:
            stack_name = url_name

        if soup is None:
            return {"message": "There is no name"}, 400

        for a in soup.select('.stack-logo > .similar-services-items > a'):
            stack_similar_name = a.get('href')[1:]
            similar.append(stack_similar_name)

        stack = StackModel.find_by_name(stack_name)
        if stack is not None:
            return {"message": "A stack with that name already exists"}, 400

        stack = StackModel(stack_name)
        for name in similar:
            similar_stack = SimilarStackModel(name)
            similar_stack.save_to_db()
            stack.similar.append(similar_stack)
        stack.save_to_db()

        return {'name': stack_name, 'similar': similar}, 201
