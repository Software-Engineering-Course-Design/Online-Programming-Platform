<template>
  <el-container id="tab">
    <el-header>发起面试页</el-header>
    <el-main>
      <el-form ref="form" :model="form" :rules="rules">
        <el-form-item label="请选择题目数量" prop="num">
          <el-radio-group v-model="form.num">
            <el-radio-button v-for="n in 5" :label="n"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="请选择出题类型" prop="type">
          <el-radio-group v-model="form.type">
            <el-radio-button v-for="item in options" :label="item.value"></el-radio-button>
          </el-radio-group>
        </el-form-item>
        <div v-if="form.type=='自主选题'">
          <div>test</div>
        </div>
        <el-form-item label="请输入要邀请的面试者ID（可选）" prop="people">
          <el-input v-model="form.people">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submit">发起面试</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
    </el-main>
  </el-container>
</template>

<script>
//by qzx
export default {
  name: "addNewExam",
  data(){
    return{
      form: {
        num: 'null',
        type: -1,
        people: '',
      },
      rules:{
        num:[
          { type:'number', require: true, message: '请选择题目数量'},
        ],
        type:[
          { type:'string', require: true, message: '请选择出题方式'},
        ],
        people: [
          { message: '请输入面试者id', trigger: 'blur'}
        ]

      },
      options:[
        { value: '自主选题'},
        { value: '随机抽题'}
      ]
    }
  },
  methods:{
    submit(){
      console.log(this.form);
      this.$refs.form.validate((valid) => {
        if(valid()){
          console.log('submit!');
        }
        else {
          console.log('error!');
          return false;
        }
      });
    },
    reset(){
      this.$refs.form.resetFields();
    }
  }
}
</script>

<style scoped>
@import "../assets/qzx_css.css";
</style>
