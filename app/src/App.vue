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
body{
    background-color: #222;
    min-height: 1000px;
    color: white;
}

.center{
    display: flex;
    justify-content: center;
}

.center-container {
    justify-content: center;
    min-width: 500px;
    min-height: 600px;
    background-image: url(' ./assets/mountains.jpeg');
    /* background-image: linear-gradient(to bottom, rgba(245, 246, 252, 0.52), rgba(117, 19, 93, 0.73)), url(' ./assets/mountains.jpeg'); */
    /* background-image: linear-gradient(to bottom, #b331237a, #9b120617), url(' ./assets/mountains.jpeg'); */
    background-image: linear-gradient(to bottom,rgba(126, 34, 33, 0.5), rgba(58, 9, 4, 0.6)), url(' ./assets/mountains.jpeg');

    /* background-image: linear-gradient(to bottom,#444E8DCC, #222222AA), url(' ./assets/mountains.jpeg'); */
    background-position-x: -100px;
    background-position-y: 0px;
     background-blend-mode: normal;
}

#app {
  font-family: 'Calibri', 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;

  height: 100%;
  margin: 0;

}
</style>
