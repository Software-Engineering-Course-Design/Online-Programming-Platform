<template>
  <el-container id="tab">
    <el-header><h1>在线编程平台</h1></el-header>
    <user-quit :username="username"></user-quit>
      <el-page-header @back="goBack" content="新建题目页"></el-page-header>
      <el-main>
        <el-form>
          <el-form-item>
            <el-input  v-model="q_title" placeholder="请输入题目标题"></el-input>
          </el-form-item>
          <el-form-item>
            <el-input v-model="q_answer" placeholder="请输入正确答案"></el-input>
          </el-form-item>
          <div>
          <editor :p_content="q_content" @updateContent="getContent" style=""></editor>
          <el-form-item>
            <el-button type="primary" @click="submit">立即创建</el-button>
            <el-button @click="cancel">取消</el-button>
          </el-form-item>
          </div>
        </el-form>
      </el-main>


  </el-container>
</template>

<script>
//by qzx
import editor from "../components/editor";
import UserQuit from "../components/UserQuit";
export default {
  data() {
    return{
      username: '',
      q_title: '',
      q_content: '',
      q_answer: '我是答案',
    }
  },
  components: {
    editor,
    UserQuit,

  },
  methods: {
    goBack(){
      this.$router.go(-1);
    },
    getContent(content){
      this.q_content=content;
      console.log(this.q_content);
    },
    test(){
      console.log(this.q_content);
    },
    submit(){
      const temp_q = {
        username: this.username,
        heading: this.q_title,
        question: this.q_content,
        answer: this.q_answer,
      };
      const postData = {
        "username": this.username,
        "heading": this.q_title,
        "question": this.q_content,
        "answer": this.q_answer,
      };
      console.log(postData);
      this.$store.dispatch('addNewQuestionRequest',postData).then(res => {
        console.log(res);
      })
    },
    cancel(){

    },

  },
  created() {
    this.username = this.$route.params.username;
  },

}
</script>

<style scoped>
@import "../assets/qzx_css.css";
.el-main > .el-input{
  width: 90%;
  height: 60px;
}
/*修改inner要用>>>*/
.el-textarea >>> .el-textarea__inner{
  resize: none;
  height: 200px;
  width: 90%;
  margin: 0 auto;
}

.el-main > .el-button{
  margin: 20px auto auto;
}
.el-main > .el-form{
  margin-top: 20px;
  position: relative;
  top: 30%;
}
</style>
