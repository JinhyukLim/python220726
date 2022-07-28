# Web1.py
# 웹문서를 검색(패키지는 폴더형태)
from bs4 import BeautifulSoup

# 페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
# 검색이 용이한 객체\
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())

