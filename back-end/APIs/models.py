from flask_mongoengine import MongoEngine
from flask_login import UserMixin
from APIs import db
import json
from copy import deepcopy
import socket

#mongodb model
class User(db.Document, UserMixin):
    username = db.StringField(max_length=20, required=True, unique=True)
    password = db.StringField(max_length=255, required=True)
    email = db.StringField(max_length=255)
    is_active = db.BooleanField(default=True)
    is_admin = db.BooleanField(default=False)
    days_remaining = db.IntField()


#mudb.json functions
def change_key_name(dic, key_old, key_new):
	dic[key_new] = dic.pop(key_old)

def change_keys(dic):
    change_key_name(dic,"d","downward_transfer")
    change_key_name(dic,"u","upward_transfer")
    change_key_name(dic,"passwd","ss_password")
    dic["enable"] = bool(dic["enable"])
    return dic

def change_keys_back(dic):
    change_key_name(dic,"downward_transfer","d")
    change_key_name(dic,"upward_transfer","u")
    change_key_name(dic,"ss_password","passwd")
    dic["enable"] = int(dic["enable"])
    return dic

def get_available_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    addr, port = s.getsockname()
    s.close()
    return port


#mudb.json model
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
        pass
    
    def get_all(self):
        with open("/var/www/shadowsocksr/mudb.json", "r") as f:
            data = json.load(f)
        data = {line.pop("user"):line for line in map(change_keys, data)}
        return data

    def get(self, username):
        data = self.get_all()
        if not data.get(username):
            return False
        return data.get(username)

    
    def add(self, username, password, method = 'aes-128-ctr', protocol = 'auth_aes128_md5', obfs = 'tls1.2_ticket_auth_compatible'):
        available_port = get_available_port()
        #prepare a dictionary with user info 
        #(without username, in the form of self.data)
        if self.get(username):
            return False
        user_info = dict()
        user_info["enable"] = False
        user_info["method"] = method
        user_info["obfs"] = obfs
        user_info["protocol"] = protocol
        user_info["ss_password"] = password
        user_info["port"] = available_port
        user_info["transfer_enable"] = 21474836480
        user_info["upward_transfer"] = 0
        user_info["downward_transfer"] = 0
        change_keys_back(user_info)
        #then add username back
        user_info["user"]=username
        #file operation to put user_info back to mudb.json
        with open("/var/www/shadowsocksr/mudb.json", "r") as f:
            json_data = json.load(f)
            json_data.append(user_info)
        with open("/var/www/shadowsocksr/mudb.json", "w") as f:
            json.dump(json_data,f,sort_keys = True,indent = 4)

    def modify(self, username, args):
        #args is a dict, try to update self.data[username] from args
        #args may or maynot contain all possible things (i.e. password, obfs, protocol)
        data = self.get_all()
        data[username].update(args)
        write_back = list()
        for k, v in data.items():
            change_keys_back(v)
            v["user"]=k
            write_back.append(v)
        with open("/var/www/shadowsocksr/mudb.json", "w") as f:
            json.dump(write_back,f,sort_keys = True,indent = 4)

    def delete(self, username):
        #delete everything from mudb.json and self.data
        with open("/var/www/shadowsocksr/mudb.json", "r") as f:
            json_data = json.load(f)
        for index, line in enumerate(json_data):
            if line["user"] == username:
                del json_data[index]
                break
        with open("/var/www/shadowsocksr/mudb.json", "w") as f:
            json.dump(json_data,f,sort_keys = True,indent = 4)

