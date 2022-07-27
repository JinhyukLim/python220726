# class1.py
# 1) 클래스 형식을 정의
class Person:
    #클래스 멤버 변수(클래스 자체에 추가-주로 데이터 공유)
    num_person = 0
    # 초기화 메서드
    def __init__(self):
        # 소속이 인스턴스 멤버 변수
        self.name = "default name"
        # 소속이 클래스 멤버 변수
        Person.num_person += 1
    #인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

# 내어쓰기(shift+tab), 들여쓰기(tab)
# 2) 인스턴스 행성
p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스 개수:{0}".format(Person.num_person))

# 동적으로 변수를 추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

# 인스턴스에 추가
p1.age = 30
print(p1.age)
#print(p2.age)

