import requests

# here all the http methods can redirects except head

r=requests.get('http://github.com')
print(r.url)
print(r.history)