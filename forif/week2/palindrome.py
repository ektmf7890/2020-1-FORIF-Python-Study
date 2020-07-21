#palindrome.py
#week2, 회문 판별, 반복문과 문자열 공부

#나의 방법 
temp = input("Input String : ")
text = temp.replace(' ','')

a = 0
b = len(text)-1

is_palindrome = True
while a<b:
    if text[a] != text[b]:
        is_palindrome = False
    a+=1
    b-=1

print(is_palindrome)

#방법2
temp = input("Input String : ")
text = temp.replace(' ','')
is_palindrome = True

for i in range(len(text)//2):
    if text[i] != text[-i-1]:
        is_palindrome = False
        break
print(is_palindrome)

#방법3
text = input("Input String : ")
text = text.replace(' ','')
is_palindrome = True

if len(text) > 1:
    front = text[:len(text)//2]
    rear = text[-(len(text)//2):]
    rear = rear[::-1]

    if front != rear:
        is_palindrome = False
    
print(is_palindrome)

# [::-1]을 사용해서 문자열을 뒤집거나, 리스트로 만들어서 reversed 함수를 사용하는 등
#슬라이싱도 하지 않고 바로 뒤집어서 비교하는 방법도 있음 



















    
        



