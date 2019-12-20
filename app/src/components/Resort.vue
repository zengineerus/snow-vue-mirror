<template>
  <div id='resort'>
    <h1>Keystone</h1>Last Updated: 10/10/19 7:15
    <SnowFall></SnowFall>

    <TravelTime></TravelTime>
  </div>
</template>

<style>
  #resort h1{
    color: white;
    text-transform: uppercase;
    margin: 0;
    margin-top:20px;
  }
</style>

<script>
import SnowFall from './SnowFall'
import TravelTime from './TravelTime'

export default {
  name: 'Resort',
  components: {
    SnowFall,
    TravelTime
  }
};
</script>
