from flask_restful import Resource, fields, marshal_with, Api, reqparse
from flask import jsonify, make_response, abort, request, g, url_for, current_app
from flask_login import current_user
from App.auth import login_required

class Users(Resource):
    @login_required(admin=True)
    def get(self):
        # if not current_user.is_authenticated:
        #     return current_app.login_manager.unauthorized()
        # if not current_user.is_admin:
        #     return current_app.login_manager.unauthorized()     
        return jsonify(Status="allright")

class Serverinfo(Resource):
    @login_required()
    def get(self):
        return jsonify(Status="allright")

# class Login(Resource):
#     def post(self):
#         args = reqparse.RequestParser() \
#             .add_argument('username', type=str, location='json', required=True, help="用户名不能为空") \
#             .add_argument('password', type=str, location='json', required=True, help="密码不能为空") \
#             .parse_args()
#         user = User.authenticate(args['username'], args['password'])
#         if user:
#             login_user(username=user)
#             return {"message": "登陆成功", "token": user.get_auth_token()}, 200
#         else:
#             return {"message": "用户名或密码错误"}, 401