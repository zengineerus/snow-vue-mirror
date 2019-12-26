<template>
  <ion-card id="travel-time" name="ion_card" color="secondary">

    <ion-card-content
      v-if="this.location.Location || travelTime.TrafficReport"
      name="ion_content"
    >
      <ion-grid v-if="travelTime.TrafficReport">
        <ion-row>
          <ion-col>
            <ion-label>Travel Time</ion-label>
          </ion-col>
          <ion-col>
            <ion-label>Home Zip</ion-label>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-col>
              <ion-label>{{travelTime.TrafficReport.travel_time.hours}} hours</ion-label>
              <ion-label>{{travelTime.TrafficReport.travel_time.minutes}} minutes</ion-label>
          </ion-col>
          <ion-col>
              <ion-label>{{travelTime.TrafficReport.start_location}}</ion-label>
          </ion-col>
        </ion-row>
      </ion-grid>
      <ion-label v-else>Server is unavailable.</ion-label>

    </ion-card-content>
    <ion-card-content v-else>
        <ion-input name="zip" v-model="zip">Enter Zip</ion-input>
        <ion-button v-on:click="updateLocation()">submit</ion-button>
    </ion-card-content>
  </ion-card>
</template>

<style>
  #travel-time{
    background-color: #222222b0;
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
      travelTime: {},
      location: {},
      zip: 80000
    };
  },
  created () {
    Promise.all([SnowVueService.getCurrentLocation(),
      SnowVueService.travelTime()])
      .then(([locationResponse, travelTimeResponse]) => {
        this.location = locationResponse.body;
        this.travelTime = travelTimeResponse.body;
      });
  },
  methods: {
    updateLocation () {
      SnowVueService.travelTimeZip(
        document.querySelector('input[name=zip]').value
      ).then(
        response => {
          console.log('^^^^^^^^^', response.body);
          this.travelTime = response.body;
        },
        response => {
          console.log('&&&&&&&&&&', response.body);
          this.travelTime = { message: 'Data is not available.' };
        }
      );
    }
  }
};
</script>
