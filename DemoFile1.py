# DemoFile1.py
# 파일에 저장
f = open("c:\\work\\demo.txt", "wt")
print("file write", file=f)
f.close()

print("---정렬---")
for x in range(1,6):
    print(x, "*", x, "=", x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3))

print("---공백문자---")
for x in range(1,6):
    print(x, "*", x, "=",str(x*x).zfill(3))

# 서식문자를 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:c}".format(65))
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))