import requests
from bs4 import BeautifulSoup
from flask_restful import Resource, reqparse

from models.mariadb.okky import OkkyModel


class OkkyScrap(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=str, required=True, help="This id field cannot be left blank!")

    def get(self, id):
        okky = OkkyModel.find_by_id(id)
        if okky:
            return okky.json()
        return {'message': 'okky not found'}, 404

    def delete(self, id):
        okky = OkkyModel.find_by_id(id)
        if okky:
            okky.delete_from_db()
        return {'message': 'okky deleted'}

    def put(self, id):
        data = OkkyScrap.parser.parse_args()
        okky = OkkyModel.find_by_id(id)
        if okky:
            okky.id = data['id']
        else:
            okky = OkkyModel(id)

        okky.save_to_db()
        return {'okky': okky}


# okky scrap function
class OkkyScrapPost(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('id', type=int, required=True, help="This id field cannot be left blank!")

    def post(self):
        data = OkkyScrapPost.parser.parse_args()
        id = data['id']
        page = requests.get('https://okky.kr/article/' + id)
        soup = BeautifulSoup(page.content, 'html.parser')

        if soup is None:
            return {"message": "There is no Id"}, 400

        type = soup.select_one('.sub-title').get_text()
        print("------------------" + type + "------------------")
        created_date = soup.select_one('.content > .date-created')
        print("------------------" + created_date + "------------------")
        title = soup.select_one('#content-body > .panel-title')
        print("------------------" + title + "------------------")
        content = soup.select_one('.content-text')
        print("------------------" + content + "------------------")
        comment_depth = soup.select('.content-identity-count')
        print("------------------" + comment_depth + "------------------")
        hits = soup.select('.content-identity-count')
        print("------------------" + hits + "------------------")
        likes = soup.select_one('.content > .date-created')
        print("------------------" + likes + "------------------")
        scraps = soup.select_one('.content > .date-created')
        print("------------------" + scraps + "------------------")

        # for a in soup.select('.okky-logo > .similar-services-items > a'):
        #     okky_similar_name = a.get('href')[1:]

        okky = OkkyModel.find_by_id(id)
        # if okky is not None:
        #     return {"message": "A okky with that name already exists"}, 400
        return {"message": "A okky with that name already exists"}, 400
        # okky.save_to_db()
        # return {"message": "okky created successfully.", 'id': id}, 201
