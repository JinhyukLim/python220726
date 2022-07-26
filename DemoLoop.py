# DemoLoop.py
# 초기값
value = 5
while value > 0:
    print(value)
    value -= 1

print("---반복구문---")

d = {"apple":100, "kiwi":200, "orange":300}
for item in d.items():
    print(item)

for i in [2,3,4,5,6]:
    print("---{0}단---".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i, j, i*j))

print("---break구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    # 다중 라인 주석처리: ctlr+/
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue구문---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

#수열: 규칙이 있는 숫자의 열
print(list(range(5)))
print(list(range(1,11)))
print(list(range(2000,2023)))
#range(start,end,step)
print(list(range(10,0,-1)))

print("---리스트 컴프리헨션---")
lst = list(range(1,11))
print(lst)
result = [i**2 for i in lst if i > 5]
print(result)
tp = ("apple", "kiwi", "orange")
print([len(i) for i in tp])

