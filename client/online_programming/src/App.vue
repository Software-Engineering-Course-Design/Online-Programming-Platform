<template>
  <div>
    <router-link to="/">
        Home
      </router-link>
      |
      <router-link to="/login">Login</router-link>
      |
      <router-link to="/register">register</router-link>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {

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
