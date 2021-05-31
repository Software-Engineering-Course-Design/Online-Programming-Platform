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
      path: '/applicant',//面试者首页
      name: 'applicant',
      component: resolve => require(['../views/Applicant.vue'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/applicant/interview',//面试页面
      name: 'appInterview',
      component: resolve => require(['../views/AppInterview.vue'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/interviewer/addNewQuestion',
      name: 'interviewerToAddQuestion',
      component: resolve => require(['../views/addNewQuestion'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/interviewer/viewQuestionDetails',
      name: 'interviewerToQuestionDetails',
      component: resolve => require(['../views/viewQuestionDetails'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/interviewer/updateQuestion',
      name: 'interviewerToUpdateQuestion',
      component: resolve => require(['../views/updateQuestion'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/interviewer/viewQuestionCodeList',
      name: 'interviewerToViewQuestionCodeList',
      component: resolve => require(['../views/viewQuestionCodeList'], resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/interviewer/addNewExam',
      name: 'interviewerToAddNewExam',
      component:resolve => require(['../views/addNewExam'],resolve),
    },
    {
      path: '/applicant/viewResult',//面试者查看已面试结果的页面
      name: 'viewResult',
      component:resolve => require(['../views/viewResult'],resolve),
      meta: {
        isLogin: false
      },
    },
    {
      path: '/interviewer/inviteToExam',
      name: 'interviewerToInvite',
      component:resolve => require(['../views/inviteToExam'],resolve),
    },
    {
      path: '/interviewer/viewExamList',
      name: 'interviewerToViewExamList',
      component:resolve => require(['../views/viewExamList'],resolve),
    },
    {
      path: '/interviewer/checkExam',
      name: 'interviewerToCheckExam',
      component:resolve => require(['../views/checkExam'],resolve),
    },
  ]
})
