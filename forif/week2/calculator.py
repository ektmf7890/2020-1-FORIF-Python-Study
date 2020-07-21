#calculator.py

def add (a, b):
    return a+b
def sub (a, b):
    return a-b
def mul (a, b):
    return a*b
def div (a, b):
    return a/b

while True:
    print("Menu.".center(25,'-'))
    print("1.Add 2.Sub 3.Mul 4.Div\n")
    choice = int(input("Your choice(0 to end) : "))
    if choice == 0:
        break
    a,b = input("Enter two numbers : ").split()
    a = int(a)
    b = int(b)
    if choice == 1:
        print("Result :", add(a,b))
    if choice == 2:
        print("Result :", sub(a,b))
    if choice == 3:
        print("Result :", mul(a,b))
    if choice == 4:
        print("Result :", div(a,b))

        








        
