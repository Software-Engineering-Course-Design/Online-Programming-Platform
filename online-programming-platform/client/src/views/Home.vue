<template>
  <div class="home">
    <logout></logout>
    <img alt="Vue logo" src="../assets/logo.png">
    <p>
      If Element is successfully added to this project, you'll see an
      <code v-text="'<el-button>'"></code>
      below
    </p>
    <el-button @click="testClick">{{msg}}</el-button>
    

  </div>
</template>

<script>
//import Logout from "../components/Logout.vue"
import logout from "../components/UserQuit.vue"
  export default {
    components: {
      logout
    },
    data() {
      return {
        msg: '1111',
      };
    },
    methods: {
      testClick() {
        let obj = {
          name: '444',
          age:'18',
        }
        // this.$store.dispatch('testget', obj).then(res=>{
        //   console.log(res);
        // })
        let getFlag = this.$cookies.get("LoginStatus");
        this.msg = getFlag;
      }
    },

  }

</script>
<style>

</style>
