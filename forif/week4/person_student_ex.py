#person_student_ex.py

class Person:
    def __init__(self):
        print("Person 클래스의 생성자가 호출 되었습니다.")
        self.name = "길동이"

    def greeting(self):
        print("안녕하세요. 저는 {0}입니다.".format(self.name))
        

class Student(Person):
    def __init__(self):
        print("Student 클래스의 생성자가 호출 되었습니다.")
        super().__init__()
        self.school = "호그와트 마법 학교"

    #method overriding
    def greeting(self):
        super().greeting()
        print("저는 {0}를 다닙니다.".format(self.school))
    


