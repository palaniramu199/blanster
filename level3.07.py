import sys, string, math
N = int(input())
n = list(map(int,input().split()))
L2 = []
for i in range(0,len(n)) :
    if (i+1)%2 == 1 :
        if n[i] %2 == 1 :
            L2.append(n[i])
    else :
        if n[i] %2 == 0 :
            L2.append(n[i])
print(*L2)
