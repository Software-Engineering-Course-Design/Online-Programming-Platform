<template>
  <el-container>
    <quill-editor
      v-model="content"
      :options="editorOption"
      @blur="onEditorBlur($event)"
      @focus="onEditorFocus($event)"
      @ready="onEditorReady($event)"
      @change="onEditorChange($event)">
  </quill-editor>
    <el-button @click="test2">test2</el-button>
  </el-container>
</template>

<script>
import { quillEditor } from 'vue-quill-editor'
import Quill from 'quill'
import highlight from 'highlight.js'
import 'highlight.js/styles/zenburn.css'

export default {
  name: "editor",
  data(){
    return {
      content: this.p_content,
      editorOption: {
        placeholder: '请输入题目描述',
        theme: 'snow', // 主题
        modules: {
          toolbar: {
            container: [
              ['bold', 'italic', 'underline', 'strike'],//加粗、斜体、下划线、删除
              ['blockquote', 'code-block'],//引用、代码块
              [{ header: [1, 2, 3, 4, 5, 6, false]}],//1、2级标题
              [{indent: "-1"}, {indent: "+1"}],//缩进

            ], // 工具栏选项
            //handlers: handlers // 事件重写
          },
          syntax: {
            highlight:text => {
              return highlight.highlightAuto(text).value;
            }
          }
        },
      },
    }
  },
  components:{
    quillEditor,
    Quill
  },
  methods:{
    test2(){
      this.$emit('updateContent',this.content);
      console.log(this.content);
    },
    onEditorBlur(editor) {
      },
    onEditorFocus(editor) {
      },
    onEditorReady(editor) {
      },
    onEditorChange(editor) {
      this.content = editor.html;
    },
  },

  computed: {
    editor() {
      return this.$refs.myTextEditor.quillEditor;
    }
  },
  props:{
    p_content: { type: String},
  },
  mounted () {
    console.log(this.$emit('update:q_content',this.content));
  }
}
</script>

<style scoped>

.editor {
  line-height: normal !important;
  height: 800px;
}
.ql-snow .ql-tooltip[data-mode=link]::before {
  content: "请输入链接地址:";
}
.ql-snow .ql-tooltip.ql-editing a.ql-action::after {
  border-right: 0px;
  content: '保存';
  padding-right: 0px;
}

.ql-snow .ql-tooltip[data-mode=video]::before {
  content: "请输入视频地址:";
}

.ql-snow .ql-picker.ql-size .ql-picker-label::before,
.ql-snow .ql-picker.ql-size .ql-picker-item::before {
  content: '14px';
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value=small]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value=small]::before {
  content: '10px';
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value=large]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value=large]::before {
  content: '18px';
}
.ql-snow .ql-picker.ql-size .ql-picker-label[data-value=huge]::before,
.ql-snow .ql-picker.ql-size .ql-picker-item[data-value=huge]::before {
  content: '32px';
}

.ql-snow .ql-picker.ql-header .ql-picker-label::before,
.ql-snow .ql-picker.ql-header .ql-picker-item::before {
  content: '文本';
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="1"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="1"]::before {
  content: '标题1';
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="2"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="2"]::before {
  content: '标题2';
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="3"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="3"]::before {
  content: '标题3';
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="4"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="4"]::before {
  content: '标题4';
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="5"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="5"]::before {
  content: '标题5';
}
.ql-snow .ql-picker.ql-header .ql-picker-label[data-value="6"]::before,
.ql-snow .ql-picker.ql-header .ql-picker-item[data-value="6"]::before {
  content: '标题6';
}

.ql-snow .ql-picker.ql-font .ql-picker-label::before,
.ql-snow .ql-picker.ql-font .ql-picker-item::before {
  content: '标准字体';
}
.ql-snow .ql-picker.ql-font .ql-picker-label[data-value=serif]::before,
.ql-snow .ql-picker.ql-font .ql-picker-item[data-value=serif]::before {
  content: '衬线字体';
}
.ql-snow .ql-picker.ql-font .ql-picker-label[data-value=monospace]::before,
.ql-snow .ql-picker.ql-font .ql-picker-item[data-value=monospace]::before {
  content: '等宽字体';
}
</style>
