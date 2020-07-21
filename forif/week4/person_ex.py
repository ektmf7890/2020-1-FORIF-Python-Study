#person_ex.py
#비공개 속성

class Person:
    def __init__(self, name, age, addr, money):
        self.name = name
        self.age = age
        self.addr = addr
        self.__money = money

    def pay(self, amount):
        self.__money -= amount
        print("you have {0} left.".format(self.__money))


