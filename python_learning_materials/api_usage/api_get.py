import urllib.parse
import urllib.request
import json

url = 'https://jsonplaceholder.typicode.com/posts'
request = urllib.request.Request(url)

response = urllib.request.urlopen(request)
response_data = json.loads(response.read())
length = len(response_data)

# for i in range(length):
print(response_data)
#print("message: %s") % str(response_data[i].userId)
