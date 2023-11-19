# 웹 서버에 요청하고 응답받기

import requests

url = "https://www.python.org/"
resp = requests.get(url)
print(resp)

url2 = "https://www.python.org/1"
resp2 = requests.get(url2)
print(resp2)