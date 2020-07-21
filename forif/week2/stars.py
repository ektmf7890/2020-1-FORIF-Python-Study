#stars.py


def stars(n):
    for i in range(n):
        for k in range(n-1-i):
            print(' ', end = '')
        for j in range(2*i+1):
            print("*", end = '')
        print()
            
n = int(input("정수 입력 : "))
stars(n)
