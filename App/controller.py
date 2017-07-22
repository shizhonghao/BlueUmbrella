from flask_restful import Resource, fields, marshal_with, Api, reqparse
from flask_security import auth_token_required, roles_required, login_user, login_required
from flask import jsonify, make_response, abort, request, g, url_for
from flask_security.utils import encrypt_password, verify_password

class Users(Resource):
    @login_required
    @auth_token_required
    @roles_required('admin')
    def get(self):
        pass

class Serverinfo(Resource):
    @login_required
    def get(self):
        pass

class Login(Resource):
    def post(self):
        args = reqparse.RequestParser() \
            .add_argument('username', type=str, location='json', required=True, help="用户名不能为空") \
            .add_argument('password', type=str, location='json', required=True, help="密码不能为空") \
            .parse_args()
        user = User.authenticate(args['username'], args['password'])
        if user:
            login_user(user=user)
            return {"message": "登陆成功", "token": user.get_auth_token()}, 200
        else:
            return {"message": "用户名或密码错误"}, 401