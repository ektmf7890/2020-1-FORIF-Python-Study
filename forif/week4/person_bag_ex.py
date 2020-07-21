#person_bag_ex.py
#비공개 속성

class Person:
    '''person class'''
    bag = []

    def put_bag(self, item):
        '''put bag method'''
        Person.bag.append(item)
