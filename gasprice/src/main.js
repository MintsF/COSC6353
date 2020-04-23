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

Vue.prototype.$axios=axios
Vue.prototype.$cookie = VueCookies
Vue.prototype.$qs = qs

axios.defaults.baseURL = 'http://127.0.0.1:8000';
// ///////////
router.beforeEach((to, from, next) => {

  if (to.meta.requireAuth) { 
    if (sessionStorage.getItem('loginstatus')) { 
      next()
    } else {
      next({
        path: '/',
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


