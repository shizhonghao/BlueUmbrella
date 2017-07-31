// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import axios from 'axios'
import Vuex from 'vuex'
import 'element-ui/lib/theme-default/index.css'

Vue.use(ElementUI)
Vue.use(Vuex)
Vue.prototype.$ajax = axios
// $state stands for logging in state
localStorage.setItem("state", false)
localStorage.setItem("username", '')
Vue.config.productionTip = false
axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://api.tbufoundation.tk'


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})