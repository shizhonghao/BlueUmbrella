from flask import Flask, jsonify, make_response, abort, request, g, url_for
from flask.ext.mongoengine import MongoEngine
from App import config


app = Flask(__name__)
app.config.from_object(config)
#Extensions here
auth = HTTPBasicAuth()
db = MongoEngine(app)

from App.models import User, Role
from App.routes import api

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)