<template>
  <ion-card id="new-snow" color="secondary">
    <!-- <ion-card-header>
        <ion-card-title>SnowFall</ion-card-title>
        <ion-card-subtitle>Overnight and 24 hour</ion-card-subtitle>
    </ion-card-header>-->
    <ion-card-content>
      <ion-grid v-if="snowData.SnowReport">
        <ion-row>
          <ion-col>
            <ion-label>Overnight SnowFall</ion-label>
          </ion-col>
          <ion-col>
            <ion-label>24 Hour Snow</ion-label>
          </ion-col>
        </ion-row>
        <ion-row>
          <ion-col>
            <ion-label id="overnight">{{snowData.SnowReport[0].Depth.Inches}} inches</ion-label>
          </ion-col>
          <ion-col>
            <ion-label id="day">{{snowData.SnowReport[1].Depth.Inches}} inches</ion-label>
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
#new-snow .left {
  display: inline;
}
#new-snow .right {
  display: inline;
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
    SnowVueService.snowReports().then(response => {
      this.snowData = response.body;
    }, response => {
      this.snowData = { 'message': 'Data is not available.' }
    });
  }
};
</script>
