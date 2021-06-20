<template>
  <el-container id="tab">
    <el-header><h1>在线编程平台</h1></el-header>
    <el-page-header @back="goBack" content="已提交代码面试者列表"></el-page-header>
    <el-main>
<!--此处使用element-ui折叠面板-->
      <el-collapse v-model="activeName" accordion>
        <div v-for="(code, idx) in codeList" :key="idx">
          <el-collapse-item :title="code.id" :name="idx">
            用户id：{{code.id}}<br />
            用户提交代码：{{code.value}}<br />
            批改结果：{{code.result}}
          </el-collapse-item>
        </div>
      </el-collapse>
      <br />
      <chat :p_username="username" :p_question-i-d="questionID" :p_user-type="userType"></chat>
    </el-main>
    <el-footer> <el-button  @click="goBack">返回</el-button> </el-footer>

  </el-container>
</template>

<script>
//by qzx
import chat from "../components/chat";
export default {
  data(){
    return{
      activeName: '',
      username: '',
      questionID:'',
      userType:true,
      id_applicant:[],
      codeList:[],/*[
        {
          id:"0000",
          value:"print('hello world0!')",
          currShowStatus:false,
        },
        {
          id:"0001",
          value:"print('hello world1!')",
          currShowStatus:false,
        },
        {
          id:"0002",
          value:"print('hello world2!')",
          currShowStatus:false,
        }
      ],*/

    }
  },
  methods:{
    onStart(){
      //viewQuestionCodeListRequest
      const postData = {
        "questionID": this.questionID,
      }
      this.$store.dispatch('viewQuestionCodeListRequest',postData).then(res=>{
        console.log(res);
        /*{
          id:"0000",
          value:"print('hello world0!')",
          currShowStatus:false,
        },*/
        const temp=JSON.parse(JSON.stringify(res.info));
        for(let i=0; i<temp.length; i++){
          this.codeList.push({
            id: temp[i].applicant,
            value: temp[i].code,
            currShowStatus:false,
            result: temp[i].result,
          })
        }

      })
    },
    goBack(){
      this.$router.back();
    }
  },
  components:{
    chat
  },
  created() {
    this.username=this.$route.params.username;
    this.questionID=this.$route.params.q_id;
    this.id_applicant=this.$route.params.id_applicant;
    /*username: '',
      questionID:'',
      userType:'',*/
  },
  mounted() {
    this.onStart();
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
