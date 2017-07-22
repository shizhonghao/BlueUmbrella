from flask.ext.restful import Resource, fields, marshal_with, Api, reqparse
from flask.ext.mongoalchemy import MongoAlchemy
from flask.ext.security import auth_token_required, roles_required, login_user
from flask import jsonify, make_response, abort, request, g, url_for

class Users(Resource):
    @auth_token_required
    @roles_required('admin')
    def get(self):
        pass

class Serverinfo(Resource):
    def get(self):
        pass