from flask_mongoengine import MongoEngine
from flask_login import UserMixin
from App import db


class User(db.Document, UserMixin):
    username = db.StringField(max_length=20, required=True, unique=True)
    password = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255)
    is_active = db.BooleanField(default=True)
    is_admin = db.BooleanField(default=False)