<template>
  <!--Drawer 抽屉实现侧边栏评论区-->
  <div>
    <div>你是： {{userType}}</div>
    <el-button @click="drawer=true" type="primary">点我打开评论区</el-button>
    <el-drawer
      title="评论内容"
      :visible.sync="drawer"
      :before-close="handleClose"
    > <!---->
      <div>
        <div v-for="(item, idx) in commentList" :key="idx">
          >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
          <p>id： {{ item.id}}</p>
          <p>L{{ item.layIDX}}</p>
          <p>评论内容：{{ item.content}}</p>
          <div v-if="item.isSub==false">
            <div v-for="(subitem,index) in item.sublayer" style="margin-left: 50px" :key="index">
              ------------------------------------
              <p>id： {{ subitem.id}}</p>
              <p>L{{ subitem.layIDX}}</p>
              <p>评论内容：{{ subitem.content}}</p>
            </div>
          </div>
        </div>
      </div>
    </el-drawer>
  </div>
</template>

<script>
//by qzx - component
export default {
  data() {
    return{
      userType: '面试官/面试者',
      drawer: false,
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
      ]
    }
  },
  methods: {
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

.el-drawer__body {
  overflow: auto;
}

</style>
