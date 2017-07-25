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
    change_key_name(dic,"downward_transfer","d")
    change_key_name(dic,"upward_transfer","u")
    change_key_name(dic,"ss_password","passwd")
    dic["enable"] = int(dic["enable"])
    return dic
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

    def atomic_cmp(json_data):
        #compare self.data with json data
        #which side of the data should be preserved will be decided later

    def get_all(self):
        return self.data

    def get(self, username):
        return self.data.get(username)
    
    def add(self, username, password, method = 'aes-128-ctr', protocol = 'auth_aes128_md5', obfs = 'tls1.2_ticket_auth_compatible'):
        available_port = get_available_port()
        #prepare a dictionary with user info 
        #(without username, in the form of self.data)
        user_info = {}
        user_info["downward_transfer"] = 0
        user_info["enable"] = 0
        user_info["method"] = method
        user_info["obfs"] = obfs
        user_info["passwd"] = password
        user_info["port"] = available_port
        user_info["transfer_enable"] = 9007199254740992
        user_info["upward_transfer"] = 0
        pass
        self.data["username"] = user_info.copy()
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
        user_info = self.data[username]
        for (key,val) in args.items():
            user_info[key] = val

        write_back = user_info.copy()
        change_keys_back(write_back)
        write_back["user"]=username
        with open("/var/www/shadowsocksr/mudb.json", "r") as f:
            json_data = json.load(f)
            for user_info in json_data:
                if(user_info["user"] == username):
                    user_info = write_back
                    break

        with open("/var/www/shadowsocksr/mudb.json", "w") as f:
            json.dump(json_data,f,sort_keys = True,indent = 4)

    
    def delete(self, username):
        #delete everything from mudb.json and self.data
        self.data.pop(username)
        with open("/var/www/shadowsocksr/mudb.json", "r") as f:
            json_data = json.load(f)
            for user_info in json_data:
                if(user_info["user"] == username):
                    user_info.remove(user_info)
                    break
                    
        with open("/var/www/shadowsocksr/mudb.json", "w") as f:
            json.dump(json_data,f,sort_keys = True,indent = 4)

