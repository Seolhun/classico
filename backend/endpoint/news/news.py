from flask import request, jsonify
from flask_restful import Resource, reqparse
from setting.databases import mongo


class News(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('index', type=int, required=True, help="This index field cannot be left blank!")

    def get(self, index):
        # # Get URI Resources : this is Index only
        # resource_data = News.parser.parse_args()
        news = mongo.db.news.find_one({"index": index})
        print("---------------")
        print("index", index)
        print("news", news)
        print("---------------")
        if news:
            return {'news': news}, 404
        return {'message': 'news not found'}, 404

    def delete(self, index):
        return {'message': 'news deleted'}

    def post(self):
        # Get Body data writting json
        news_json = request.get_json()
        index = news_json['index']
        print("---------------")
        print("news_json", news_json)
        print("---------------")
        if index:
            if mongo.db.news.find_one({"index": index}):
                return {"response": "News already exists."}
            else:
                mongo.db.news.insert(news_json)
                return {"response": "News insert OK"}
        return {"response": "Please. Write index field"}


class NewsList(Resource):
    # def get(self):
    #     return {'stacks': list(map(lambda x: x.__str__(), news))}

    def post(self):
        return {"message": "An error occurred inserting the stack."}, 500
