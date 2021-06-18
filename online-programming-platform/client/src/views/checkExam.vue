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
      form:{answerList:[]},//存放批改结果
      sessionID: '',//面试id
      content: [],//面试题id数组
      detail: [],//后端返回的面试题目列表
      id_arr: [],//每道题面试者数组
      codeList: [],//代码列表
      result: [],//处理后的结果
    }
  },
  methods:{
    onStart(){
    },
    submit(){
      console.log(this.form.answerList);
      /*
      this.form.answerList.push({
              q_id: this.content[i],//面试题id
              u_id: this.id_arr[i][j],//面试者id
              value:'unread',
      });
      */
      //提交批改结果
      for(let i=0;i<this.form.answerList.length;i++){

      }
      const postData = {
        "username": this.username,
        "sessionID": this.sessionID,
        "result": this.result,
      }
      this.$store.dispatch('checkExamCodeRequest',postData).then(res => {
        console.log(res);
      })
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
    this.sessionID = this.$route.params.id;//面试id
    this.content = this.$route.params.content;//面试题信息数组，里面都是questionID
    /*
      content: [],//面试题id数组
      detail: [],//后端返回的面试题目列表
      id_arr: [],//面试者数组
      codeList: [],//代码列表
      */
    //请求题目信息
    for(let i=0; i<this.content.length; i++){
      const postData = {
        'uid': this.content[i],
      };
      this.$store.dispatch('viewQuestionRequest',postData).then(res => {
        //获取题目内容、用户id
        this.detail.push({
          uid: this.content[i],
          content: res.question,
        });
        this.id_arr.push(res.id_arr);
      });
    }
    for(let i=0;i<this.content.length;i++){
      let temp=[];
        for(let j=0;j<this.id_arr[i].length;j++){
          const postData2 = {
            "applicant": this.id_arr[i][j],
            "questionID" : this.content[i],
          }
          this.$store.dispatch('viewCodesRequest',postData2).then(res => {
            this.codeList.push({
              applicant: this.id_arr[i][j],
              questionID : this.content[i],
              code: res.code,
              result: res.result
            });
            this.form.answerList.push({
              q_id: this.content[i],//面试题id
              u_id: this.id_arr[i][j],//面试者id
              value:'unread',
            });
          });
        }
      }





    /*for(let i=0; i<this.content.length; i++){
      this.form.answerList.push({  idx:this.content[i],  value:'unread'});
    }
    console.log(this.form.answerList);*/
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
