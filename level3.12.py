a,b=map(int,input().split())
c=list(map(int,input().split()))
s=sorted(c)
#print(s)
e=s[::-1]
#print(e)
print(e[b-1])

