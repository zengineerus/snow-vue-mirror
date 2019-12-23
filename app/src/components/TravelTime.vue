<template>
  <form novalidate>
  <ion-card name="ion_card" color="secondary">
    <ion-card-header name="ion_header">
      <ion-card-title name="ion_title">Travel Time</ion-card-title>
      <ion-card-subtitle>From Zip code to resort</ion-card-subtitle>
    </ion-card-header>
    <ion-card-content name="ion_content">
      <ion-list v-if="travelTime.TrafficReport" >
        <ion-item name="ion_item">
          <ion-label>Zip Code:</ion-label>
          <span :class="{'error': errors.has('zip')}">
            <ion-input id="inputZip" name="zip" type="text" value="80202" placeholder="80202" maxlength="5" v-validate="{ required: true, regex: /^\d{5}$/}"></ion-input>
          </span>
        </ion-item>
        <ion-item v-show="errors.has('zip')" class="error">
          <ion-label>{{ errors.first('zip') }}</ion-label>
        </ion-item>
        <ion-item name="ion_item">
          <ion-label name="ion_label">To: {{travelTime.TrafficReport.destination}}</ion-label>
        </ion-item>
        <ion-item>
          <ion-label>{{travelTime.TrafficReport.travel_time.hours}} hours</ion-label>
          <ion-label>{{travelTime.TrafficReport.travel_time.minutes}} minutes</ion-label>
        </ion-item>
      </ion-list>
      <ion-label v-else id="travelTimeMessage">{{travelTime.message}}</ion-label>
    </ion-card-content>
  </ion-card>
  </form>
</template>

<style scoped>
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
  mounted () {
    SnowVueService.travelTime().then(response => {
      this.travelTime = response.body;
    }, response => {
      this.travelTime = { 'message': 'Data is not available.' }
    })
  }
}
</script>
