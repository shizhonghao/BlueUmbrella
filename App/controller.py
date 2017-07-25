from flask import jsonify, make_response, abort, request, g, url_for, current_app
from flask_restful import Resource, fields, marshal_with, reqparse
from flask_login import current_user, login_required
from App.auth import admin_required
from App.models import SSUsers

import os
import re
import json

class Users(Resource):
	@login_required
	@admin_required
	def get(self):
		return SSUsers().get_all()

class SpecUser(Resource):
	@login_required
	def get(self, username):
		if (not current_user.is_admin) and current_user.username != username:
			return current_app.login_manager.unauthorized()
		if not SSUsers().get(username):
			#Need an error handler later
			return {"Status":"Error, no such user"}, 500
		return SSUsers().get(username)

class Serverinfo(Resource):
	@login_required
	def get(self):
		return {"Try":True, "admin":current_user.is_admin}

