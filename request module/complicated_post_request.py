import requests

payload={'key1':['value','value1'],'key2':'value2'}   #here a key can have multiple values also using list
r=requests.post('https://httpbin.org/post',data=payload)
print(r.text)


print('in json format')
r=requests.post('https://httpbin.org/post',json=payload)
print(r.text)