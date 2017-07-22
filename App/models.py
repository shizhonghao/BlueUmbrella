from flask_security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, login_required
from flask_mongoengine import MongoEngine
from App import db

class Role(db.Document, RoleMixin):
    name = db.StringField(max_lentgh=80, unique=True)
    description = db.StringField(max_length=255)

class User(db.Document, UserMixin):
    username = db.StringField(max_length=20)
    password = db.StringField(max_length=255)
    email = db.StringField(max_length=255)
    expire_date = db.DateTimeField()
    active = db.BooleanField(default=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])