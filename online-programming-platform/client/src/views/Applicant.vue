<template>
    <div class="applicant">
    <el-container>
      <!-- header显示用户id和用户类型 -->
      <el-header>Hello,用户 {{username}}!</el-header>
      <el-main>
        <el-tabs v-model="interviewName" @tab-click="handleClick">
          <el-tab-pane label="可参加面试" name="interview">
            <el-collapse v-model="sessionName1" accordion>
              <el-collapse-item v-for="(item, index) in interviewList" :key="index" :name="index">
                <template slot="title">
                  <h3 class="interviewTitle">面试场次{{item.sessionID}}</h3>
                </template>
                <div class="interviewInfo">
                  <div class="info">
                    <div>出题者：{{item.interviewer}}</div>
                    <div>题数：{{item.questionNumber}}</div>
                    <div>面试开始时间：{{item.startTime}}</div>
                    <div>面试时长：{{item.timeUsed}}分钟</div>
                  </div>
                  <el-button type="primary" class="start-btn"
                    @click="startInterview(item.sessionID,item.startTime,item.endTime,item.timeUsed)" plain>
                    开始面试
                  </el-button>
                </div>

              </el-collapse-item>

            </el-collapse>
          </el-tab-pane>
          <el-tab-pane label="已参加面试" name="result">
            <el-collapse v-model="sessionName2" accordion>
              <el-collapse-item v-for="(item, index) in resultList" :key="index" :name="index">
                <template slot="title">
                  <h3 class="interviewTitle">面试场次{{item.sessionID}}</h3>
                </template>
                <div class="interviewInfo">
                  <div class="info">
                    <div>出题者：{{item.interviewer}}</div>
                    <div>题数：{{item.questionNumber}}</div>
                    <div>面试时间：{{item.startTime}} —— {{item.endTime}}</div>
                    <div>批改状态：{{item.status?'已批改':'未批改'}}</div>
                    <!-- 状态为已批改的时候显示面试分数 -->
                    <div v-if="item.status">面试分数：{{item.score}}</div>
                  </div>
                  <el-button type="primary" class="check-btn" @click="jumpToResultURL(item.sessionID)" plain>查看面试详情
                  </el-button>
                </div>


              </el-collapse-item>

            </el-collapse>
          </el-tab-pane>
        </el-tabs>
        <!-- <el-drawer title="我是标题" :visible.sync="drawer" :direction="direction" :before-close="handleClose">
          <span>我来啦!</span>
        </el-drawer> -->
      </el-main>
    </el-container>
      
    <!-- 提示框 -->
      <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
      <span>{{alertMsg}}</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        username: this.$cookies.get("username"),
        sessionName1: '0',
        sessionName2: '0',
        interviewName: 'interview',

        interviewList: [], //可参加的面试场次
        resultList: [], //已参加的面试场次
        dialogVisible: false,
        alertMsg: '',
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
            startTime: arr[i].startTime,
            endTime: arr[i].endTime,
            timeUsed: arr[i].timeUsed,
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
            startTime: arr[i].startTime,
            endTime: arr[i].endTime,
          });
        }
      },
      //跳转并传参 跳转至面试页面
      jumpToInterviewURL(s_id, s_time, e_time, time) {
        this.$router.push({
          path: '/applicant/interview',
          query: {
            username: this.username,
            sessionID: s_id,
            startTime: s_time,
            endTime: e_time,
            time: time,
          }
        })
      },
      //点击开始面试按钮触发，判断是否满足开始面试的条件
      startInterview(s_id, s_time, e_time, time) {
        // 获取当前时间
        let newTime = new Date().getTime();
        //获取面试开始时间
        let interviewStartTime = new Date(s_time).getTime();
        //获取结束时间
        let interviewEndTime = new Date(e_time).getTime();
        //可提前10分钟进入面试链接,可迟到15分钟
        var pre = 10 * 60000;
        var late = 15 * 60000;
        if (interviewStartTime - newTime > pre) {
          this.alertMsg = '面试尚未开始，不能进入面试';
          this.dialogVisible = true;
        } else if (interviewStartTime - newTime <= pre && interviewStartTime - newTime >= 0) { //提前进场
          this.jumpToInterviewURL(s_id, s_time, e_time, time);
        } else if (newTime - interviewStartTime < late && newTime - interviewStartTime >= 0) { //迟到15分钟以内可进场
          this.jumpToInterviewURL(s_id, s_time, e_time, time);
        } else if (newTime - interviewStartTime > late) {
          if (newTime - interviewEndTime > 0) {
            this.alertMsg = '面试已结束，无法再进入';
            this.dialogVisible = true;
          } else {
            this.alertMsg = '您已迟到，无法再进入面试';
            this.dialogVisible = true;
          }
        }

      },
      //跳转并传参 跳转至查看面试结果页面
      jumpToResultURL(s_id) {
        this.$router.push({
          path: '/applicant/viewResult',
          query: {
            username: this.username,
            sessionID: s_id,
          }
        })
      },
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
      //页面刚加载时调用，在mounted里调用
      onStart() {
        var postData = {
          'username': this.username,
        }
        //根据面试场次请求题目列表
        this.$store.dispatch('interviewListRequest', postData).then(res => {
          console.log(res);

          this.createInterviewList(res.notjoin, this.interviewList);
          this.createResultList(res.join, this.resultList);
        })

      },
    },
    mounted: function () {
      this.onStart();
    },
  }

</script>

<style>
  .interviewInfo {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }

  .interviewTitle {
    font-size: 20px;
  }

  .info {
    font-size: 15px;
  }

</style>
