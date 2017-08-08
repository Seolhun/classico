# Classico Dependencies
from flask import Flask

from flask_swagger import swagger
from raven.contrib.flask import Sentry

app = Flask(__name__)

# Sentry : Monitoring System
sentry = Sentry(app, dsn='https://2519ad4fac6f453b9f3d28364c9544fb:2f17efbd161243ce889d3a03a8a5eaf4@sentry.io/200070')

# Swagger
swag = swagger(app)
