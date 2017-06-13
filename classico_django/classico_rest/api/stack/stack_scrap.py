import settings
from flask_restful import Resource, reqparse
from models.stack import StackModel, SimilarStackModel
import requests
from bs4 import BeautifulSoup
from os.path import basename
import os.path


class StackScrap(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('stack_name', type=str, required=True, help="This stack_name field cannot be left blank!")

    def get(self, stack_name):
        stack = StackModel.find_by_stack_name(stack_name)
        if stack:
            stack.delete_from_db()
        return {'message': 'stack deleted'}

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

        similar = []
        stack_name = soup.find("meta", attrs={"name": "keywords"})['content']
        stack_home_url = soup.select('.sp-service-logo > a')[0].get('href')
        stack_home_img_src = soup.select('.sp-service-logo > a > img')[0].get('src')

        if stack_name != url_name:
            stack_name = url_name

        if soup is None:
            return {"message": "There is no name"}, 400

        for a in soup.select('.stack-logo > .similar-services-items > a'):
            stack_similar_name = a.get('href')[1:]
            similar.append(stack_similar_name)

        stack = StackModel.find_by_stack_name(stack_name)
        if stack is not None:
            return {"message": "A stack with that name already exists"}, 400

        stack = StackModel(stack_name)
        stack.stack_home_url = stack_home_url
        for name in similar:
            similar_stack = SimilarStackModel(name)
            similar_stack.save_to_db()
            stack.similars.append(similar_stack)

        img_file_path = get_stack_img(stack_home_img_src, stack_name)
        stack.save_to_db()

        return {"message": "Stack created successfully.", 'stack_name': stack_name, 'similar': similar}, 201


def get_stack_img(img_src, stack_name):
    img_directory = settings.BASE_NAME + "stack/" + stack_name + "/";
    if not os.path.exists(img_directory):
        os.makedirs(img_directory)
    with open(img_directory+basename(img_src), "wb") as f:
        f.write(requests.get(img_src).content)
    return img_directory+basename(img_src)

