<template>
  <div>
    <el-collapse v-for="(item, idx) in qList" v-model="activeName" accordion :key="idx">
      <el-collapse-item  :title="item[1]">
        <el-button @click="view(item[0],idx)">查看题目{{item[0]}}</el-button>
        <el-button v-if="p_pageStatus==2" @click="add(item[0],idx)">选择</el-button>
      </el-collapse-item>
    </el-collapse>
    <!--<el-pagination
      small
      layout="prev, pager, next"
      :total="50">
    </el-pagination>-->
  </div>
</template>

<script>
export default {
  name: "questionList",
  data(){
    return{
      activeName: '1',
      username: '',
      qList:'',
      sList:[],//选中题号的数组
      pageStatus: this.p_pageStatus,//1:显示查看题目 2:显示选中
    }
  },
  methods:{
    view(id,idx){
      this.$router.push({
        name: 'interviewerToQuestionDetails',
        params:{
          username: this.username,
          qID: id,
          title: this.qList[idx][1],
        }
      })
    },
    add(id,idx){
      this.sList.push(id);
      this.$emit('updateQuestionList',this.sList);
      console.log(this.sList);
    },
  },
  mounted() {

  },
  props:{
    p_qList: Array,
    p_pageStatus: Number,
  },
  created() {
    this.qList = this.p_qList;
  },
  watch: {
    p_qList(val) {
      this.qList = val;
    }
  },
}
</script>

<style scoped>

</style>
