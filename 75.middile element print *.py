import sys, string
s = input()
k = len(s)
m = k//2
if k%2 == 1 : 
	a = s[:m] + '*' + s[m+1:]
	print(a)
else :        
	a = s[:m-1] + '**' + s[m+1:]
	print(a)
