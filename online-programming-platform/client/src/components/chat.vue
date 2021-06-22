<template>
  <!--Drawer 抽屉实现侧边栏评论区-->
  <div id="drawer">
    <el-button @click="drawer=true" type="primary" plain>查看评论</el-button>
    <el-drawer
      title="评论内容"
      :visible.sync="drawer"
      :before-close="handleClose"> <!---->
      <div style="padding: 5%">
      <div>{{username}}，你好！</div>
      <el-collapse v-model="activeName">
        <div v-for="(item, idx) in commentList" :key="idx">
          <el-collapse-item :title="'L'+(idx+1).toString()+': '+item.content" :name="idx">
            <p>id： {{ item.username}}</p>
            <el-button @click="reply(item.username)">回复</el-button>
          </el-collapse-item>
        </div>
      </el-collapse>
      <el-form ref="form" :model="form" :rules="rules">
        <el-form-item prop="commentText">
          <el-input v-model="form.commentText"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">发送评论</el-button>
        </el-form-item>
    </el-form>
      </div>
    </el-drawer>
  </div>
</template>

<script>
//by qzx - component
export default {
  data() {
    return {
      activeName: '0',
      activeName2: '0',
      userType: this.p_userType,
      username: this.p_username,
      questionID: this.p_questionID,
      drawer: false,
      form: {
        commentText: '',
      },
      rules: {
      commentText: [{
        required: true,
        message: '请输入评论内容！',
        trigger: 'blur'
      }],
    },
      commentList: [
        {
          id: 'testUsr0',//用户id
          layIDX: 1,//主楼层数
          content: 'testComment0',//评论内容
        },
        {
          id: 'testUsr1',
          layIDX: 2,
          content: 'testComment1',
        },
      ],
      commentTemp:[],
    }
  },
  props:{
    p_username: String,
    p_userType: Boolean,
    p_questionID: Number
  },
  methods: {
    reply(name){
      this.form.commentText = "回复@"+name+'：';
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done();
        })
        .catch(_ => {});
    },
    onSubmit(){
      console.log(this.form);
      this.$refs.form.validate((valid) => {
        if (valid) {

          this.$message({
              showClose: true,
              message: '发送成功！',
              type: 'success'
            });
          let len = this.commentList.length;
          const temp_c = {
            id: this.username,
            layIDX: len + 1,
            content: this.form.commentText,
          };
          this.commentList.push(temp_c);
          const postData = {
            "senderID": this.username,
            "commentContent": this.form.commentText,
            "questionID": this.questionID,
          };
          this.$store.dispatch('pubDiscussRequest',postData).then(res=>{
            console.log(res);
            this.form.commentText='';
          });

        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
    onStart(){
      const postData = {
        'username': this.username,
        'userType': this.userType,
        'questionID': this.questionID,
      };
      this.$store.dispatch('discussRequest',postData).then(res => {
        console.log(res);
        this.commentList = res.commentList;
      });
    },
  },
  mounted() {
    console.log(this.p_questionID,'pid')
    this.onStart();
  },
  watch:{
    p_questionID(val){
      console.log(this.p_questionID,'pid',val,'val')
      this.questionID=val;
      this.onStart();
    }
  }
}
</script>

<style>


#drawer{
  margin: 0 auto;
  left: 95%;
}

</style>
