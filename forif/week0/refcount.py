#refcount.py
import sys
'''
x = 3
y = x
x = 4
print(y)
'''

print(sys.getrefcount(1000))

x = 1000
print(sys.getrefcount(1000))

y = 1000
print(sys.getrefcount(1000))

print(x is y)


