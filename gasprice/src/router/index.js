import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/Login'
import SignUp from '@/components/SignUp'
import Profile from '@/components/Profile.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
    	path: '/SignUp',
    	name: 'SignUp',
    	component: SignUp
    },
    {
    	path: '/Profile',
    	name: 'Profile',
    	component: Profile
    }

  ]
})


