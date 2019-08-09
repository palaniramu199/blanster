#117 
n=int(input())
s=str(n)
l=list(s)
#print(l)
a=len(l)
sum=0
for i in range(0,a):
    b=int(l[i])
    #print(b)
    c=b**i
    sum=sum+c
print(sum)
