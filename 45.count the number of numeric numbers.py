import sys, string
num= int(input())
value = 0
while num :
    value += 1
    num //= 10
print(value)
