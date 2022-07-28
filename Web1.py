# Web1.py
# 웹문서를 검색(패키지는 폴더형태)
from bs4 import BeautifulSoup

# 페이지 로딩: 메서드나 함수를 연속으로 호출(메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
# 검색이 용이한 객체\
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

# 문서에 있는 <p>전부 검색
# print(soup.find_all("p"))

# 문서에 있는 첫번째<p> 검색
# print(soup.find("p"))

# 조건이 있는 경우: <p class='outer-text'>
# print(soup.find_all("p", class_="outer-text"))
# <p id='first'>
# print(soup.find_all("p", id="first"))
# 태그 내부의 문자열 검색
for item in soup.find_all("p"):
    # 태크 내부의 문자열: .text
    title = item.text.strip()
    title = title.replace("\n", "")
    print(title)
