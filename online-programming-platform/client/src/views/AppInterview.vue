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
            <!-- <count-down></count-down> -->
          </el-col>
        </el-row>

      </el-header>
      <el-main>
        <el-row :gutter="10">
          <el-col :span="12">
            <question-details></question-details>
          </el-col>

          <el-col :span="12">
            <code-editor></code-editor>
            <div class="btn-box">
              <el-row>
                <!-- <el-button type="primary" id="run-btn" round>运行</el-button> -->
                <el-button type="primary" id="save-btn" round>保存</el-button>
                <el-button type="primary" id="submit-btn" @click="submitDialogVisible=true" round>提交</el-button>
                <el-button type="danger" id="clear-btn" round>清空</el-button>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
       <el-dialog title="提示" :visible.sync="submitDialogVisible" width="30%" :before-close="handleClose">
      <span>是否提交代码</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="submitDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="submit()">确定</el-button>
      </span>
    </el-dialog>
      
  </div>
</template>

<script>
  import questionDetails from '../components/questionDetails.vue'
  import CodeEditor from '../components/CodeEditor.vue'
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
      CodeEditor,
      CountDown,
    },
    data() {
      return {
        question: '', //当前问题

        questionOptions: [], //
        submitDialogVisible: false,
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

        //socket: io('localhost:3001'),
      };
    },
    methods: {
      sendMessage(e) {
        e.preventDefault();
      },
      //设置当前题目禁点击,调用时机：监听选择器，question发生变化时
      currentQuestion() {
        var cur_q = this.question;
        console.log("现在题号：", cur_q);
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
      displayQuestionInfo() {

      },
      //一点开即调用
      onStart() {
        //暂时写死面试场次，以后要用session或者cookie保存该值
        var sessionID = 1;
        var postData = {
          'sessionID': sessionID,
        }
        //根据面试场次请求题目列表
        this.$store.dispatch('questionListRequest', postData).then(res => {
          console.log(res);
          var id_arr = res.id_arr;
          var heading_arr = res.heading_arr;
          var question_arr = res.question_arr; //富文本格式题目暂时还没写
          this.question = id_arr[0];
          this.createOptions(id_arr);
          this.currentQuestion();
        })
        //默认显示第一题
        //学习组件间通信，将题目内容传到questionDetails组件上
      },
    },
    mounted: function () {
      //let sessionID = this.$route.query.sessionID
      let sessionID = 1;
      this.onStart();
      let that = this;
      this.editor = CodeMirror.fromTextArea(this.$refs.codeEditor, {
        mode: 'javascript',
        lineNumbers: true,
        lineWrapping: true,
        indentUnit: 4, // 缩进
        foldGutter: true,
        styleActiveLine: true,
        theme: 'cobalt',
        gutters: ['CodeMirror-linenumbers', 'CodeMirror-foldgutter']
      });
      //实时
      // this.editor.on('change', (coder, option) => {
      //   let newCode = coder.getValue();
      //   if (newCode !== that.code) {
      //     that.socket.emit('changeCode', {
      //       code: newCode,
      //       option: option,
      //     })
      //   }
      //   this.code = coder.getValue();
      // })

      //window的鼠标事件
      window.onmousedown = this.ctrlMouseDown
      window.onmousemove = this.ctrlMouseMove
      window.onmouseup = this.ctrlMouseUp
      document.addEventListener('mouseleave', this.mouseLeaveWindow)

      // var vm = this
      // var sessionID = this.$route.query.sessionID
      // vm.sessionID = sessionID
      

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
