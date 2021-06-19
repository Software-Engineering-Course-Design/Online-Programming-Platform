<template>
  <el-container id="tab">
    <user-quit :username="username"></user-quit>
    <el-header><h1>在线编程平台</h1></el-header>
    <el-page-header @back="goBack" content="题库管理"></el-page-header>
    <el-main>
    <question-list :p_username="username" :p_qList="h_id_arr" :p_page-status="1"></question-list>
    </el-main>
  </el-container>
</template>

<script>
import questionList from "../components/questionList";
import UserQuit from "../components/UserQuit";
export default {
  name: "viewQuestionList",
  data(){
    return{
      username:'',
      h_id_arr:[],
    }
  },
  components:{
    questionList,
    UserQuit,
  },
  methods:{
    onStart() {
      const postData = {
        'username': this.username,
        //'sessionID': this.sessionID,
      };
      this.$store.dispatch('viewQuestionListRequest').then(res =>{
        //请求题目列表

        console.log(res);
        //处理后端传的数据
        this.h_id_arr = res.id_arr;
        //console.log(this.h_id_arr);
      });
    },
    goBack(){
      this.$router.go(-1);
    },
  },
  created() {
    this.username = this.$route.params.username;
  },
  mounted() {
    this.onStart();
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
