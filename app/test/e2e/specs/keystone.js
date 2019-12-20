// For authoring Nightwatch tests, see
// http://nightwatchjs.org/guide#usage

module.exports = {
  "default e2e tests": function(browser) {
    // automatically uses dev Server port from /config.index.js
    // default: http://localhost:8080
    // see nightwatch.conf.js
    const devServer = browser.globals.devServerURL;

    // Helpful code:  (Delete as soon as we use these in an actual test)
    // browser.expect.element("h1#resortId").text.to.equal("KEYSTONE");
    // browser.getText("h1#resortId", function (result) {
    //   console.log("value is here", result.value);
    // });

    browser
      .url(devServer)
     // .waitForElementVisible("body")
      .assert.titleContains("app")
      .assert.elementPresent("h1#resortId")
      .assert.containsText("h1#resortId", "KEYSTONE")
      // .assert.containsText("body",`KEYSTONE
      // Overnight SnowFall
      // 24 Hour Snow
      // 2 inches
      // 8 inches
      // Enter Zip
      // SUBMIT`)
      .getText("body", function(result) {
          console.log("value is here", result.value);
        })
      .end();

      // browser
      // .url(devServer)
      // .waitForElementVisible("body")
      // .getText("body", function(result) {
      //   console.log("value is here", result.value);
      // }).end();
  }
};
