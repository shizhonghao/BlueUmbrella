from flask import Flask
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore
from App import config



app = Flask(__name__)
app.config.from_object(config)
#Extensions here
#auth = HTTPBasicAuth()
db = MongoEngine(app)

from App.models import User, Role
from App.routes import api

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    test_role = user_datastore.find_or_create_role('test')
    user_datastore.create_user(
        email='a@example.com', password='abc123', roles=[test_role]
    )
    admin_role = user_datastore.find_or_create_role('admin')
    user_datastore.create_user(
        email='b@example.com', password='abcd1234',
        roles=[admin_role]
    )
