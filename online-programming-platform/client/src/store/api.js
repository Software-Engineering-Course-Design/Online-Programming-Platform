import {
  post,
  get
} from './request.js'

//url
//例子
//const getData = get('url');
//在别的地方引入 import {getData} from 'api',按钮点击可以绑定这个方法
const url = {
  //test: 'http://127.0.0.1:8000/testget',
  signup: 'http://127.0.0.1:5000/signup/signup_info',
  login: 'http://127.0.0.1:5000/login/login_info',
  // signup: 'http://127.0.0.1:8000/signup',
  // login: 'http://127.0.0.1:8000/login',
  questionList: 'http://127.0.0.1:8000/questionList',
  interviewList: 'http://127.0.0.1:8000/interviewList',
  resultList: 'http://127.0.0.1:8000/resultList',
};


export default {
  state:{},
  actions:{
    // testget:(s)=>{
    //   return get(url.test,{s});
    // },
    signupRequest: ({state},postData) => {
      return post(url.signup, postData);
    },
    loginRequest: ({state},postData) => {
      return post(url.login, postData);
    },
    questionListRequest:({state},postData)=>{
      return post(url.questionList, postData);
    },
    interviewListRequest:({state},postData)=>{
      return post(url.interviewList,postData);
    },
    resultListRequest:({state},postData)=>{
      return post(url.resultList,postData);
    },
  }
  
}
