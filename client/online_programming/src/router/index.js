import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Sign from '../views/Sign.vue'

import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/',
      name: '/',
      component: Home
    },
    {
      path: '/sign',
      name: 'sign',
      component: Sign
    },
  ]
})
