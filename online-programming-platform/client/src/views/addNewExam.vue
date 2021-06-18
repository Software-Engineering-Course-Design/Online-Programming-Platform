<template>
  <el-container id="tab">
    <el-alert
      :title="msg"
      type="info"
      effect="dark"
      v-show="showMsg==true">
    </el-alert>

    <user-quit :username="username"></user-quit>
    <el-header><h1>在线编程平台</h1></el-header>
    <el-page-header @back="goBack" content="发起面试页">
    </el-page-header>
    <el-main>
      <el-form ref="form" :model="form" :rules="rules">
        <el-form-item label="请选择题目数量" prop="num" required>
          <el-radio-group v-model="form.num">
            <el-radio-button v-for="n in 5" :label="n" :key="n"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="请选择出题类型" prop="type" required>
          <el-radio-group v-model="form.type">
            <el-radio-button v-for="(item,index) in options" :label="item.value" :key="index"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <div v-if="form.type=='自主选题'">
          <div>
            已选择的题号：{{selectedQ}}
          </div>
          <question-list :p_qList="h_id_arr" :p_page-status="2" @updateQuestionList="selectQuestionList"></question-list>

        </div>

        <el-form-item label="请选择起止时间" required>
            <el-form-item prop="time1">
              <el-date-picker type="date" placeholder="选择日期" v-model="form.time1"
              value-format="yyyy-MM-dd"
              ></el-date-picker>
            </el-form-item>
<!--
            <el-form-item prop="time2">
              <el-time-picker placeholder="选择时间" v-model="form.time2"></el-time-picker>
            </el-form-item>
-->
            <el-form-item prop="time2">
              <el-time-picker
                is-range
                v-model="form.time2"
                range-separator="至"
                start-placeholder="开始时间"
                end-placeholder="结束时间"
                placeholder="选择时间范围">
              </el-time-picker>
            </el-form-item>

        </el-form-item>

        <el-form-item label="请输入要邀请的面试者ID" prop="people">
          <el-input v-model="form.people">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submit">发起面试</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
    </el-main>
  </el-container>
</template>

<script>
import UserQuit from "../components/UserQuit";
import questionList from "../components/questionList";
//by qzx
export default {
  name: "addNewExam",

  components:{
    UserQuit,
    questionList
  },
  data(){
    return{
      form: {
        num: 'null',
        type: -1,
        time1: '',
        time2: '',
        people:'abc',
        qArr:[1,2],
      },
      username: '',
      h_id_arr:[],
      selectedQ:[],
      showMsg: false,
      msg:'',
      rules:{
        num:[
          { type:'number', require: true, message: '请选择题目数量'},
        ],
        type:[
          { type:'string', require: true, message: '请选择出题方式'},
        ],
        time1: [
          { required: true, message: '请选择日期', trigger: 'change' }
        ],
        time2: [
          { type: 'array', required: true, message: '请选择时间', trigger: 'change' }
        ],
        people: [
          { message: '请输入面试者id', trigger: 'blur'}
        ]

      },
      options:[
        { value: '自主选题'},
        { value: '随机抽题'}
      ]
    }
  },
  methods:{
    test(){
      console.log(this.selectedQ);
    },
    goBack(){
      this.$router.go(-1);
    },
    submit(){
      //console.log(this.form);
      this.$refs.form.validate((valid) => {

        if(valid){
          console.log('submit!');
          var temp = this.form.type;
          if(temp=='自主命题'){
            temp = true;
          }
          else{
            temp = false;
          }
          const startTime = this.form.time1 + ' ' + this.form.time2[0].getHours().toString() + ':' + this.form.time2[0].getMinutes().toString() + ':' + this.form.time2[0].getSeconds().toString();
          const endTime = this.form.time1 + ' ' + this.form.time2[1].getHours().toString() + ':' + this.form.time2[1].getMinutes().toString() + ':' + this.form.time2[1].getSeconds().toString();

          const postData = {
            "username": this.username,
            "applicant": [this.form.people],
            "questionNumber": this.form.num,
            "questionID": this.selectedQ,
            "createWay": temp,
            "startTime": startTime,
            "endTime": endTime
          };
          this.$store.dispatch('addNewExamRequest', postData).then(res => {
            //console.log(postData);
            console.log(res);
          })
        }
        else {
          console.log('error!');
          return false;
        }
      });
    },
    reset(){
      this.$refs.form.resetFields();
    },
    selectQuestionList(list){
      this.selectedQ = list;
      console.log(this.selectedQ);
      //题号
    }
  },
  created() {
    this.username = this.$route.params.username;
  },
  mounted() {
    this.$store.dispatch('viewQuestionListRequest').then(res =>{
      //请求题目列表
      console.log(res);
      //处理后端传的数据
      this.h_id_arr = res.id_arr;
      //console.log(this.h_id_arr);
    });
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
