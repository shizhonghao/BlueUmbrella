from flask import Flask
from flask_mongoengine import MongoEngine
from APIs import config
from APIs.auth import auth
from APIs.auth import login_manager


app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(auth)
#Extensions here
db = MongoEngine(app)
login_manager.init_app(app)

from APIs.models import User
from APIs.routes import api
