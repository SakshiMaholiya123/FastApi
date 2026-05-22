import requests

files={'file':('employee_data.xls',open('report.xls','rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

r=requests.post('https://httpbin.org/post',files=files)

print(r.text)