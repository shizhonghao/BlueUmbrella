# edit /etc/crontab to set time interval of resetting data
# check whether user's account is available each day.

from pymongo import MongoClient
import json 

client = MongoClient('localhost',27017)
db = client.TBU
collection = db.user

user_dat = collection.find()

def disable_user(username):
    with open("/var/www/shadowsocksr/mudb.json","r") as f:
        json_data = json.load(f)
    for index,line in enumerate(json_data):
        if line["user"] == username:
            line["enable"] = 0
    with open("/var/www/shadowsocksr/mudb.json","w") as f:
        json.dump(json_data,f,sort_keys = True,indent = 4)

for user in user_dat:
    if days_remaining in user:
        days_rem = user["days_remaining"]
        if days_rem == 1:
            disable_user(user["username"])
            collection.update({"username":user["username"]}, {"$set":{"days_remaining":0}}
        elif days_rem > 1:
            collection.update({"username":user["username"]}, {"$set":{"days_remaining":user[days_remaining]-1}}
        else:
            pass

    # if field wasn't set, init days_remaining to 7d
    else:
        collection.update({"username":user["username"]}, {"$set":{"days_remaining":7}}
    #print(user["username"])


