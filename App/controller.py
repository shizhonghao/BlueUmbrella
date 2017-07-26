from flask import jsonify, make_response, abort, request, g, url_for, current_app
from flask_restful import Resource, fields, marshal_with, reqparse
from flask_login import current_user, login_required
from App.auth import admin_required
from App.models import User, SSUsers

import os
import re
import json

class Users(Resource):
	@login_required
	@admin_required
	def get(self):
		all_users = SSUsers().get_all()
		for user in all_users:
			all_users[user]['email']=User.objects(username=user).first().email
		return all_users

	@login_required
	@admin_required
	def post(self):
		pass
		#Do we really need it or just work with registration?


class SpecUser(Resource):
	@login_required
	def get(self, username):
		if (not current_user.is_admin) and current_user.username != username:
			return current_app.login_manager.unauthorized()
		current_info = SSUsers().get(username)
		if not current_info:
			#if the user is not existed
			#Need an error handler later
			return {"Status":"Error, no such user"}, 500
		current_info['email'] = User.objects(username=username).first().email
		return current_info

	def patch(self, username):
		pass

	def delete(self, username):

class Serverinfo(Resource):
	@login_required
	def get(self):
		return {"Try":True, "admin":current_user.is_admin}

