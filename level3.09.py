N=int(input())
n=list(map(int,input().split()))
m=min(n)
for i in n:
    if m == -(i):
        print(m,i)
