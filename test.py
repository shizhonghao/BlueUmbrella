import os
import re
import json
user_list = {}
os.chdir("/var/www/shadowsocksr")
cmd = "python mujson_mgr.py -l"
res = os.popen(cmd)
doc = res.read()
doc = doc.split('\n')
users = []
for line in doc:
	name = re.findall("\[.*\]",line)
	if(name):#list is not empty
		user_info = {}
		name = name[0][1:-1]
		user = os.popen(cmd + " -u " + name)
		user = user.read()
		user = user.split('\n')
		for line in user:
			pair = re.split(':',line)
			print(pair)
			if(len(pair)==2):
				user_info[pair[0].strip()] = pair[1].strip()

		user_list[name] = user_info
		
info = {"users":user_list}
info_json = json.dumps(info)
print(info_json)
