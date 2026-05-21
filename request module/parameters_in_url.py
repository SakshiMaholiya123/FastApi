import requests
data={'key1':'value1','key2':'value2'}

r=requests.get('https://httpbin.org/get',params=data)

print(r.url)


#can pass the list of values

data=data={'key1':'value1','key2':['value2','value3']}

r=requests.get('https://httpbin.org/get',params=data)

print(r.url)