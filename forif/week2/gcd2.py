#gcd2.py

a,b = map(int, input().split())
if b>a:
    a,b = b,a
    
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
    
print("GCD :", gcd(a,b))
