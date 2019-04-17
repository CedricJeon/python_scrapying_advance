from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

#Fake Agent 생성
ua = UserAgent()

#요청 URL
URL = "https://www.wishket.com/accounts/login/"

with requests.Session() as s:
    #URL연결
    s.get(URL)
    #login정보 payload
    LOGIN_INFO = {
        "identification": "wjstpgus1993",
        "password": "Cedric93!",
        "csrfmiddlewaretoken": s.cookies["csrftoken"] #Cookies 섹션에서 csrftoken을 키로 토큰값을 따옴
    }

#요청 response

response = s.post(URL, data=LOGIN_INFO, headers={"User-Agent": str(ua.chrome), "Referer": "https://www.wishket.com/accounts/login/"})

if response.status_code == 200 and response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    projectList = soup.select("table.table.table-responsive > tbody > tr")
    for i in projectList:
        print(i.find("th").string, i.find("td").text)
