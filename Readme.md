#Readme

A platform to help our friends to escape some walls.

## Functions

The platform we are building in should be capable of:

1. Letting a user sign in/up.

2. Allowing a user to check his/her current account status(dataflow, connection time, available time etc). 

3. Allowing a user to pay for his/her account(10￥/month)

4. Providing VPN services for those users who still has available time in their account.

5. Allowing administrator to check the users status, may have to set user's available time manually.

## database design

relational schema:

user(id,pwd)

account(id,expire_date)

stat(id,dataflow,connection_time)

with primary key id(username)
