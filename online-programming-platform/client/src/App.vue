<template>
  <div id="app">
    <router-link to="/home">Home</router-link>|
    <router-link to="/sign">登录注册</router-link>|
    <router-link to="/applicant">面试者首页</router-link>|
    <router-link to="/applicant/interview">面试模块</router-link>|
    <router-link to="/interview/addNewQuestion">新建题目</router-link>|
    <router-link to="/interview/questionDetails">题目详情</router-link>|
    <router-link to="/interview/updateQuestion">修改题目</router-link>|

    <router-view></router-view>

  </div>
</template>

<script>
  import Test from './components/Test.vue'

  export default {
    components: {
      Test
    }
  }

</script>

<style>
  body,
  html {
    margin: 0;
    height: 100%;
    width: 100%;
    background-size: cover;
  }

  #app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

</style>
