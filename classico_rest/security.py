from werkzeug.security import safe_str_cmp
from models.user import UserModel
from flask_bcrypt import Bcrypt

# security
bcrypt = Bcrypt()


def authenticate(nickname, password):
    user = UserModel.find_by_nickname(nickname)
    validation = bcrypt.check_password_hash(user.password ,password)
    # if user and safe_str_cmp(user.password, password):
    if user and validation:
        return user


def identity(payload):
    user_nickname = payload['identity']
    return UserModel.find_by_nickname(user_nickname)
