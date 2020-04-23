import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'

import FuelQuote from '@/components/FuelQuote'


import SignUp from '@/components/SignUp'
import Profile from '@/components/Profile.vue'


Vue.use(Router)

export default new Router({

  mode: 'history',

  routes: [
    {
      path: '/',
      redirect: '/Login',
      meta: {
        requireAuth: false,
        }
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login,
      meta: {
        requireAuth: false,
      }
    },
    {
    	path: '/SignUp',
    	name: 'SignUp',
    	component: SignUp,
      meta: {
        requireAuth: false,
      }
    },
    {
    	path: '/Profile',
    	name: 'Profile',
    	component: Profile,
      meta: {
        requireAuth: true,
      }
    } ,
    {
      path: '/FuelQuote',
      name: 'FuelQuote',
      component: FuelQuote,
      meta: {
        requireAuth: true,
      }
    }


  ]
})


