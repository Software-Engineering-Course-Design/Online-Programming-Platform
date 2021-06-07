<template>
  <!--Drawer 抽屉实现侧边栏评论区-->
  <div id="drawer">
    <div>你是： {{username}}</div>
    <el-button @click="drawer=true" type="primary">点我打开评论区</el-button>
    <el-drawer
      title="评论内容"
      :visible.sync="drawer"
      :before-close="handleClose"> <!---->
      <el-collapse v-model="activeName">
        <div v-for="(item, idx) in commentList" :key="idx">
          <el-collapse-item :title="item.content" :name="idx">
            <p>id： {{ item.id}}</p>
            <p>L{{ item.layIDX}}</p>
            <div v-if="item.isSub==false">
              <el-collapse v-model="activeName2">
                <div v-for="(subitem,index) in item.sublayer" style="margin-left: 50px" :key="index">
                  <el-collapse-item :title="subitem.content" :name="index">
                    <p>id： {{ subitem.id}}</p>
                    <p>L{{ subitem.layIDX}}</p>
                  </el-collapse-item>

                </div>
              </el-collapse>
            </div>
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
      userType: '面试官',
      username: this.p_username,
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
          isSub: false,//是否为楼中楼回复
          sublayer: [
            {
            id: 'testUsr1',
            layIDX: 1,
            content: 'testComment1',
            isSub: true,
            sublayer: []
            },
            {
              id: 'testUsr2',
              layIDX: 2,
              content: 'testComment2',
              isSub: true,
              sublayer: []
            },
          ]//楼中楼回复列表，如果isSub为true，设置sublayer为空；如果isSub为false，允许给sublayer赋值
        },
        {
          id: 'testUsr1',
          layIDX: 2,
          content: 'testComment1',
          isSub: false,
          sublayer: [
            {
            id: 'testUsr2',
            layIDX: 1,
            content: 'testComment2',
            isSub: true,
            sublayer: []
            },
          ]
        },
      ],

    }
  },
  props:{
    p_username: String,
  },
  methods: {
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
          alert('submit!');

          /*
          id: 'testUsr0',//用户id
          layIDX: 1,//主楼层数
          content: 'testComment0',//评论内容
          isSub: false,//是否为楼中楼回复
          sublayer: [
            {
            id: 'testUsr1',
            layIDX: 1,
            content: 'testComment1',
            isSub: true,
            sublayer: []
            },
            {
              id: 'testUsr2',
              layIDX: 2,
              content: 'testComment2',
              isSub: true,
              sublayer: []
            },
          ]*/
          let len = this.commentList.length;
          const temp_c = {
            id: this.username,
            layIDX: len + 1,
            content: this.form.commentText,
            isSub: false,
            sublayer: [],
          };
          this.commentList.push(temp_c);

        } else {
          console.log('error submit!!');
          return false;
        }
      });
    },
  }
}
</script>

<style>

.el-drawer__body {
  overflow: auto;
}
#drawer{
  margin: 0 auto;
  left: 95%;
}

</style>
