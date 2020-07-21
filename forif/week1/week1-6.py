#week1-6.py
ID = "ektmf7890"
password = "&password&"

a = input("ID : ")
b = input("password : ")

if a == ID and b == password:
    print(ID+"님, 환영합니다!")
elif a ==ID and b != password:
    print("비밀번호를 까먹으셨나요?\n")
    ans = input("힌트를 드릴까요?(y/n) : ")
    if ans == 'y':
        print(password[:4]+"****")
    else:
        print("로그인에 실패했습니다.")
else :
    print("존재하지 않는 계정입니다.\n로그인에 실패하였습니다.")

