import sys, string
num = int(input())
value1 = list(map(int,input().split()))
for i in range(len(value1)) :
    print(value1[i],i)
