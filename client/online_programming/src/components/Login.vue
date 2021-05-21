<template>
  <div id="login_form">
    <el-row type="flex" justify="center">
      <el-col :span="6">
        <div class="grid-content"></div>
      </el-col>
    </el-row>

    <el-row type="flex" justify="center">
      <el-col :span="20">
        <!-- <el-card shadow="always">
          <h1>登录页面</h1>
          <el-divider></el-divider> -->

        <el-form :model="validateForm" :rules="formRules" ref="validateForm" label-width="100px" class="demo-ruleForm">
          <!-- 用户ID -->
          <el-form-item label="用户ID" prop="username">
            <el-input placeholder="请输入用户ID" type="text" v-model="validateForm.username" autocomplete="off"></el-input>
          </el-form-item>

          <!-- 密码 -->
          <el-form-item label="密码" prop="password">
            <el-input placeholder="请输入密码" v-model="validateForm.password" show-password></el-input>
          </el-form-item>

          <!-- 确认按钮 -->
          <el-form-item>
            <el-button type="primary" @click="submitForm('validateForm')">确认</el-button>
            <el-button @click="resetForm('validateForm')">重置</el-button>
          </el-form-item>
        </el-form>

        <!-- </el-card> -->
      </el-col>

    </el-row>
    <div class="test">{{msg}}</div>
  </div>
</template>

<script>
  import {
    testget
  } from '../store/api.js'

  export default {
    data() {
      return {
        msg: "测试文本",
        validateForm: {
          username: '',
          password: ''
        },
        formRules: {
          username: [{
            required: true,
            message: '用户ID不能为空',
            trigger: 'blur',
          }, ],
          password: [{
            required: true,
            message: '密码不能为空',
            trigger: 'blur',
          }, ],
        },
      };
    },
    methods: {
      //发送axios请求
      sendRequest() {
        testget().then(res => {
          this.msg = res;
          console.log(res);
        });
        
      },
      open(){
        this.msg = 'open';
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            console.log("success!");
            let that = this;
            let loginData = {
              username: that.validateForm.username,
              password: that.validateForm.password,
            }
            //this.sendRequest();
            
            this.$store.dispatch('signupRequest', signupData).then(res => {
              console.log(res);
              var ifExist = res.ifExist;
              var msg = res.msg;
              if(ifExist){
                //登录成功
                
              }else{
                //用户不存在，登录失败
              }
            })

            // this.axios.post(url, loginData).then(response => {
            //   console.log(response.data) // 得到返回结果数据 
            //   var ifExist = response.data.ifExist;
            //   var msg = response.data.msg;
            //   if(ifExist){
            //     if(response.data.userType){//面试官true
            //       //跳转到面试官首页，在首页显示
            //     }else{//面试者false
            //       //跳转到面试者首页
            //     }
            //   }
            // }).catch(error => {
            //   console.log(error.message)
            // })

          } else {
            console.log('error submit!!');
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      }
    }
  }

</script>

<style>
  .content {
    margin: 0 auto;
  }

  .el-card {
    border-radius: 30px;
    /* box-shadow: 0 2px 12px 0 rgb(243, 102, 102); */
    /* box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); */
  }

  .grid-content {
    /* background: rgb(14, 214, 131); */
    border-radius: 4px;
    min-height: 30px;
  }

  .el-row {
    margin-bottom: 20px;
  }

</style>
