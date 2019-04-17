import requests, json

# r = requests.get("https://api.github.com/events")
# r.raise_for_status() #예외처리
# print(r.text)

jar = requests.cookies.RequestsCookieJar() #jar의 인스턴스
jar.set("name", "kim", domain="httpbin.org", path="/cookies") #jar의 인스턴스 안에 .set 메소드로 내용 입력

#r = requests.get("https://httpbin.org/cookies", cookies=jar)
#r.raise_for_status #예외처리
#print(r.text)

#r = requests.get("https://github.com", timeout=3)
#print(r.text)

#r = requests.post("https://httpbin.org", data={"name": "jeon"}, cookies=jar)
#print(r.text)

payload1 = {"greeting": "hello", "recruiting": "fighting"} #딕셔너리 형태
payload2 = (("greeting", "hello"), ("recruiting", "fighting")) #튜플 형태'''
payload3 = {"some": "nice"}

r = requests.post("http://httpbin.org/post", data=payload2) #form
print(r.text)

r = requests.post("http://httpbin.org/post", data=json.dumps(payload3)) #json
print(r.text)
