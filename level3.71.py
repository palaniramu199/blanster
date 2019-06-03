n,m=map(int,input().split())
a=list(map(int,input().split()))
b=len(a)
c=b-m
for i in range(c+1,n+1):
    print(i,end=' ')
