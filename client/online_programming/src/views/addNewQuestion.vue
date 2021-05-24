<template>
  <el-container id="tab">
    <el-header>新建题目页</el-header>
    <el-container>
      <el-aside width="150px">Aside</el-aside>
      <el-main>
        <el-input  v-model="q_title" placeholder="请输入题目标题"></el-input>
        <el-input  v-model="q_content" type="textarea" placeholder="请输入题目描述"></el-input>
        <el-form>
          <el-form-item>
            <el-button type="primary" @click="submit">立即创建</el-button>
            <el-button @click="cancel">取消</el-button>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
//by qzx
import axios from "axios";

export default {
  data() {
    return{
      q_title: '',
      //q_keyWords: '',
      //q_forbiddenWords: '',
      q_content: '',
    }
  },
  components: {

  },
  methods: {
    submit(){

    },
    cancel(){

    },
  }

}
</script>

<style scoped>
@import "../assets/qzx_css.css";
.el-main > .el-input{
  width: 90%;
  height: 60px;
}
/*修改inner要用>>>*/
.el-textarea >>> .el-textarea__inner{
  resize: none;
  height: 200px;
  width: 90%;
  margin: 0 auto;
}
.el-main > .el-button{
  margin: 20px auto auto;
}
.el-main > .el-form{
  margin-top: 20px;
}
</style>
