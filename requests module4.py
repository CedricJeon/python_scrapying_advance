import requests, json

#Rest : POST - 올리기, GET - 가져오기, PUT(FETCH) - update, replace, modify, DELETE - 삭제
#                                   PUT - update, replace(교체의 성격이 강함)
#                                   FETCH - update, modify(수정의 성격이 강함)

payload1 = {"greeting": "hello", "recruiting": "fighting"} #딕셔너리 형태
payload2 = (("greeting": "hello", "recruiting": "fighting")) #튜플 형태
payload3 = {"some": "nice"}
