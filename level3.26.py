n=int(input())
s=list(map(int,input().split()))
num=sorted(s)
N=num[::-1]
a=[]
for i in N:
    a.append(i)
    if i>N[n-1]:
        a.append("->")
print(*a,sep='')
