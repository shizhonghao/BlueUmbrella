from mongoengine import *
import requests
from bs4 import BeautifulSoup
from werkzeug.security import generate_password_hash as g

connect('TBU')
class User(Document):
    username = StringField(max_length=20, required=True, unique=True)
    password = StringField(max_length=255, required=True)
    email = StringField(max_length=255)
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)

def add_user(name, passwd, email, active=True, admin=False):
    new = User.objects(username=name)
    if new:
        return "Existed!"
    new = User(username=name, password=g(passwd), email=email, is_active=active, is_admin=admin)
    new.save()

def get_user(name):
    user = User.objects(username=name).first()
    if user:
        return user
    else:
        return "No such user!"

def list_all():
    users = User.objects().all()
    return {user.username : user for user in users}