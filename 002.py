# 웹 페이지 소스코드 확인하기

import requests

url = "https://www.python.org/"
resp = requests.get(url)

html = resp.text
print(html)
