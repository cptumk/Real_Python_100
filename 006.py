# 웹 문서의 그림 이미지 파일을 PC에 저장하기

import os
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp = requests.get(url)
html_src = resp.text

soup = BeautifulSoup(html_src, 'html.parser')

target_img = soup.find(name='img', attrs={'alt':'Seoul Metro 2000 series train on Line 2'})
print('HTML요소: ', target_img)
print("\n")

target_img_src = target_img.get('src')
print('이미지 파일 경로: ', target_img_src)
print("\n")

# 이미지 파일 확장자 얻기
img_extension = os.path.splitext(target_img_src)[-1]

# User-Agent를 변경하여 요청
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
target_img_resp = requests.get('http:' + target_img_src, headers=headers)

# 가져올 주소 및 내보낼 폴더 주소 설정
target_img_resp = requests.get('http:' + target_img_src)
out_file_path = "./output/download_image" + img_extension

with open(out_file_path, 'wb') as out_file:
    out_file.write(target_img_resp.content)
    print("이미지를 저장하였습니다.")
