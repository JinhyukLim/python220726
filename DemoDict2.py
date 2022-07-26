#DemoDict2.py

phone = {"kim":"111", "lee":"222", "park":"333"}
print(phone["kim"])
#in은 단독으로 사용하면 include(멤버십 테스트)
print("park" in phone)
print("moon" in phone)
print("moon" not in phone)

#참조를 복사

p = phone
print(p)
print(phone)
print(id(phone), id(p))

#

print(10 > 5)
print(10 < 5)
print(1 != 2)
print(1 == 2)

print("\n")
#파이썬의 판단 기준
print(bool(0))
print(bool(-3))
print(bool(3))
print(bool(""))
print(bool("demo"))
print(bool([]))
print(bool(1,2,3))





