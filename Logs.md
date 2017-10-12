## Have Done 

### Jul 10

* Setup basic env: zsh (oh-my-zsh for users), git, tmux, python
* User management in VPS and pubkeys for logging into SSH

### Jul 11

* Installed LEMP Stack ([link](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-in-ubuntu-16-04))

* Installed ShadowsocksR ([link](https://github.com/breakwa11/shadowsocks-rss/wiki/Server-Setup(manyuser-with-mysql)))  **Succeed with mudbjson**

### Jul 12

* Installed eve([link](http://python-eve.org/quickstart.html#database-interlude)) and Mongodb([link](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)) 
    * Note: May use Flask instead.

* Tested availability under /home/frank/test

### Jul 13

* Installed Hexo, running a simple static blog as our main page.

* Configurated virtual hosts of Nginx. ([link](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04))
* Configurated the logs of Nginx.

* Deploy Hexo in server, modified `hexo-deployer-rsync` for using it at `localhost`.

### Jul 14

* Build database on mongodb, which has the following structure:

> mongodb  
>> TBU  
>>> user  
>>>> id  
>>>> pwd  
>>>> e_mail  
>>> account  
>>>> id  
>>>> expire_date  
>>>
>> admin  
>> local  
>> user(for testing, will be deleted later)

* Build database_opt.py under /home/frank/test for any database command

### Jul 23

After a long time of afking, we started to work on the back-end.

* Restructured the back-end

* Implemented authentication (cookies & token) based on `flask_login`

* Rewrote the schema of the database (See App/models.py `class User`)

* Wrote a small toolbox based on mongoengine to manage the database

### Jul 27

A short overview of recently works

* Implemented a model dealing with maintaining the status of mudb.json (the database of shadowsocksR) (by a singleton class) (tested all functions, works well)

* Wrote a register interface (tested)

* Controller for `GET /users` and `GET /users/<string:username>` (added the email part, tested)

* Controller for `DELETE /users/<username>` and `PATCH /users/<username>` (for PATCH, distinguish the function allowed by admin and regular users) (tested)

Basically, we've accomplished the development of the back-end.

### Jul 31

* Fix bugs: SSUsers.add -- lack of `protocol` key

* Add feature: Allow user to modify their password in mongodb

* Formally pushed our back-end onto the server at `api.tbufoundation.tk`

* Note: Adding vue supporting into hexo-theme-next:
    * themes/next/layout/_layout.swig add
    `<script type="text/javascript" src="{{ url_for(theme.js) }}/src/vue.js"></script>`

### Apr 4

* Working on front-end, for more details check our github history

* Apparently the working on Vue is not as smooth as on flask, but at least now the only thing remaining for normal users is editing their account info. We are planning to put the whole system online in few days.

* Tmr I'm gonna fix the bug of error handler, the different view of `View` in Firefox and Chrome, the base64 and QRCode support. At the very last I'm gonna try to merge it into our hexo page.

### Apr 5

* The bug of error handler is caused by the CORS handling of non-200 request. It has been fixed by adding `always` at the end of `add_header`.

* The whole page has been merged into the hexo page, by re-rendering the index.html to index.md. In the very beginning I tried to fix names of js files, then I realized the reason why we need hash in the filename is caching.

* HTTPs support is added by Let's Encrypt!. Thanks EFF.

### Apr 6

* Add a logo on the QRCode.

* Add a password double-checking process in registration.

* Add routing checking when accessing `/logout` and `register` (for the other two I've done it in the beginning")

### Oct 11

* Add monthly reset plan. Altered `/etc/crontab` to run `/root/BlueUmbrella/db/monthly_reset.py` on the 1st of each month.

### Oct 12

* Add backup plan before the dataflow reset.
