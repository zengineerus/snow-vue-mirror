
exports.assertion = function (selector, expression) {
  this.message = 'Testing if element <' + selector + '> matches ' + expression
  this.expected = expression
  this.pass = function (val) {
    var regex = new RegExp(this.expected, "i");
    return regex.test(val);
  }
  this.value = function (res) {
    return res.value
  }
  this.command = function (cb) {
    var self = this
    return this.api.execute(function (selector) {
      return document.querySelector(selector).innerText
    }, [selector], function (res) {
      cb.call(self, res)
    })
  }
}
