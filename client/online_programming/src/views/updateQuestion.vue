<template>
  <div>
    <el-button type="primary" @click="hello">修改题目</el-button>
    <el-button type="primary" @click="viewCodes">查看已提交代码</el-button>
  </div>
</template>

<script>
export default {
  data(){
    return{
      msg:"Updating the question!"
    }
  },
  methods:{
    hello(){
      console.log(this.msg);
    },
    viewCodes(){

    }
  }
}
</script>

<style scoped>

</style>
