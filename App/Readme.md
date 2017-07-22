## Intro

### CRUD
           Path         |     Meaning
------------------------|-------------------------
    $WHERE=shadowsocks  | users in mudb.json
    $WHERE=website      | users in mongodb
<br>

        Endpoint        |     Meaning
------------------------|-------------------------
       POST auth        | Add a new authentication
    GET /users          | List all users
   GET /users/1/$WHERE  | List a specific user ($WHERE decides src)
   POST /users          | Add a new user
   PUT /users/1/$WHERE  | Update a specific user (completely)
  PATCH /users/1/$WHERE | Update a specific user (partially)

### Requeset body structure

For all users (Only accessible for admins)
```json
  {
    "users": [
      "user":{
        "email" : str,
        \\Others are inherented the structure of a specific user in shadowsocks
      }
    ],
  }
```

#### shadowsocks

```json
For a specific user
  {
    "token" : str,
    "user" : str,               //Primary key, Only Available in GET
    "password" : str,
    "enable" : bool,            //Only Available in GET
    "port" : int,               //Only Available in GET
    "method" : str,
    "protocol" : str,
    "obfs" : str,
    "transfer_enable" : int,    //Only Available in GET
    "upward_transfer" : int,    //Only Available in GET
    "downward_transfer" : int   //Only Available in GET
  }
```
Returns `{"Accepted":bool}`

#### website
``` json
  {
    "token" : str,
    "user" : str,     //Primary key
    "password_hash" : str,
    "email" : str
  }
```

#### auth

For all user:

``` json
  {
    "user" : str,
    "password_hash" : str,
  }

