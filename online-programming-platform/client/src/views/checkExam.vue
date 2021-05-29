<template>
  <el-container id="tab">
    <el-header>面试批改页</el-header>
    <el-form ref="form" :model="form">
      <div v-for="(q, idx) in qList" :key="idx">
      <el-form-item>
      <question-details
        :p_id="q.id"
        :p_title="q.title"
        :p_content="q.content"
        :p_time="q.time"></question-details>
        <el-select v-model="form.answerList[idx].value" placeholder="请选择">
          <el-option label="WA" value="WA"></el-option>
          <el-option label="AC" value="AC"></el-option>
        </el-select>
      </el-form-item>
      </div>
      <el-form-item>
        <el-button-group>
          <el-button @click="submit">完成</el-button>
          <el-button @click="reset">重置</el-button>
        </el-button-group>
      </el-form-item>
    </el-form>

  </el-container>

</template>

<script>
import QuestionDetails from "../components/questionDetails";
export default {
  name: "checkExam",
  components: {QuestionDetails},
  data(){
    return{
      form:{answerList:[]},
      id: '',//面试id
      title: '',//面试标题
      //后端返回的面试题目列表
      qList:[
        {
          title: '我是标题1',
          time: '我是时间1',
          content: '我是题目内容1',
          id: 1,
        },
        {
          title: '我是标题2',
          time: '我是时间2',
          content: '我是题目内容2',
          id: 2,
        },
        {
          title: '我是标题3',
          time: '我是时间3',
          content: '我是题目内容3',
          id: 3,
        },
        {
          title: '我是标题4',
          time: '我是时间4',
          content: '我是题目内容4',
          id: 4,
        },
        {
          title: '我是标题5',
          time: '我是时间5',
          content: '我是题目内容5',
          id: 5,
        },
      ],

      //还应添加面试者id，此处假设是一位考生的一张试卷
    }
  },
  methods:{
    submit(){
      console.log(this.form.answerList);
      this.$message({
        message: '批改完成',
        type: 'success'
      });
    },
    reset(){
      this.$refs.form.resetFields();
      console.log(this.form.answerList);
    }
  },
  created() {
    this.id = this.$route.params.id;
    this.title = this.$route.params.title;
    for(let i=0; i<this.qList.length; i++){
      this.form.answerList.push({  idx:this.qList[i],  value:'unread'});
    }
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
