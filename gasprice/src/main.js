// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import axios from 'axios'
import store from './store/store'
import VueCookies from 'vue-cookies'
import qs from 'qs'

// import vueCountryRegionSelect from 'vue-country-region-select'

import ElementUI from '../node_modules/element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import elementLocale from 'element-ui/lib/locale/lang/en';
Vue.use(ElementUI, { locale: elementLocale });


Vue.config.productionTip = false
// Vue.use(ElementUI)
Vue.prototype.$axios=axios
Vue.prototype.$cookie = VueCookies
Vue.prototype.$qs = qs
// Vue.use(vueCountryRegionSelect)

// axios.defaults.withCredentials=true;
axios.defaults.baseURL = 'http://127.0.0.1:8000';
// ///////////
router.beforeEach((to, from, next) => {
  // console.log("怎么没有运行")
  if (to.meta.requireAuth) { // 判断该路由是否需要登录权限
    if (sessionStorage.getItem('loginstatus')) { // 判断本地是否存在access_token
      next()
    } else {
      // 未登录,跳转到登陆页面，并且带上 将要去的地址，方便登陆后跳转。
      next({
        path: '/',
        // query:{ referrer: to.fullPath}
      })
    }
  } else {
    next()
  }
});
  // ////////////////////////////
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'

})


// 路由判断登录 根据路由配置文件的参数
// router.beforeEach((to, from, next) => {
//      console.log("怎么没有运行")
//    if (to.matched.some(record => record.meta.requireAuth)){ // 判断该路由是否需要登录权限
//       console.log('need login');
//     if (localStorage.token) { // 判断当前的token是否存在 ； 登录存入的token
//       next();
//     }
//     else {
//      next({
//       path: '/',
//       query: {redirect: to.fullPath} // 将跳转的路由path作为参数，登录成功后跳转到该路由
//      })
//     }
//    }
//    else {
//     next();
//    }
//   });

// 配置路由权限
// router.beforeEach((to, from, next) => {
//   console.log("怎么没有运行")
//   if (to.meta.requireAuth) { // 判断该路由是否需要登录权限
//     if (sessionStorage.getItem('loginstatus')) { // 判断本地是否存在access_token
//       next()
//     } else {
//       // 未登录,跳转到登陆页面，并且带上 将要去的地址，方便登陆后跳转。
//       next({
//         path: '/',
//         query:{ referrer: to.fullPath}
//       })
//     }
//   } else {
//     next()
//   }
// })

// // export default Vue.extend({
//   data: () => ({
//     country: '',
//     region: ''
//   })
// })

// router.beforeEach((to, from, next) => {

//   //获取用户登录成功后储存的登录标志
//   let getFlag = localStorage.getItem("Flag");

//   //如果登录标志存在且为isLogin，即用户已登录
//   if(getFlag === "isLogin"){

//     //设置vuex登录状态为已登录
//     store.state.isLogin = true
//     next()

//     //如果已登录，还想想进入登录注册界面，则定向回首页
//     if (!to.meta.isLogin) {
//        //iViewUi友好提示
//       iView.Message.error('请先退出登录')
//       next({
//         path: '/Profile'
//       })
//     }
  
//   //如果登录标志不存在，即未登录
//   }else{

//     //用户想进入需要登录的页面，则定向回登录界面
//     if(to.meta.isLogin){
//       next({
//         path: '/Login',
//       })
//       //iViewUi友好提示
//       iView.Message.info('请先登录')
//     //用户进入无需登录的界面，则跳转继续
//     }else{
//       next()
//     }

//   }

// });

// router.afterEach(route => {
//   window.scroll(0, 0);
// });





