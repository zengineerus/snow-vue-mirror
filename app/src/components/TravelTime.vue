<template v-if='travelTime !== undefined'>
  <div id="travel-time">
    <div>
      <div>Travel Time</div>
    </div>
    <div>
      <div class="left">
        <span v-if="travelTime.TrafficReport">{{travelTime.TrafficReport.travel_time.hours}} hours</span>
        <span v-if="travelTime.TrafficReport">{{travelTime.TrafficReport.travel_time.minutes}} minutes</span>
      </div>
      <div class="right">
        <div v-if="travelTime.TrafficReport">To: {{travelTime.TrafficReport.destination}}</div>
        <div v-if="travelTime.TrafficReport">From: {{travelTime.TrafficReport.start_location}}</div>
      </div>
    </div>
  </div>
</template>

<style>
  #travel-time{
    background-color: rgb(112, 42, 42);
    border-bottom: 1px;
  }
  #travel-time .left{
    display: inline;
  }
   #travel-time .right{
    display: inline;
  }
</style>

<script>
import SnowVueService from '../services/snow-data';

export default {
  name: 'TravelTime',
  data () {
    return {
      travelTime: {}
    }
  },
  created () {
    SnowVueService.travelTime().then(response => {
      console.log('!!!!!!!!!!!!!!!', response.body);
      this.travelTime = response.body;
    });
  }
}
</script>
