<template>
  <el-container>
    <el-header id="qTitle"><h2>{{ title }}</h2></el-header>
    <el-main>
      <div v-html="content" v-highlight></div>
    </el-main>
  </el-container>
</template>

<script>
  //by qzx - component
  export default {
    data() {
      return {
        title: '',
        content: '',
      }
    },
    props: {
      p_title: String,
      p_content: String,
    },
    created() {
      this.title = this.p_title;
      this.content = this.p_content;
    },

    //这里用watch方法来监听父组件传过来的值，来实现实时更新
    watch: {
      p_title(val) { //mp_title即为父组件的值，val参数为值
        this.title = val; //将父组件的值赋给 子组件的值
      },
      p_content(val) {
        this.content = val;
      }
    }


  }

</script>

<style scoped>
  .el-container {
    overflow: auto;
  }
  #qTitle{

  }
</style>
