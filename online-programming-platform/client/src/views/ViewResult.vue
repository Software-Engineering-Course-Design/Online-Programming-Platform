<template>
    <div class="view-result">
    <el-page-header @back="goBack" class="goback">
    </el-page-header>
    <logout :username="username"></logout>
    <div style="float: right">
      <chat :p_username="username" :p_question-i-d="questionID"></chat>
    </div>

    <el-container >
      <el-header>
        <h3 class="header">面试场次{{sessionID}}结果</h3>
      </el-header>

      <el-main>

        <el-tabs type="border-card" class="view-card">
          <el-tab-pane v-for="item in allObj" :key="item.questionID" :label="item.label" :value="item.questionID">
            <!-- 如何实现点击获取题目ID -->
            <span slot="label">{{item.label}}</span>
            <el-row :gutter="10" class="el-row">
              <el-col :span="10">
                <question-details :p_title="item.heading" :p_content="item.body"></question-details>
              </el-col>
              <!-- <el-divider direction="vertical"></el-divider> -->
              <el-col :span="14" id="right-side">
                <el-tabs :tab-position="tabPosition" type="card">
                  <el-tab-pane label="代码">
                    <!-- <code>{{item.code}}</code> -->
                    <code-editor :value="item.code"></code-editor>
                  </el-tab-pane>
                  <el-tab-pane label="答案">
                    <!-- <code>{{item.answer}}</code> -->
                    <code-editor :value="item.answer"></code-editor>
                  </el-tab-pane>
                  <el-tab-pane label="结果">
                    <div>
                      批改结果：{{item.result}}
                      <div>注意：0表示尚未批改，AC表示通过，WA表示错误</div>
                    </div>
                  </el-tab-pane>

                </el-tabs>
              </el-col>

            </el-row>
          </el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  import questionDetails from '../components/questionDetails.vue'
  import codeEditor from '../components/CodeEditor.vue'
  import logout from "../components/UserQuit.vue"
  import chat from "../components/chat";
  export default {
    components: {
      questionDetails,
      codeEditor,
      logout,
      chat
    },
    data() {
      return {
        questionID: '',
        tabPosition: 'right',
        username: this.$route.query.username,
        sessionID: this.$route.query.sessionID,
        allObj: [], //存放后端传来的数据

        p_title: '',
        p_content: '',

      };
    },

    methods: {
      goBack() {
        this.$router.push('/applicant');
      },
      onStart() {
        var postData = {
          'username': this.username,
          'sessionID': this.sessionID,
        }
        this.$store.dispatch('viewResultRequest', postData).then(res => {
          console.log(res);
          //处理后端传的数据
          var interview_result_list = res.interview_result_list;
          for (var i = 0; i < interview_result_list.length; i++) {
            var tmp = 'Question' + (i + 1);
            this.allObj.push({
              //题目
              questionID: interview_result_list[i].questionID,
              heading: interview_result_list[i].heading,
              body: interview_result_list[i].body,
              //代码
              code: interview_result_list[i].code,
              //答案
              answer: interview_result_list[i].answer,
              //该题结果（0：未批改，AC,WA）
              result: interview_result_list[i].result,
              //题目选项卡
              label: tmp,
            })

            //显示代码、答案、结果
          }
          this.questionID = interview_result_list[0].questionID;
        })
      },


    },
    mounted() {
      this.onStart();

    },

  }

</script>

<style>
  .view-result {
    height: 100%;
  }

  .view-card {
    padding: 0px;
    margin: 10px;
    min-height: 600px;
    width: 100%;
  }

  .header {
    font-size: 25px;
    text-align: center;
  }

  .el-row {
    height: 100%;
  }

  .goback {
    position: absolute;
    top: 10px;
    left: 10px;
  }

</style>
