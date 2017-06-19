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
SQLALCHEMY_DATABASE_URI = 'mysql://hooney:blue1220@@127.0.0.1/classico'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

# MongoDB Settings
MONGOALCHEMY_USER = 'shooney'
MONGOALCHEMY_PASSWORD = 'blue1220@'
MONGOALCHEMY_DATABASE = 'shooney'
MONGOALCHEMY_SERVER = '127.0.0.1'
MONGOALCHEMY_PORT = 27017

# SQLALCHEMY_BINDS = {
#     'users':        'mysqldb://localhost/users',
#     'appmeta':      'sqlite:////path/to/appmeta.db'
# }