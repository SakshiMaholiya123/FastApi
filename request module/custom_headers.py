import requests

headers={'user-agent':'my-app/0.0.1'}
auth=('user','pass')

r=requests.get('https://api.github.com/some/endpoint',headers=headers)

print(r.headers)