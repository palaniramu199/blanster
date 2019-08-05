N=int(input())
n=list(map(int,input().split()))
s=[]
for i in n:
  a=n.count(i)
  if a>1:
    s.append(i)
m=set(s)
print(*m)
