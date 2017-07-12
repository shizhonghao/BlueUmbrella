## Have Done 

### Jun 10

* Setup basic env: zsh (oh-my-zsh for users), git, tmux, python
* User management in VPS and pubkeys for logging into SSH

### Jun 11

* Install LEMP Stack ([link](https://www.digitalocean.com/community/tutorials/how-to-install-linux-nginx-mysql-php-lemp-stack-in-ubuntu-16-04))

* Install ShadowsocksR ([link](https://github.com/breakwa11/shadowsocks-rss/wiki/Server-Setup(manyuser-with-mysql)))  **Succeed with mudbjson**


## Gonna Do

* Install ss-panel ([link](https://sspanel.xyz/docs/install/manual)) **Not working properly due to configuration of PHP** **May be dropped**

* Optimizing Shadowsocks ([link](http://www.jianshu.com/p/17522251883e))

    * Note: we are not going to completely follow this one, since there's a better way to do tcp congestion control (bbr) which has already been installed.

* For configuration of multiple sites (Virtual host) ([link](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04))

### Added Jun 11 late nignt

* Develope interfaces for ShadowsocksR many users, and maybe a front-end for later work.

    * Note: as the version of many users we have used so far is based on mudbjson, the coordination with a **real** database may be concerned as a hidden problem.

* Start to operate the service