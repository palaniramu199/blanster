n=int(input())
sum=0
while n>0:
	a=n%10
	sum=sum+a
	n//=10
#print(sum)
s=str(sum)
if s==s[::-1]:
	print("YES")
else:
	print("NO")
	
