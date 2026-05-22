import requests

r=requests.get('https://api.github.com/events')

print(r.text)

print(r.encoding)
r.encoding = 'ISO-8859-1'
print(r.encoding)

