#week1-5.py

hour, minute = map(int, input("내일 몇시에 일어나시나요? ").split(':'))

if minute>=50:
    minute -= 50
elif hour!=0 and minute<50:
    hour -= 1
    sub = 50 - minute
    minute = 60 - sub #minute+=10 과 동일
elif hour == 0 and minute <50:
    hour = 23
    minute+=10

print(hour, "시", minute,"분에 알람을 맞춰 드릴께요!\n")




