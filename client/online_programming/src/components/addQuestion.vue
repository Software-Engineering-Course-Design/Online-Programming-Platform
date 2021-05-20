<template>
  <el-container id="newQuestion">
    <el-header>
      <el-input v-model="q_title" placeholder="请输入题目标题"></el-input>
    </el-header>
    <!--<el-aside width="200px">
      <el-input v-model="q_keyWords" placeholder="请输入题目关键词"></el-input>
      <el-input v-model="q_forbiddenWords" placeholder="请输入不允许使用的关键词"></el-input>
    </el-aside>-->
    <el-main>
      <el-input v-model="q_content" placeholder="请输入题目描述"></el-input>
    </el-main>
  </el-container>
</template>

<script>
export default {
  data() {
    return{
      q_title: '',
      //q_keyWords: '',
      //q_forbiddenWords: '',
      q_content: ''
    }
  },
  methods:{

  }
}
</script>

<style scoped>

</style>
