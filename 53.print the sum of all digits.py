import sys, string
num = int(input())
value = 0
while num :
    value += num%10
    num //= 10
print(value)
