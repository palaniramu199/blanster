n=input()
s=list(n)
a=[]
for i in s:
    if ord(i)>=97 and ord(i)<=122:
        a.append(i)
    if ord(i)>=65 and ord(i)<=90:
        a.append(i)
print(*a,sep='')
    
        
