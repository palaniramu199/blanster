num=12
sum=0
temp=num
while temp>0:
	value=temp%10
	sum=sum+value**3
	temp=temp//10
if num==sum:
	print("yes")
else:
	print("no")
	
