import {
  post,
  get
} from './request.js'

//url
//例子
//const getData = get('url');
//在别的地方引入 import {getData} from 'api',按钮点击可以绑定这个方法
const url = {
  signup: 'http://127.0.0.1:5000/signup/signup_info',
  login: 'http://127.0.0.1:5000/login/login_info',
  // signup: 'http://127.0.0.1:8000/signup',
  // login: 'http://127.0.0.1:8000/login',
  questionList: 'http://127.0.0.1:8000/questionList',//面试模块，请求面试题目
  interviewList: 'http://127.0.0.1:8000/interviewList',//面试者首页，请求可参加的和已参加的面试场次信息
  //resultList: 'http://127.0.0.1:8000/resultList',//面试者首页，请求已参加的面试场次信息
  submitCode: 'http://127.0.0.1:8000/submitCode',//提交代码
  viewResult:'http://127.0.0.1:8000/viewResult',//查看已参加面试详情
  handin:'http://127.0.0.1:8000/handin',//交卷
  submitJudge:'http://127.0.0.1:8000/submitJudge',//判断代码是否已提交过

  examList: 'http://127.0.0.1:8000/viewExamList',
  questionContent: 'http://127.0.0.1:5000/interviewer/questionID',

};


export default {
  state: {
    isLogin: false,
  },
  getters: {
    //获取登录状态
    isLogin: state => state.isLogin,
  },
  mutations: {
    //保存登录状态
    userStatus(state, flag) {
      state.isLogin = flag
    },
  },
  actions: {
    //获取登录状态
    setUser({commit}, flag) {
      commit("userStatus", flag)
    },
    signupRequest: ({
      state
    }, postData) => {
      return post(url.signup, postData);
    },
    loginRequest: ({
      state
    }, postData) => {
      return post(url.login, postData);
    },
    questionListRequest: ({
      state
    }, postData) => {
      return post(url.questionList, postData);
    },
    interviewListRequest: ({
      state
    }, postData) => {
      return post(url.interviewList, postData);
    },
    // resultListRequest: ({
    //   state
    // }, postData) => {
    //   return post(url.resultList, postData);
    // },
    submitCodeRequest: ({
      state
    }, postData) => {
      return post(url.submitCode, postData);
    },
    viewResultRequest: ({
      state
    }, postData) => {
      return post(url.viewResult, postData);
    },
    handinRequest: ({
      state
    }, postData) => {
      return post(url.handin, postData);
    },
    submitJudgeRequest: ({
      state
    }, postData) => {
      return post(url.submitJudge, postData);
    },
    viewExamListRequest:({
                           state
                         }, postData) => {
      return post(url.examList, postData);
    },
    viewQuestionRequest:({
                           state
                         }, postData) => {
      return post(url.questionContent, postData);
    },

  }

}
