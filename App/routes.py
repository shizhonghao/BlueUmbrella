from App import app
from flask.ext.restful import Api
from App.controller import Users, Serverinfo

api = Api(app, default_mediatype="application/json")
api.add_resource(Users, '/users')
api.add_resource(Serverinfo, '/info')