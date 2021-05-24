<template>
  <div>
    <p class="msg">
        {{msg}}
    </p>
  </div>
</template>

<script>
export default {// 配置对象（与Vue一致）
  data () { // 必须函数
    return {
      msg: 'shiyixia'
    }
  }
}
</script>

<style>
.msg{
    color:red;
    font-size: 40px;
}
</style>
