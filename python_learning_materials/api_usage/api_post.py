import urllib.parse
import urllib.request
import json

url = 'https://jsonplaceholder.typicode.com/posts'
auth_token = 'c775bcfe-8a33-4b28-925f-7717527c5ffa'
headers = {'Authorization': auth_token}
payload = {
    'name': 'Michael Foord',
    'location': 'Northampton',
    'language': 'Python'
}
encode_payload = urllib.parse.urlencode(payload).encode('utf-8')
request = urllib.request.Request(url)

with urllib.request.urlopen(request, data=encode_payload) as f:
    response = f.read()
    print(response)
