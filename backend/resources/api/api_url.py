from flask_cors import CORS
from flask_restful import Api

# Classico API URL information
from resources.api.news.news import News
from resources.api.question.okky.okky_scrap import OkkyScrap, OkkyScrapPost
from resources.api.stack.stack import Stack, StackList
from resources.api.stack.stack_scrap import StackScrap, StackScrapPost
from resources.api.user.user import UserList, UserRegister, User

cors = CORS(resources={r"/api/*": {"origins": "*"}})

# Add Resources Part
api = Api(prefix="/api/v1")


# Stack Part
api.add_resource(Stack, '/stack/<string:stack_name>')
api.add_resource(StackList, '/stacks')

# Stack Scrap Part
api.add_resource(StackScrap, '/scrap/stack/<string:stack_name>')
api.add_resource(StackScrapPost, '/scrap/stack')

# Stack Scrap Part
api.add_resource(OkkyScrap, '/scrap/okky/<int:id>')
api.add_resource(OkkyScrapPost, '/scrap/okky')

# User Part
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/home/<string:nickname>')
api.add_resource(UserList, '/users')

# Mongo Part
api.add_resource(News, '/news/<string:index>')
