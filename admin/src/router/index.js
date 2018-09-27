import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Logout from '@/components/Logout'
import View from '@/components/View'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/logout',
      name: 'Logout',
      component: Logout
    },
    {
      path: '/View',
      name: 'View',
      component: View
    }
  ]
})
