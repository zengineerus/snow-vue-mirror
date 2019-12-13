<template>
  <div id="new-snow">
    <div>
      <div class="left">Overnight SnowFall</div>
      <div class="right">24 Hour Snow</div>
    </div>
    <div>
      <div class="left" v-if="snowData.SnowReport"> {{snowData.SnowReport[0].Depth.Inches}}</div>
      <div class="right" v-if="snowData.SnowReport"> {{snowData.SnowReport[1].Depth.Inches}}</div>
    </div>
  </div>
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
      this.snowData = response.body;
    });
  }
};
</script>
