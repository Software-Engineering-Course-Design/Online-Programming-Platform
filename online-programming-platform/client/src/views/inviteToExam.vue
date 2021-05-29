<template>
  <el-container id="tab">
    <el-header>邀请页</el-header>
    <el-main>
      <new-exam :prop_num="num" :prop_type="type" :prop_q-i-d="qID"></new-exam>
    </el-main>
  </el-container>
</template>

<script>
//by qzx
import newExam from "../components/newExam"
export default {
  name: "inviteToExam",
  data(){
    return{
      num: 1,
      type: '自主选题',
      qID: ['0001'],
    }
  },
  components:{
    newExam
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";

</style>
