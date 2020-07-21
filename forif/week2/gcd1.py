#gcd1.py

a, b = map(int, input("a,b = ").split())

if b>a:
    b,a = a,b
n=1
while n!=0:
    n = a%b
    a=b
    b=n
    
print(f"GCD : {a}")

