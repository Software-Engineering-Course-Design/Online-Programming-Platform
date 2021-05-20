<template>
  <div>
    <el-row type="flex" justify="center">
      <el-col :span="6">
        <div class="grid-content"></div>
      </el-col>
    </el-row>
    <p>题目详情页</p>
    <question-details></question-details>
  </div>
</template>

<script>
import questionDetails from "../components/questionDetails";
export default {
  data(){
    return{

    }
  },
  components:{
    questionDetails
  }
}
</script>

<style scoped>

</style>
