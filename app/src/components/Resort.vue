<template>
  <div id='resort'>
    <h1 id='resortId'>Keystone</h1>
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
