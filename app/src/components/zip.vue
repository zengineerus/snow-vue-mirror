<template>
    <div>
    </div>
</template>

<style scoped>

</style>

<script>
import SnowVueService from '../services/snow-data';


export default {
  name: 'zip',
  data () {
    return {
        location: {}
    };
  },
  created () {
    Promise.all([
      SnowVueService.getCurrentLocation()
    ]).then(([locationResponse]) => {
      console.log('reposnes complete', locationResponse )
      this.location = locationResponse.body;
    });
  },
  methods: {
    updateLocation () {
      SnowVueService.travelTimeZip(
        document.querySelector('input[name=zip]').value
      ).then(
        response => {
          this.travelTime = response.body;
        },
        response => {
          this.travelTime = { message: 'Data is not available.' };
        }
      );
    }
  }
};
</script>
