<template>
  <el-container>
    <el-header>题目名称：{{ title }}</el-header>
    <el-main>
      <div>题目id：{{ id }}</div>
      <div>题目内容：</div>
      <div v-html="content"></div>
      <div>时间： {{ time}}</div>
    </el-main>
  </el-container>
</template>

<script>
//by qzx - component
export default {
  data(){
    return{
      id: this.p_id,
      title: this.p_title,
      content: this.p_content,
      time: this.p_time,
    }
  },
  props:{
    p_id: Number,
    p_title: String,
    p_content: String,
    p_time: String
  }
}
</script>

<style scoped>
.el-container{
  overflow: auto;
}
</style>
