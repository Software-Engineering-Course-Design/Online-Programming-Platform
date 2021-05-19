import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Sign from '../views/Sign.vue'

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
    //后面都用懒加载，防止组件加载过慢
    {
      path: '/applicant',
      name: 'applicant',
      component:resolve=>require(['../views/Applicant.vue'],resolve),
    },
    {
      path: '/applicant/interview',
      name: 'appInterview',
      component:resolve=>require(['../views/AppInterview.vue'],resolve),
    },
    // {
    //   path: '/applicant/result',
    //   name: 'appResult',
    //   component:resolve=>require(['../views/AppResult.vue'],resolve),
    // },
  ]
})
