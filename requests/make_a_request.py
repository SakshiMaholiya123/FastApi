import requests

# get request
r=requests.get('https://api.github.com/events')  #get request
print(r.text)
print(r.status_code)

print(r.headers)


#r=requests.post('http://org',data={'key':'value'})


# make a post request


data={
    'name':'sakshi',
    'age':21
}

print('post request')
r=requests.post("https://httpbin.org/post",json=data)
print(r.json())


#head and option requests
print('head and option request')
a = requests.head('https://httpbin.org/get')
b = requests.options('https://httpbin.org/get')


import requests

url = "https://httpbin.org/get"

head_response = requests.head(url)
print(head_response.headers)

options_response = requests.options(url)
print(options_response.headers)