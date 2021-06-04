<template>
  <div>
    <el-collapse v-for="(e, idx) in eList" v-model="activeName" accordion :key="idx">
      <el-collapse-item  title="我是面试">
        <div>面试场次：{{e.sessionID}} </div>
        <el-button v-if="check_flag==true" @click="check(e.sessionID, idx)">批改</el-button>
      </el-collapse-item>
    </el-collapse>
    <el-pagination
      small
      layout="prev, pager, next"
      :total="50">
    </el-pagination>

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
    }
  },
  methods:{

    check(eID, idx){
      const that = this;
      this.$router.push({
        name: 'interviewerToCheckExam',
        params: {
          id: eID,
          content: that.eList[idx].content
        }
      });
    },
  },
  props:{
    p_check: Boolean,//true:显示批改按钮
    p_eList: Array,
  },
}
</script>

<style scoped>

</style>
