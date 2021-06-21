<template>
    <div class="applicant">
    <logout :username="username"></logout>
    <!-- <i class="el-icon-user-solid">{{username}}</i> -->
    <el-container class="container">
      <el-header>
        <h2 class="header">在线编程面试平台</h2>
      </el-header>
      <el-main>
        <div class="top">
          <el-button @click="drawer = true" type="primary" icon="el-icon-warning" id="info-btn">
            查看面试注意事项
          </el-button>
        </div>
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
                    <div>批改状态：{{item.status=="true"?'已批改':'未批改'}}</div>
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
        <!-- 面试信息提示 -->
        <el-drawer title="面试须知" :visible.sync="drawer" :direction="direction" size="50%" :before-close="handleClose">
          <p class="wel">欢迎{{username}}参与面试！</p>
          <ol class="tips">
            <li>请在面试开始前10分钟内进入面试，若已迟到，在面试开始之后15分钟内仍可进入面试；</li>
            <li>若没有在面试开始前10分钟到面试开始后15分钟内进入面试，则失去该场次的面试资格；</li>
            <li>进入面试之后，切勿退出页面；</li>
            <li>点击左上角的选择框切换题目，切换时，编辑器中的代码将自动保存；</li>
            <li>每道题目只有一次提交机会，一旦提交，不能再修改该题，提交之前请谨慎选择；</li>
            <li>可点击“结束面试”按钮提前结束面试，结束面试将自动提交尚未提交的题目；</li>
            <li>右上角有时间提示，若到点尚未结束面试将自动结束面试回到首页。</li>
          </ol>
        </el-drawer>
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
  import logout from "../components/UserQuit.vue"
  export default {
    components: {
      logout
    },
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
        drawer: true, //面试提示
        direction: 'rtl',
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
            interviewer: arr[i].username,
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
            interviewer: arr[i].username,
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
          console.log(res.notjoin);
          console.log(res.join);
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
  #info-btn {
    position: relative;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
  }

  .top {
    display: flex;
    justify-content: flex-end;

  }

  .header {
    font-size: 25px;
    text-align: center;
  }

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

  .tips {
    font-size: 20px;
    line-height: 35px;
  }

  .wel {
    text-indent: 2em;
    font-size: 20px;
    line-height: 35px;
  }
.container{
  margin-left: 1.5%;
  margin-right: 1.5%;
}
/* .el-icon-user-solid{
  font-size: 20px;
  position: absolute;
  top:10px;
  right: 10px;
} */
</style>
