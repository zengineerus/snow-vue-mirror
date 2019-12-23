require("babel-register");
var config = require("../../config");

// http://nightwatchjs.org/gettingstarted#settings-file
module.exports = {
  src_folders: ["test/e2e/specs"],
  output_folder: "test/e2e/reports",
  custom_assertions_path: ["test/e2e/custom-assertions"],

  selenium: {
    start_process: true,
    server_path: require("selenium-server").path,
    host: "127.0.0.1",
    port: 4723,
    cli_args: {
      "webdriver.chrome.driver": require("chromedriver").path
    }
  },

  test_settings: {
    default: {
      selenium_port: 4723,
      selenium_host: "localhost",
      silent: true,
      globals: {
        devServerURL:
          "http://localhost:" + (process.env.PORT || config.dev.port)
      }
    },

    chrome: {
      desiredCapabilities: {
        browserName: "chrome",
        javascriptEnabled: true,
        acceptSslCerts: true,
        chromeOptions: {
          w3c: false,
          args: ["--no-sandbox", "--headless"]
        }
      }
    },

    ios: {
      selenium_port: 4723,
      selenium_host: "127.0.0.1",
      desiredCapabilities: {
        appiumVersion: "1.15.1",
        automationName: "xcuitest",
        browserName: "Safari",
        platformName: "iOS",
        platformVersion: "12.2",
        deviceName: "iPhone 6",
        waitForAppScript: "true"
      },
      selenium: {
        start_process: false
      },
      appium: {
        start_process: true
      }
    },

    android: {
      selenium_port: 4723,
      selenium_host: "127.0.0.1",
      desiredCapabilities: {
        appiumVersion: "1.15.1",
        automationName: "UiAutomator2",
        browserName: "Chrome",
        platformName: "Android",
        platformVersion: "9",
        device: "emulator-5554",
        deviceName: "emulator-5554",
        avd: "Pixel_API_28",
        avdArgs: "-netfast -noaudio -no-boot-anim",
        autoGrantPermissions: true,
        autoAcceptAlerts: true
      },
      selenium: {
        start_process: false
      },
      appium: {
        start_process: true
      }
    },

    firefox: {
      desiredCapabilities: {
        browserName: "firefox",
        javascriptEnabled: true,
        acceptSslCerts: true
      }
    }
  }
};
