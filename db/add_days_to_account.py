# edit /etc/crontab to set time interval of resetting data
# check whether user's account is available each day.

from pymongo import MongoClient
import json 

client = MongoClient('localhost',27017)
db = client.TBU
collection = db.user

user_dat = collection.find()

def enable_user(username):
    with open("/var/www/shadowsocksr/mudb.json","r") as f:
        json_data = json.load(f)
    for index,line in enumerate(json_data):
        if line["user"] == username:
            line["enable"] = 1
    with open("/var/www/shadowsocksr/mudb.json","w") as f:
        json.dump(json_data,f,sort_keys = True,indent = 4)

def add_days(username,days):
    collection.update({"username":user["username"]}, {"$inc":{"days_remaining":days}})
    enable_user(username)   

