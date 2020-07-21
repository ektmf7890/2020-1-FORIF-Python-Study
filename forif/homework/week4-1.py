#week4-1.py


class Person:
    def __init__(self, name, energy, age):
        self.name = name
        self.energy = energy
        self.age = age
        
    def eat(self):
        print("밥을 먹어 기운이 납니다.")
        self.energy += 10
        print("{0}님의 현재 에너지 : {1}".format(self.name, self.energy))

    def greeting(self):
        print("안녕하세요, 저는 {0}입니다. {1}살 입니다.".format(self.name,self.age))
    
    
                
    
        

