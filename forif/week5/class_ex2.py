#class_ex2.py

class Cafe:
    def __init__(self, _name, _location, _menu):
        self.name = _name
        self.location = _location
        self.menu = _menu

QueueCafe = Cafe('Queue', 'ITBT', ['아메리카노','오레오 프라푸치노', '블루베리 베이글'])
print('Cafe name : ', QueueCafe.name)
print('Location : ', QueueCafe.location)
print('-------------<Menu>--------------')
count = 0
for i in QueueCafe.menu:
    count += 1
    print('{0}. {1}'.format(count, i))

