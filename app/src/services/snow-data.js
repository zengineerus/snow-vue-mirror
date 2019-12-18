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
  },
  getCurrentLocation () {
    var promise1 = new Promise(function (resolve, reject) {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(pos => {
          resolve({'Location': {'latutude': pos.coords.latitude.toFixed(4), 'longitude': pos.coords.longitude.toFixed(4)}})
        });
      } else {
        reject(Error('Location cannot be determined'))
      }
    })

    return promise1
  }
}
