#private_attr.py

class Cafe:
    def __init__(self, _name, _location, _menu, cash):
        self.name = _name
        self.location = _location
        self.menu = _menu
        #비공개 속성
        self.__cash = cash

    def show_info(self):        
        print('Cafe name : ', self.name)
        print('Location : ', self.location)
        print('Cash : ', self.__cash)
        print('-------------<Menu>--------------')
        count = 0
        for i in self.menu:
            count += 1
            print('{0}. {1}'.format(count, i))
        print('\n')

    def sales(self, amount):
        self.__cash += amount*3000
        print('Cash : ', self.__cash, '(sales : %d)'%amount)


QueueCafe = Cafe('Queue', 'ITBT', ['아메리카노','오레오 프라푸치노', '블루베리 베이글'], 3000)
QueueCafe.show_info()
QueueCafe.sales(3)

#QueueCafe.__cash += 1000


