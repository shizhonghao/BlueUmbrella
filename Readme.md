# Readme

A platform to help our friends to escape some walls.

## Functions

The whole platform is more likely to be a front-end wrapping the ShadowsocksR manyuser in mudb.json.

What we are providing is an authentication system corresponding to each individual shadowsocks account, and a RESTful API manipulating those info. (See documentation of APIs).

Currently, we are using Vue.js to build the front-end and embedded it into a page of hexo (See `front-end/deploy`).

At the same time, we are using Flask and Mongodb to maintain the back-end and the authentication.


## Current status

Here's a [Todo list](https://github.com/raycursive/BlueUmbrella/blob/master/Todolist.md).

Here's our [working logs](https://github.com/raycursive/BlueUmbrella/blob/master/Logs.md), updating by our progress.

Here's the [documentation](https://github.com/raycursive/BlueUmbrella/blob/master/App/Readme.md) of the API.