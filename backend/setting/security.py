from datetime import timedelta

from flask_bcrypt import Bcrypt

from models.mariadb.user import UserModel

CONFIG_DEFAULTS = {
    'JWT_AUTH_URL_RULE': '/auth',
    'JWT_AUTH_USERNAME_KEY': 'nickname',
    'JWT_AUTH_PASSWORD_KEY': 'password',
    'JWT_ALGORITHM': 'HS256',
    'JWT_LEEWAY': timedelta(seconds=10),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_EXPIRATION_DELTA': timedelta(seconds=1800),
    'JWT_NOT_BEFORE_DELTA': timedelta(seconds=0),
}

# security
bcrypt = Bcrypt()


def authenticate(nickname, password):
    user = UserModel.find_by_nickname(nickname)
    # if user and safe_str_cmp(user.password, password):
    if user and bcrypt.check_password_hash(user.password, password):

        return user


def identity(payload):
    user_id = payload['identity']
    print("--------------------------------")
    print(user_id)
    print("--------------------------------")
    user = UserModel.find_by_id(user_id)
    return user.json()
