<template>
  <el-container id="tab">
    <el-header>查看面试页</el-header>
    <el-tabs @tab-click="">
      <el-tab-pane label="已批改面试" name="first">
        <exam-list :p_check="false"></exam-list>
      </el-tab-pane>
      <el-tab-pane label="待批改面试" name="second">
        <exam-list :p_check="true"></exam-list>
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

    }
  },
  methods:{
  },
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
