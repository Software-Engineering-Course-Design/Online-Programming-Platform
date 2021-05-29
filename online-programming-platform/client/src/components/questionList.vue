<template>
  <div>
    <el-collapse v-for="q in qList" v-model="activeName" accordion :key="q.id">
      <el-collapse-item  :title="q.title">
        <div>{{q.time}}</div>
        <a href="/interviewer/viewQuestionDetails">{{q.title}}</a>
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
      qList:[
        {
          title: '我是标题1',
          time: '我是时间1',
          id: 1,
        },
        {
          title: '我是标题2',
          time: '我是时间2',
          id: 2,
        },
        {
          title: '我是标题3',
          time: '我是时间3',
          id: 3,
        },
        {
          title: '我是标题4',
          time: '我是时间4',
          id: 4,
        },
        {
          title: '我是标题5',
          time: '我是时间5',
          id: 5,
        },
      ],

    }
  },

}
</script>

<style scoped>

</style>
