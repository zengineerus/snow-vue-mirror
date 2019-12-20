// For authoring Nightwatch tests, see
// http://nightwatchjs.org/guide#usage

module.exports = {
  'default e2e tests': function (browser) {
    // automatically uses dev Server port from /config.index.js
    // default: http://localhost:8080
    // see nightwatch.conf.js
 
    // const devServer = browser.globals.devServerURL;
    // console.log("devServer is: ", devServer);
    // browser
    //   .url(devServer)
    //   .element('#resortId').text.to.be('Keystone');

    //   //.waitForElementVisible('h1')
    //   // .assert.elementPresent('#resortId')
    //   // .assert.containsText('#resortId', 'K', 'K')
    //   // .assert.containsText('#resortId', 'Keystone')      

    //   //.end();

    // browser
    //   .url(devServer)
    //   //.waitForElementVisible('body')
    //   .assert.elementPresent('#new-snow')
    //   .end();

    Given(/^I open Google's search page$/, () => {
      return client
        .url('http://google.com')
        .waitForElementVisible('body', 1000);
    });

  }
};
