<template>
  <el-container id="tab">
    <el-header>面试批改页</el-header>
    <el-form ref="form" :model="form">
      <div v-for="(q, idx) in content" :key="idx">
      <el-form-item>
      <question-details
        :p_id="q.questionID"
        :p_title="q.heading"
        :p_content="q.question"
        p_time="我是时间test"></question-details>
        <el-select v-model="form.answerList[idx].value" placeholder="请选择">
          <el-option label="WA" value="WA"></el-option>
          <el-option label="AC" value="AC"></el-option>
        </el-select>
      </el-form-item>
      </div>
      <el-form-item>
        <el-button-group>
          <el-button @click="submit">完成</el-button>
          <el-button @click="reset">重置</el-button>
        </el-button-group>
      </el-form-item>
    </el-form>

  </el-container>

</template>

<script>
import QuestionDetails from "../components/questionDetails";
export default {
  name: "checkExam",
  components: {QuestionDetails},
  data(){
    return{
      form:{answerList:[]},
      id: '',//面试id
      examineeID: 123,//考生id
      content: [],//面试题信息数组
      //后端返回的面试题目列表

      //还应添加面试者id，此处假设是一位考生的一张试卷
    }
  },
  methods:{
    onStart(){
      const postData = {
        'username': this.username,
        //'sessionID': this.sessionID,
      };

    },
    submit(){
      console.log(this.form.answerList);
      this.$message({
        message: '批改完成',
        type: 'success'
      });
    },
    reset(){
      this.$refs.form.resetFields();
      console.log(this.form.answerList);
    }
  },
  created() {
    this.id = this.$route.params.id;//面试id
    console.log(this.id);
    this.content = this.$route.params.content;//面试题信息数组
    console.log(this.content);
    //this.onStart();
    for(let i=0; i<this.content.length; i++){
      this.form.answerList.push({  idx:this.content[i].questionID,  value:'unread'});
    }
    console.log(this.form.answerList);
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
