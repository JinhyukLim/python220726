# demoDict.py
# 사전식구조
color = {"apple":"red", "banana":"yellow"}
print(color)
print(len(color))
print(color["apple"])
color["cherry"] = "red"
print(color)
del color["apple"]
print(color)
for item in color.items():
    print(item)


print("---key---")
for k in color.keys():
    print(k)

print("---value---")
for v in color.values():
    print(v)

#장비를 관리
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(device)
print(len(device))
print(device["아이폰"])
#입력
device["안드로이드"] = 30
#삭제
del device["아이폰"]
#수정
device["아이패드"] = 11
print(device)

#무조건 파이썬은 참조를 복사해서 전달
#Pass By Referenece
device2 = device
device2["맥북"] = 20
print(device)
print(device2)





