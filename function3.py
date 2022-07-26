# function3.py
# 기본값이 있는 경우
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