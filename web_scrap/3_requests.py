import requests


res = requests.get("http://google.com")
res.raise_for_status()

# res = requests.get("http://nadocoding.tistory.com")
# print("응답코드 : ",res.status_code)                    #200 이면 정상


# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("비정상입니다.")

# print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)