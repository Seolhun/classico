from flask import render_template
from flask_cors import cross_origin
from flask_restful import Resource


class Home(Resource):
    @cross_origin()
    def get(self):
        return render_template('index.html', titile="title", passwd="123456")
