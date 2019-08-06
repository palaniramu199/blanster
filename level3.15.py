a=int(input())
b=list(map(int,input().split()))
c=max(b)
d=b.index(c)
e=[]
for i in range(d,len(b)):
    e.append(b[i])
#print(*e)
d=[]
for j in range(0,len(e)-1):
    if e[j]>e[j+1]:
        d.append(e[j])
d.append(e[len(e)-1])
print(*d)
f=max(e)
print(f)
