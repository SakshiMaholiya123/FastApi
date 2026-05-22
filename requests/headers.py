import requests

r=requests.get("https://httpbin.org/get")

print(r.headers)

# to access a specific header

print(r.headers['Content-Type'])

# using .get()
print(r.headers.get('Content-Type'))
