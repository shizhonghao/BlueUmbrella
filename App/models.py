from flask_mongoengine import MongoEngine
from flask_login import UserMixin
from App import db
import json
from copy import deepcopy

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
    dic["enable"] = bool(dic["enable"])
	return dic

def change_keys_back(dic):
    pass

def get_available_port():
    pass

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
    
    def add(self, username, password, method = '', protocol = '', obfs = ''):
        available_port = get_available_port()
        #prepare a dictionary with user info 
        #(without username, in the form of self.data)
        user_info = dict()
        pass
        self.data["username"] = user_info.copy()
        change_keys_back(user_info)
        #then add username back
        user_info["user"]=username
        #file operation to put user_info back to mudb.json
    
    def modify(self, username, args):
        #args is a dict, try to update self.data[username] from args
        #args may or maynot contain all possible things (i.e. password, obfs, protocol)
        pass
    
    def delete(self, username):
        #delete everything from mudb.json and self.data
        pass
        
