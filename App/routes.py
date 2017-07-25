from App import app
from flask_restful import Api
from App.controller import Users, Serverinfo, SpecUser

api = Api(app, default_mediatype="application/json")
api.add_resource(Users, '/users', endpoint='users')
api.add_resource(Serverinfo, '/info')
api.add_resource(SpecUser, '/users/<string:username>', endpoint='user')