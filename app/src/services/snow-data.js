import Vue from 'vue';
// import baseUrl from 'variables'

var baseurl = 'http://localhost:3000'; // to use this run
// var baseurl = 'https://5kn6ac4359.execute-api.us-east-1.amazonaws.com/dev'

export default {
  snowReport () {
    return Vue.http.get(`${baseurl}/weather`);
  },
  travelTime () {
    return Vue.http.get(`${baseurl}/traffic?location=80203`)
  },
  travelTimeZip (zip) {
    return Vue.http.get(`${baseurl}/traffic?location=${zip}`)
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
    });
    return promise1;
  }
}
