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
    if i > 5:
        break
    print("Item:{0}".format(i))

