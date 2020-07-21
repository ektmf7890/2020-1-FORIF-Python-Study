#gugudan.py

while True:
    dan = int(input("단을 입력하세요 : "))
    if dan>=1 and dan<=9: break
    else : print("1~9 이내의 값을 다시 입력해주세요\n")

print("---------------------------------------")

num=1
#while문 사용
while num<10:
    print(dan, '*', num, "=",dan*num)
    num += 1
    

for i in range(1,10):
    print(dan, "*",i, "=",dan*i)
    i += 1
    
