a,b=input().split()
a,b=list(a),list(b)
c,d=len(a),len(b)
#print(c,d)
e=max(c,d)
f=min(c,d)
g=e-f
for i in range(1,g+1):
    if c>d:
        b.append(i)
    else:
        a.append(i)
#print(a)
#print(b)
for i,j in zip(a,b):
    print(i,j,end='',sep='')
