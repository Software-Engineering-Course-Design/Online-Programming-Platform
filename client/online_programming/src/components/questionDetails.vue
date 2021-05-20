<template>
  <el-container>
    <el-header>题目名称：{{ q_title }}</el-header>
    <el-main>题目内容：{{ q_content }}</el-main>
  </el-container>
</template>

<script>
export default {
  data(){
    return{
      q_title: '我是题目',
      q_content: '我是题目内容',
    }
  },
}
</script>

<style scoped>

</style>
