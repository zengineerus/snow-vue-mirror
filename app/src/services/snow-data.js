import Vue from 'vue';
export default {
  getPosts () {
    return Vue.http.get('https://www.reddit.com/r/gifs/top/.json?limit=20&sort=hot');
  },
  snowReports () {
    return Vue.http.get('https://5kn6ac4359.execute-api.us-east-1.amazonaws.com/dev/weather');
  },
  travelTime () {
    return Vue.http.get('https://5kn6ac4359.execute-api.us-east-1.amazonaws.com/dev/traffic?location=80202')
  }
}
