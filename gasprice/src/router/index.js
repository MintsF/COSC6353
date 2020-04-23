import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'

import FuelQuote from '@/components/FuelQuote'
// import SignUp from '@/components/SignUp'

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
        isLogin: false
        }
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login,
      meta: {
        isLogin: false
      }
    },
    {
    	path: '/SignUp',
    	name: 'SignUp',
    	component: SignUp,
      meta: {
        isLogin: false
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
    },
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld,
      meta: {
        requireAuth: true,
      }
    }

  ]
})


