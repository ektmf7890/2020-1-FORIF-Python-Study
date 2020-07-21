#variable.py

x=12.2
print(x)
print(id(x))

x=14
print(x)
print(id(x))

x=9
print(x)
print(id(x))

x='HelloWorld'
print(x)
print(id(x))

'''
x=12.2라는 대입문은 x가 항상 12.2라는 소리가 아니라,
메모리공간을 찾아서 x라는 이름을 주고 거기에 12.2라는 데이터를 저장하라는  명령을 내리는 것이다!
따라서, 변수에 저장된 값을 계속 변경 할 수 있는 것이다.
파이썬에서는 변수 값을 바꿀 때마다 주소값이 바뀌네요!
계속 새로운 공간을 할당하고 있음을 알 수 있습니다.
'''

x = 5
y = 1.2
print(x, y)

x = "나는 문자열!"
print(x,y)









