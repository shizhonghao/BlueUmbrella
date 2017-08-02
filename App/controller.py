from flask import jsonify, make_response, abort, request, g, url_for, current_app
from flask_restful import Resource, fields, marshal_with, reqparse
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash
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

	@login_required
	def patch(self, username):
		if (not current_user.is_admin) and current_user.username != username:
			return current_app.login_manager.unauthorized()
		req = request.get_json()
		args = dict()
		#A request parser, to avoid request that is not allowed
		if 'password' in req:
			user = User.objects(username=username).first()
			user.password = generate_password_hash(req['password'])
			user.save()
		if 'email' in req:
			user = User.objects(username=username).first()
			user.email = req['email']
			user.save()
		if 'ss_password' in req:
			args['ss_password'] = req['ss_password']
		if 'method' in req:
			args['method'] = req['method']
		if 'protocol' in req:
			args['protocol'] = req['protocol']
		if 'obfs' in req:
			args['obfs'] = req['obfs']
		if current_user.is_admin:
			#Allow admin to enable or disable users
			if 'enable' in req and isinstance(req['enable'], bool):
				args['enable'] = req['enable']
				#PLACEHOLDER
				#set the expire_date in the mongodb
			if 'transfer_enable' in req:
				args['transfer_enable'] = req['transfer_enable']
		SSUsers().modify(username, args)
		return {"Success": True}

	@login_required
	@admin_required
	def delete(self, username):
		SSUsers().delete(username)
		User.objects(username=username).first().delete()
		return {"Success": True}

class Serverinfo(Resource):
	@login_required
	def get(self):
		return {"Try":True, "admin":current_user.is_admin}

