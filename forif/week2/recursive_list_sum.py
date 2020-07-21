#recursive_list_sum.py
import random

def list_sum(a):
    if len(a) == 1:
        return a[0]
    return a[len(a)-1] + list_sum(a[:len(a)-1])
    
a = []
n = int(input("몇 개의 정수를 생성? "))
for i in range(n):
    temp = random.randint(1, 100)
    a.append(temp)
    
print(a)
print("합계 :",list_sum(a))
