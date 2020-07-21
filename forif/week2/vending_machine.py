#vending_machine.py



def show_menu():
    print("[MENU]".center(20,'-'))
    print("1. Cola".ljust(15),"2000")
    print("2. Sprite".ljust(15),"2500")
    print("3. Coffee".ljust(15),"3000")
    print("4. MintChoco".ljust(15),"4500")
    print("-"*20)
    
def buy(choice):
    global money
    global price
    global menu
    if money<price[choice]:
        print("Not enough money")
        return
    money-=price[choice]
    print(f"You got a {menu[choice]}!")
    

if __name__ == "__main__":
    money = int(input("Insert money : "))
    while True:
        if money<2000:
            print(f"You can't buy anything with {money}원")
            break
        show_menu()
        choice = int(input("Choice(0 to end) : "))
        print()
        menu = ["Cola", "Sprite", "Coffee", "MintChoco"]
        price = [2000, 2500, 3000, 4500]
        if choice == 0:
            break
        elif choice>=1 and choice<=4:
            buy(choice-1)
            print(f"Money : {money}\n")
        else:
            print("Error, your choice should be between 0~4")
            print(f"Money : {money}\n")
            
        
        
        
