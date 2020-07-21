#find_char.py
#week2의 문자열 복습 심화과제 제출 후보
import string
text = 'Some say, "the world will end in fire.". Some say in ice. From what I have tasted of desire, I hold with those who favor fire. But if it had to perish twice, I think I know enough of hate to know that for destruction, ice is also great and would suffice'

words = text.split()
for word in words:
    if word.find('t') != -1:
        print(word.strip(string.punctuation))
        
