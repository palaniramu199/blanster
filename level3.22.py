N=int(input())
n=list(map(int,input().split()))
sum=1
for i in n:
	sum=sum*i
#print(sum)
for i in n:
	s=sum//i
	print(s,sep='',end=' ')
