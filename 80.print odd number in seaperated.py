import sys, string, math
n = int(input())
N = []
while n :
    a = n%10
    if a%2 == 1 : N.append(a)
    n //= 10
N = N[::-1]
print(*N)
