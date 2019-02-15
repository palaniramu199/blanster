import sys, string, math
s = input()
N = []
for c in s :
    if c.isdigit() : N.append(c)
print(*N,sep='')
