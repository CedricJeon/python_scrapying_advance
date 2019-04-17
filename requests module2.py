import requests

s = requests.Session()
# response 상태 코드
'''with requests.Session() as s:
    r = s.get("https://httpbin.org/get")
    print(r.status_code)
    print(r.ok)
'''

#https://jsonplaceholder.typicode.com

r = s.get("https://jsonplaceholder.typicode.com/posts/1")
print(r.text)
print(r.json()) #json으로 변환
print(r.json().keys())
print(r.json().values())
print(r.encoding)
print(r.content)
print(r.raw)

s.close()
