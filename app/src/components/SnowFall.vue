<template>
<ion-card id="new-snow">
  <ion-card-header>
    <ion-card-title>SnowFall</ion-card-title>
    <ion-card-subtitle>Overnight and 24 hour</ion-card-subtitle>
  </ion-card-header>
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
        <ion-label>{{snowData.SnowReport[0].Depth.Inches}} inches</ion-label>
      </ion-col>
      <ion-col>
        <ion-label>{{snowData.SnowReport[1].Depth.Inches}} inches</ion-label>
      </ion-col>
    </ion-row>
  </ion-grid>
  <ion-label v-else>{{snowData.message}}</ion-label>
</ion-card-content>
</ion-card>
  <!-- <div id="new-snow">
    <div>
      <div class="left">Overnight SnowFall</div>
      <div class="right">24 Hour Snow</div>
    </div>
    <div>
      <div class="left" v-if="snowData.SnowReport"> {{snowData.SnowReport[0].Depth.Inches}}</div>
      <div class="right" v-if="snowData.SnowReport"> {{snowData.SnowReport[1].Depth.Inches}}</div>
    </div>
  </div> -->
</template>

<style>
  #new-snow{
    background-color: #BBB;
    border-bottom: 1px;
  }
  #new-snow .left{
    display: inline;
  }
   #new-snow .right{
    display: inline;
  }
</style>

<script>
import SnowVueService from '../services/snow-data';

export default {
  name: 'SnowFall',
  data () {
    return {
      snowData: []
    }
  },
  created () {
    SnowVueService.snowReports().then(response => {
      console.log('!!!!!!!!!!!!!!!', response.body);
      this.snowData = { 'message': 'Data is not available.' };
    }, response => {
      console.log('###############', response.body);
      this.snowData = { 'message': 'Data is not available.' }
    });
  }
};
</script>
