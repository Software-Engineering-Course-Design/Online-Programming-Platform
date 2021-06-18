<template>
  <el-container id="tab">
    <el-header><h1>在线编程平台</h1></el-header>
    <el-page-header @back="goBack" content="修改题目"></el-page-header>
    <el-main>
      <el-input v-model="heading"></el-input>
      <editor :p_content="content" @updateContent="getContent"></editor>
    </el-main>
    <el-footer>
      <el-form>
        <el-form-item>
          <el-button type="info" @click="submit">确认</el-button>
          <el-button  @click="goBack">返回</el-button>
        </el-form-item>
      </el-form>
    </el-footer>

  </el-container>
</template>

<script>
//by qzx
import editor from "../components/editor";
export default {
  data(){
    return{
      questionID:0,
      heading:'',
      content:'',
      info:[
        {
          name:'title',
          value:'',
        },
        {
          name:'content',
          value:'',
        },
      ],
      button:[ '修改', '修改'],
      active:[ false, false],
    }
  },
  created() {
    //this.info.splice(0,1,{name: 'id',value: this.$route.params.id});
    this.username = this.$route.params.username;
    this.questionID = this.$route.params.id;
    this.heading = this.$route.params.title;
    this.content = this.$route.params.content;
  },
  methods:{
    test(){
      console.log(this.content);
      console.log(this.questionID);
    },
    change(idx){
      if(this.button[idx]=='修改'){
        this.button.splice(idx, 1,'完成');
        this.active.splice(idx ,1,true);
      }
      else{
        this.button.splice(idx, 1,'修改');
        this.active.splice(idx ,1,false);
        console.log(this.info[idx].value);
      }
    },
    submit(){
      const postData = {
        "username": this.username,
        "questionID": this.questionID,
        "newHeading": this.heading,
        "newQuestion": this.content,
      }
      this.$store.dispatch('updateQuestionRequest', postData).then(res => {
        //console.log(postData);
        console.log(res);
      })
    },
    getContent(content){
      this.content=content;
    },
    goBack(){
      this.$router.back();
    },
  },
  components:{
    editor
  },
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
.open{
  background-color: #DCDFE6;
}
.el-main > div{
  border: 1px solid #DCDFE6;
  border-radius: 10px;
  margin: 20px;
  padding: 5px;
  font-size: 13px;
  height: auto;
}

.el-main >>> .el-button{
  position: absolute;
  right: 0;
}



</style>
