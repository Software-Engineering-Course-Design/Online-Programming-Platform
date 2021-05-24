<template>

    <div>
        <div id="whole" v-if="loginState">
      <router-view></router-view>
    </div>
    <div v-else id="loginTab">
      <div class="tab-title">
        <div :class="{'active': tab1State}" v-text="tabs[0]" @click="switchTab(tabs[0])"></div>
        <div :class="{'active': tab2State}" v-text="tabs[1]" @click="switchTab(tabs[1])"></div>
      </div>
      <div class="tab-content">
        <component :is="tabsContent" :login-state="loginState" @change-login-state="changeLoginState"></component>
      </div>   
    </div>
    

  </div>
</template>

<script>
  import login from "../components/Login.vue"
  import signup from "../components/Signup.vue"
  export default {
    data() {
      return {
        
        loginState: false,
        tabs: ["login", "signup"],
        tabsContent: "login",
        tab1State: true, //登录页面显示
        tab2State: false, //注册页面关闭

      }
    },
    components: {
      login,
      signup,
    },
    methods: {
      switchTab(tabName) {
        this.tabsContent = tabName;
        if (tabName === "login") {
          this.tab1State = true;
          this.tab2State = false;
        } else {
          this.tab1State = false; //登录页面关闭
          this.tab2State = true; //注册页面显示
        }
      },
      changeLoginState(b) {
        this.loginState = b;
      },
      
    }
  }

</script>

<style>
  #whole {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #loginTab {
    width: 60%;
    height: 70%;
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    margin: auto;
    box-shadow: 0 0 10px 2px darkgray;
    border-radius: 3px;
  }

  .tab-title {
    width: 100%;
    height: 50px;
    /*border-bottom: 1px #242424 solid;*/
    font-size: 16px;
    background-color: rgba(207, 237, 200, 0.71);
  }

  .tab-title>div {
    float: left;
    width: 50%;
    height: 50px;
    text-align: center;
    line-height: 50px;
    color: #868085;
    cursor: pointer;
    user-select: none;
    text-transform: capitalize;
  }

  .tab-title>div:first-child {
    border-radius: 3px 0 0 0;
  }

  .tab-title>div:last-child {
    border-radius: 0 3px 0 0;
  }

  .active {
    background-color: #5093d2;
    color: white !important;
    font-size: 16px !important;
    text-transform: uppercase !important;
  }

</style>
