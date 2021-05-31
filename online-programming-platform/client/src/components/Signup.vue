<template>
  <div id="signup_form">
    <el-row type="flex" justify="center">
      <el-col :span="6">
        <div class="grid-content"></div>
      </el-col>
    </el-row>

    <el-row type="flex" justify="center">
      <el-col :span="20">
        <!-- <el-card shadow="always">
          <h1>注册页面</h1>
          <el-divider></el-divider> -->

        <el-form :model="validateForm" ref="validateForm" :rules="formRules" label-width="100px" class="validateForm">
          <!-- 用户名 -->
          <el-form-item label="用户ID" prop="username">
            <el-input placeholder="请输入用户ID" type="text" v-model="validateForm.username" autocomplete="off"></el-input>
          </el-form-item>

          <!-- 密码 -->
          <el-form-item label="密码" prop="password">
            <el-input placeholder="请输入密码" v-model="validateForm.password" show-password></el-input>
          </el-form-item>

          <!-- 确认密码 -->
          <el-form-item label="确认密码" prop="checkpwd">
            <el-input placeholder="请确认密码" v-model="validateForm.checkpwd" show-password></el-input>
          </el-form-item>

          <!-- 用户类型 -->
          <el-form-item label="用户类型" prop="userType">
            <el-radio-group v-model="validateForm.userType">
              <el-radio :label=false>面试者</el-radio>
              <el-radio :label=true>面试官</el-radio>
            </el-radio-group>
          </el-form-item>

          <!-- 面试官邀请码 -->
          <el-form-item label="邀请码" prop="hr_code" v-show="validateForm.userType">
            <el-input placeholder="请输入邀请码" v-model="validateForm.hr_code"></el-input>
          </el-form-item>

          <!-- 确认按钮 -->
          <el-form-item>
            <el-button type="primary" @click="submitForm('validateForm')">提交</el-button>
            <el-button @click="resetForm('validateForm')">重置</el-button>
          </el-form-item>
        </el-form>

        <!-- </el-card> -->
      </el-col>

    </el-row>
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
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.validateForm.password) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
      var validateHR = (rule, value, callback) => {
        if (this.validateForm.userType == true) {
          if (value === '') {
            callback(new Error('邀请码不能为空'));
          } else {
            callback();
          }
        } else {
          callback();
        }
      };
      return {
        dialogVisible: false, //提示框显示
        alertMsg: '',
        validateForm: {
          username: '',
          password: '',
          checkpwd: '',
          userType: false,
          hr_code: '',
        },
        formRules: {
          username: [{
            required: true,
            message: '用户ID不能为空',
            trigger: 'blur'
          }],
          password: [{
            required: true,
            message: '密码不能为空',
            trigger: 'blur'
          }],
          checkpwd: [{
            required: true,
            message: '两次输入密码不一致',
            validator: validatePass,
            trigger: 'blur'
          }],
          hr_code: [{
            validator: validateHR,
            message: '面试官邀请码不能为空',
            trigger: 'blur'
          }],
        },
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            let that = this;
            let signupData = {
              username: that.validateForm.username,
              password: that.validateForm.password,
              checkpwd: that.validateForm.checkpwd,
              userType: that.validateForm.userType,
              hr_code: that.validateForm.hr_code,
            };
            // axios请求
            this.$store.dispatch('signupRequest', signupData).then(res => {
              console.log(res);
              var ifExist = res.ifExist;
              var msg = res.msg;
              if (!ifExist) {
                //注册成功，可以登录了
                this.alertMsg = '注册成功！请前往登录';
                this.dialogVisible = true;

              } else {
                //用户已存在，重新取一个用户名
                //this.alertMsg = msg;
                this.alertMsg = '注册失败！该用户名已存在，请更换用户名';
                this.dialogVisible = true;
              }
            })


            // this.axios.post(url, loginData).then(response => {
            //   console.log(response.data) // 得到返回结果数据 
            //   var ifExist = response.data.ifExist;
            //   var msg = response.data.msg;
            //   if(!ifExist){
            //     //注册成功，可以登录
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
      },
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
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
