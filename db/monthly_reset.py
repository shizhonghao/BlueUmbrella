# Edit /etc/crontab to set time interval of resetting data.

import json

with open("/var/www/shadowsocksr/mudb.json","r") as f:
    json_data = json.load(f)
for index, line in enumerate(json_data):
    line["u"] = 0
    line["d"] = 0

with open("/var/www/shadowsocksr/mudb.json","w") as f:
    json.dump(json_data,f,sort_keys = True,indent = 4)
    print("data reseted")
