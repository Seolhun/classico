BASE_NAME="/Users/HunSeol/Desktop/"

# Flask Settings
FLASK_SERVER_NAME = 'localhost:5000'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus Settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy Settings
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://hooney:blue1220@@127.0.0.1/classico'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# MongoDB Settings
MONGO_USERNAME = 'shooney'
MONGO_PASSWORD = 'blue1220@'
MONGOALCHEMY_DATABASE = 'classico'
# MONGO_HOST = '127.0.0.1'
MONGO_HOST = '192.168.0.2'
MONGO_PORT = 27017

# SQLALCHEMY_BINDS = {
#     'users':        'mysqldb://localhost/users',
#     'appmeta':      'sqlite:////path/to/appmeta.db'
# }