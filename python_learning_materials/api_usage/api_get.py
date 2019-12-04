import urllib
import urllib2
import json

url = 'http://server.lvh.me:4567/users'
request = urllib2.Request(url)

try:
    response = urllib2.urlopen(request)
    response_data = json.loads(response.read())
    print "message: %s" % str(response_data['users'])
except urllib2.HTTPError as error:
    print "error: %s - %s" % (error.code, error.reason)

