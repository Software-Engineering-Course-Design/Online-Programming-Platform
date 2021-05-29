<template>
  <div>
    <el-form ref="form" :model="form" :rules="rules">
      <!--题目数量-------------------------->
      <el-form-item label="请选择题目数量" prop="num" required>
        <el-radio-group v-model="form.num">
          <el-radio-button v-for="n in 5" :label="n" :key="n"></el-radio-button>
        </el-radio-group>
      </el-form-item>
      <!--出题方式-------------------------->
      <el-form-item label="请选择出题方式" prop="type" required>
        <el-radio-group v-model="form.type">
          <el-radio-button v-for="(item, idx) in options" :label="item.value" :key="idx"></el-radio-button>
        </el-radio-group>
      </el-form-item>
      <div v-if="form.type=='自主选题'">
        此处应该使用浏览题目列表组件进行浏览选题(此处仅测试)
        <div v-for="i in form.num">
          <el-form-item label="请输入要选择的题目ID" >{{i}}
            <el-input></el-input>

          </el-form-item>
        </div>
      </div>
      <!--考试时长-------------------------->
      <el-form-item label="请选择面试起止时间" required>

        <el-form-item prop="time_date">
          <el-date-picker v-model="form.time_date" type="date" value-format="yyyy-MM-dd" placeholder="选择日期" :picker-options="pickerOptions"
          style=""></el-date-picker>
        </el-form-item>
        <el-form-item prop="time_detail">
          <el-time-picker v-model="form.time_detail" value-format="HH:mm:ss" placeholder="选择时间范围" is-range arrow-control
          range-separator="至" start-placeholder="开始时间" end-placeholder="结束时间"  style=""></el-time-picker>
        </el-form-item>

      </el-form-item>
      <!--面试者名单-------------------------->
      <el-form-item label="请输入要邀请的面试者ID（可选）" prop="people">
        <el-input v-model="form.people">
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submit">发起面试</el-button>
        <el-button @click="reset">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "newExam",
  data(){
    return{
      form: {
        num: this.prop_num,
        type: this.prop_type,
        qID: this.prop_qID,
        time_date: 0,
        time_detail:0,
        people: '',
      },
      rules:{
        num:[
          { type: "number", require: true, message: '请选择题目数量', trigger: 'blur'},
        ],
        type:[
          { require: true, message: '请选择出题方式', trigger: 'blur'},
        ],
        time_date: [
          { type: "string", require: true, message: '请选择日期', trigger: 'change'},
        ],
        time_detail: [
          {  type: "array", require: true, message: '请选择时间', trigger: 'change'},
        ],
        people: [
          { message: '请输入面试者id', trigger: 'blur'}
        ]

      },
      options:[
        { value: '自主选题'},
        { value: '随机抽题'}
      ],
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now();
        },
        shortcuts: [{
          text: '今天',
          onClick(picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: '昨天',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24);
            picker.$emit('pick', date);
          }
        }, {
          text: '一周前',
          onClick(picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
            picker.$emit('pick', date);
          }
        }],
      }
    }
  },
  methods:{
    submit(){
      this.$refs.form.validate((valid) => {

        if(valid){
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
      this.form.time_date=0;
      this.form.time_detail=0;
    },
  },
  props:{
    prop_num: { default: 'test'},
    prop_type: { default: '随机抽题'},
    prop_qID: Array
  },
  created() {

  }
}
</script>

<style scoped>

</style>
