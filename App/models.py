from flask_mongoengine import MongoEngine
from flask_login import UserMixin
from App import db
import json

#mongodb model
class User(db.Document, UserMixin):
    username = db.StringField(max_length=20, required=True, unique=True)
    password = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255)
    is_active = db.BooleanField(default=True)
    is_admin = db.BooleanField(default=False)


#mudb.json model
def change_key_name(dic, key_old, key_new):
	dic[key_new] = dic.pop(key_old)

def change_keys(dic):
	change_key_name(dic,"d","downward_transfer")
	change_key_name(dic,"u","upward_transfer")
	change_key_name(dic,"passwd","ss_password")
	return dic

def singleton(cls, *args, **kw):  
    instances = {}  
    def _singleton():  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton  

@singleton
class SSUsers():
    def __init__(self):
        with open("/var/www/shadowsocksr/mudb.json", "r") as f:
            self.data = json.load(f)
        self.data = {line.pop("user"):line for line in map(change_keys, self.data)}

    def get_all(self):
        return self.data

    def get(self, username):
        return self.data.get(username)