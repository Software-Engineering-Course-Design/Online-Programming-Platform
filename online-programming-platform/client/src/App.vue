<template>
  <div id="app">
    <!-- <router-link to="/home">Home</router-link>|
    <router-link to="/sign">登录注册</router-link>|
    <router-link to="/applicant">面试者首页</router-link>|
    <router-link to="/applicant/interview">面试模块</router-link>|
    <router-link to="/interviewer/addNewExam">发起面试</router-link>|
    <router-link to="/interviewer/viewExamList">面试官查看面试</router-link>
    <router-link to="/interviewer/addNewQuestion">新建题目</router-link>|
    <router-link to="/interviewer/viewQuestionDetails">题目详情</router-link>| -->
    <router-view></router-view>

  </div>
</template>

<script>
  export default {
    mounted() {
      window.addEventListener('unload', this.saveState);
    },
    methods: {
      saveState() {
        if (this.$cookies.get("LoginStatus") == 'isLogin') {
          this.$store.commit("userStatus", true);
        }
        if(this.$cookies.get("userType") == 'HR'){
          this.$store.commit("setUserType", true);
        }else if(this.$cookies.get("userType") == 'applicant'){
          this.$store.commit("setUserType", false);
        }
      }
    },
  }

</script>

<style>
  body,
  html {
    padding: 0px;
    margin: 0px;
    height: 100%;
    width: 100%;
    background-size: cover;
  }

  #app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /* text-align: center; */
    color: #2c3e50;
    margin-top: 60px;
  }

</style>
