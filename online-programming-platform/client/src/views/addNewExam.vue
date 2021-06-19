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
        <!--<el-form-item label="请选择出题类型" prop="type" required>
          <el-radio-group v-model="form.type">
            <el-radio-button v-for="(item,index) in options" :label="item.value" :key="index"></el-radio-button>
          </el-radio-group>
        </el-form-item>-->
        <div>
          <div>
            已选择的题号：
          </div>
          <el-tag v-for="(selection, idx) in selectedQ" :key="idx" closable @close="handleClose(idx)">
            {{selection}}
          </el-tag>
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



        <el-tag
          :key="tag"
          v-for="tag in dynamicTags"
          closable
          :disable-transitions="false"
          @close="handleDeletePeople(tag)">
          {{tag}}
        </el-tag>
        <el-input
          class="input-new-tag"
          v-if="inputVisible"
          v-model="inputValue"
          ref="saveTagInput"
          size="small"
          @keyup.enter.native="handleInputConfirm"
          @blur="handleInputConfirm"
        >
        </el-input>
        <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>


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
        //type: -1,
        time1: '',
        time2: '',
        people:[],
        qArr:[1,2],
      },
      username: '',
      h_id_arr:[],
      selectedQ:[],
      showMsg: false,
      msg:'',
      dynamicTags: [],
      inputVisible: false,
      inputValue: '',

      rules:{
        num:[
          { type:'number', require: true, message: '请选择题目数量'},
        ],
        //type:[
        //  { type:'string', require: true, message: '请选择出题方式'},
        //],
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
    }
  },
  methods:{
    test(){
      console.log(this.selectedQ);
    },
    goBack(){
      this.$router.go(-1);
    },
    handleClose(idx){
      this.selectedQ.splice(idx,1);
    },
    //删除面试者
    handleDeletePeople(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },
    //添加面试者
    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },
    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
        this.form.people.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = '';
    },
    //提交面试
    submit(){
      //console.log(this.form);
      this.$refs.form.validate((valid) => {

        if(valid){
          if(this.selectedQ.length==0){
            alert('请选择题目！');
            return false;
          }
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
            "applicant": this.form.people,
            "questionNumber": this.form.num,
            "questionID": this.selectedQ,
            //"createWay": temp,
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
    //重置表单
    reset(){
      this.$refs.form.resetFields();
    },
    //实时收取子组件信息更新
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
.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
</style>
