#iterative_fibo.py

def fibo(n):
    a=0
    b=1
    for i in range(n):
        temp = a
        a = b
        b = temp + b
    return a

n = int(input())
print(fibo(n))
    
