import sys,string
N,M=list(map(int,input().split()))
value=N*M
if value%2==0:
    print("even")
else:
    print("odd")
