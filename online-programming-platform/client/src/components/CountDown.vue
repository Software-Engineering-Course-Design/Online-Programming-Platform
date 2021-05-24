<template>
  <div class="count-down" style="height:40px">
    {{surplus|filterTime}}
  </div>
</template>
<script>
  export default {
    name: 'CountDown',
    props: {
      endHours: {
        type: Number,
        required: true,
        default: 0
      }
    },
    created() {
      this.beforeDestroy();
    },
    data() {
      return {
        surplus: '',
        diffSeconds: 0,
        interval: undefined,
        year: '',
        month: '',
        day: '',
        hours: '',
        minutes: '',
        seconds: '',
        endHours:'',
        endMinutes:'',
        endSeconds:'',
      }
    },
    methods: {
      getTime() {
        var date1 = new Date();
        this.year = date1.getFullYear();
        this.month = date1.getMonth() + 1;
        this.day = date1.getDate();
        this.hours = date1.getHours();
        this.minutes = date1.getMinutes();
        this.seconds = date1.getSeconds();
        //return year + "年" + month + "月" + day + "日" + hours + ":" + minutes + ":" + seconds
      },
      setEndTime(){

      },

      beforeDestroy() {
        if (this.interval) {
          clearInterval(this.interval)
        }
        let date = new Date();
        if (date.getHours() > this.endHours) {
          this.surplus = '面试结束';
          return
        }
        if (date.getHours() === this.endHours) {
          this.surplus = '面试中';
          return
        }
        //差距小时数
        const diffHours = this.endHours - date.getHours() - 1;
        // 差距分钟数
        const diffMinutes = 60 - date.getMinutes() - 1;
        // 差距秒数
        const diffSeconds = 60 - date.getSeconds();
        // 转化为对应的秒数
        this.diffSeconds = diffHours * 3600 + diffMinutes * 60 + diffSeconds;
        // 当时间每过1秒 秒数差距应该 - 1
        this.interval = setInterval(() => {
          this.diffSeconds -= 1
        }, 1000)
      }
    },
    watch: {
      diffSeconds(newV) {
        // 当前的秒数 / 3600，向下取整，获取到转化的小时数
        let hours =
          Math.floor(newV / 3600);
        // 当前秒数 / 60，向下取整
        // 获取到所有分钟数 3600 / 60 = 60分钟
        // 对60取模，超过小时数的分钟数
        let minutes =
          Math.floor(newV / 60) % 60;
        // 当前的秒数 % 60，获取到 超过小时数、分钟数的秒数（秒数）
        let seconds = newV % 60;
        // 拼装数据
        this.surplus = hours + ':' + minutes + ':' + seconds;
        /**
         * 在当前秒数 变为 0， 需要修改展示数据
         */
        if (newV === 0) {
          this.beforeDestroy()
        }
      }
    }
  }

</script>
<style scoped>
  .count-down {
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff
  }

</style>
