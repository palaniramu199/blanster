num=121
sum=0
temp=num
while temp>0:
	value=temp%10
	sum=sum*10+value
	temp=temp//10
if num==sum:
	print("yes")
else
	print("no")
	
