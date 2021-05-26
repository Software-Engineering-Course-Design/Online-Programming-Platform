<template>
  <el-container id="tab">
    <el-header>题目详情页</el-header>
    <el-main>
      <question-details></question-details>
    </el-main>
    <el-footer>
      <el-button type="info" @click="newExam">发起面试</el-button>
      <el-button type="info" @click="update">修改题目</el-button>
      <el-button type="info" @click="viewCodes">查看已提交代码</el-button>
    </el-footer>
  </el-container>
</template>

<script>
//by qzx
import questionDetails from "../components/questionDetails";
import updateQuestion from "./updateQuestion";
export default {
  data(){
    return{
      msg: "Updating the question!",
      q_title: '我是题目',
      q_content: '我是题目内容',
    }
  },
  components:{
    questionDetails,
    updateQuestion
  },
  methods:{
    newExam(){
      this.$router.push('./addNewExam');
    },
    viewCodes(){
      this.$router.push('./viewQuestionCodeList');//需要传参
    },
    update(){
      this.$router.push({
        name: 'interviewToUpdateQuestion',
        params: {
          id: '0000',
          title: this.q_title,
          content: this.q_content
        }
      })
    },
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";

</style>
