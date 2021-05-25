import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Sign from '../views/Sign.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [{
      path: '/home',
      name: 'home',
      component: Home,
      meta: {
        isLogin: false
      },
    },
    {
      path: '/',
      name: '/',
      component: Sign,
      meta: {
        isLogin: false
      },
    },
    {
      path: '/sign',
      name: 'sign',
      component: Sign,
      meta: {
        isLogin: false
      },
    },
    //后面都用懒加载，防止组件加载过慢
    {
      path: '/applicant',
      name: 'applicant',
      component: resolve => require(['../views/Applicant.vue'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/applicant/interview',
      name: 'appInterview',
      component: resolve => require(['../views/AppInterview.vue'], resolve),
      meta: {
        isLogin: false
      },
    },
    // {
    //   path: '/applicant/result',
    //   name: 'appResult',
    //   component:resolve=>require(['../views/AppResult.vue'],resolve),
    // },
    {
      path: '/interview/addNewQuestion',
      name: 'interviewToAddQuestion',
      component: resolve => require(['../views/addNewQuestion'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/interview/questionDetails',
      name: 'interviewToQuestionDetails',
      component: resolve => require(['../views/viewQuestionDetails'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/interview/updateQuestion',
      name: 'interviewToUpdateQuestion',
      component: resolve => require(['../views/updateQuestion'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/interview/viewQuestionCodeList',
      name: 'interviewToViewQuestionCodeList',
      component: resolve => require(['../views/viewQuestionCodeList'], resolve),
      meta: {
        isLogin: false
      },
    },

  ]
})
