import requests

r=requests.get('https://httpbin.org/get')

print(r.status_code)

print(requests.codes.ok)   # we canm use the requests.codes to check the status code also if we dont remember the status code numbers

# print(requests.codes.unauthorized)

#if we made a bad request ,for that we can raise a error using raise_for_status()
print(r.raise_for_status())  # none here because our request was ok that why it gave none
