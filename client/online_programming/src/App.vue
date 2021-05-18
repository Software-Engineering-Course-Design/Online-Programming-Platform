<template>
  <div id="app">
    <router-link to="/">
        Home
      </router-link>
      |
      <router-link to="/sign">登录注册</router-link>
      |
      <!-- <router-link to="/login">Login</router-link> -->
      
      <router-view></router-view>
      
  </div>
</template>

<script>
import Test from './components/Test.vue'

export default {
  components:{
    Test
  }
}
</script>

<style>
 body, html {
    margin: 0;
    height: 100%;
    width: 100%;
    background-size:cover;
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
