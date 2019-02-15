import sys, string
n = int(input())
N = []
for i in range(1,n+1) :
    if n%i == 0 : N.append(i)
print(*N)
