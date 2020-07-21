#N-gram.py
text = input('글자 단위 n-gram')

for i in range(len(text)-2):
    print(text[i:i+3])

text = input("단어 단위 n-gram")
words = text.split()

for i in range(len(words)-1):
    print(words[i],words[i+1])






































