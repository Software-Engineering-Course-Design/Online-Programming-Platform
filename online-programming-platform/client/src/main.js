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
import 'highlight.js/styles/monokai-sublime.css' //导入代码高亮样式
import VueCookies from 'vue-cookies'
Vue.use(VueCookies)

import {
  Message
} from 'element-ui';
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
Vue.directive('highlight', function (el) {
  let highlight = el.querySelectorAll('pre code');
  highlight.forEach((block) => {
    hljs.highlightBlock(block);
  })
})
//VueCookies.config('3d')
router.beforeEach((to, from, next) => {
  //刷新后vuex state数据会被还原，用cookie解决
  if (VueCookies.get("LoginStatus") == 'isLogin') {
    store.commit("userStatus", true);
  }
  if (VueCookies.get("userType") == 'HR') {
    store.commit("setUserType", true);
  } else if (VueCookies.get("userType") == 'applicant') {
    store.commit("setUserType", false);
  }

  if (to.meta.isLogin == true & to.meta.userType == true) { //需要面试官权限的页面
    if (store.getters.isLogin == true & store.getters.userType == true) { //已登录+用户类型面试官
      next();
    } else {
      next({
        path: '/sign'
      })
    }
  } else if (to.meta.isLogin == true & to.meta.userType == false) { //需要面试者权限的页面
    if (store.getters.isLogin == true & store.getters.userType == false) { //已登录+用户类型面试者
      next();
    } else {
      next({
        path: '/sign'
      })
    }
  } else {
    next();
  }

});

// router.afterEach(route => {
//   window.scroll(0, 0);
// });
