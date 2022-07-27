# Demofile2.py
# 파일 쓰기
f = open(r"c:\work\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

f = open("c:\work\demo.txt", "rt", encoding="utf-8")
# print(f.read())
# 리스트에 담기
# lst = f.readlines()
# print(lst)
print(f.readline(), end="")
print(f.readline(), end="")
f.close()

# for item in lst:
#     print(item, end="")

# 파일을 첨부(a+, wt)
f = open("C:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("새로운 데이터\n")
f.close()
