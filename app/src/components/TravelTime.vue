<template>
  <div>
    <ion-card id='travel-time' name='ion_card' color='secondary'>
      <ion-card-content>
        <ion-grid v-if='travelTime.TrafficReport'>
          <ion-row>
            <ion-col>
              <ion-label id='travel-time-label'>Travel Time</ion-label>
            </ion-col>
            <ion-col>
              <ion-label id='start-zip-label'>Start Zip</ion-label>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col>
              <ion-label>
                {{
                travelTime.TrafficReport.travel_time.hours
                }}
                hours
              </ion-label>
              <ion-label>
                {{
                travelTime.TrafficReport.travel_time.minutes
                }}
                minutes
              </ion-label>
            </ion-col>
            <ion-col>
              <ion-label>
                {{ travelTime.TrafficReport.start_location }}
              </ion-label>
              <ion-buttton >change zip</ion-buttton>
            </ion-col>
          </ion-row>
        </ion-grid>
        <ion-label v-else>Server is unavailable.</ion-label>
      </ion-card-content>
      <!-- <ion-card-content v-else>
        <ion-input name="zip" v-model="zip">Enter Zip</ion-input>
        <ion-button v-on:click="updateLocation()">submit</ion-button>
      </ion-card-content>-->
    </ion-card>

    <!-- <form novalidate>
      <ion-card name='ion_card' color='secondary'>
        <ion-card-header name='ion_header'>
          <ion-card-title name='ion_title'>Travel Time</ion-card-title>
          <ion-card-subtitle>From Zip code to resort</ion-card-subtitle>
        </ion-card-header>
        <ion-card-content name='ion_content'>
          <ion-list v-if='travelTime.TrafficReport'>
            <ion-item name='ion_item'>
              <ion-label>Zip Code:</ion-label>
              <span :class='{ error: errors.has('zip') }'>
                <ion-input
                  id='inputZip'
                  name='zip'
                  type='text'
                  value='80202'
                  placeholder='80202'
                  maxlength='5'
                  v-validate='{ required: true, regex: /^\d{5}$/ }'
                ></ion-input>
              </span>
            </ion-item>
            <ion-item v-show='errors.has('zip')' class='error'>
              <ion-label>{{ errors.first("zip") }}</ion-label>
            </ion-item>
            <ion-item name='ion_item'>
              <ion-label name='ion_label'>To: {{ travelTime.TrafficReport.destination }}</ion-label>
            </ion-item>
            <ion-item>
              <ion-label>
                {{
                travelTime.TrafficReport.travel_time.hours
                }}
                hours
              </ion-label>
              <ion-label>
                {{
                travelTime.TrafficReport.travel_time.minutes
                }}
                minutes
              </ion-label>
            </ion-item>
          </ion-list>
          <ion-label v-else id='travelTimeMessage'>
            {{
            travelTime.message
            }}
          </ion-label>
        </ion-card-content>
      </ion-card>
    </form> -->
  </div>
</template>

<style scoped>
#travel-time {
  background-color: #222222b0;
  border-bottom: 1px;
}
#travel-time .left {
  display: inline;
}
#travel-time .right {
  display: inline;
}
#travel-time #travel-time-label {
  text-transform: uppercase;
}
#travel-time #start-zip-label {
  text-transform: uppercase;
}
</style>

<script>
import SnowVueService from '../services/snow-data';

export default {
  name: 'TravelTime',
  data () {
    return {
      travelTime: {
        // TrafficReport: {
        //   travel_time: {
        //     hours: '2',
        //     minutes: '35'
        //   },
        //   start_location: '80203',
        //   destination: '100 Dercum Square, Keystone, CO 80435'
        // }
      },
      location: {},
      zip: 80000
    };
  },
  created () {
    Promise.all([
      SnowVueService.getCurrentLocation(),
      SnowVueService.travelTime()
    ]).then(([locationResponse, travelTimeResponse]) => {
      console.log('reposnes complete', locationResponse, travelTimeResponse)
      this.location = locationResponse.body;
      this.travelTime = travelTimeResponse.body;
    });
  },
  methods: {
    updateLocation () {
      SnowVueService.travelTimeZip(
        document.querySelector('input[name=zip]').value
      ).then(
        response => {
          console.log('^^^^^^^^^', response.body);
          this.travelTime = response.body;
        },
        response => {
          console.log('&&&&&&&&&&', response.body);
          this.travelTime = { message: 'Data is not available.' };
        }
      );
    }
  }
};
</script>
