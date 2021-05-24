<template>
  <el-container id="tab">
    <el-header>已提交代码列表</el-header>
    <el-main>
<!--此处使用element-ui折叠面板-->
      <div v-for="(code, idx) in codeList" :key="idx">
        用户id：{{code.id}}
        <el-button type="info" @click="viewThisCode(idx)">点击显示或折叠代码</el-button>
        <div v-show="code.currShowStatus==true">{{code.value}}</div>
      </div>
      <br />
      <chat></chat>
    </el-main>
    <el-footer> <el-button  @click="goBack">返回</el-button> </el-footer>

  </el-container>
</template>

<script>
//by qzx
import chat from "../components/chat";
export default {
  data(){
    return{
      codeList:[
        {
          id:"0000",
          value:"print('hello world0!')",
          currShowStatus:false,
        },
        {
          id:"0001",
          value:"print('hello world1!')",
          currShowStatus:false,
        },
        {
          id:"0002",
          value:"print('hello world2!')",
          currShowStatus:false,
        }
      ]
    }
  },
  methods:{
    viewThisCode(idx){
      this.codeList[idx].currShowStatus=!this.codeList[idx].currShowStatus;
    },
    goBack(){
      this.$router.back();
    }
  },
  components:{
    chat
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
