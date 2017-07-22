from flask import Flask
from flask_mongoengine import MongoEngine
from App import config
from App.auth import auth
from App.auth import login_manager


app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(auth)
#Extensions here
db = MongoEngine(app)
login_manager.init_app(app)


from App.models import User
from App.routes import api

# @app.before_first_request
# def create_user():
#     test_role = user_datastore.find_or_create_role('test')
#     user_datastore.create_user(
#         email='a@example.com', password='abc123', roles=[test_role]
#     )
#     admin_role = user_datastore.find_or_create_role('admin')
#     user_datastore.create_user(
#         email='b@example.com', password='abcd1234',
#         roles=[admin_role]
#     )
