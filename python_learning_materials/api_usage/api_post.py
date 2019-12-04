import urllib
import urllib2
import json

url = 'http://server.lvh.me:4567/users'
auth_token = 'c775bcfe-8a33-4b28-925f-7717527c5ffa'
headers = {'Authorization': auth_token}
payload = {
        'name': 'Michael Foord',
        'location': 'Northampton',
        'language': 'Python'
         }
encode_payload = urllib.urlencode(payload)
request = urllib2.Request(url, encode_payload, headers)

try:
    response = urllib2.urlopen(request)
    response_data = json.loads(response.read())
    print "message: %s" % response_data['message']
except urllib2.HTTPError as error:
    print "error: %s - %s" % (error.code, error.reason)

