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

* Configurated the logs of Nginx.

* Dealing with multiusers in Hexo, I decided to symlink the `blogs` in our git depository to `source` in the root dictionary of hexo, since for the other direction, Git deals the symlink just as a irregular file instead of a link, but hexo works well.

* By the way, I'm gonna modify the `hexo-deployer-rsync` to automatically commit and push the folder `blogs` to Github.

## Gonna Do

* Install ss-panel ([link](https://sspanel.xyz/docs/install/manual)) **Not working properly due to configuration of PHP** **May be dropped**

* Optimizing Shadowsocks ([link](http://www.jianshu.com/p/17522251883e))

    * Note: we are not going to completely follow this one, since there's a better way to do tcp congestion control (bbr) which has already been installed.

* For configuration of multiple sites (Virtual host) ([link](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04))

* Build front-end & back-end base on vue(js) & eve(python) 

### Added Jul 11 late nignt

* Develope interfaces for ShadowsocksR many users, and maybe a front-end for later work.

    * Note: as the version of many users we have used so far is based on mudbjson, the coordination with a **real** database may be concerned as a hidden problem.

* Start to operate the service

### Added Jul 13

* Get a 404 and 50x page (Path: /usr/share/nginx/html)

* Get a favicon
