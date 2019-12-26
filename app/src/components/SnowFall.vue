<template>
  <ion-card id="new-snow" color="secondary">
    <!-- <ion-card-header>
        <ion-card-title>SnowFall</ion-card-title>
        <ion-card-subtitle>Overnight and 24 hour</ion-card-subtitle>
    </ion-card-header>-->
    <ion-card-content>
      <ion-grid v-if="snowData.SnowReport">
        <ion-row>
          <ion-col id="overnight-header">
            <ion-label >Overnight SnowFall</ion-label>
          </ion-col>
          <ion-col  id="day-header">
            <ion-label>24 Hour Snow</ion-label>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-col id="overnight-label">
            <ion-label id="overnight">{{snowData.SnowReport[0].Depth.Inches}} in</ion-label>
          </ion-col>
          <ion-col id="day-label">
            <ion-label id="day">{{snowData.SnowReport[1].Depth.Inches}} in</ion-label>
          </ion-col>
        </ion-row>
      </ion-grid>
      <ion-label v-else>{{snowData.message}}</ion-label>
    </ion-card-content>
  </ion-card>
</template>

<style>
#new-snow {
  background-color: #222222b0;
  border-bottom: 1px;
}
#new-snow #overnight-header{
  text-align: left;
}
#new-snow #day-header{
  text-align: left;
}
#new-snow #overnight-label{
  text-align: left;
  text-transform: uppercase;
}
#new-snow #day-label{
  text-align: left;
  text-transform: uppercase;
}
</style>

<script>
import SnowVueService from '../services/snow-data';

export default {
  name: 'SnowFall',
  data () {
    return {
      snowData: {}
    };
  },
  created () {
    SnowVueService.snowReport().then(response => {
      this.snowData = response.body;
    }, response => {
      this.snowData = { 'message': 'Data is not available.' }
    });
  }
};
</script>
