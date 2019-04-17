import requests

s = requests.Session()
# r = s.get('https://naver.com') #PUT(FETCH), DELETE, GET, POST
# print('1', r.text)

# r = s.get("https://httpbin.org/cookies", cookies={"from": "myName"})
# print(r.text)

url = "https://httpbin.org/get"
header = {"user-agent" : "myPythonApp_1.0.0"}
# r = s.get(url, headers=header)
# print(r.text)

s.close()

with requests.Session() as s:
    r = s.get("https://www.naver.com")
    print(r.text)
