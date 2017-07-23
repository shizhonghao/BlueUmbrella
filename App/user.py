import json

def change_key_name(dic,key_old,key_new):
	dic[key_new] = dic.pop(key_old)

def get_mongodb_info(dic):
	pass

def get_all_users():
	with open("/var/www/shadowsocksr/mudb.json","r") as f:
		data = json.load(f)
	user_info = {}
	for line in data:
		change_key_name(line,"d","downward_transfer")
		change_key_name(line,"u","upward_transfer")
		change_key_name(line,"passwd","password")
		line.pop("transfer_enable")
		change_key_name(line,"enable","transfer_enable")
		get_mongodb_info(line)
		user_info[line["user"]] = line
    return user_info

def get_user(username):
	with open("/var/www/shadowsocksr/mudb.json","r") as f:
		data = json.load(f)
	for line in data:
		if(line["user"] == username):
			change_key_name(line,"d","downward_transfer")
			change_key_name(line,"u","upward_transfer")
			change_key_name(line,"passwd","password")
			line.pop("transfer_enable")
			change_key_name(line,"enable","transfer_enable")
			info = line
	return info

def modify_user(username):
    pass

def delete_user(username):
    pass
