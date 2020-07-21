#week4-2.py

class Account:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def deposit(self, amount):
        self.money += amount
        print("-----{0}님의 계좌-----".format(self.name))
        print("{0}원을 입급했습니다.".format(amount))
        print("잔액 : {0}".format(self.money))

    def withdraw(self, amount):
        print("-----{0}님의 계좌-----".format(self.name))
        if amount <= self.money:
            self.money -= amount
            print("{0}를 출금했습니다.\n잔액 : {1}".format(amount,self.money))
        else:
            print("잔액이 부족합니다.\n잔액 : {0}".format(self.money))

if __name__=="__main__":
    account_list = []
    num = int(input("몇 개의 계좌를 만드시겠습니까? >>> "))

    for i in range(num):
        print()
        print(f"계좌{i+1}번".center(20, '-'))
        name = input("이름 : ")
        money = int(input("입금액 : ").replace(',', ''))
        temp = Account(name, money)
        account_list.append(temp)
                    
        
        

