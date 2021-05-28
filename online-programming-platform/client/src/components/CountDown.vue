<template>
  <div class="count-down" style="height:40px">
    剩余时间：{{countDownList}}
  </div>
</template>
<script>
  export default {
    name: 'CountDown',
    props: {
      interviewTime: {
        type: Number,
        // required: true,
        default: 0
      },
      startTime: {
        type: String,
      },
      endTime: {
        type: String,
      }
    },
    created() {
      this.countDownAction();
    },
    data() {
      return {
        countDownList: '00时00分00秒',

      };
    },
    methods: {
      //格式
      timeFormat(param) {
        return param < 10 ? '0' + param : param;
      },
      //时间处理
      countDownAction(it) {
        var interval = setInterval(() => {
          // 获取当前时间
          let newTime = new Date().getTime();
          //获取面试开始时间
          let interviewStartTime = new Date(this.startTime).getTime();
          //获取结束时间
          let interviewEndTime = new Date(this.endTime).getTime();

          let obj = null;
          //if (newTime - interviewStartTime > 0) {
            // 如果活动未结束，对时间进行处理
            if (interviewEndTime - newTime > 0) {
              let time = (interviewEndTime - newTime) / 1000;
              // 获取天、时、分、秒
              let day = parseInt(time / (60 * 60 * 24));
              let hour = parseInt(time % (60 * 60 * 24) / 3600);
              let min = parseInt(time % (60 * 60 * 24) % 3600 / 60);
              let sec = parseInt(time % (60 * 60 * 24) % 3600 % 60);
              obj = {
                day: this.timeFormat(day),
                hour: this.timeFormat(hour),
                min: this.timeFormat(min),
                sec: this.timeFormat(sec)
              };
            } else { // 活动已结束，全部设置为'00'
              obj = {
                day: '00',
                hour: '00',
                min: '00',
                sec: '00'
              };
              clearInterval(interval);
            }
          //} else {
          //  console.log('面试还没开始')
          //}

          this.countDownList = obj.hour + '时' + obj.min + '分' + obj.sec + '秒';
        }, 1000);
      },
    }
  }

</script>
<style scoped>
  .count-down {
    display: flex;
    justify-content: center;
    align-items: center;
    color: black;
  }

</style>
