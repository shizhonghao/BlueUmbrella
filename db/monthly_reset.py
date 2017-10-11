import json

with open("/var/www/shadowsocksr/mudb.json","r"):
    json_data = json.load(f)
for index, line in enumerate(json_data):
    line["u"] = 0
    line["d"] = 0

with open("/var/www/shadowsocksr/mudb.json","w"):
    json.dump(json_data,f,sort_keys = True,indent = 4)
    print("data reseted")
