<template>
  <div class='center'>
    <div class='center-container'>
      <div id='app'>
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
};
</script>

<style>
@import './assets/styles.css';
#app {
  font-family: 'Calibri', 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;

}
</style>
