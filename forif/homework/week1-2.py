#week1-2.py
ID = input("주민등록번호를 입력하세요 : ")
a = ID[7]
print("\n생년월일 :", ID[:6])

if a == '1':
    print("성별 : 남")
elif a == '2':
    print("성별 : 여")
else:
    print("어느 시대 사람인가요?")
