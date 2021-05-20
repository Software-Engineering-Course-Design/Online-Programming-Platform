<template>
    <div id="app-interview">
    <el-container>
      <el-header>
        <el-row :gutter="20">
          <el-col :span="4">
            <div class="grid-content">
              <el-select v-model="question">
                <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value"
                  :disabled="item.disabled">
                  <span style="float: left">{{ item.label }}</span>
                  <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
                </el-option>
              </el-select>
            </div>
          </el-col>
          <el-col :span="4">
            <div class="grid-content bg-purple">评论区</div>
          </el-col>
          <el-col :span="8">
            <div class="grid-content bg-purple"></div>
          </el-col>
          <el-col :span="4">
            <div class="grid-content bg-purple"></div>
          </el-col>
          <el-col :span="4">
            <div class="grid-content bg-purple">倒计时</div>
          </el-col>
        </el-row>

      </el-header>
      <el-main>
        <el-row :gutter="10">
          <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12">
            <div class="grid-content bg-purple"></div>
          </el-col>

          <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12">
            <code-editor></code-editor>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
      
      
  </div>
</template>

<script>
  import CodeEditor from '../components/CodeEditor.vue'

  export default {
    components: {
      CodeEditor
    },
    data() {
      return {
        question: 'Question1',
        questionOptions: [],
        options: [{
          value: 'Question1', //value是questionID
          label: 'Question1'
        }, {
          value: 'Question2',
          label: 'Question2',
          disabled: true
        }, {
          value: 'Question3',
          label: 'Question3'
        }, {
          value: 'Question4',
          label: 'Question4'
        }, {
          value: 'Question5',
          label: 'Question5'
        }],

      };
    },
    methods: {
      currentQuestion() {

      },
      createOptions() {

      },
      mounted() {
        const url = '';
        this.axios.post(url, loginData).then(response => {
          console.log(response.data) // 得到返回结果数据 
          var ifExist = response.data.ifExist;
          var msg = response.data.msg;
          if (ifExist) {
            if (response.data.userType) { //面试官true
              //跳转到面试官首页，在首页显示
            } else { //面试者false
              //跳转到面试者首页
            }
          }
        }).catch(error => {
          console.log(error.message)
        })
      },
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
