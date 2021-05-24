<template>
    <div id="app-interview">
    <el-container>
      <el-header>
        <el-row :gutter="20">
          <el-col :span="4">
            <div class="grid-content">
              <el-select v-model="question" @change="currentQuestion"> 
                <el-option v-for="item in questionOptions" :key="item.value" :label="item.label" :value="item.value"
                  :disabled="item.disabled">
                  <span style="float: left">{{ item.label }}</span>
                  <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
                </el-option>
              </el-select>
            </div>
          </el-col>
          <el-col :span="4">
            <div class="grid-content bg-purple"></div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content bg-purple"></div>
          </el-col>
          <el-col :span="4">
            <div class="grid-content bg-purple"></div>
          </el-col>
          <!-- 倒计时插件，以后写 -->
          <el-col :span="4">
            <div class="grid-content bg-purple">倒计时</div>
          </el-col>
        </el-row>

      </el-header>
      <el-main>
        <el-row :gutter="10">
          <el-col :span="12">
            <question-details></question-details>>
          </el-col>

          <el-col :span="12">
            <code-editor></code-editor>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
      
      
  </div>
</template>

<script>
import questionDetails from '../components/questionDetails.vue'
  import CodeEditor from '../components/CodeEditor.vue'

  export default {
    components: {
      questionDetails,
      CodeEditor,
    },
    data() {
      return {
        question: '', //当前问题

        questionOptions: [],//

      };
    },
    methods: {
      //设置当前题目禁点击,调用时机：监听选择器，question发生变化时
      currentQuestion() {
        var cur_q = this.question;
        console.log("现在题号：",cur_q);
        for (var i = 0; i < this.questionOptions.length; i++) {
          if (this.questionOptions[i].value == cur_q) {
            this.questionOptions[i].disabled = true;
          } else {
            this.questionOptions[i].disabled = false;
          }
        }
      },
      //动态生成题目选项
      createOptions(id_arr) {
        for (var i = 0; i < id_arr.length; i++) {
          var tmp = 'Question' + (i + 1);
          this.questionOptions.push({
            value: id_arr[i],
            label: tmp,
            disabled: false,
          });
        }
      },
      //根据question显示相应题目信息 组件间通信
      displayQuestionInfo(){

      },
      //一点开即调用
      onStart() {
        //暂时写死面试场次，以后要用session或者cookie保存该值
        var sessionID = 1;
        var postData = {
          'sessionID' : sessionID,
        }
        //根据面试场次请求题目列表
        this.$store.dispatch('questionListRequest',postData).then(res=>{
          console.log(res);
          var id_arr = res.id_arr;
          var heading_arr = res.heading_arr;
          var question_arr = res.question_arr;//富文本格式题目暂时还没写
          this.question = id_arr[0];
          this.createOptions(id_arr);
          this.currentQuestion();
        })
        //默认显示第一题
        //学习组件间通信，将题目内容传到questionDetails组件上
      },
    },
    mounted:function(){
      this.onStart();
    },
  }

</script>

<style>
  .el-col {
    border-radius: 4px;
  }

  .bg-purple-dark {
    background: #99a9bf;
  }

  .bg-purple {
    background: #d3dce6;
  }

  .bg-purple-light {
    background: #e5e9f2;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    text-align: center;
  }

</style>
