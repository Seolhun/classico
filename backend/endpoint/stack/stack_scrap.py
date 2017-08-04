import os.path
from os.path import basename

import requests
from bs4 import BeautifulSoup
from flask_restful import Resource, reqparse

from models.mariadb.stack import StackModel, SimilarStackModel
from setting import settings


class StackScrap(Resource):
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
        data = StackScrap.parser.parse_args()
        stack = StackModel.find_by_stack_name(stack_name)
        if stack:
            stack.stack_name = data['stack_name']
        else:
            stack = StackModel(stack_name)

        stack.save_to_db()
        return {'stack': stack}


# Stack scrap function
class StackScrapPost(Resource):
    def post(self):
        data = StackScrap.parser.parse_args()
        url_name = data['stack_name']
        page = requests.get('https://stackshare.io/' + url_name)
        soup = BeautifulSoup(page.content, 'html.parser')

        similars = []
        stack_name = soup.find("meta", attrs={"name": "keywords"})['content']
        stack_home_url = soup.select('.sp-service-logo > a')[0].get('href')
        stack_home_img_src = soup.select('.sp-service-logo > a > img')[0].get('src')

        if stack_name != url_name:
            stack_name = url_name

        if soup is None:
            return {"message": "There is no name"}, 400

        for similar in soup.select('.stack-logo > .similar-services-items > a'):
            stack_similar_name = similar.get('href')[1:]
            similars.append(stack_similar_name)

        stack = StackModel.find_by_stack_name(stack_name)
        if stack is not None:
            return {"message": "A stack with that name already exists"}, 400

        # Create Stack and Set value Getting from Stack.IO
        stack = StackModel(stack_name)
        stack.stack_home_url = stack_home_url
        for name in similars:
            similar_stack = SimilarStackModel.find_by_stack_name(name)
            if similar_stack is None:
                similar_stack = SimilarStackModel(name)
                similar_stack.save_to_db()

            stack.similars.append(similar_stack)

        # Need to save file path and Must be Created Database
        img_file_path = get_stack_img(stack_home_img_src, stack_name)
        stack.save_to_db()

        return {"message": "Stack created successfully.", 'stack_name': stack_name, 'similars': similars}, 201


def get_stack_img(img_src, stack_name):
    img_directory = settings.BASE_NAME + "stack/" + stack_name + "/";
    if not os.path.exists(img_directory):
        os.makedirs(img_directory)

    with open(img_directory+basename(img_src), "wb") as file:
        file.write(requests.get(img_src).content)

    return img_directory+basename(img_src)

