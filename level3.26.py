n=int(input())
n=list(map(int,input().split()))
N=n[::-1]
a=[]
for i in N:
    a.append(i)
    if i>1:
        a.append("->")
print(*a,sep='')
