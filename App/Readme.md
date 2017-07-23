## Intro

### CRUD
* Login: 
    * GET: if login, return `current_user.name` (for debugging), else return unauthorized.
    * POST: receive `username` and `password`, return `Token`

* Logout:
    * GET: return `Success` (Maybe remove or normalize later)

Users:

 |       Endpoint   |        Meaning         |
 | ---------------- | ---------------------- |
 |   GET /users     | List all users *admin* |
 |  GET /users/1/   | List a specific user   |
 |  POST /users     | Add a new user *admin* | 
 | PATCH /users/1/  | Update a specific user |
 | DELETE /users/1/ | Delete a user          |

About status code : [link](http://www.restapitutorial.com/lessons/httpmethods.html)


### Requeset body structure

For all users (Only accessible for admins)
```javascript
  {
    "user": {
      "email" : "str",
      "user" : "str",
      "..." : "from spec user"
    }
  }
```

For a specific user
```javascript
  {
    "user" : "str",               //Primary key, Only Available in GET
    "password" : "str",
    "enable" : "bool",            //Only Available in GET
    "port" : "int",               //Only Available in GET
    "method" : "str",
    "protocol" : "str",
    "obfs" : "str",
    "transfer_enable" : "int",    //Only Available in GET
    "upward_transfer" : "int",    //Only Available in GET
    "downward_transfer" : "int"   //Only Available in GET
  }
```