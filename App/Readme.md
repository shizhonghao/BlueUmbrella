## Intro

### CRUD
* `/login`: 
    * GET: if login, return `current_user.username` (for debugging), else return unauthorized.

    * POST: receive `username` and `password`, return `Token` if successfully logged in.

* `/logout`:
    * GET: return `Success:True` (Maybe remove or normalize later)

* `/register`:
    * POST: receive `username`, `password` and `email`(optional), return `Success:true` and `Token` if successfully registered and automatically logged in.

* `/users`:
    * GET: return user information (See below), required admin permission.

* `/uesrs/<string:username>`
    * GET: return specific user information (See below), required admin permission or `current_user.username == username`.

    * PATCH: receive allowed args (See below), return `Success:true`, required admin permission or `current_user.username == username`.

    * DELETE: return `Success:true`, required admin permission
    
    
About status code : [link](http://www.restapitutorial.com/lessons/httpmethods.html)


### Requeset body structure

For all users (Only accessible for admins)
```json
  {
    "user": {
      "email" : "str",
      "user" : "str",
      "..." : "from spec user"
    }
  }
```

For a specific user
```json
  {
    "user" : "str",
    "ss_password" : "str",
    "email":"str",
    "enable" : "bool",
    "port" : "int",
    "method" : "str",
    "protocol" : "str",
    "obfs" : "str",
    "transfer_enable" : "int",
    "upward_transfer" : "int",
    "downward_transfer" : "int"
  }
```

Allowed args:
```json
  {
    "email" : "str",
    "ss_password" : "str",
    "method" : "str",
    "protocol": "str",
    "obfs" : "str",
    "transfer_enable" : "int, only by admin",
    "enable" : "bool, only by admin"
  }