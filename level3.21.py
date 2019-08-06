a,b=map(int,input().split())
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=[]
f=[]
for i in range(0,len(c)-1):
    if c[i]==c[i+1]:
        e.append(c[i])
        print(*d)
        break
    else:
        print("0 "*len(c),sep=' ')
        break
for j in range(0,len(d)-1):
    if d[j]==d[j+1]:
        f.append(d[j])
        print(*c)
        break
    else:
        print("0 "*len(d),sep='')
        break
