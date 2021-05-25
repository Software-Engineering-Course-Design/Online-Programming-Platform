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
  questionList: 'http://127.0.0.1:8000/questionList',
  interviewList: 'http://127.0.0.1:8000/interviewList',
  resultList: 'http://127.0.0.1:8000/resultList',
  submitCode: 'http://127.0.0.1:8000/submitCode',
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
    resultListRequest: ({
      state
    }, postData) => {
      return post(url.resultList, postData);
    },
    submitCodeRequest: ({
      state
    }, postData) => {
      return post(url.submitCode, postData);
    },
  }

}
