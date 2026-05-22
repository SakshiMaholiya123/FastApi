import requests

r=requests.get('https://api.github.com/events')

print(r.json())

# raw response

r=requests.get('https://api.github.com/events',stream=True)

print('raw response')
print(r.raw.read(10))


