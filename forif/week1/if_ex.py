#if_ex.py

#들여쓰기
x = 10
if x == 5:
    print("5입니다.")
print('x가 5일 때만 실행되는 코드입니다.') #들여쓰기를 하지 않았기 때문에 if문과 전혀 상관 없는 코


#비교연산자 사용해서 점심메뉴 선정하기
money = 3000
tired = True
lunch = '미정'

if money >= 5000:
    lunch = '꼬꼬아찌'
elif tired:
    lunch = '대연각'
else:
    lunch = '학식'
print('오늘의 점심은???\n',lunch)

#조건문 중첩시켜서 점심메뉴 선정하기
money = int(input('돈 : '))
ans = input('피곤한가요?  ')
if ans == '네':
    tired = True
else:
    tired = False  #tired = True if ans == '네' else False (조건부 표현식으로 짧게 표현 가능)

if money>=5000 :
    if tired:
        print('돈까스 배달')
    else:
        print('왕십리')
elif tired:
    print('대연각 배달')
else:
    print('학식')


#논리연산자 사용하기
ans = input('돈이 있나요?')
rich = True if ans == '네' else False
late = input('늦잠을 잤나요? ')

if late == '네' and rich:
    print('택시를 타고 지각을 면하세요')
if late == '네' and not rich:
    print('그냥 늦으세요')
if late != '네':
    print('부지런하시군요!')















    
