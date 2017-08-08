from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from models.mariadb.user import UserModel
from setting.logging import logger
from setting.security import bcrypt

ROUNDS = 5  # Number of hash rounds, set low for development, increase for production


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")
    parser.add_argument('nickname', type=str, required=True, help="This field cannot be blank.")

    def post(self):
        data = UserRegister.parser.parse_args()

        email = data['email']
        nickname = data['nickname']
        password = data['password']

        if email and UserModel.find_by_email(email):
            return {"message": "A user with that email already exists"}, 400
        elif nickname and UserModel.find_by_nickname(nickname):
            return {"message": "A user with that nickname already exists"}, 400

        pw_hash = bcrypt.generate_password_hash(password, ROUNDS)
        valid_login = bcrypt.check_password_hash(pw_hash, password)
        if valid_login:
            user = UserModel(email, pw_hash, nickname)
            user.save_to_db()
        return {"message": "User created successfully.", "email": email, "nickname": nickname}, 201


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=False)
    parser.add_argument('re_password', type=str, required=False)
    parser.add_argument('new_password', type=str, required=False)

    def get(self, nickname):
        user = UserModel.find_by_nickname(nickname)
        logger.info('[DB Result] : {}'.format(user.json()))
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def put(self, nickname):
        data = User.parser.parse_args()
        user = UserModel.find_by_nickname(nickname)
        password = data['password']
        validation = bcrypt.check_password_hash(user.password, password)
        if not validation:
            return {"message": "Your nickname or password is not valid"}, 401
        new_password = data['new_password']
        re_password = data['re_password']

        if re_password == new_password:
            new_password = bcrypt.generate_password_hash(new_password, ROUNDS)
        else:
            return {"message": "Your password and re_password is unmatched."}, 401

        if user and validation:
            user.password = new_password
        else:
            return {"message": "Your nickname or password is incorrect."}, 401

        user.save_to_db()
        return user.json()


class UserList(Resource):
    @jwt_required()
    def get(self):
        return {'Users': list(map(lambda x: x.json(), UserModel.query.all()))}
