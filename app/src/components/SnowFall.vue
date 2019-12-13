<template>
  <div id="new-snow">
    <div>
      <div class="left">Overnight SnowFall</div>
      <div class="right">24 Hour Snow</div>
    </div>
    <div>
      <div class="left">  <span >{{snowData.SnowReport[0].Depth.Inches}}</span>"</div>
      <div class="right"> <span id="depth24">{{snowData.SnowReport[1].Depth.Inches}}</span>"</div>
    </div>
    <Reddit></Reddit>
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
import Reddit from './Reddit';
export default {
  name: 'SnowFall',
  components: {
    Reddit
  },
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
