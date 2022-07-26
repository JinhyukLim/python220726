# function3.py
# 기본값이 있는 경우
from unittest import result


def times(a=10, b=20):
    return a*b

# 호출
print(times())
print(times(5))
print(times(5,6))

# 키워드 인자
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

# 호출
print(connectURI("credu.com", "80"))
print(connectURI(port="80", server="credu.com"))

# 가변인자
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

# 정의되지 않은 인자(필수와 옵션이 있는 경우)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL
# 호출
print(userURIBuilder("credu.com", "80", id="kim"))
print(userURIBuilder("credu.com", "80", id="kim", passwd="1234"))

# 람다함수(이름이 없는 간결한 함수 정의)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print( (lambda x:x*x)(3) )
print( globals() )

