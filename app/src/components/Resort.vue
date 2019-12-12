<template>
  <div id="resort">
    <h1>Keystone</h1>
    <SnowFall></SnowFall>
    <TravelTime></TravelTime>
  </div>
</template>

<style>
  
</style>

<script>
import SnowFall from "./SnowFall";
import TravelTime from "./TravelTime";

export default {
  name: "Resort",
  components: {
    SnowFall,
    TravelTime
  }
};
</script>
