<template>
    <div class="applicant">
    <el-container>
      <!-- header显示用户id和用户类型 -->
      <el-header>Hello,用户1111</el-header>
      <el-main>
        <el-tabs v-model="interviewName" @tab-click="handleClick">
          <el-tab-pane label="可参加面试" name="first">
            <el-collapse v-model="sessionName1" accordion>
              <el-collapse-item v-for="(item, index) in interviewList" :key="index" :name="index">
                <template slot="title">
                  <h3>面试场次{{item.sessionID}}</h3>
                </template>
                <div>出题者：{{item.interviewer}}</div>
                <div>题数：{{item.questionNumber}}</div>
                <div>面试时长：{{item.time}}</div>
                <el-button type="primary" class="start-btn" round>开始面试</el-button>
              </el-collapse-item>

            </el-collapse>
          </el-tab-pane>
          <el-tab-pane label="已参加面试" name="second">
            <el-collapse v-model="sessionName2" accordion>
              <el-collapse-item v-for="(item, index) in resultList" :key="index" :name="index">
                <template slot="title">
                  <h3>面试场次{{item.sessionID}}</h3>
                </template>
                <div>出题者：{{item.interviewer}}</div>
                <div>题数：{{item.questionNumber}}</div>
                <div>批改状态：{{item.status?'已批改':'未批改'}}</div>
                <div>面试分数：{{item.score}}</div>
                <el-button type="primary" class="check-btn" round>查看面试详情</el-button>
              </el-collapse-item>

            </el-collapse>
          </el-tab-pane>
        </el-tabs>
        <!-- <el-row :gutter="10">
          <el-col :span="12">
            <h3>可参加面试</h3>
          </el-col>

          <el-col :span="12">
            <h3>已参加面试</h3>
          </el-col>
        </el-row> -->
      </el-main>
    </el-container>
      
  </div>
</template>

<script>
  export default {
    data() {
      return {
        sessionName1: '0',
        sessionName2: '0',
        interviewName: 'first',
        new_session_arr: [],
        old_session_arr: [],
        new_info_arr: [],
        old_info_arr: [],
        interviewList: [],
        resultList: [],
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      },
      //动态生成list
      createInterviewList(s_arr, i_arr, list) {
        for (var i = 0; i < s_arr.length; i++) {
          list.push({
            sessionID: s_arr[i],
            interviewer: i_arr[i][0],
            questionNumber: i_arr[i][1],
            time: i_arr[i][2],
          });
        }
      },
      createResultList(s_arr, i_arr, list) {
        for (var i = 0; i < s_arr.length; i++) {
          list.push({
            sessionID: s_arr[i],
            interviewer: i_arr[i][0],
            questionNumber: i_arr[i][1],
            status: i_arr[i][2],
            score:i_arr[i][3],
          });
        }
      },
      onStart() {
        var username = 'aaa';
        var postData = {
          'username': username,
        }
        //根据面试场次请求题目列表
        this.$store.dispatch('interviewListRequest', postData).then(res => {
          console.log(res);
          this.new_session_arr = res.new_session_arr;
          this.old_session_arr = res.old_session_arr;
          this.new_info_arr = res.new_info_arr;
          this.old_info_arr = res.old_info_arr;

          this.createInterviewList(this.new_session_arr, this.new_info_arr, this.interviewList);
          this.createResultList(this.old_session_arr,this.old_info_arr,this.resultList);
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
