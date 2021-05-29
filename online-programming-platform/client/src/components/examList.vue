<template>
  <div>
    <el-collapse v-for="(e, idx) in eList" v-model="activeName" accordion :key="idx">
      <el-collapse-item  :title="e.title">
        <div>{{e.time}}</div>
        <el-button v-if="check_flag==true" @click="check(e.id, idx)">批改</el-button>
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
      eList:[
        {
          title: '我是面试标题1',
          time: '我是时间1',
          id: 1,
        },
        {
          title: '我是面试标题2',
          time: '我是时间2',
          id: 2,
        },
        {
          title: '我是面试标题3',
          time: '我是时间3',
          id: 3,
        },
        {
          title: '我是面试标题4',
          time: '我是时间4',
          id: 4,
        },
        {
          title: '我是面试标题5',
          time: '我是时间5',
          id: 5,
        },
      ],
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
          title: that.eList[idx].title
        }
      });
    },
  },
  props:{
    p_check: Boolean,//true:显示批改按钮
  },
}
</script>

<style scoped>

</style>
