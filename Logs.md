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

>> admin
>> local
>> user(for testing, will be deleted later)

* Build database_opt.py under /home/frank/test for any database command
