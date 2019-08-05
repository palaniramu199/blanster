N=int(input())
n=list(map(int,input().split()))
m=min(n)
s=sorted(n)
for i in n:
    a=n.count(i)
    if a>1:
        print(m,i)
        break
