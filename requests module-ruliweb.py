import requests
from bs4 import BeautifulSoup

#로그인 유저 정보
LOGIN_INFO = {
    "user_id": "asdf",
    "user_pw": "asdf"
}

#Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    login_req = s.post("https://user.ruliweb.com/member/login_proc", data=LOGIN_INFO)
    #HTML소스 확인
    print(login_req.text)
    #Header 확인
    #print(login_req.headers)
    if login_req == 200 and login_req.ok():
        post_one = s.get("http://bbs.ruliweb.com/market/board/300141/read/30591085?")
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, "html.parser")
        #print(soup.prettify())
        article = soup.select_one("table:nth-of-type(3)").find_all("p")
        for i in article:
            if i is not None:
                print(i.string)
