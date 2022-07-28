# Web3.py
# 웹크롤링
from bs4 import BeautifulSoup
# 웹서버에 요청(웹서버 통신 모듈)
import urllib.request

# 파일에 저장
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
for i in range(1, 6):
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    # 웹서버에 요청해서 실행된 문자열 받기
    data = urllib.request.urlopen(url)
    # 검색할 객체
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")
    for item in cartoons:
        title = item.find("a").text.strip()
        print(title)
        f.write(title + "\n")

f.close()