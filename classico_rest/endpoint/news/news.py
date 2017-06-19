from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from flask import jsonify

from app import mongo


class News(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('news_id', type=str, required=True, help="This news_id field cannot be left blank!")

    def get(self, news_id):
        news = mongo.db.news.find(news_id);
        if news:
            return jsonify({'news': news})
        return {'message': 'news not found'}, 404

    def delete(self, news_id):
        return {'message': 'news deleted'}

    def put(self, news_id):
        return {'message': 'news deleted'}


class NewsList(Resource):
    def get(self):
        news = mongo.db.news.find();
        return {'stacks': list(map(lambda x: x.__str__(), news))}

    @jwt_required()
    def post(self):
        return {"message": "An error occurred inserting the stack."}, 500
