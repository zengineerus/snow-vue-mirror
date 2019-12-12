<template>
  <div>
    <h1>Keystone</h1>
    <SnowFall></SnowFall>
    <TravelTime></TravelTime>
  </div>
</template>

<script>
import SnowFall from './SnowFall'
import TravelTime from './TravelTime'

export default {
  name: 'Resort',
  components: {
    SnowFall,
    TravelTime
  }
}

</script>
