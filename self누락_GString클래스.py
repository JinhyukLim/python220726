# 전역변수(이름충돌)
str = "Not Class Member"
class GString:
    def __init__(self):
        # 인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        # 꼼꼼하게 코딩(명시적 코딩)
        print(self.str)

# 인스턴스(object), 객체
g = GString()
g.set("First Message")
g.print()
