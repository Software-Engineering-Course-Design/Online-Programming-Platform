<template>
  <el-container id="tab">
    <el-header>查看面试页</el-header>
    <el-tabs @tab-click="">
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
import ExamList from "../components/examList";
export default {
  name: "viewExamList",
  components: {
    ExamList
  },
  data(){
    return{
      username: 'testusr',
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
        console.log(res);
        //处理后端传的数据
        const unread_eList = res.unreadList;
        const read_eList = res.readList;

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
    },
  },
  mounted() {
    this.onStart();
  },
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
