from flask_restful import Resource, reqparse
from flask import jsonify

from models.mongodb.news import NewsModel

class News(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('index', type=str, required=True, help="This index field cannot be left blank!")

    def get(self, index):
        news = NewsModel.find_by_index(index)
        print("------------------------")
        print("news", news)
        print("------------------------")
        if news:
            return news
        return {'message': 'news not found'}, 404

    def delete(self, index):
        return {'message': 'news deleted'}

    def put(self, index):
        return {'message': 'news deleted'}


class NewsList(Resource):
    def get(self):
        news = NewsModel.find_all()
        return {'stacks': list(map(lambda x: x.__str__(), news))}

    def post(self):
        return {"message": "An error occurred inserting the stack."}, 500
