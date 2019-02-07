import sys, string
num = int(input())
value = []
while num :
    a = num%10
    value.append(a)
    num //= 10
value = value[::-1]
print(*value)
