<template>
  <el-container id="tab">
    <user-quit :username="username"></user-quit>
    <el-header>面试批改页</el-header>
    <el-form ref="form" :model="form">
      <div v-for="(q, idx) in detail" :key="idx">
      <el-form-item>
        <question-details
        :p_id="q.uid"
        :p_title="q.heading"
        :p_content="q.content"></question-details>
        <div v-for="(code, idx2) in codeList" :key="idx2">
          <div v-if="code.questionID==q.uid">
            <div>code:{{code.code}}</div>
            <div>applicant:{{code.applicant}}</div>
            <el-select v-model="form.answerList[idx2].value" placeholder="请选择">
              <el-option label="WA" value="WA"></el-option>
              <el-option label="AC" value="AC"></el-option>
            </el-select>
          </div>

        </div>
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
<!--
 /*
    this.detail.push({
          uid: this.content[i],
          heading: res.heading,
          content: res.question,
        });
    this.codeList.push({
                applicant: this.id_arr[i][j],//面试者id
                questionID : this.content[i],//面试题id
                code: res2.code,//代码
                result: res2.result//结果
              });
   this.form.answerList.push({
                applicant: this.id_arr[i][j],//面试者id
                questionID: parseInt(this.content[i]),
                value:'unread',
              });
    */
-->


<script>
import QuestionDetails from "../components/questionDetails";
import UserQuit from "../components/UserQuit";
export default {
  name: "checkExam",
  components: {QuestionDetails, UserQuit},
  data(){
    return{
      username: '',
      form:{answerList:[]},//存放批改结果
      sessionID: '',//面试id
      content: [],//面试题id数组
      detail: [],//后端返回的面试题目列表
      id_arr: [],//每道题面试者数组
      codeList: [],//代码列表
    }
  },
  methods:{
    onStart(){
    },
    submit(){
      const postData = {
        "username": this.username,
        "sessionID": this.sessionID,
        "result": this.form.answerList,
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
    this.username = this.$route.params.username;

    //请求题目信息
    for(let i=0; i<this.content.length; i++){
      const postData = {
        'uid': this.content[i],
      };
      console.log('test',i);
      this.$store.dispatch('viewQuestionRequest',postData).then(res => {
        //获取题目内容、用户id
        this.detail.push({
          uid: parseInt(this.content[i]),
          heading: res.heading,
          content: res.question,
        });
        this.id_arr.push(res.id_arr);//第一个元素：对应题目id在content中的索引，第二个元素：面试者id的索引
        console.log(this.id_arr,'idarr',i,'i');
        for(let j=0;j<this.id_arr[i].length;j++){
          const postData2 = {
            "applicant": this.id_arr[i][j],
            "questionID": this.content[i],
            "sessionID": this.sessionID,
          }
          this.$store.dispatch('viewCodesRequest',postData2).then(res2 => {
            if(res2.hasOwnProperty('code')){
              this.codeList.push({
                applicant: this.id_arr[i][j],//面试者id
                questionID :  parseInt(this.content[i]),
                code: res2.code,//代码
                result: res2.result//结果
              });
              this.form.answerList.push({
                applicant: this.id_arr[i][j],//面试者id
                questionID: parseInt(this.content[i]),
                value:'unread',
              });
            }

          });
        }
      });
    }

    //console.log(this.id_arr, "id_arr");
    //console.log(this.form.answerList, "answerList");
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
