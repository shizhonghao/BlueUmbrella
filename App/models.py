from flask.ext.security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, login_required
from flask.ext.mongoengine import MongoEngine
from App import db

class Role(db.Document, RoleMixin):
    name = db.StringField(max_lentgh=80, unique=True)
    description = db.StringField(max_length=255)
    def __init__(self, name, description):
        self.name = name
        self.description = description

class User(db.Document, UserMixin):
    username = db.StringField(max_length=20)
    password = db.StringField(max_length=255)
    email = db.StringField(max_length=255)
    expire_date = db.DateTimeField()
    active = db.BooleanField(default=True)
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def __init__(self, username=None, password=None, email=None, expire_date=None, active=True):
        self.username = username
        self.password = password
        self.email = email
        self.expire_date = expire_date
        self.active = active
    
    @staticmethod
    def authenticate(username, password):
        pass