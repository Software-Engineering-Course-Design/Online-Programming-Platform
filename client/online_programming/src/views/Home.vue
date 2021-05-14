<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <p>
      If Element is successfully added to this project, you'll see an
      <code v-text="'<el-button>'"></code>
      below
    </p>
    <el-button>el-button</el-button>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'home',
  components: {
    HelloWorld
  }
//   template: '<HelloWorld/>'
}
</script>
<style>

</style>
