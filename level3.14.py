import sys, string, math, itertools
a=input()
l=list(itertools.permutations(a))
b=[]
for i in range(0,len(l)):
    s=''.join(list(l[i]))
    b.append(s)
b.sort()
c=[b[0]]
for i in range(0,len(b)-1):
    if b[i]!=b[i+1]:
        c.append(b[i+1])
for j in range(0,len(c)):
    print(c[j])
    
