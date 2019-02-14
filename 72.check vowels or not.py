import sys, string
n=input()
b=0
for c in n:
	if c =='a' or c=='i' or c=='e' or c=='o' or c=='u' or c =='A' or c=='I' or c=='E' or c=='O' or c=='U':
		b=1
		break
if b:
	print("yes")
else:
	print("no")
