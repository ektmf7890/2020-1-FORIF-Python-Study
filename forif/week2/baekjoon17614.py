#baekjoon17614.py

n = int(input())
total = 0
for i in range(1,n+1):
    while i:
        k = i%10
        if k==3 or k==6 or k==9: total+=1
        i=i//10
print(total)

