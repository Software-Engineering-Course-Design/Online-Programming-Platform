<template>
  <div>
    <el-button type="primary" id="logout-btn" @click="dialogVisible=true" icon="el-icon-user-solid" plain>{{username}}
    </el-button>
      <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
      <p class="para">尊敬的用户 {{username}}:</p>
      <p class="para" id="in">是否退出登录？</p>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="user_logout()">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
  export default {
    props: {
      username: {
        type: String,
      },
    },
    data() {
      return {
        dialogVisible: false,
      };
    },
    methods: {
      user_logout() {
        let getStatus = this.$cookies.get("LoginStatus");
        if (getStatus === 'isLogin') {
          this.$cookies.remove("LoginStatus");
          this.$cookies.remove("username");
          this.$cookies.remove("userType");
          this.$store.commit("userStatus", false);
          this.$store.commit("setUserType", '');
          this.dialogVisible = false;
          //跳转回登录注册页面
          this.$router.push('/sign');
        } else {
          this.$message({
            showClose: true,
            message: '您尚未登录，无法退出登录',
            type: 'warning',
            duration: 2300,

          })
        }

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
  #logout-btn {
    position: absolute;
    padding: 5px;
    text-align: center;
    right: 10px;
    top: 10px;
    font-size: 22px;
  }

  .para {
    font-size: 20px;
  }

  #in {
    text-indent: 2em;
  }

</style>
