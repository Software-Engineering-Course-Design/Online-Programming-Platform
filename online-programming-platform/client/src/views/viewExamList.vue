<template>
  <el-container id="tab">
    <el-header>查看面试页</el-header>
    <el-tabs @tab-click="">
      <el-tab-pane label="已批改面试" name="first">
        <exam-list :p_check="false" :p_e-list="eList"></exam-list>

      </el-tab-pane>
      <el-tab-pane label="待批改面试" name="second">
        <exam-list :p_check="true" :p_e-list="eList"></exam-list>
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
      eList: [],
    }
  },
  methods:{
    onStart(){
      const postData = {
        'username': this.username,
        'sessionID': this.sessionID,
      };
      this.$store.dispatch('viewExamListRequest',postData).then(res => {
        console.log(res);
        //处理后端传的数据
        var temp_elist = res.unread;
        console.log(temp_elist);
        for(var i=0;i<temp_elist.length;i++){
          this.eList.push({
              title: temp_elist[i].title,
              id: temp_elist[i].id,
              sessionTitle: temp_elist[i].sessionTitle,
              sessionID: temp_elist[i].sessionID,
              content: temp_elist[i].content,
              startTime: temp_elist[i].startTime,
              endTime: temp_elist[i].endTime,
              status: temp_elist[i].status,
          });
          console.log(this.eList);
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
