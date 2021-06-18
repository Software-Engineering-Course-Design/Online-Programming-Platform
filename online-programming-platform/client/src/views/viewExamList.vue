<template>
  <el-container id="tab">
    <el-header><h1>在线编程平台</h1></el-header>
    <user-quit :username="username"></user-quit>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">面试情况</el-menu-item>
      <el-menu-item index="2" @click="toAddNewQuestion">新建题目</el-menu-item>
      <el-menu-item index="3" @click="toAddNewExam">发起新面试</el-menu-item>
      <el-menu-item index="4" @click="toViewQuestionList">查看题库</el-menu-item>
    </el-menu>

    <el-tabs>
      <el-tab-pane label="已批改面试" name="first">
        <exam-list :p_check="false" :p_e-list="readList"></exam-list>

      </el-tab-pane>
      <el-tab-pane label="待批改面试" name="second">
        <exam-list :p_check="true" :p_e-list="unreadList"></exam-list>
      </el-tab-pane>

    </el-tabs>
  </el-container>
</template>

<script>
import UserQuit from "../components/UserQuit";
import ExamList from "../components/examList";
import axios from "axios";
export default {
  name: "viewExamList",
  components: {
    UserQuit,
    ExamList
  },
  data(){
    return{
      activeIndex: '1',
      username: this.$cookies.get("username"),
      sessionID: '',
      unreadList: [],
      readList: [],
    }
  },
  methods:{

    onStart(){
      const postData = {
        'username': this.username,
        //'sessionID': this.sessionID,
      };
      this.$store.dispatch('viewExamListRequest',postData).then(res => {
        //处理后端传的数据
        const unread_eList = res.unread;
        const read_eList = res.read;

        for(let i=0; i<unread_eList.length; i++){
          this.unreadList.push({
              sessionID: unread_eList[i].sessionID,
              content: unread_eList[i].content,
              startTime: unread_eList[i].startTime,
              endTime: unread_eList[i].endTime,
          });
        }
        for(let j=0;j<read_eList.length; j++){
          this.readList.push({
            sessionID: read_eList[j].sessionID,
            content: read_eList[j].content,
            startTime: read_eList[j].startTime,
            endTime: read_eList[j].endTime,
          });
        }
      })
      // axios.post('http://127.0.0.1:5000/interviewer/interview_info',postData).then(function (response) {
      //   console.log(response);
      // })
      //   .catch(function (error) {
      //     console.log(error);
      //   });
    },
    handleSelect(key){
      console.log(key);
    },
    toAddNewQuestion(){
      this.$router.push({
        name:'interviewerToAddQuestion',
        params: {
          username: this.username
        },
      });
    },
    toAddNewExam(){
      this.$router.push({
        name:'interviewerToAddNewExam',
        params: {
          username: this.username
        },
      })
    },
    toViewQuestionList(){
      this.$router.push({
        name:'interviewerToViewQuestionList',
        params: {
          username: this.username
        },
      })
    }
  },
  mounted() {
    this.onStart();
  },
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
