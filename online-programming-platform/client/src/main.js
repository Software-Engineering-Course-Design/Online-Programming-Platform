
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
Vue.use(VueQuillEditor,{
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
  components: { App },
  template: '<App/>'
})
