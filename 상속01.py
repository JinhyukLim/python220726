# 부모 클래스를 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
    def coding(self):
        print("코딩중입니다.")
    def eating(self):
        print("식사중입니다.")

# 자식 클래스를 정의
class Student(Person):
    # 초기화 메서드를 재정의
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        # 명시적으로 부모 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    # 상속 받은 메서드를 재정의(덮어 쓰기)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
p.printInfo()
s.printInfo()

# print(p.__dict__)
# print(s.__dict__)

s.coding()
s.eating()

