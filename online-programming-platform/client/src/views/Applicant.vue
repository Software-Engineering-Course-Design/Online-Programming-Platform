<template>
    <div class="applicant">
    <el-container>
      <!-- header显示用户id和用户类型 -->
      <el-header>Hello,用户1111</el-header>
      <el-main>
        <el-tabs v-model="interviewName" @tab-click="handleClick">
          <el-tab-pane label="可参加面试" name="interview">
            <el-collapse v-model="sessionName1" accordion>
              <el-collapse-item v-for="(item, index) in interviewList" :key="index" :name="index">
                <template slot="title">
                  <h3>面试场次{{item.sessionID}}</h3>
                </template>
                <div>出题者：{{item.interviewer}}</div>
                <div>题数：{{item.questionNumber}}</div>
                <div>面试时长：{{item.time}}</div>
                <el-button type="primary" class="start-btn" @click="jumpToInterviewURL(item.sessionID)" round>开始面试
                </el-button>
              </el-collapse-item>

            </el-collapse>
          </el-tab-pane>
          <el-tab-pane label="已参加面试" name="result">
            <el-collapse v-model="sessionName2" accordion>
              <el-collapse-item v-for="(item, index) in resultList" :key="index" :name="index">
                <template slot="title">
                  <h3>面试场次{{item.sessionID}}</h3>
                </template>
                <div>出题者：{{item.interviewer}}</div>
                <div>题数：{{item.questionNumber}}</div>
                <div>批改状态：{{item.status?'已批改':'未批改'}}</div>
                <div>面试分数：{{item.score}}</div>
                <el-button type="primary" class="check-btn" @click="jumpToResultURL(item.sessionID)" round>查看面试详情</el-button>
              </el-collapse-item>

            </el-collapse>
          </el-tab-pane>
        </el-tabs>
      </el-main>
    </el-container>
      
  </div>
</template>

<script>
  export default {
    data() {
      return {
        username: sessionStorage.getItem("username"),
        sessionName1: '0',
        sessionName2: '0',
        interviewName: 'interview',

        interviewList: [],//可参加的面试场次
        resultList: [],//已参加的面试场次

      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      },
      //动态生成list 可参加面试
      createInterviewList(arr, list) {
        for (var i = 0; i < arr.length; i++) {
          list.push({
            sessionID: arr[i].sessionID,
            interviewer: arr[i].hr_username,
            questionNumber: arr[i].questionNumber,
            time: arr[i].time,
          });
        }
      },
      //动态生成list 已参加面试
      createResultList(arr, list) {
        for (var i = 0; i < arr.length; i++) {
          list.push({
            sessionID: arr[i].sessionID,
            interviewer: arr[i].hr_username,
            questionNumber: arr[i].questionNumber,
            status: arr[i].status,
            score: arr[i].score,
          });
        }
      },
      //点击按钮跳转并传参
      jumpToInterviewURL(s_id) {
        this.$router.push({
          path: '/applicant/interview',
          query: {
            username: this.username,
            sessionID: s_id,
          }
        })
      },
      jumpToResultURL(s_id) {
        this.$router.push({
          path: '/applicant/viewResult',
          query: {
            username: this.username,
            sessionID: s_id,
          }
        })
      },
      onStart() {
        //var username = sessionStorage.getItem("username");
        var username = "111";
        var postData = {
          'username': username,
        }
        //根据面试场次请求题目列表
        this.$store.dispatch('interviewListRequest', postData).then(res => {
          console.log(res);

          this.createInterviewList(res.join, this.interviewList);
          this.createResultList(res.notjoin, this.resultList);
        })

      },
    },
    mounted: function () {
      this.onStart();
    },
  }

</script>

<style>

</style>
