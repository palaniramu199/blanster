n,k=map(int,input().split())
m=list(map(int,input().split()))
sum=[]
for i in range(n-k,n):
	sum.append(str(m[i]))
print(" ".join(sum))
