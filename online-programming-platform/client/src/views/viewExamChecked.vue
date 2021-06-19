<template>
  <el-container id="tab">
    <user-quit :username="username"></user-quit>
    <el-header>面试{{ sessionID }}批阅情况</el-header>
      <div v-for="(q, idx) in detail" :key="idx">
        <question-details
            :p_id="q.uid"
            :p_title="q.heading"
            :p_content="q.content"></question-details>
        <div v-for="(code, idx2) in codeList" :key="idx2">
          <div v-if="code.questionID==q.uid">
            <div>code:{{code.code}}</div>
            <div>applicant:{{code.applicant}}</div>
              {{answerList[idx2].value}}
          </div>
        </div>
      </div>
  </el-container>
</template>

<script>
import QuestionDetails from "../components/questionDetails";
import UserQuit from "../components/UserQuit";
export default {
  name: "checkExam",
  components: {QuestionDetails, UserQuit},
  data(){
    return{
      username: '',
      sessionID: '',//面试id
      content: [],//面试题id数组
      detail: [],//后端返回的面试题目列表
      codeList: [],//代码列表
    }
  },
  methods:{
  },
  created() {
    this.sessionID = this.$route.params.id;//面试id
    this.content = this.$route.params.content;//面试题信息数组，里面都是questionID
    this.username = this.$route.params.username;
    //console.log(this.username,'username');
    //请求题目信息
    for(let i=0; i<this.content.length; i++){
      const postData = {
        'uid': parseInt(this.content[i]),
      };
      this.$store.dispatch('viewQuestionRequest',postData).then(res => {
        console.log(res,'res');
        //获取题目内容、用户id
        this.detail.push({
          uid: parseInt(this.content[i]),
          heading: res.heading,
          content: res.question,
        });
        const postData2 = {
          "questionID": parseInt(this.content[i]),
        }
        this.$store.dispatch('viewQuestionCodeListRequest',postData2).then(res2 => {
          console.log(res2,'res2');
          this.codeList.push({
            code:res2.code,
            applicant:res2.applicant,
            result:res2.result,
          })
          console.log(this.codeList, "codeList");
        });

      });


    }

    //console.log(this.form.answerList, "answerList");
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
