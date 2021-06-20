<template>
  <el-container id="tab">
    <el-header><h1>在线编程平台</h1></el-header>
    <el-page-header @back="goBack" :content="'第' + sessionID + '场面试批阅情况'"></el-page-header>
    <user-quit :username="username"></user-quit>
    <el-collapse v-model="activeName" accordion v-for="(q, idx) in detail" :key="idx">
      <el-collapse-item :title="q.heading" :name="idx">
        <question-details
          :p_id="q.uid"
          :p_title="q.heading"
          :p_content="q.content"></question-details>
        <el-container v-for="(code, idx2) in codeList" :key="idx2">
          <div v-if="code.questionID==q.uid">
            代码：<div>{{code.code}}</div>
            用户：<div>{{code.applicant}}</div>
          </div>
        </el-container>
      </el-collapse-item>
    </el-collapse>

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
      activeName:'1',
      username: '',
      sessionID: '',//面试id
      content: [],//面试题id数组
      detail: [],//后端返回的面试题目列表
      codeList: [],//代码列表
      id_arr:[],
    }
  },
  methods:{
    goBack(){
      this.$router.go(-1);
    },
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

      /*for(let i=0; i<this.content.length; i++){
      const postData = {
        'uid': this.content[i],
      };*/
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
            }
          });
        }
      });
    }

      /*this.$store.dispatch('viewQuestionRequest',postData).then(res => {
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

      });*/


    },
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
