require('babel-register')
var config = require('../../config')

// http://nightwatchjs.org/gettingstarted#settings-file
module.exports = {
  src_folders: ['test/e2e/specs'],
  output_folder: 'test/e2e/reports',
  custom_assertions_path: ['test/e2e/custom-assertions'],

  selenium: {
    start_process: true,
    server_path: require('selenium-server').path,
    host: '127.0.0.1',
    port: 4444,
    cli_args: {
      'webdriver.chrome.driver': require('chromedriver').path
    }
  },

  test_settings: {
    default: {
      selenium_port: 4444,
      selenium_host: 'localhost',
      silent: true,
      globals: {
        devServerURL: 'http://localhost:' + (process.env.PORT || config.dev.port)
      }
    },

    chrome: {
      desiredCapabilities: {
        browserName: 'chrome',
        javascriptEnabled: true,
        acceptSslCerts: true
      }
    },

    "ios" : {
      "selenium_start_process": false,
      "selenium_port" : 4723,
      "selenium_host" : "127.0.0.1",
      "silent": true,
      "desiredCapabilities" : {
        "browserName" : "Safari",
        "platformName" : "iOS",
        "platformVersion" : "9.3",
        "deviceName" : "iPhone 6s Plus"
      }
    },

    android : {
      "selenium_start_process": false,
      "selenium_port" : 4723,
      "selenium_host" : "127.0.0.1",
      "silent": true,
      "desiredCapabilities": {
          "browserName": "Chrome",
          "platformName": "Android",
          "platformVersion": "4.4",
          "device": "CQ3000QTJB",
          "deviceName": "CQ3000QTJB"
      }
  },

    firefox: {
      desiredCapabilities: {
        browserName: 'firefox',
        javascriptEnabled: true,
        acceptSslCerts: true
      }
    }
  }
}
