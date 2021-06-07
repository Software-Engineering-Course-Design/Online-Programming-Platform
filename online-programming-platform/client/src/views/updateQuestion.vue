<template>
  <el-container id="tab">
    <el-header><h1>在线编程平台</h1></el-header>
    <el-page-header @back="goBack" content="修改题目"></el-page-header>
    <el-main>
      <div v-for="(item, idx) in info" :class="{ open:active[idx]}" :key="idx">
        <el-row type="flex" class="row-bg" justify="space-around">
          <div v-if="button[idx]=='完成'">
            <el-input v-model="item.value"></el-input>
          </div>
          <div v-else-if="button[idx]=='修改'">
            <el-col :span="16" :pull="2">{{ item.name }} : {{ item.value }}</el-col>
          </div>
          <el-col :span="4"><el-button @click="change(idx)" size="small"> {{ button[idx] }}</el-button></el-col>
        </el-row>
      </div>
    </el-main>
    <el-footer>
      <el-form>
        <el-form-item>
          <el-button type="info" @click="submit">确认</el-button>
          <el-button  @click="goBack">返回</el-button>
        </el-form-item>
      </el-form>
    </el-footer>

  </el-container>
</template>

<script>
//by qzx
export default {
  data(){
    return{
      info:[
        {
          name:'title',
          value:'',
        },
        {
          name:'content',
          value:'',
        },
      ],
      button:[ '修改', '修改'],
      active:[ false, false],
    }
  },
  created() {
    //this.info.splice(0,1,{name: 'id',value: this.$route.params.id});
    this.info.splice(0,1,{name: 'title',value: this.$route.params.title});
    this.info.splice(1,1,{name: 'content',value: this.$route.params.content});
  },
  methods:{
    change(idx){
      if(this.button[idx]=='修改'){
        this.button.splice(idx, 1,'完成');
        this.active.splice(idx ,1,true);
      }
      else{
        this.button.splice(idx, 1,'修改');
        this.active.splice(idx ,1,false);
        console.log(this.info[idx].value);
      }
    },
    submit(){

    },
    goBack(){
      this.$router.back();
    },
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
.open{
  background-color: #DCDFE6;
}
.el-main > div{
  border: 1px solid #DCDFE6;
  border-radius: 10px;
  margin: 20px;
  padding: 5px;
  font-size: 13px;
  height: auto;
}

.el-main >>> .el-button{
  position: absolute;
  right: 0;
}



</style>
