// For authoring Nightwatch tests, see
// http://nightwatchjs.org/guide#usage

const request = require("request");

module.exports = {
  "default e2e tests": function(browser) {
    // automatically uses dev Server port from /config.index.js
    // default: http://localhost:8080
    // see nightwatch.conf.js
    const devServer = browser.globals.devServerURL;

    request(
      "https://5kn6ac4359.execute-api.us-east-1.amazonaws.com/dev/weather",
      (error, response, body) => {
        console.log(response.body);
        browser.assert.equal(response.statusCode, 200);
      }
    );

    browser
      .url(devServer)
      // .waitForElementVisible("body")
      .assert.titleContains("app");
    // .assert.elementPresent("h1#resortId")
    // .assert.containsText("h1#resortId", "KEYSTONE")
    browser.assert
      .elementCount("h1#resortId", 1)
      // .assert.regex("h1#resortId", /stone/g)

      .waitForElementVisible("#overnight")
      .assert.regex("#overnight", /in/g)
      .end();
  }
};
