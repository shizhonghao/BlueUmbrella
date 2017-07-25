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
