<template>
    <p id="current-time">{{ currentTime }}</p>
    <p id="current-date">{{ currentDate }}</p>
</template>

<script>
  // Using a clock API to get the current time in a simple format
  import moment from 'moment';

  export default {
    name: 'DateTime',
    data() {
      return {
        // Elements for getDateTime function -- placeholder date/time for debugging
        currentDate: "OCTOBER 06 1989",
        currentTime: "PM 7:07",
      };
    },
    methods: {
      getDateTime: function() {
        var time = this;

        setInterval(function () {
          // Get the time and date from Moment.js
          // https://momentjs.com/
          time.currentDate = moment().format('MMMM D YYYY').toUpperCase();
          time.currentTime = moment().format('A h:mm');
        }, 1000);
      }
    },
    created (){
      this.currentDate = moment().format('MMMM D YYYY').toUpperCase();
      this.currentTime = moment().format('A h:mm');
      this.getDateTime()
    }
  }

</script>

<style></style>