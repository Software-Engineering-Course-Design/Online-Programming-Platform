<template>
  <div>
    <el-collapse v-for="(e, idx) in eList" v-model="activeName" accordion :key="idx">
      <el-collapse-item  :title="'第' + e.sessionID + '场面试'">
        <div>面试场次：{{e.sessionID}} </div>
        <el-button v-if="check_flag==true" @click="check(e.sessionID, idx)">批改</el-button>
        <el-button v-if="check_flag==false" @click="view(e.sessionID, idx)">查看详情</el-button>
      </el-collapse-item>
    </el-collapse>


  </div>
</template>

<script>
export default {
  name: "examList",
  data(){
    return{
      activeName: '1',
      eList: this.p_eList,
      check_flag:this.p_check,
      username:this.p_username,
    }
  },
  methods:{
    view(eID,idx){
      const that = this;
      this.$router.push({
        name: 'interviewerToViewExamChecked',
        params: {
          id: eID,
          content: that.eList[idx].content,
          username: that.username,
        }
      });
    },
    check(eID, idx){
      const that = this;
      this.$router.push({
        name: 'interviewerToCheckExam',
        params: {
          id: eID,
          content: that.eList[idx].content,
          username: that.username,
        }
      });
    },
  },
  props:{
    p_check: Boolean,//true:显示批改按钮
    p_eList: Array,
    p_username: String,
  },
}
</script>

<style scoped>

</style>
