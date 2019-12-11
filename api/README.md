**R&D**

Weather APIs
CPD - Calls per day

---

- [Weatherbit](https://www.weatherbit.io/api/weather-current)
  Free: 500 CPD + $0.00075 each
  Starter:  $35/Month: 50,000 CPD + $0.0001 each
  Developer: $160/Month 500,000 CPD

- [Dark Sky](https://darksky.net/dev/docs)
  Free: 1,000 CPD + \$0.0001 each

- [Weather 2020](http://api.weather2020.com/)
  Free: 1,000 CPD

- [AccuWeather API](https://developer.accuweather.com/packages?gclid=EAIaIQobChMIhK_qmcOc5gIVGKSzCh2biQgFEAAYASABEgLUX_D_BwE)
  Free: 50 CPD
  Standard: $25/Month 225,000 PCD + $0.12 each
  Prime: $250 / Month 1,800,000 CPD + $.015 each

- [Weather Underground](https://www.wunderground.com/api/)

Resort APIs
---

**Keystone**

* Weather API data: [https://www.keystoneresort.com/api/PageApi/GetWeatherDataForHeader](https://www.keystoneresort.com/api/PageApi/GetWeatherDataForHeader)

**Loveland**

* Snow report (also has aggregated trail/lift data): [https://skiloveland.com/snow-report](https://skiloveland.com/snow-report)
* Trail & Lift report (individual trail/lift data): [https://skiloveland.com/trail-lift-report](https://skiloveland.com/trail-lift-report)

**Copper**

* Weather forecast API: [https://www.coppercolorado.com/api/v1/dor/weather](https://www.coppercolorado.com/api/v1/dor/weather)
* Snow conditions API: [https://www.coppercolorado.com/api/v1/dor/condition](https://www.coppercolorado.com/api/v1/dor/condition)

**Eldora**

* Weather forecast API: [https://www.eldora.com/api/v1/dor/weather](https://www.eldora.com/api/v1/dor/weather)
* Snow conditions API: [https://www.eldora.com/api/v1/dor/conditions](https://www.eldora.com/api/v1/dor/conditions)

**Winter Park**

* Weather API: [https://mtnpowder.com/feed/5/weather](https://mtnpowder.com/feed/5/weather)
* Webcam feed API: [https://mtnpowder.com/feed/5/webcam](https://mtnpowder.com/feed/5/webcam)
* Lift info API: [https://mtnpowder.com/feed/5/lift](https://mtnpowder.com/feed/5/lift)

**Breckenridge**

* Weather API: [https://www.breckenridge.com/api/PageApi/GetWeatherDataForHeader](https://www.breckenridge.com/api/PageApi/GetWeatherDataForHeader)

**Vail**

* Snow and Weather data API: [https://www.vail.com/api/PageApi/GetWeatherDataForHeader](https://www.vail.com/api/PageApi/GetWeatherDataForHeader)

# Python

# AWS

>`sls deploy` should default to the dev profile. Before you can run `sls deploy` or `sls deploy --aws-profile dev` you must create a `~/.aws/credentials` file with **[dev]** and **[prod]** with defined AKID (Access Key ID) and Secret Keys.

### Setup

********************************************************
keystone example object:
{
   "HeaderSettings":{
      "EnableCart":true,
      "SignInTitleText":"Sign In",
      "ShowSignIn":true,
      "SearchLink":{
         "Anchor":"",
         "Class":"",
         "Text":"Search",
         "Query":"",
         "Title":"",
         "Url":"/search/search-results.aspx",
         "Target":"",
         "TargetId":"c2d706e8-7075-4774-9b4a-dd521d666158",
         "Type":4,
         "Style":""
      },
      "ShowSearch":false,
      "WeatherTitleForMobileNavigation":"Weather and Conditions",
      "ShowWeatherWidget":true,
      "DefaultWeatherLocation":{
         "Latitude":39.604538,
         "Longitude":-105.954529,
         "LocationDisplayName":"Keystone",
         "WeatherSponsorImage":null,
         "WeatherSponsorLink":null,
         "WeatherSponsorCopy":"",
         "ElevationText":"",
         "Elevation":"",
         "Id":"f8bc00e1-0007-49c8-8552-04ac8517212c",
         "Name":"Keystone",
         "SortOrder":0
      },
      "DailyForecastTitle":"TODAY'S FORECAST",
      "ShowWeatherIconMenu":true,
      "SnowReportTitle":"SNOW REPORT",
      "ShowSnowReportSection":true,
      "SnowReportSections":[
         {
            "Id":"3925634c-5104-4534-8b5d-fa8dcf9ae996",
            "Name":"Overnight Snowfall",
            "SortOrder":0
         },
         {
            "Id":"14441dd9-8284-4132-862a-ece9b02ca2d8",
            "Name":"24 Hour",
            "SortOrder":0
         }
      ],
      "LiftAndTerrainStatusTitle":"LIFT & TERRAIN STATUS",
      "ShowLiftAndTerrainStatusSection":true,
      "ShowLiftsOpenSection":false,
      "ShowLiftsGraph":false,
      "Id":"fb312252-e9f1-48fa-beca-da22bde9f283",
      "Name":"Header Settings",
      "SortOrder":0
   },
   "UnitOfMeasure":1,
   "WeatherShortDescription":"Partly Cloudy",
   "CurrentTempStandard":21.0,
   "CurrentTempMetric":-6.0,
   "HighTempStandard":36.0,
   "HighTempMetric":2.0,
   "LowTempStandard":18.0,
   "LowTempMetric":-8.0,
   "SnowReportSections":[
      {
         "Depth":{
            "Inches":"1",
            "Centimeters":"3"
         },
         "Description":"Overnight <br> Snowfall"
      },
      {
         "Depth":{
            "Inches":"4",
            "Centimeters":"10"
         },
         "Description":"24 Hour<br/>Snowfall"
      }
   ],
   "TotalLifts":21,
   "OpenLifts":20,
   "HoursOfOperationTitle":"Hours of Operation",
   "CurrentWorkDay":{
      "Description":"Lifts Open: 9:00 AM; See schedule for closing time",
      "Id":"3a5fe120-31eb-41a3-8b2e-106464462e60",
      "Name":"Friday",
      "SortOrder":0
   },
   "WeatherIcon":"partly-cloudy-night",
   "MountainCamLink":{
      "Anchor":"",
      "Class":"",
      "Text":"Mountain Cams",
      "Query":"",
      "Title":"",
      "Url":"/the-mountain/mountain-conditions/mountain-cams.aspx",
      "Target":"",
      "TargetId":"3ec13f9c-7bb3-46ed-aede-80b6eb466511",
      "Type":4,
      "Style":""
   },
   "TerrainStatusLink":{
      "Anchor":"",
      "Class":"",
      "Text":"Terrain and Lift Status",
      "Query":"",
      "Title":"",
      "Url":"/the-mountain/mountain-conditions/terrain-and-lift-status.aspx",
      "Target":"",
      "TargetId":"a3d41c8c-d2f4-49a9-aa74-9dd6be8fb37b",
      "Type":4,
      "Style":""
   },
   "WeatherReportLink":{
      "Anchor":"",
      "Class":"",
      "Text":"Snow and Weather Report",
      "Query":"",
      "Title":"",
      "Url":"/the-mountain/mountain-conditions/snow-and-weather-report.aspx",
      "Target":"",
      "TargetId":"e32b1dc3-2b7c-40bb-8ad4-35e985157fdf",
      "Type":4,
      "Style":""
   }
}

end keystone example object
********************************************************

google travel time api
https://developers.google.com/maps/documentation/distance-matrix/intro

TODO: 
 - output validation from external API's
 - change unit tests to reflect new inheritance structure
 - add unit tests for new getters/setters and travel time functionality
 - add endpoint tests for all paths of keystone handler
 - add tests to gitlab ci pipeline
 - add serverless deploy to **dev** to gitlab ci pipeline for feature branches
 - add serverless deploy to **dev** and **prod** to gitlab ci pipeline for master branch
 - add AppDynamics to keystone handler
