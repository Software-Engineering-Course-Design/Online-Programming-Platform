<template>
  <el-container id="tab">
    <el-header>题目详情页</el-header>
    <el-main>
      <question-details
        :p_id="q_id"
        :p_title="q_title"
        :p_content="q_content"
        :p_time="q_time"
      ></question-details>
    </el-main>
    <el-footer>
      <el-button type="info" @click="invite">邀请一位面试者来答题</el-button>
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
      q_id: 123,
      q_title: '我是题目',
      q_content: '我是题目内容',
      q_time: '我是时间',
    }
  },
  components:{
    questionDetails,
    updateQuestion
  },
  methods:{
    invite(){
      this.$router.push('./inviteToExam');
    },
    viewCodes(){
      this.$router.push('./viewQuestionCodeList');//需要传参
    },
    update(){
      this.$router.push({
        name: 'interviewerToUpdateQuestion',
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
