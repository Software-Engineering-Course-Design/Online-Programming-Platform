// 入口JS 创建Vue实例
import Vue from 'vue'
import App from './App.vue'

import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import qs from 'qs'
import store from './store/index.js'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import VueQuillEditor from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

import hljs from 'highlight.js' //导入代码高亮文件
import 'highlight.js/styles/monokai-sublime.css'  //导入代码高亮样式
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)

import { Message } from 'element-ui';
Vue.use(VueQuillEditor, {
  placeholder: '请输入内容',
})

Vue.use(VueAxios, axios)
Vue.use(ElementUI)
Vue.config.productionTip = false
// Vue.prototype.$axios = axios
// Vue.prototype.$qs = qs
Vue.prototype.$axios = axios


global.axios = axios


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: {
    App
  },
  template: '<App/>'
})
//自定义一个代码高亮指令
Vue.directive('highlight',function (el) {
  let highlight = el.querySelectorAll('pre code');
  highlight.forEach((block)=>{
      hljs.highlightBlock(block);
  })
})
//this.$cookies.config('3d')
// router.beforeEach((to, from, next) => {
//   //获取用户登录成功后储存的登录标志
//   let getFlag = localStorage.getItem("Flag");
//   //用户已登录
//   if (getFlag === "isLogin") {
//     //设置vuex登录状态为已登录
//     store.state.isLogin = true
//     next()
//     //如果已登录，还想想进入登录注册界面，则定向回首页
//     if (!to.meta.isLogin) {
//       //提示
//       Message({
//         showClose: true,
//         message: '您已登录，无法进入登录注册界面',
//         type: 'warning',
//         duration: 2300,
//       })
//       next({
//         path: '/home'
//       })
//     }
//     //如果登录标志不存在，即未登录
//   } else {
//     //用户想进入需要登录的页面，则定向回登录注册界面
//     if (to.meta.isLogin) {
//       next({
//         path: '/sign',
//       })
//       //提示
//       Message({
//         showClose: true,
//         message: '您尚未登录，请先登录',
//         type: 'warning',
//         duration: 2300,

//       })
//       //用户进入无需登录的界面，则跳转继续
//     } else {
//       next()
//     }
//   }

// });

// router.afterEach(route => {
//   window.scroll(0, 0);
// });
