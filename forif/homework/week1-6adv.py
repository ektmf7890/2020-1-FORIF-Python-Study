#week1-6adv.py

ID = "ektmf7890"
password = "&passw0rd&"

a = input("ID : ")

if a==ID:
    b= input("password : ")
    if b==password:
        print(ID+"님, 환연합니다!")
    else:
        print("비밀번호를 까먹으셨나요?\n")
        ans = input("힌트를 드릴까요?(y/n) : ")
        if ans == 'y':
            print(password[:4]+"****")
        else:
            print("로그인에 실패했습니다.")
else:
    print("존재하지 않는 계정입니다.\n로그인에 실패했습니다.")
    
