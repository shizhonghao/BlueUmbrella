#Flask
DEBUG = True

#Database
MONGODB_DB = 'TBU'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

#Security
SECRET_KEY = 'hitherecheerslove'
SECURITY_USER_IDENTITY_ATTRIBUTES = 'username'
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = b'hahaha'