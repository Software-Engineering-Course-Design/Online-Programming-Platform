<template>
    <div id="app-interview">
    <el-container>
      <el-header class="top-header">
        <el-row :gutter="20">
          <el-col :span="4">
            <div>
              <el-select v-model="questionID" @change="currentQuestion">
                <el-option v-for="item in questionOptions" :key="item.value" :label="item.label" :value="item.value"
                  :disabled="item.disabled">
                  <span style="float: left">{{ item.label }}</span>
                  <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
                </el-option>
              </el-select>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content"></div>
          </el-col>
          <el-col :span="2" >
            <chat :p_username="username" :p_questionID="parseInt(questionID)" ></chat>
          </el-col>
          <el-col :span="4" class="close">
            <el-button type="primary" id="final-btn" @click="finalDialogVisible=true" plain>结束面试</el-button>
          </el-col>

          <el-col :span="4">
            <count-down :interviewTime="interviewTime" :startTime="startTime" :endTime="endTime" @endInterview="timeUp">
            </count-down>

            <!-- 倒计时 -->
          </el-col>
        </el-row>

      </el-header>
      <el-main>
        <el-row :gutter="10">
          <el-col :span="12">
            <question-details :p_title="p_title" :p_content="p_content"></question-details>

          </el-col>

          <el-col :span="12">
            <div id="code-editor-all">
              <div class="editor">
                <textarea ref="codeEditor" spellcheck="false" autocapitalize="none" autocorrect="off"
                  class="code-editor"></textarea>
                <div class="mode-selector">
                  <el-select class="mode-changing" v-model="mode" @change="changeMode">
                    <el-option v-for="mode in modes" :key="mode.value" :label="mode.label" :value="mode.value">
                    </el-option>
                  </el-select>
                </div>

              </div>
            </div>
            <div class="btn-box">
              <el-row>
                <!-- <el-button type="primary" id="run-btn" round>运行</el-button> -->
                <el-button type="primary" id="save-btn" @click="saveCodeAndAlert()" :disabled="ifDisabled" plain>保存
                </el-button>
                <el-button type="primary" id="submit-btn" @click="submitDialogVisible=true" :disabled="ifDisabled"
                  plain>提交</el-button>
                <el-button type="danger" id="clear-btn" @click="clear()" :disabled="ifDisabled" plain>清空</el-button>
              </el-row>
              <p>{{submit_msg}}</p>
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
       <el-dialog title="提示" :visible.sync="submitDialogVisible" width="30%" :before-close="handleClose">
      <span>每题只允许提交一次，是否提交本题代码？</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="submitDialogVisible = false">取消</el-button>
        <!-- submit传题目ID -->
        <el-button type="primary" @click="submitJudge(questionID)">确定</el-button>
      </span>
    </el-dialog>
      <el-dialog title="提示" :visible.sync="finalDialogVisible" width="30%" :before-close="handleClose">
      <span>是否结束面试,您尚未提交的题目将会一起提交</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="finalDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="handin()">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
  import questionDetails from '../components/questionDetails.vue'
  //import CodeEditor from '../components/CodeEditor.vue'
  import CountDown from '../components/CountDown.vue'
  import chat from "../components/chat";
  import io from 'socket.io-client';
  // 引入全局实例
  import _CodeMirror from 'codemirror'

  // 核心样式
  import 'codemirror/lib/codemirror.css'
  // 引入主题后还需要在 options 中指定主题才会生效
  import 'codemirror/theme/material-darker.css'

  import 'codemirror/addon/scroll/annotatescrollbar.js'
  import 'codemirror/addon/search/matchesonscrollbar.js'
  import 'codemirror/addon/search/match-highlighter.js'
  import 'codemirror/addon/search/jump-to-line.js'

  import 'codemirror/addon/dialog/dialog.js'
  import 'codemirror/addon/dialog/dialog.css'
  import 'codemirror/addon/search/searchcursor.js'
  import 'codemirror/addon/search/search.js'


  import 'codemirror/mode/javascript/javascript.js'
  import 'codemirror/mode/css/css.js'
  import 'codemirror/mode/xml/xml.js'
  import 'codemirror/mode/clike/clike.js'
  import 'codemirror/mode/markdown/markdown.js'
  import 'codemirror/mode/python/python.js'
  import 'codemirror/mode/r/r.js'
  import 'codemirror/mode/shell/shell.js'
  import 'codemirror/mode/sql/sql.js'
  import 'codemirror/mode/swift/swift.js'
  import 'codemirror/mode/vue/vue.js'

  // 尝试获取全局实例
  const CodeMirror = window.CodeMirror || _CodeMirror
  export default {
    components: {
      questionDetails,
      //CodeEditor,
      CountDown,
      chat
    },
    data() {
      return {

        questionOptions: [], //selector题号显示
        questionObj: [], //存放题目
        submitDialogVisible: false,
        finalDialogVisible: false,

        username: this.$route.query.username,
        sessionID: this.$route.query.sessionID,

        questionID: '', //当前问题的id 即item.value
        pre_questionID: '', //记录变化前的id


        p_title: '', //题目显示问题，传给子组件
        p_content: '',

        ifDisabled: false, //判断题目是否已提交，已提交的话disable按钮
        submit_msg: '',

        interviewTime: parseInt(this.$route.query.time), //传给倒计时组件的,面试时长
        startTime: this.$route.query.startTime, //传给倒计时组件的,面试开始时间
        endTime: this.$route.query.endTime, //传给倒计时组件的,面试结束时间

        code: '',
        coder: null,
        mode: 'javascript',
        modes: [{
          value: 'css',
          label: 'CSS'
        }, {
          value: 'javascript',
          label: 'JavaScript'
        }, {
          value: 'html',
          label: 'XML/HTML'
        }, {
          value: 'x-java',
          label: 'Java'
        }, {
          value: 'x-objectivec',
          label: 'Objective-C'
        }, {
          value: 'x-python',
          label: 'Python'
        }, {
          value: 'x-rsrc',
          label: 'R'
        }, {
          value: 'x-sh',
          label: 'Shell'
        }, {
          value: 'x-sql',
          label: 'SQL'
        }, {
          value: 'x-swift',
          label: 'Swift'
        }, {
          value: 'x-vue',
          label: 'Vue'
        }, {
          value: 'markdown',
          label: 'Markdown'
        }],
        options: {
          mode: 'javascript',
          theme: 'material-darker',
          indentUnit: 2, //缩进
          tabSize: 4,
          indentWithTabs: true,
          smartIndent: true, //自动缩进
          matchBrackets: true,
          lineNumbers: true, //行数
          //lineWrapping: true,
          autoRefresh: true,
          foldGutter: true,
          styleActiveLine: true,
          // gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter']
        }
      };
    },

    methods: {
      // 初始化
      _initialize() {
        // 初始化编辑器实例，传入需要被实例化的文本域对象和默认配置
        this.coder = CodeMirror.fromTextArea(this.$refs.codeEditor, this.options)
        // 编辑器赋值
        this.coder.setValue(this.value || this.code)
        // 支持双向绑定
        this.coder.on('change', (coder) => {
          this.code = coder.getValue();
          if (this.$emit) {
            this.$emit('input', this.code)
          }
        })

        // 尝试从父容器获取语法类型
        if (this.language) {
          // 获取具体的语法类型对象
          let modeObj = this._getLanguage(this.language)

          // 判断父容器传入的语法是否被支持
          if (modeObj) {
            this.mode = modeObj.label
          }
        }
      },
      // 获取当前语法类型
      _getLanguage(language) {
        // 在支持的语法类型列表中寻找传入的语法类型
        return this.modes.find((mode) => {
          // 所有的值都忽略大小写，方便比较
          let currentLanguage = language.toLowerCase()
          let currentLabel = mode.label.toLowerCase()
          let currentValue = mode.value.toLowerCase()

          // 由于真实值可能不规范，例如 java 的真实值是 x-java ，所以讲 value 和 label 同时和传入语法进行比较
          return currentLabel === currentLanguage || currentValue === currentLanguage
        })
      },
      // 更改模式
      changeMode(val) {
        // 修改编辑器的语法配置
        this.coder.setOption('mode', `text/${val}`)

        // 获取修改后的语法
        let label = this._getLanguage(val).label.toLowerCase()

        // 允许父容器通过以下函数监听当前的语法值
        this.$emit('language-change', label)
      },
      sendMessage(e) {
        e.preventDefault();
      },
      //设置当前题目禁点击,调用时机：监听选择器，question发生变化时
      currentQuestion() {
        var cur_q = this.questionID;
        for (var i = 0; i < this.questionOptions.length; i++) {
          if (this.questionOptions[i].value == cur_q) {
            this.questionOptions[i].disabled = true;
          } else {
            this.questionOptions[i].disabled = false;
          }
        }
      },

      //根据questionID显示相应题目信息 组件间通信
      displayQuestionInfo(questionID) {

        for (var i = 0; i < this.questionObj.length; i++) {
          if (this.questionObj[i].questionID == questionID) {
            this.p_title = this.questionObj[i].heading;
            this.p_content = this.questionObj[i].body;
            break;
          }
        }
      },
      //点击保存按钮，保存本题代码(只能保存没提交过的代码)
      saveCode() {
        if (this.judgeStatus(this.questionID) == false) {
          var tmp = 'QuestionID' + this.questionID;
          var codeStorage = this.coder.getValue();
          sessionStorage.setItem(tmp, codeStorage);
        }
        // else {
        //   this.$message({
        //     showClose: true,
        //     message: '该题已提交过，无法更改',
        //     type: 'warning',
        //     duration: 2300,
        //   })
        // }
      },
      saveCodeAndAlert() {
        this.saveCode();
        this.$message({
          showClose: true,
          message: '已保存该题代码',
          type: 'success',
          duration: 2300,
        })
      },
      //切换题目时，保存编辑器中上一题的代码(只能保存没提交过的代码)
      saveLastCode() {
        if (this.judgeStatus(this.pre_questionID) == false) {
          var tmp = 'QuestionID' + this.pre_questionID;
          var codeStorage = this.coder.getValue();
          sessionStorage.setItem(tmp, codeStorage);
          this.clear();
        }
      },
      //切换题目时，显示这一题的代码（之前保存的）
      displayCode() {
        var tmp = 'QuestionID' + this.questionID;
        var codeStorage = sessionStorage.getItem(tmp);
        if (codeStorage != null) {
          this.coder.setValue(codeStorage);
        }
      },
      //判断当前题目状态
      judgeStatus(q_id) {
        var cur_q_status;
        for (var i = 0; i < this.questionObj.length; i++) {
          if (this.questionObj[i].questionID == q_id) {
            cur_q_status = this.questionObj[i].questionStatus;
            break;
          }
        }
        return cur_q_status;
      },
      //切换题目的时候判断一下，如果题目已提交过，提交按钮disable
      disableBtn() {
        if (this.judgeStatus(this.questionID) == true) {
          this.ifDisabled = true;
          this.submit_msg = '该题已提交，不可再更改或提交';
        } else {
          this.ifDisabled = false;
          this.submit_msg = '';
        }
      },
      //一点开即调用
      onStart() {
        var postData = {
          'sessionID': this.sessionID,
          'username': this.username,
        }
        //根据面试场次请求题目列表
        this.$store.dispatch('questionListRequest', postData).then(res => {
          var question_list = res.question_list;
          for (var i = 0; i < question_list.length; i++) {
            var str = 'Status' + question_list[i].questionID;
            var tmp_status = sessionStorage.getItem(str); //代码提交状态放在sessionStorage里面
            console.log("初始化:", tmp_status);
            if (tmp_status == null) { //代码没有提交过
              this.questionObj.push({
                heading: question_list[i].heading,
                body: question_list[i].body,
                questionID: question_list[i].questionID,
                questionStatus: false, //代码提交状态，false是未提交
              })
            } else {
              this.questionObj.push({
                heading: question_list[i].heading,
                body: question_list[i].body,
                questionID: question_list[i].questionID,
                questionStatus: true, //代码提交状态，true是已提交
              })
            }



            //题号selector显示
            var tmp = 'Question' + (i + 1);
            this.questionOptions.push({
              value: question_list[i].questionID,
              label: tmp,
              disabled: false,
            })
          }
          //默认显示第一题
          this.questionID = this.questionObj[0].questionID;
          this.currentQuestion();
          this.displayQuestionInfo(this.questionID);
          console.log(this.questionID,'aaa')
        })

        //学习组件间通信，将题目内容传到questionDetails组件上
      },
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
      submitJudge(questionID) {
        var data = {
          username: this.username,
          sessionID: this.sessionID,
          questionID: questionID,
        };
        this.$store.dispatch('submitJudgeRequest', data).then(res => {
          if (res.ifExist) { //已经提交过，不能再提交
            this.$message({
              showClose: true,
              message: res.msg,
              type: 'warning',
              duration: 2300,
            })
          } else { //提交
            this.submit(questionID);
          }
        })
      },

      submit(questionID) { //传入题目ID，提交该题代码
        this.submitDialogVisible = true;
        var data = {};
        data.username = this.username;
        data.sessionID = this.sessionID;
        data.questionID = questionID;

        if (questionID == this.questionID) { //提交的题目为当前题目
          data.code = this.coder.getValue();
          this.saveCode();
        } else { //提交的题目不是当前题目，交卷统一提交
          var tmp = 'QuestionID' + questionID;
          var codeStorage = sessionStorage.getItem(tmp);
          data.code = codeStorage;
        }

        this.$store.dispatch('submitCodeRequest', data).then(res => {
          var ifSuccess = res.ifSuccess;
          var msg = res.msg;
          if (ifSuccess) {
            this.$message({
              showClose: true,
              message: msg,
              type: 'success',
              duration: 2300,
            })
            //更改题目的状态为 已提交
            for (var i = 0; i < this.questionObj.length; i++) {
              if (this.questionObj[i].questionID == questionID) {
                this.questionObj[i].questionStatus = true;
                var str = 'Status' + questionID;
                sessionStorage.setItem(str, true); //代码提交状态放在sessionStorage里面
                //console.log('submit ', questionID, "set session:", str, " ", sessionStorage.getItem(str));
                break;
              }
            }
            //删掉sessionStorage里存的代码
            var tmp = 'QuestionID' + questionID;
            sessionStorage.removeItem(tmp);
            //disable当前按钮，添加提示信息
            this.ifDisabled = true;
            this.submit_msg = '该题已提交，不可再更改或提交';
          } else {
            this.$message({
              showClose: true,
              message: msg,
              type: 'error',
              duration: 2300,
            });
          }
          this.submitDialogVisible = false;
        })
      },
      handin() {
        for (var i = 0; i < this.questionObj.length; i++) {
          //检查每道题是否提交过，没提交的就一起提交
          if (this.questionObj[i].questionStatus == false) {
            this.submit(this.questionObj[i].questionID);
          }
        }
        var newTime = new Date().getTime();
        var data = {
          username: this.username,
          sessionID: this.sessionID,
          submitTime: newTime,
        }
        this.$store.dispatch('handinRequest', data).then(res => {
          if (res.ifSuccess) {
            this.$message({
              showClose: true,
              message: res.msg,
              type: 'success',
              duration: 2300,
            });
            //清除本地保存的代码、本地保存的代码提交状态
            for (var i = 0; i < this.questionObj.length; i++) {
              var tmp = 'QuestionID' + this.questionObj[i].questionID;
              if (sessionStorage.getItem(tmp) != null) {
                sessionStorage.removeItem(tmp);
              }
              var tmp_status = 'Status' + this.questionObj[i].questionID;
              if (sessionStorage.getItem(tmp_status) != null) {
                sessionStorage.removeItem(tmp_status);
              }
            }
            //跳转回首页
            this.$router.push('/applicant');
          } else {
            this.$message({
              showClose: true,
              message: res.msg,
              type: 'error',
              duration: 2300,
            });
          }
        })
        this.finalDialogVisible = false;

      },
      clear() {
        this.coder.setValue('');
      },
      //面试时间结束，交卷
      timeUp() {
        this.handin();
      }
    },

    watch: {
      // 此处监听questionID变量，当期有变化时执行
      questionID(item1, item2) {
        // item1为新值，item2为旧值
        this.pre_questionID = item2;
        this.displayQuestionInfo(item1);
        this.saveLastCode();
        this.displayCode();
        this.disableBtn();
      },
    },

    mounted: function () {
      this._initialize();
      this.onStart();
      let that = this;

      //实时
      // this.coder.on('change', (coder, option) => {
      //   let newCode = coder.getValue();
      //   if (newCode !== that.code) {
      //     that.socket.emit('changeCode', {
      //       code: newCode,
      //       option: option,
      //     })
      //   }
      //   this.code = coder.getValue();
      // })





    },
  }

</script>

<style>
  .close {
    display: flex;
    flex-direction: row-reverse;
  }

  .btn-box {
    margin-top: 2.5%;
    display: flex;
    justify-content: flex-end;
  }

  .el-col {
    border-radius: 4px;
  }

  .grid-content {
    border-radius: 4px;
    min-height: 36px;
    /* text-align: center; */
  }

  #code-editor-all {
    display: flex;
    flex-direction: column;
    /* justify-content: flex-end;
    margin-left: auto; */

  }

  .editor {
    flex-grow: 1;
    display: flex;
    position: relative;
    height: 100%;
  }

  .top-header {
    padding: 10px 20px;
  }

  .el-container {
    margin-bottom: 40px;
  }

  .CodeMirror {
    flex-grow: 1;
    z-index: 1;
    height: 600px;

  }

  /* .CodeMirror-scroll {
    height: auto;
    overflow-y: hidden;
    overflow-x: auto;
  } */

  .CodeMirror-code {
    line-height: 23px;
    font-size: 17px;
  }


  .mode-changing {
    position: absolute;
    z-index: 2;
    right: 10px;
    top: 10px;
    max-width: 130px;
  }

</style>
