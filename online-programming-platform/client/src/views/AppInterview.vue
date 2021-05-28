<template>
    <div id="app-interview">
    <el-container>
      <el-header>
        <el-row :gutter="20">
          <el-col :span="4">
            <div class="grid-content">
              <el-select v-model="questionID" @change="currentQuestion">
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
            <el-button type="primary" id="final-btn" @click="finalDialogVisible=true" round>结束面试</el-button>
          </el-col>
          <!-- 倒计时 -->
          <el-col :span="4">
            <count-down :interviewTime="interviewTime" :startTime="startTime" :endTime="endTime" @endInterview="timeUp"></count-down>
          </el-col>
        </el-row>

      </el-header>
      <el-main>
        <el-row :gutter="10">
          <el-col :span="12">
            <question-details></question-details>
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
                <el-button type="primary" id="save-btn" @click="saveCodeAndAlert()" round>保存</el-button>
                <el-button type="primary" id="submit-btn" @click="submitDialogVisible=true" round>提交</el-button>
                <el-button type="danger" id="clear-btn" @click="clear()" round>清空</el-button>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
       <el-dialog title="提示" :visible.sync="submitDialogVisible" width="30%" :before-close="handleClose">
      <span>是否提交本题代码</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="submitDialogVisible = false">取消</el-button>
        <!-- submit传题目ID -->
        <el-button type="primary" @click="submit(questionID)">确定</el-button>
      </span>
    </el-dialog>
      <el-dialog title="提示" :visible.sync="finalDialogVisible" width="30%" :before-close="handleClose">
      <span>是否结束面试</span>
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
  import io from 'socket.io-client';
  // 引入全局实例
  import _CodeMirror from 'codemirror'

  // 核心样式
  import 'codemirror/lib/codemirror.css'
  // 引入主题后还需要在 options 中指定主题才会生效
  import 'codemirror/theme/cobalt.css'

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
    },
    data() {
      return {
        //question: '', //当前问题

        questionOptions: [], //selector题号显示
        submitDialogVisible: false,
        finalDialogVisible: false,

        username: this.$route.query.username,
        sessionID: this.$route.query.sessionID,

        questionID: '', //当前问题的id 即item.value
        pre_questionID: '', //记录变化前的id
        questionStatus: [], //每道题的提交状态

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
          theme: 'cobalt',
          lineNumbers: true, //行数
          lineWrapping: true,
          indentUnit: 4, //缩进
          foldGutter: true,
          styleActiveLine: true,
          gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter']
        }
        //socket: io('localhost:3001'),
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
      //动态生成题目选项，初始化题目提交状态——未提交
      createOptions(id_arr) {
        for (var i = 0; i < id_arr.length; i++) {
          var tmp = 'Question' + (i + 1);
          this.questionOptions.push({
            value: id_arr[i],
            label: tmp,
            disabled: false,
          });
          this.questionStatus.push({
            value: id_arr[i],
            status: false,
          });
        }
      },
      //根据questionID显示相应题目信息 组件间通信
      displayQuestionInfo() {

      },
      //点击保存按钮，保存本题代码
      saveCode() {
        var tmp = 'QuestionID' + this.questionID;
        var codeStorage = this.coder.getValue();
        sessionStorage.setItem(tmp, codeStorage);
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
      //切换题目时，保存编辑器中上一题的代码
      saveLastCode() {
        var tmp = 'QuestionID' + this.pre_questionID;
        var codeStorage = this.coder.getValue();
        sessionStorage.setItem(tmp, codeStorage);
        this.clear();
      },
      //切换题目时，显示这一题的代码（之前保存的）
      displayCode() {
        var tmp = 'QuestionID' + this.questionID;
        var codeStorage = sessionStorage.getItem(tmp);
        if (codeStorage != null) {
          this.coder.setValue(codeStorage);
        }
      },
      //一点开即调用
      onStart() {
        var postData = {
          'sessionID': this.sessionID,
        }
        //根据面试场次请求题目列表
        this.$store.dispatch('questionListRequest', postData).then(res => {
          console.log(res);
          var id_arr = res.id_arr;
          var heading_arr = res.heading_arr;
          var question_arr = res.question_arr; //富文本格式题目暂时还没写
          this.questionID = id_arr[0];
          this.createOptions(id_arr);
          this.currentQuestion();
        })
        //默认显示第一题
        //学习组件间通信，将题目内容传到questionDetails组件上
      },
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
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
            for (var i = 0; i < this.questionStatus.length; i++) {
              if (this.questionStatus[i].value == questionID) {
                this.questionStatus[i].status = true;
              }
            }
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
        for (var i = 0; i < this.questionStatus.length; i++) {
          //检查每道题是否提交过，没提交的就一起提交
          if (this.questionStatus[i].status == false) {
            this.submit(this.questionStatus[i].value);
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
            //跳转回首页
            //this.$router.push('/applicant');
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
        //清除本地保存的代码
        for (var i = 0; i < this.questionStatus.length; i++) {
          var tmp = 'QuestionID' + this.questionStatus[i].value;
          if (sessionStorage.getItem(tmp) != null) {
            sessionStorage.removeItem(tmp);
          }

        }
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
        this.saveLastCode();
        this.displayCode();
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

  #code-editor-all {
    display: flex;
    flex-direction: column;
    /* justify-content: flex-end;
    margin-left: auto; */

  }

  .editor {
    /* width: 50%; */
    flex-grow: 1;
    display: flex;
    position: relative;
  }


  .CodeMirror {
    flex-grow: 1;
    z-index: 1;

  }

  .CodeMirror-code {
    line-height: 19px;
  }


  .mode-changing {
    position: absolute;
    z-index: 2;
    right: 10px;
    top: 10px;
    max-width: 130px;
  }

</style>
