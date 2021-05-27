<template>
    <div>
        <el-container>
      <el-header>
        <!-- 题号 -->
        <el-tabs type="border-card">
          <el-tab-pane v-for="item in questionList" :key="item.value" :label="item.label" :value="item.value"
            :disabled="item.disabled">
            <span slot="label">{{item.label}}</span>
            <el-row :gutter="20">
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

            </el-row>
          </el-tab-pane>
        </el-tabs>
      </el-header>
      <!-- 内容，左边是题目内容，右边通过标签页切换 提交的代码、标准答案、成绩状态等 -->
      <el-main>
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
      </el-main>
    </el-container>
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
        username: '1',
        sessionID: 1, //如何获取
        questionList: [],//存放题目题号
        allObj:[],//存放后端传来的数据
      };
    },
    methods: {
      //动态生成题目选项
      createOptions(id_arr) {
        for (var i = 0; i < id_arr.length; i++) {
          var tmp = 'Question' + (i + 1);
          this.questionList.push({
            value: id_arr[i],
            label: tmp,
            disabled: false,
          });
        }
        console.log(this.questionList)
      },
      //处理后端传
      onStart() {
        var postData = {
          'username': this.username,
          'sessionID': this.sessionID,
        }
        this.$store.dispatch('viewResultRequest', postData).then(res => {
          console.log(res);
          var id_arr = res.id_arr;

          //var msg = res.msg;
          //console.log(msg);
          this.createOptions(id_arr);
        //   var heading_arr = res.heading_arr;
        //   var question_arr = res.question_arr;
        //   var code_arr = res.code_arr;
        //   var answer_arr = res.answer_arr;
        //   var result_arr = res.result_arr;
        })
      },

    },
    mounted() {
      this.onStart();
    },
  }

</script>

<style>

</style>
