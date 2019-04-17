import requests
import urllib.parse as rep
from bs4 import BeautifulSoup

#로그인 유저 정보
Login_Info = {
    "user[email]": "wjstpgus1993@gmail.com",
    "user[password]": "Qldrndkssud93!",
    "commit": rep.quote_plus("로그인")
    }

with requests.Session() as s:
    login_req = s.post("https://www.codeit.kr/users/sign_in", data=Login_Info)
    print(login_req.text)
