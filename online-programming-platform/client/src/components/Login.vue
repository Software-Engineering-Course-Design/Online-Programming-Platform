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
        dialogVisible: false, //提示框显示
        alertMsg: '',
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
      open() {
        this.msg = 'open';
      },
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            let that = this;
            let loginData = {
              username: that.validateForm.username,
              password: that.validateForm.password,
            }
            //this.sendRequest();

            this.$store.dispatch('loginRequest', loginData).then(res => {
              console.log(res);
              var ifExist = res.ifExist;
              var userType = res.userType;
              var msg = res.msg;
              if (ifExist) {
                //登录成功
                this.$store.commit("userStatus", true);
                this.$store.commit("setUserType", userType);
                // this.$store.dispatch("setStatus",true);
                // this.$store.dispatch("setType", userType);
                //Vuex在用户刷新的时候userStatus会回到默认值false，所以需要用到HTML5储存
                //记录登录状态、用户名、用户类型
                // sessionStorage.setItem("LoginStatus", "isLogin");
                // sessionStorage.setItem("username", that.validateForm.username);
                this.$cookies.set("LoginStatus", "isLogin");
                this.$cookies.set("username", that.validateForm.username);
                if (userType) {
                  // sessionStorage.setItem("userType", "HR");
                  this.$cookies.set("userType", "HR");
                } else {
                  // sessionStorage.setItem("userType", "applicant");
                  this.$cookies.set("userType", "applicant");
                }

                this.$message({
                  showClose: true,
                  message: msg,
                  type: 'success',
                  duration: 2300,

                })
                //登录成功后跳转到指定页面

                if (!userType) {//跳转到面试者首页
                  this.$router.push("/applicant");
                }else{//跳转到面试官首页
                  this.$router.push("/interviewer/viewExamList");//以后更改路径
                }

              } else {
                //用户不存在，登录失败
                this.alertMsg = msg;
                this.dialogVisible = true;
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
      },
      handleClose(done) {
        this.$confirm('确认关闭？')
          .then(_ => {
            done();
          })
          .catch(_ => {});
      },
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
