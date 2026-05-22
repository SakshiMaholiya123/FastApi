from  requests import Request, Session

s=Session()

req=Request(
    'POST',
    'https://httpbin.org/post',
    data={'name':'sakshi'}
   
)

prep=req.prepare()   #  dont use this instead use
prep=s.prepare_request(req)
resp = s.send(prep)
print(resp.status_code)
print(prep.body)
print(prep.headers)
