from flask_restful import Resource, reqparse
from models.user import UserModel
from flask_jwt import jwt_required
from security import bcrypt

ROUNDS = 5  # Number of hash rounds, set low for development, increase for production


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('nickname',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        email = data['email']
        nickname = data['nickname']
        password = data['password']

        if UserModel.find_by_email(email):
            return {"message": "A user with that email already exists"}, 400
        elif UserModel.find_by_nickname(nickname):
            return {"message": "A user with that nickname already exists"}, 400

        pw_hash = bcrypt.generate_password_hash(password, ROUNDS)
        valid_login = bcrypt.check_password_hash(pw_hash, password)
        print("------------------- authenticate ------------------- ", valid_login)
        user = UserModel(email, pw_hash, nickname)
        user.save_to_db()
        return {"message": "User created successfully.", "email": email, "nickname": nickname}, 201


class UserList(Resource):
    @jwt_required()
    def get(self):
        return {'Users': list(map(lambda x: x.__str__(), UserModel.query.all()))}
