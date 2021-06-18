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

  // questionList: 'http://127.0.0.1:8000/questionList', //面试模块，请求面试题目
  // interviewList: 'http://127.0.0.1:8000/interviewList', //面试者首页，请求可参加的和已参加的面试场次信息
  // submitCode: 'http://127.0.0.1:8000/submitCode', //提交代码
  // viewResult: 'http://127.0.0.1:8000/viewResult', //查看已参加面试详情
  // handin: 'http://127.0.0.1:8000/handin', //交卷
  // submitJudge: 'http://127.0.0.1:8000/submitJudge', //判断代码是否已提交过
  questionList: 'http://127.0.0.1:5000/applicant/question_message', //面试模块，请求面试题目
  interviewList: 'http://127.0.0.1:5000/applicant/join_message', //面试者首页，请求可参加的和已参加的面试场次信息
  submitCode: 'http://127.0.0.1:5000/applicant/commit_code', //提交代码
  viewResult: 'http://127.0.0.1:5000/applicant/interview_result', //查看已参加面试详情
  handin: 'http://127.0.0.1:5000/applicant/end_session', //交卷
  submitJudge: 'http://127.0.0.1:5000/applicant/submit_message', //判断代码是否已提交过

  examList: 'http://127.0.0.1:5000/interviewer/interview_info',//查看面试情况
  questionContent: 'http://127.0.0.1:5000/interviewer/questionID',//查看面试题详情
  questionLibrary: 'http://127.0.0.1:5000/interviewer/interviewer_info',//查看面试题目列表
  addNewQuestion: 'http://127.0.0.1:5000/interviewer/add_question',//新建题目
  addNewExam: 'http://127.0.0.1:5000/interviewer/initial_interview',//发起面试
  updateQuestion: 'http://127.0.0.1:5000/interviewer/edit_question',//修改面试题
  viewCodes: 'http://127.0.0.1:5000/interviewer/code',//查看代码
  checkExamCode: 'http://127.0.0.1:5000/interviewer/check_code',//批改代码

  chatPage: 'http://127.0.0.1:5000/comment/comment_search',//查看评论列表
};


export default {
  state: {
    isLogin: false,
    userType: '',
  },
  getters: {
    //获取登录状态
    isLogin: state => state.isLogin,
    //获取用户类型
    userType: state => state.userType,
  },
  mutations: {
    //保存登录状态
    userStatus(state, flag) {
      state.isLogin = flag
    },
    //保存用户类型
    setUserType(state, flag) {
      state.userType = flag
    }
  },
  actions: {
    //登录状态
    setStatus({
      commit
    }, flag) {
      commit("userStatus", flag)
    },
    setType({
      commit
    }, flag) {
      commit("setUserType", flag)
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
    viewExamListRequest: ({
      state
    }, postData) => {
      return post(url.examList, postData);
    },
    viewQuestionRequest: ({
      state
    }, postData) => {
      return post(url.questionContent, postData);
    },
    viewQuestionListRequest:(state) =>{
      return get(url.questionLibrary);
    },
    addNewQuestionRequest:({
                               state
                             },postData) =>{
      return post(url.addNewQuestion,postData);
    },
    addNewExamRequest:({
      state
    },postData) => {
      return post(url.addNewExam,postData);
    },
    updateQuestionRequest:({
                         state
                       },postData) => {
      return post(url.updateQuestion,postData);
    },
    viewCodesRequest:({
                        state
                      },postData) => {
      return post(url.viewCodes,postData);
    },
    checkExamCodeRequest:({
                            state
                          },postData) => {
      return post(url.checkExamCode,postData);
    },

    discussRequest:({
                      state
                    },postData) => {
      return post(url.chatPage,postData);
    },

  }

}
