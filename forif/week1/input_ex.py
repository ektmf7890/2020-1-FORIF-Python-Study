#input_ex.py

x = input()
print(x)


a = input("num1 : ")
b = input("num2 : ")
print(a+b)

#입력 값의 자료형 변환
name = input('이름 : ')
age = int(input('나이 : '))
pet_list = input('당신의 애완동물들을 ","로 구분하여 입력하세요 : ').split(',')
#참고로, 문자열 안에 '나"를 포함하려면 위처럼 따옴표, 큰따옴표를 구분해서 써야됨. 잘못하면 오류
print(name, age, pet_list)

#input으로 여러 개의 값을 한 번에 입력 받기!
a, b = input("당신의 최애와 차애 배달음식을 입력하세요 : ").split()
print("최애 : ", a)
print("차애 : ", b)

#map함수 활용해서 한 번에 정수로 변환하기
c, d = map(int, input("Enter 2 numbers : ").split(,))
