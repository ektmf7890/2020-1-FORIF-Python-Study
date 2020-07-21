#bool_logic.py
#숫자의 비교
print(10==10) 
print(5>10)

#문자열의 비교
if('kimchi' != 'Kimchi'):
    print('김치찌개 먹고 싶어!')


#객체의 같고 다름 비교
print(1 is 2)
print(1 is not '1')

1 is 1.0 #False
1 == 1.0 #True
id(1) == id(1.0) #False

#논리연산에서의 단락 평가->IDLE에서 실행
False and True
True or False
True and 'Python'
True or 'Python'
False or 'Python'
#...(코딩도장 논리연산자 부분 확인하면 예시 많음)

























