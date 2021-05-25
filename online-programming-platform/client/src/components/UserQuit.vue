<template>
  <div>
    <el-button type="primary" id="logout-btn" @click="dialogVisible=true" round>退出登录</el-button>
    <!-- 提示框 -->
      <el-dialog title="提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
      <span>是否退出登录？</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" @click="user_logout()">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        dialogVisible: false,
      };
    },
    methods: {
      user_logout() {
        let getStatus = localStorage.getItem("LoginStatus");
        if (getStatus === 'isLogin') {
          localStorage.removeItem("LoginStatus");
          this.dialogVisible = false;
          console.log('退出登录');
        }else{
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
    position: fixed;
    padding: 5px;
    text-align: center;
    left: 10px;
    top: 10px;
  }

</style>
