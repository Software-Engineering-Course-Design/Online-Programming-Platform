<template>
  <el-container id="tab">
    <user-quit :username="username"></user-quit>
    <el-header><h1>在线编程平台</h1></el-header>
    <el-page-header @back="goBack" content="当前题目详情"></el-page-header>
    <el-main>
      <question-details
        :p_id="q_id"
        :p_title="q_title"
        :p_content="q_content"
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
import UserQuit from "../components/UserQuit";

export default {
  data(){
    return{
      msg: "Updating the question!",
      username:'',
      q_id: '',//从上一个页面中route获取
      //向后端请求返回
      q_title: '',
      q_content: '',
      id_applicant: [],
      /*
      username
      questionID
      heading
      question
      id_arr
      * */
    }
  },
  components:{
    UserQuit,
    questionDetails,
    updateQuestion,
  },
  methods:{
    goBack(){
      this.$router.go(-1);
    },
    onStart(){
      //console.log(this.q_id);
      const postData = {
        'uid': this.q_id,
      };
      this.$store.dispatch('viewQuestionRequest',postData).then(res => {
        console.log(res);
        this.q_title = res.heading;
        this.q_content = res.question;
        this.id_applicant = res.id_arr;
      });
    },
    invite(){
      this.$router.push({
        name:'interviewerToInvite',
        params:{
          q_id:this.q_id
        }
      });
    },
    viewCodes(){
      this.$router.push({
        name:'interviewerToViewQuestionCodeList',
        params:{
          q_id:this.q_id,
          id_applicant:this.id_applicant,//提交了代码的面试者数组
          username: this.username,
        }
      });//需要传参
    },
    update(){
      this.$router.push({
        name: 'interviewerToUpdateQuestion',
        params: {
          id: this.q_id,
          title: this.q_title,
          content: this.q_content
        }
      })
    },
  },
  created(){
    this.q_id = parseInt(this.$route.query.qID);
    this.q_title = this.$route.query.title;
    this.username = this.$route.query.username;
  },
  mounted(){

    this.onStart();
  }

}
</script>

<style scoped>
@import "../assets/qzx_css.css";

</style>
