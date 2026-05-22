import requests

r=requests.get('https://en.wikipedia.org/wiki/Monty_Python')
print(r)

#to access headers
print(r.headers)
print(r.status_code)

print(r.request.headers)  #give the request headers