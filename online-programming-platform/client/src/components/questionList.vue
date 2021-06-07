<template>
  <div>
    <el-collapse v-for="(q,idx) in qList" v-model="activeName" accordion :key="idx">
      <el-collapse-item  :title="q.heading">
        <el-button @click="view(q.questionID)">查看题目{{q.questionID}}</el-button>
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
  name: "questionList",
  data(){
    return{
      activeName: '1',
      qList:this.p_qList

    }
  },
  methods:{
    view(id){
      this.$router.push({
        name: 'interviewerToQuestionDetails',
        params:{
          qID: id
        }
      })
    }
  },
  props:{
    p_qList: Array,
  },
}
</script>

<style scoped>

</style>
