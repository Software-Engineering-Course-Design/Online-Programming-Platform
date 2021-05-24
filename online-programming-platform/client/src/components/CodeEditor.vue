<template>
  <div>
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
      <div class="btn-box">
        <el-row>
          <!-- <el-button type="primary" id="run-btn" round>运行</el-button> -->
          <el-button type="primary" id="save-btn" round>保存</el-button>
          <el-button type="primary" id="submit-btn" round>提交</el-button>
          <el-button type="danger" id="clear-btn" round>清空</el-button>
        </el-row>
      </div>
    </div>
  </div>

</template>

<script type="text/ecmascript-6">
  // 引入全局实例
  import _CodeMirror from 'codemirror'

  // 核心样式
  import 'codemirror/lib/codemirror.css'
  // 引入主题后还需要在 options 中指定主题才会生效
  import 'codemirror/theme/cobalt.css'


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
    name: 'code-editor',
    props: {
      // 外部传入的内容，用于实现双向绑定
      value: String,
      // 外部传入的语法类型
      language: {
        type: String,
        default: null
      }
    },
    data() {
      return {
        // 内部真实的内容
        code: '',
        // 默认的语法类型
        mode: 'javascript',
        // 编辑器实例
        coder: null,
        // 默认配置
        options: {
          // 缩进格式
          tabSize: 2,
          // 主题，对应主题库 JS 需要提前引入
          theme: 'cobalt',
          // 显示行号
          lineNumbers: true,
          line: true
        },
        // 支持切换的语法高亮类型，对应 JS 已经提前引入
        // 使用的是 MIME-TYPE ，不过作为前缀的 text/ 在后面指定时写死了
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
        }]
      }
    },
    mounted() {
      // 初始化
      this._initialize()
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
          this.code = coder.getValue()

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
      }
    }
  }

</script>

<style>
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

  .btn-box {
    position: relative;
    bottom: 0;
  }

</style>
