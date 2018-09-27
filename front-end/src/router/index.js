import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Logout from '@/components/Logout'
import Register from '@/components/Register'
import View from '@/components/View'
import Edit from '@/components/Edit'

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
      path: '/register',
      name: 'Register',
      component: Register
    },
      {
      path: '/view',
      name: 'View',
      component: View
    },
      {
      path: '/edit',
      name: 'Edit',
      component: Edit
    }
  ]
})
