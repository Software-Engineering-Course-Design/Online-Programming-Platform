<template>
    <div class="view-result">
    <!--     <el-container> -->
    <!-- <el-header> -->

    <el-tabs type="border-card" class="view-card">
      <el-tab-pane v-for="item in allObj" :key="item.questionID" :label="item.label" :value="item.questionID">
        <!-- 如何实现点击获取题目ID -->
        <span slot="label">{{item.label}}</span>
        <el-row :gutter="20">
          <el-col :span="10">
            <question-details></question-details>
          </el-col>
          <!-- <el-divider direction="vertical"></el-divider> -->
          <el-col :span="14" id="right-side">
            <el-tabs :tab-position="tabPosition" style="height: 200px;" type="card">
              <el-tab-pane label="代码">
                {{item.code}}
              </el-tab-pane>
              <el-tab-pane label="答案">
                {{item.answer}}
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
    <!-- </el-header> -->
    <!-- 内容，左边是题目内容，右边通过标签页切换 提交的代码、标准答案、成绩状态等 -->
    <!-- <el-main> -->
    <!-- <el-row :gutter="20">
          <el-col :span="10">
            <question-details></question-details>
          </el-col>
          <el-col :span="14">
            <el-tabs :tab-position="tabPosition" style="height: 200px;">
              <el-tab-pane label="已提交代码">

              </el-tab-pane>
              <el-tab-pane label="标准答案">

              </el-tab-pane>
              <el-tab-pane label="结果查询">
                <div>
                  批改结果：
                </div>
                <div>
                  批改面试官：
                </div>
              </el-tab-pane>

            </el-tabs>
          </el-col>

        </el-row> -->
    <!-- </el-main>
    </el-container> -->
      
  </div>
</template>

<script>
  import questionDetails from '../components/questionDetails.vue'
  export default {
    components: {
      questionDetails,
    },
    data() {
      return {
        tabPosition: 'right',
        username: this.$route.query.username,
        sessionID: this.$route.query.sessionID,
        allObj: [], //存放后端传来的数据
      };
    },
    methods: {
      //根据后端传来的数据动态显示题目
      displayQuestions() {

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
        })
      },

    },
    mounted() {
      this.onStart();
    },
  }

</script>

<style>
  .view-card {
    padding: 0px;
    margin: 0px;
    height: 100%;
    width: 100%;
  }

</style>
