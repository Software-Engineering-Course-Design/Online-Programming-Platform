<template>
  <div id="app">
    <el-row type="flex" justify="center">
      <!-- justify 对齐方式 -->
      <el-col :span="6">
        <div class="grid-content"></div>
      </el-col>
    </el-row>

    <el-row type="flex" justify="center">

      <el-col :span="6">
        <el-card shadow="always">
          <h1>注册页面</h1>
          <el-divider></el-divider>

          <el-form :model="nameValidateForm" ref="nameValidateForm" label-width="100px" class="demo-ruleForm">
            <!-- 用户名 -->
            <el-form-item label="用户ID" prop="name" :rules="[
                    { required: true, message: '用户ID不能为空'},
                    ]">
              <el-input placeholder="请输入用户ID" type="text" v-model="nameValidateForm.name" autocomplete="off"></el-input>
            </el-form-item>

            <!-- 密码 -->
            <el-form-item label="密码" prop="password" :rules="[
                    { required: true, message: '密码不能为空'},
                    ]">
              <el-input placeholder="请输入密码" v-model="nameValidateForm.password" show-password></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitForm('nameValidateForm')">提交</el-button>
              <el-button @click="resetForm('nameValidateForm')">重置</el-button>
            </el-form-item>
          </el-form>

        </el-card>
      </el-col>

    </el-row>

  </div>
</template>

<script>
  import Vue from 'vue';
  export default {
    data() {
      return {
        nameValidateForm: {
          name: '',
          password: ''
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('Name:' + this.nameValidateForm.name + ';Password:' + this.nameValidateForm.password);
            // console.log(this.nameValidateForm.name);

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
    min-height: 80px;
  }

  .el-row {
    margin-bottom: 20px;
  }

</style>
