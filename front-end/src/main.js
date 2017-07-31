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
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App),
  watch:{ 
    '$route':'checkLogin'
  },
  created() { 
    this.getStatus();
    this.checkLogin();
  },
  methods:{ 
    getStatus(){
      axios.get('http://api.tbufoundation.tk/login')
        .then((response) => {
          this.$state = response.data.LoggedIn;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    checkLogin() {
      if(this.$state){ 
      // If logged in
        if(this.$route.name == "Login" || this.$route.name == "Register" || this.$route.path == "/"){
          this.$router.push('/view')
        }
      } else { 
      // If didn't log in
        if(this.$route.name == "View" || this.$route.name == "Logout" || this.$route.name == "Edit" || this.$route.path == "/"){
          this.$router.push('/login');
        }
      }
    }
  }
})