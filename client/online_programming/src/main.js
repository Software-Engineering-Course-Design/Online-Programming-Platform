
// 入口JS 创建Vue实例
import Vue from 'vue'
import App from './App.vue'
// import Validator from 'vue-validator'
// Vue.use(Validator)
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
//import axios from "axios";

Vue.use(ElementUI)
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
