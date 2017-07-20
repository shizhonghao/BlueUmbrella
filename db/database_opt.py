from pymongo import MongoClient
import datetime
from calendar import monthrange

class TBU_db:
	
	def __init__(self):
		self.client = MongoClient('localhost', 27017) 
		self.db = self.client.TBU
		self.init_date = datetime.date(2017,7,7)

	#operations for checking the TBU database	
	def get_email(self,uid):
		user = self.db.user
		res = user.find({"id":uid})
		for info in res:
			e_mail = info["e_mail"]
		return e_mail

	def login_check(self,uid,pwd):
		user = self.db.user
		res = user.find({"id":uid})
		for info in res:
			db_pwd = info["pwd"]
			if(db_pwd == pwd):
				return True
			else:
				return False

	def get_expire_date(self,uid):
		collection = self.db.account
		res = collection.find({"id":uid})
		for info in res:
			date = info["expire_date"]
		return date

	#operations for inserting the TBU datebase
	def new_user(self,uid,pwd,e_mail):
		collection = self.db.user
		line = {"id":uid,"pwd":pwd,"e_mail":e_mail}
		collection.insert(line)
		collection = self.db.account
		line = {"id":uid,"expire_date":self.init_date}
		collection.insert(line)
	
	
	#operations for altering the TBU datebase
	def reset_pwd(uid,new_pwd):
		collection = self.db.user
		res = collection.find({"id":uid})
		for line in res:
			line["pwd"] = new_pwd
			collection.save(line)

	def reset_email(uid,new_email):
		collection = self.db.user
		res = collection.find({"id":uid})
		for line in res:
			line["e_mail"] = new_email
			collection.save(line)
	
	def add_expire(uid,time_added):
		collection = self.db.account
		res = collection.find({"id":uid})
		for line in res:
			t = line["expire_time"].split(sep='-')
			expire = datetime.time(t[0],t[1],t[2])
			for i in range(0,time_added):
				expire = expire + datetime.timedelta(days=monthrange(expire.year,expire.month)[1])
			line["expire_time"] = expire.isoformat()
			collection.save(line)


if __name__ == '__main__':
	db = TBU_db()
	print(db.get_email("frank"))
	print(db.get_expire_date("frank"))
	print(db.login_check("frank","password"))
	print(db.login_check("frank","passwor"))
	
	db.add_expire("frank",3)
