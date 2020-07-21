#bear.py
import random

print("당신은 나무꾼입니다.")
attack = random.randint(1,10)

for i in range(1, attack+1):
    print("나무를 " + str(i) + "번 찍었습니다.")

print("나무를 찍던 중 당신은 곰을 만납니다!")
choice = input("(1)도망친다 (2)싸운다\n")
if choice == "1":
    print("당신은 (1)을 선택하셨습니다.\n최선을 다해 뛰세요!\n빨리~~~")
    success = random.randint(0,1)
    if success == 1:
        print("무사히 도망쳤네요!")
    else :
        print("붙잡혀 버렸습니다.")

elif choice == "2":
    print("당신은 2번을 선택했습니다.\n6번 안에 곰을 물리쳐야합니다.\n곰의 초기체력은 100입니다.")
    health = 100
    count=0
    for i in range(1,7):
        damage = random.randint(1, 30)
        print(str(i)+"번째 공격으로 곰의 체력이 "+str(damage)+"만큼 떨어졌습니다.")
        health -= damage
        print("남아있는 곰의 체력은 "+str(health)+"입니다.\n")
        
        if health < 0:
            print("\n승리 곰의 가죽을 얻었습니다!!")
            break
        
        count += 1
    if count == 6:
        print("당신이 졌습니다.")
        
        
        
