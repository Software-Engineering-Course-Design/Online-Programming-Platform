<template>
  <div>
  <el-row type="flex" justify="center">
    <el-col :span="6">
      <div class="grid-content"></div>
    </el-col>
  </el-row>
    <p>新建题目页</p>
    <add-question></add-question>
  </div>
</template>

<script>
import addQuestion from "../components/addQuestion";
export default {
  data(){
    return{

    }
  },
  components: {
    addQuestion
  }

}
</script>

<style scoped>

</style>
