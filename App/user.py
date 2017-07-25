import json

def change_key_name(dic, key_old, key_new):
	dic[key_new] = dic.pop(key_old)

def change_keys(dic):
	change_key_name(dic,"d","downward_transfer")
	change_key_name(dic,"u","upward_transfer")
	change_key_name(dic,"passwd","ss_password")
	return dic

def get_all_users():
	with open("/var/www/shadowsocksr/mudb.json","r") as f:
		data = json.load(f)
	return {line.pop("user"):line for line in map(change_keys, data)}

def get_user(username):
	return get_all_users()["username"]

def modify_user(username):
    pass

def delete_user(username):
    pass
