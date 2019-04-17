import requests, json

s = requests.Session()

r = s.get("https://httpbin.org/stream/20", stream = True)
#print(r.text)
#print(r.encoding)
#print(r.json)
if r.encoding is None:
    r.encoding = "utf-8" #r의 코드를 utf-8으로 전환

for line in r.iter_lines(decode_unicode=True):
    b = json.loads(line) # json dict 형태!
    for e in b.keys():
        print("key :", e, ",", "values :", b[e])


s.close()
