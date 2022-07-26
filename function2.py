# function2.py 
from re import X


print("---불변형---")
a = 1.2
print(id(a))
a = 2.3
print(id(a))

print("---가변형---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

#함수의 스코핑룰(이름 해석 규칙):LGB
#전역변수
x = 1
def func1(a):
    return a+x

#호출
print(func1(1))

#지역변수
def func2(a):
    x = 5
    return a+x

#호출
print(func2(1))

#Pass By Reference
wordlist = ["J", "A", "M"]
def change(x):
    #내부에 복사본을 생성
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)
    # 복사본 생성전
    # x[0] = "H"    

#함수 호출
change(wordlist)
print("함수 호출후:", wordlist)

# 불변형식의 전역변수는 원래 읽기만 가능
# 불변형식에 읽기+쓰기를 하는 경우 global키워드 사용
g = 0
def testGlobal(a):
    # 불변형식을 함수 내부에서 읽기+쓰기
    global g
    g += 1
    return a+g

#함수 호출
print(testGlobal(1))
print(testGlobal(1))
print(testGlobal(1))
print(testGlobal(1))
print("전역변수 g:", g)
