# Funtion1.py
# 1) 함수를 정의
def setValue(newValue):
    x = newValue
    print("내부에서 출력:", x)

# 2) 함수를 호출
retValue = setValue(5)
print(retValue)

# 다중의 값을 리턴
def swap(x,y):
    return y,x

# 호출
result = swap(3,4)
print(result[0])
print(result[1])

# 교집한 문자를 리턴하는 함수
def intersect(prelist, postlist):
    # 지역변수
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 함수 호출
print(intersect("HAM","SPAM"))
