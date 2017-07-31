// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import axios from 'axios'
import 'element-ui/lib/theme-default/index.css'

Vue.use(ElementUI)
Vue.prototype.$ajax = axios
// $state stands for logging in state
Vue.prototype.$state = false
Vue.prototype.$username = ''
Vue.config.productionTip = false
axios.defaults.withCredentials = true
axios.defaults.baseURL = 'http://api.tbufoundation.tk'


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App),
  watch:{ 
    '$route':'checkLogin'
  },
  created() { 
    this.checkLogin();
  },
  methods:{ 
    getStatus(){
      var status = false
      axios.get('/login')
        .then((response) => {
          console.log("1", response.data.LoggedIn)
           status = response.data.LoggedIn
        })
        .catch((error) => {
          console.log(error);
        });
        console.log("2", status)
      return status
      
    },
    checkLogin(){
      console.log("3",(this.getStatus().then()))
    }
  }
})