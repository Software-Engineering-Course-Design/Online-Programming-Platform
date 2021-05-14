import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
// import Home from './views/Home.vue'
// import Home from './views/Home.vue'
// import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
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
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/Register.vue')
    }
    //     {
    //       path: '/about',
    //       name: 'about',
    //       // route level code-splitting
    //       // this generates a separate chunk (about.[hash].js) for this route
    //       // which is lazy-loaded when the route is visited.
    //       component: () =>
    //         import(/* webpackChunkName: "about" */ './views/About.vue')
    //     },
    //     {
    //       path: '/interview',
    //       name: 'interview',
    //       // route level code-splitting
    //       // this generates a separate chunk (about.[hash].js) for this route
    //       // which is lazy-loaded when the route is visited.
    //       component: Interview
    //     },
    //     {
    //       path: '/applicant/home',
    //       name: 'applicantHome',
    //       component:resolve=>require(['./views/ApplicantHome.vue'],resolve),
    //     },
    // /*    {
    //       path:'/chatRoom',
    //       name: 'chatRoom',
    //       component:ChatRoom
    //     },*/
    //     {
    //       path:'/titleEditor',
    //       name: 'titleEditor',
    //       component: () =>
    //         import(/* webpackChunkName: "about" */ './views/TitleEditor.vue')
    //     },
    //     {
    //       path:'/AuditionQuestionList',
    //       name: 'auditonQuestionList',
    //       component: () =>
    //         import(/* webpackChunkName: "about" */ './views/AuditionQuestionList.vue')
    //     },
    //     {
    //       path:'/interviewer/home',
    //       name: 'InterviewerHome',
    //       component: () =>
    //         import(/* webpackChunkName: "about" */ './views/InterviewerHome')
    //     }
  ]
})
