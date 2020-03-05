import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import FuleQuote from '@/components/FuleQuote'
// import SignUp from '@/components/SignUp'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/Login',
      name: 'Login',
      component: Login
    }
    // {
    // 	path: '/',
    // 	name: 'SignUp',
    // 	component: SignUp
    // }
    ,
    {
      path: '/FuleQuote',
      name: 'FuleQuote',
      component: FuleQuote
    }
  ]
})
