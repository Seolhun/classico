from flask_caching import Cache
from flask_cors import CORS
from flask_restful import Api

# Classico API URL information
from resources.render.home.home import Home

cache = Cache()
cors = CORS(resources={r"/classico/*": {"origins": "*"}})

# Add Resources Part
api = Api(prefix="/classico")


# Stack Part
api.add_resource(Home, '/home')