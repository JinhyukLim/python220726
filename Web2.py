# Web2.py
# 웹크롤링
from bs4 import BeautifulSoup
# 웹서버에 요청(웹서버 통신 모듈)
import urllib.request

data = urllib.request.urlopen(
    "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

# 검색할 객체
soup = BeautifulSoup(data, "html.parser")

# <td class="title">
# <a href="/webtoon/detail?titleId=20853">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

for item in cartoons:
    title = item.find("a").text.strip()
    print(title)
